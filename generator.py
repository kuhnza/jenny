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

import random

from grammers import Fragment, expansions

L_BRACE = '{'
R_BRACE = '}'

class Message(object):
    
    def __init__(self, tone, mood, text):
        self.tone = tone
        self.mood = mood
        self.text = text
        
    def __str__(self):
        return self.text

def filter(fragments, tone, mood):
    filtered = []
    for f in fragments:
        if (tone in f.tones) and (mood in f.moods):
            filtered.append(f)            
    return filtered

def parse(text, tone, mood):
    open = False
    token = ''
    
    # Search text for tokens
    for c in text:
        if c == L_BRACE:
            # Beginning of token, make note now inside token.
            open = True
        elif c == R_BRACE and open:
            # End of token, close it off.
            open = False            
            
            # Expand the token and parse it as it may contain more tokens
            expanded = expand(token, tone, mood)
            expanded = parse(expanded, tone, mood)
                        
            # Replace the token in the text with the expansion.
            text = text.replace(L_BRACE + token + R_BRACE, expanded, 1)
            
            # Now we're done with it clear the token.
            token = ''
        elif open:
            # Build up the token string.
            token += c            
    return text
        
    
def expand(token, tone, mood):
    # Lookup token in list of expansions
    l = expansions[token]
    
    # If a list of fragments then we can filter it, before picking one at random.
    try:
        if isinstance(l[0], Fragment): 
            text = random.choice(filter(l, tone, mood)).text
        else:
            text = random.choice(l)
        return text
    except IndexError:
        print token
        raise

def construct_message(tone, mood):
    # Get a message structure at random that fits the mood and tone.
    text = random.choice(filter(expansions['message'], tone, mood)).text
    
    # Now recurse through the message expanding tokens as we go.
    return Message(tone, mood, parse(text, tone, mood))
