#!/usr/bin/env python

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

import csv, sys, random, getopt, time

from formatters import get_formatter
from writers import get_writer
from generator import *
from grammers import *

DEFAULT_FORMATTER = 'plain'
DEFAULT_WRITER    = 'console'

SUPPORTED_FORMATS = ['plain', 'pretty', 'csv']
SUPPORTED_OUTPUTS = ['console', 'file', 'email']

def usage():
    print """Jenny the moody message generator.
    
Usage: jenny [OPTION] [MESSAGES]

Options:    
 -d --delay        Insert a random delay between producing messages between 0 and [arg] seconds
 -f --format       The output format. Currently only supports console (default), file and email.
 -o --output       Where to output to. Supported options are console, file & email. If using email
                   you should also provide a hostname, username, password and a recipient.
 -S --server       Run in server mode. Jenny will generate messages until stopped.
    --hostname     The hostname[:port] of your SMTP server (defaults to Gmail).     
    --username     Your mail account username.
    --password     Your mail account password
    --sender       Email sender address (defaults to jenny@example.com)
    --recipient    Email recipient address 
 -h --help         Print usage summary (i.e. this)
"""

def main(argv):   
    # Parse command line arguments.
    try:                                
        opts, args = getopt.getopt(argv, 'dfoSh', ['help', 
                                                 'format=',
                                                 'output=', 
                                                 'hostname=', 
                                                 'username=', 
                                                 'password=', 
                                                 'sender=',
                                                 'recipient=',
                                                 'server',
                                                 'delay='])
    except getopt.GetoptError:          
        usage()                         
        sys.exit(2) 
    
    # Setup defaults
    delay = 0
    server = False
    format = DEFAULT_FORMATTER
    output = DEFAULT_WRITER
    hostname = 'localhost'
    username = None
    password = None
    sender = 'jenny@example.com'
    recipients = []
    
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-f', '--format'):
            format = arg
            if format not in SUPPORTED_FORMATS:
                print '%s is not a supported format.\n' % format
                usage()
                sys.exit(2)
        elif opt in ('-o', '--output'):
            output = arg
            if output not in SUPPORTED_OUTPUTS:
                print '%s is not a supported output.\n' % output
                usage()
                sys.exit(2)
        elif opt in ('--hostname'):
            hostname = arg
        elif opt in ('--username'):
            username = arg
        elif opt in ('--password'):
            password = arg
        elif opt in ('--sender'):
            sender = arg
        elif opt in ('--recipient'):
            recipients.append(arg)
        elif opt in ('-d', '--delay'):
            delay = int(arg)
        elif opt in ('-S', '--server'):
            server = True
        
    # Setup our writer object
    writer = get_writer(output)
    writer.formatter = get_formatter(format)
    if output == 'email':
        writer.hostname = hostname
        writer.username = username
        writer.password = password
        writer.sender = sender
        writer.recipients = recipients

    # Are we in server mode?
    if server:
        print 'Starting Jenny server...'
    else: 
        # Then how many messages should Jenny spew forth?
        try:
            how_many = int("".join(args))
        except ValueError:
            how_many = 1
        print 'Generating %s messages.' % how_many

    if delay: random.seed()

    # Produce the required amount of messages
    count = 1 
    while True:
        print 'Generating message %s...' % count
        # Randomly set tone and mood up front. Ideally mood should be fit a normal distribution that's in line with one of
        # our existing corpuses. I'll come back to that later though.
        tone = random.choice(tones)
        mood = random.choice(moods) 
           
        m = construct_message(tone, mood)
        writer.write(m)
        
        if not server and count >= how_many:
            break
        
        count += 1
        if delay:
            n = random.randint(0, delay)
            print 'Going to sleep for %s seconds.' % n
            time.sleep(n)
        
if __name__ == "__main__":
    main(sys.argv[1:])
