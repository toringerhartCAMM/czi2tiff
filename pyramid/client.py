#!/usr/bin/env python
# 
# Copyright 2014 University of Southern California
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
Raw network client for HTTP(S) communication with ERMREST service.
"""

import os
import subprocess
import json
import base64
import urlparse
from httplib import HTTPConnection, HTTPSConnection, HTTPException, OK, CREATED, ACCEPTED, NO_CONTENT, CONFLICT
import sys
import traceback
import time
import shutil
import smtplib
import urllib
from email.mime.text import MIMEText
from bioformats import BioformatsClient
mail_footer = 'Do not reply to this message.  This is an automated message generated by the system, which does not receive email messages.'

_base_html = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
        <script type="text/javascript" src="/%(cirm_path)s/zoomify/ZoomifyImageViewer.js"></script>
        <style type="text/css"> #myContainer { width:900px; height:550px; margin:auto; border:1px; border-style:solid; border-color:#696969;} </style>
        <script type="text/javascript"> Z.showImage("myContainer", "/%(cirm_path)s/tiles/%(slide_id)s/%(scan_id)s", "zInitialZoom=50&zFullPageInitial=1&zLogoVisible=0&zSkinPath=/%(cirm_path)s/zoomify/Assets/Skins/Default"); </script>
    </head>
    <body>
        <div id="myContainer"></div>
    </body>
</html>
"""

class ErmrestHTTPException(Exception):
    def __init__(self, value, status):
        super(ErmrestHTTPException, self).__init__(value)
        self.value = value
        self.status = status
        
    def __str__(self):
        message = "%s." % self.value
        return message

class ErmrestException(Exception):
    def __init__(self, value, cause=None):
        super(ErmrestException, self).__init__(value)
        self.value = value
        self.cause = cause
        
    def __str__(self):
        message = "%s." % self.value
        if self.cause:
            message += " Caused by: %s." % self.cause
        return message

class MalformedURL(ErmrestException):
    """MalformedURL indicates a malformed URL.
    """
    def __init__(self, cause=None):
        super(MalformedURL, self).__init__("URL was malformed", cause)

class UnresolvedAddress(ErmrestException):
    """UnresolvedAddress indicates a failure to resolve the network address of
    the Ermrest service.
    
    This error is raised when a low-level socket.gaierror is caught.
    """
    def __init__(self, cause=None):
        super(UnresolvedAddress, self).__init__("Could not resolve address of host", cause)

class NetworkError(ErmrestException):
    """NetworkError wraps a socket.error exception.
    
    This error is raised when a low-level socket.error is caught.
    """
    def __init__(self, cause=None):
        super(NetworkError, self).__init__("Network I/O failure", cause)

class ProtocolError(ErmrestException):
    """ProtocolError indicates a protocol-level failure.
    
    In other words, you may have tried to add a tag for which no tagdef exists.
    """
    def __init__(self, message='Network protocol failure', errorno=-1, response=None, cause=None):
        super(ProtocolError, self).__init__("Ermrest protocol failure", cause)
        self._errorno = errorno
        self._response = response
        
    def __str__(self):
        message = "%s." % self.value
        if self._errorno >= 0:
            message += " HTTP ERROR %d: %s" % (self._errorno, self._response)
        return message
    
class NotFoundError(ErmrestException):
    """Raised for HTTP NOT_FOUND (i.e., ERROR 404) responses."""
    pass


