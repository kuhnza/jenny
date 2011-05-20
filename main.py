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

import csv, sys, random, getopt

from functions import *
from grammers import *

def usage():
    print """Usage:
    
--help
    Print usage summary (i.e. this)
    
--format
    The output format. Currently only supports console (default) and csv so bite me.
    
--output
    The filename to use if using format other than console.
"""

def main(argv):   
    
    try:                                
        opts, args = getopt.getopt(argv, 'hfo', ['help', 'format=', 'output='])
    except getopt.GetoptError:          
        usage()                         
        sys.exit(2) 
    
    outfile = 'emails.csv'
    format = 'console'
    supported_formats = ['console', 'csv']
    
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-f', '--format'):
            format = arg
            if format not in supported_formats:
                print '%s is not a supported format.\n' % format
                usage()
                sys.exit(2)
        elif opt in ('-o', '--output'):
            outfile = arg
          
    try:
        how_many = int("".join(args))
    except ValueError:
        how_many = 1
    
    # Print headers
    if format == 'csv':
        writer = csv.writer(open(outfile, 'wb'))
        writer.writerow(['sentiment', 'message'])
            
    # Produce the required amount of messages 
    for n in range(0, how_many):
        # Randomly set tone and mood up front. Ideally mood should be fit a normal distribution that's in line with one of
        # our existing corpuses. I'll come back to that later though.
        tone = random.choice(tones)
        mood = random.choice(moods) 
           
        m = construct_message(tone, mood)
        
        if format == 'csv':
            writer.writerow([moods.index(mood), m])
        else:   
            print '--------\n'
            print 'Tone: {tone}, Mood: {mood}\n'.format(tone=tone, mood=mood)    
            print m 

if __name__ == "__main__":
    main(sys.argv[1:])
