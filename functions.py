'''
Created on 30/04/2011

@author: dave
'''

import random

from classes import *
from grammers import *

L_BRACE = '{'
R_BRACE = '}'

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
    m = random.choice(filter(expansions['message'], tone, mood)).text
    
    # Now recurse through the message expanding tokens as we go.
    return parse(m, tone, mood)