class ErmrestClient (object):
    """Network client for ERMREST.
    """
    ## Derived from the ermrest iobox service client

    def __init__(self, **kwargs):
        self.metadata = kwargs.get("metadata")
        self.baseuri = kwargs.get("baseuri")
        o = urlparse.urlparse(self.baseuri)
        self.scheme = o[0]
        host_port = o[1].split(":")
        self.host = host_port[0]
        self.path = o.path
        self.port = None
        if len(host_port) > 1:
            self.port = host_port[1]
        self.use_goauth = kwargs.get("use_goauth")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.mail_server = kwargs.get("mail_server")
        self.mail_sender = kwargs.get("mail_sender")
        self.mail_receiver = kwargs.get("mail_receiver")
        self.logger = kwargs.get("logger")
        self.tiles = kwargs.get("tiles")
        self.thumbnails = kwargs.get("thumbnails")
        self.tiff = kwargs.get("tiff")
        self.html = kwargs.get("html")
        self.extract = kwargs.get("extract")
        self.extract_rgb = kwargs.get("extract_rgb")
        self.czi = kwargs.get("czi")
        self.czirules = kwargs.get("czirules")
        self.showinf = kwargs.get("showinf")
        self.timeout = kwargs.get("timeout")
        self.cirm_path = kwargs.get("cirm_path")
        self.http_storage = kwargs.get("http_storage")
        self.header = None
        self.webconn = None
        self.logger.debug('Client initialized.')

    def send_request(self, method, url, body='', headers={}):
        if self.header:
            headers.update(self.header)
        self.webconn.request(method, url, body, headers)
        resp = self.webconn.getresponse()
        if resp.status not in [OK, CREATED, ACCEPTED, NO_CONTENT]:
            raise ErmrestHTTPException("Error response (%i) received: %s" % (resp.status, resp.read()), resp.status)
        return resp

    def connect(self):
        if self.scheme == 'https':
            self.webconn = HTTPSConnection(host=self.host, port=self.port)
        elif self.scheme == 'http':
            self.webconn = HTTPConnection(host=self.host, port=self.port)
        else:
            raise ValueError('Scheme %s is not supported.' % self.scheme)

        if self.use_goauth:
            auth = base64.encodestring('%s:%s' % (self.username, self.password)).replace('\n', '')
            headers = dict(Authorization='Basic %s' % auth)
            resp = self.send_request('GET', '/service/nexus/goauth/token?grant_type=client_credentials', '', headers)
            goauth = json.loads(resp.read())
            self.access_token = goauth['access_token']
            self.header = dict(Authorization='Globus-Goauthtoken %s' % self.access_token)
        else:
            headers = {}
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            resp = self.send_request("POST", "/ermrest/authn/session", "username=%s&password=%s" % (self.username, self.password), headers)
            self.header = dict(Cookie=resp.getheader("set-cookie"))
        
    def close(self):
        """Closes the connection to the Ermrest service.
        
        The underlying python documentation is not very helpful but it would
        appear that the HTTP[S]Connection.close() could raise a socket.error.
        Thus, this method potentially raises a 'NetworkError'.
        """
        assert self.webconn
        try:
            self.webconn.close()
        except socket.error as e:
            raise NetworkError(e)
        finally:
            self.webconn = None

    def writeHTMLFile(self, slide_id, scan_id):
        outdir = '%s/%s' % (self.html, slide_id)
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        f = open('%s/%s.html' % (outdir, scan_id), 'w')
        f.write('%s\n' % _base_html % (dict(cirm_path=self.cirm_path, scan_id=scan_id, slide_id=slide_id)))
        f.close()
        
    def writeThumbnailFile(self, slide_id, scan_id):
        outdir = '%s/%s' % (self.thumbnails, slide_id)
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        shutil.copyfile('%s/%s/%s/TileGroup0/0-0-0.jpg' % (self.tiles, slide_id, scan_id), '%s/%s.jpg' % (outdir, scan_id))
        
    def sendMail(self, subject, text):
        if self.mail_server and self.mail_sender and self.mail_receiver:
            try:
                msg = MIMEText('%s\n\n%s' % (text, mail_footer), 'plain')
                msg['Subject'] = subject
                msg['From'] = self.mail_sender
                msg['To'] = self.mail_receiver
                s = smtplib.SMTP(self.mail_server)
                s.sendmail(self.mail_sender, self.mail_receiver.split(','), msg.as_string())
                s.quit()
                self.logger.debug('Sent email notification')
            except:
                et, ev, tb = sys.exc_info()
                self.logger.error('got exception "%s"' % str(ev))
                self.logger.error('%s' % str(traceback.format_exception(et, ev, tb)))

    def start(self):
        ready = False
        while ready == False:
            self.processScans()
            time.sleep(self.timeout)
        
    def processScans(self):
        url = '%s/entity/Scan/Zoomify::null::' % self.path
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        resp = self.send_request('GET', url, '', headers)
        scans = json.loads(resp.read())
        scanids = []
        for scan in scans:
            if os.path.isdir('%s/%s' % (self.tiff, scan['Slide ID'])):
                scanids.append((scan['Slide ID'], scan['ID']))
        for slideId,scanId in scanids:
            f = self.getTiffFile(slideId, scanId)
            if f:
                if len(f) == 1:
                    args = [self.extract, '%s/%s/%s/%s' % (self.tiff, slideId, scanId, f[0]), '%s/%s/%s' % (self.tiles, slideId, scanId)]
                else:
                    args = [self.extract_rgb, '%s/%s/%s' % (self.tiff, slideId, scanId), '%s/%s/%s' % (self.tiles, slideId, scanId)]
                self.logger.debug('Extracting tiles with "%s" for slide "%s", scan "%s"' % (args[0], slideId, scanId)) 
                p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdoutdata, stderrdata = p.communicate()
                returncode = p.returncode
                if returncode != 0:
                    self.logger.error('Can not extract tiles for "%s/%s/%s".\nstdoutdata: %s\nstderrdata: %s\n' % (self.tiff, slideId, scanId, stdoutdata, stderrdata)) 
                    self.sendMail('FAILURE Tiles', 'Can not extract tiles for "%s/%s/%s".\nstdoutdata: %s\nstderrdata: %s\n' % (self.tiff, slideId, scanId, stdoutdata, stderrdata))
                    for file in f:
                        os.rename('%s/%s/%s/%s' % (self.tiff, slideId, scanId, file), '%s/%s/%s/%s.err' % (self.tiff, slideId, scanId, file))
                    continue
                self.writeHTMLFile(slideId, scanId)
                self.writeThumbnailFile(slideId, scanId)
                self.logger.debug('Extracting metadata for slide "%s", scan "%s"' % (slideId, scanId)) 
                bioformatsClient = BioformatsClient(showinf=self.showinf, \
                                                    czirules=self.czirules, \
                                                    czifile='%s/%s/%s.czi' % (self.czi, slideId, scanId))
                metadata = bioformatsClient.getMetadata()
                self.logger.debug('Metadata: "%s"' % str(metadata)) 
                os.remove('temp.xml')
                columns = ["Thumbnail","Zoomify"]
                columns.extend(self.metadata)
                columns = ','.join([urllib.quote(col, safe='') for col in columns])
                url = '%s/attribute/Scan/ID=:ID/%s' % (self.path, columns)
                body = []
                obj = {'ID': scanId,
                       'Thumbnail': '%s/%s/thumbnails/%s/%s.jpg' % (self.http_storage, self.cirm_path, slideId, scanId),
                       'Zoomify': '%s/%s/html/%s/%s.html' % (self.http_storage, self.cirm_path, slideId, scanId)
                       }
                for col in self.metadata:
                    if metadata[col] != None:
                        obj[col] = metadata[col]
                body.append(obj)
                headers = {'Content-Type': 'application/json'}
                self.send_request('PUT', url, json.dumps(body), headers)
                self.logger.debug('SUCCEEDED created the tiles directory for the slide id "%s" and scan id "%s".' % (slideId, scanId)) 
                self.sendMail('SUCCEEDED Tiles', 'The tiles directory for the slide id "%s" and scan id "%s" was created.\n' % (slideId, scanId))
        
    def getTiffFile(self, slideId, scanId):
        scanDir = '%s/%s/%s' % (self.tiff, slideId, scanId)
        if os.path.isdir(scanDir):
            # allow 30 minutes for GO transfer to be be completed
            if (time.time() - os.path.getmtime(scanDir)) > 1800:
                tifFiles = [ f for f in os.listdir(scanDir) if os.path.isfile(os.path.join(scanDir,f)) and not re.match('.*[.]err$', f) ]
                if len(tifFiles) > 0:
                    return tifFiles
        return None
        
