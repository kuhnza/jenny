'''
Created on 29/04/2011

@author: dave
'''

class Fragment():
        
    def __init__(self, text='', tones=None, moods=None, subject=None):
        self.text = text
        self.tones = [] if tones == None else tones
        self.moods = [] if moods == None else moods
        self.subject = '' if subject == None else subject

def filter(fragments, tone, mood):
    filtered = []
    for f in fragments:
        if (tone in f.tones) and (mood in f.moods):
            filtered.append(f)
            
    return filtered

tones = ['formal', 'informal']

moods = ['extremely negative', 'very negative', 'negative', 'neutral', 'positive', 'very positive'] 

subjects = [
    'General enquiry',
    'Billing and accounts',
    'Complaint',
    'Item not received',
    'Damaged goods',
    'Other'
]

message_format = '{problem} {request}'

problems = [
    'You\'re {adjective} website {repetition} crashes on me when I\'m {action}.',
    'It\'s been {time_period} since I placed my order and it still hasn\'t arrived.'
]

requests = [
    Fragment('Please help me, I\'m not sure what to do about this.', ['formal', 'informal'], ['negative', 'neutral', 'positive', 'very positive']),
    Fragment('Fix it before I call my lawyer.', ['formal', 'informal'], ['angry']),
    Fragment('You owe me assholes! I\'m going to make a YouTube video about how lame you guys are.', ['informal'], ['angry']),
]

adjectives = [
    Fragment('', ['formal', 'informal'], ['happy', 'neutral']),
    Fragment('stupid', ['formal', 'informal'], ['angry']),
    Fragment('bloody', ['informal'], ['angry']),
    Fragment('awful', ['formal', 'informal'], ['angry']),
    Fragment('horrendous', ['formal', 'informal'], ['angry']),
    Fragment('terrible', ['formal', 'informal'], ['angry']),
    Fragment('pain in the ass', ['informal'], ['angry']),
    Fragment('occasionally intermittent', ['informal'], ['angry', 'neutral']),
    Fragment('mediocre', ['informal'], ['angry', 'neutral']),
    Fragment('usually helpful', ['informal'], ['happy', 'neutral']),
    Fragment('usually wonderful', ['informal'], ['happy', 'neutral']),
    Fragment('mostly fabulous', ['informal'], ['happy']),
    Fragment('normally top-notch', ['informal'], ['happy']),
    Fragment('good', ['formal', 'informal'], ['happy']),
    Fragment('great', ['formal', 'informal'], ['happy'])
]

repetitions = [
    '',
    'never',
    'usually never',
    'sometimes',
    'occasionally',
    'frequently',
    'almost always',
    'always'
]

time_periods = [
    '3 days',
    '4 days',
    '5 days',
    'a week',
    'almost two weeks',
    'over two weeks',
    'a whole month'
]

actions = [
    'attempting to sign up',
    'browsing the store',
    'making a purchase'
]

names = {
    'first': ['Robert', 'Mary', 'John', 'Janette', 'Brett', 'Marcus', 'Remi', 'Belinda', 'Lauren', 'Simon'],
    'last': ['Robbins', 'Johnson', 'Brown', 'Doe', 'Jefferson', 'Litton', 'Terman', 'Ball', 'Bronson', 'Zelke']
}