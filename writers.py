# Copyright 2011 Chorus Technologies, Inc.
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

import smtplib 

def get_writer(writer):
    """Factory function for obtaining new writer objects."""
    if writer == 'console':
        return ConsoleWriter()
    elif writer == 'file':
        return FileWriter()
    elif writer == 'email':
        return EmailWriter()
    else:
        raise WriterDoesNotExistError('Writer: %s does not exist.' % writer)

class WriterDoesNotExistError(Exception):
    pass

class Writer(object):
    
    def __init__(self, formatter=None):
        self.formatter = formatter
        
    def write(self, obj):
        raise NotImplementedError()
    
class ConsoleWriter(Writer):
    
    def write(self, obj):
        """Write output straight to stdout"""
        print self.formatter.format(obj)

class FileWriter(Writer):
    
    def __init__(self, formatter=None, outfile='jenny.txt'):
        super(FileWriter, self).__init__(formatter)
        self.outfile = outfile
        
    def write(self, obj):
        file = open(self.outfile, 'wb')
        file.write(self.formatter.format(obj))
        file.close()
        
class EmailWriter(Writer):
    
    def __init__(self, formatter=None, hostname='localhost', username=None, password=None, sender='jenny@example.com', recipients=None):
        super(EmailWriter, self).__init__(formatter)
        self.hostname = hostname
        self.username = username
        self.password = password
        self.sender = sender
        self.recipients = recipients
        
    def write(self, obj):
        # Send the message 
        server = smtplib.SMTP(self.hostname) 
        if self.username and self.password:  
            server.starttls()
            server.login(self.username, self.password)  
        server.sendmail(self.sender, self.recipients, self.formatter.format(obj))  
        server.quit()  