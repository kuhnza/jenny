import csv, sys, random

from classes import *
from functions import *
from grammers import *

def get_name(tone):
    if tone == 'formal':
        name = '%s %s' % (random.choice(names['first']), random.choice(names['last']))
    else:
        name = random.choice(names['first'])    
    return name
        
def get_salutation(tone, mood):
    text = random.choice(filter(salutations, tone, mood)).text        
    return text    

def get_message(tone, mood):
    problem = random.choice(problems)
    problem = problem.format(adjective=random.choice(filter(adjectives, tone, mood)).text,
                      repetition=random.choice(repetitions),
                      action=random.choice(actions),
                      time_period=random.choice(time_periods))
    request = random.choice(filter(requests, tone, mood)).text
    message = message_format.format(problem=problem, request=request)
    
    return message

def get_closing(name, tone, mood):
    text = random.choice(filter(closings, tone, mood)).text
    if text.find('{name}') != -1:
        text = text.format(name=name)
    return text

def build_message(tone, mood):
    f = None
    if isinstance(f, Fragment):
        pass
    name = get_name(tone)
    salutation = get_salutation(tone, mood)
    message = get_message(tone, mood)
    closing = get_closing(name, tone, mood)
    
    if closing.strip() != '':
        message += '\n\n'
   
    return '{salutation}{message}{closing}'.format(salutation=salutation, message=message, closing=closing)

def main(argv):    
    tone = random.choice(tones)
    mood = random.choice(moods)    
    print 'Tone: {tone}, Mood: {mood}\n'.format(tone=tone, mood=mood)    
    print build_message(tone, mood)

if __name__ == "__main__":
    main(sys.argv[1:])