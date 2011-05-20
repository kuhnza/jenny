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

from classes import *

tones = ['formal', 'informal']
TF = tones[0]
TI = tones[1]

moods = ['extremely negative', 'very negative', 'negative', 'neutral', 'positive', 'very positive'] 
EN = moods[0]
VN = moods[1]
N  = moods[2]
NE = moods[3]
P  = moods[4]
VP = moods[5]

expansions = {}

#
#Message Structures
#
expansions['message'] = [
    Fragment('{complaint}', [TI], [EN, VN, N, NE]),
    Fragment('{complaint}\n\n{closing}', [TF, TI], [EN, VN, N, NE]),
    Fragment('{salutation}\n\n{complaint}', [TF, TI], [EN, VN, N, NE]),
    Fragment('{salutation}\n\n{complaint}\n\n{closing}', [TF, TI], [EN, VN, N, NE]),
    Fragment('{salutation}\n\n{complaint}\n\n{compliment}\n\n{closing}', [TF, TI], [N, NE, P]),
    Fragment('{salutation}\n\n{compliment}\n\n{complaint}\n\nThat aside, {compliment}\n\n{closing}', [TF, TI], [N,   NE, P]),
    Fragment('{question}', [TI], [NE, P, VP]),
    Fragment('{question}\n\n{closing}', [TI], [NE, P, VP]),
    Fragment('{salutation}\n\n{question}\n\n{closing}', [TF, TI], [NE, P, VP]),
    Fragment('{salutation}\n\n{compliment}\n\n{closing}', [TF, TI], [P, VP])
]

expansions['salutation'] = [
    Fragment('', [TI], [EN, VN, N, NE]),
    Fragment('To Whom It May Concern:', [TF], [P, VP, EN, VN, N, NE]),
    Fragment('Hi,', [TI], [P, VP, EN, VN, N, NE]),
    Fragment('Hi there,', [TI], [P, VP]),
    Fragment('Hey,', [TI], [P, VP, NE]),
    Fragment('Hello,', [TI, TF], [P, VP, EN, VN, N, NE]),
    Fragment('Good morning,', [TI, TF], [P, VP]),
    Fragment('Good afternoon,', [TI, TF], [P, VP])
]

expansions['closing'] = [
    Fragment('', [TI], [P, VP, EN, VN, N, NE]),
    Fragment('{name}', [TF, TI], [P, VP, EN, VN, N, NE]),
    Fragment('Sincerely,\n{name}', [TF], [P, VP, EN, VN, N, NE]),
    Fragment('Regards,\n{name}', [TF], [P, VP, EN, VN, N, NE]),
    Fragment('Best regards,\n{name}', [TF], [P, VP]),
    Fragment('Thank you,\n{name}', [TF], [P, VP]),
    Fragment('Cheers,\n{name}', [TI], [P, VP, NE]),
    Fragment('Thanks', [TI], [EN, VN, N, P, VP, NE]),
    Fragment('Thanks,\n{name}', [TI], [P, VP, NE])
]

expansions['complaint'] = [
    Fragment('I am unhappy with your {service}. {symptom}', [TI], [VN, N, NE]),
    Fragment('Your {service} is terrible. {symptom} {threat}', [TI, TF], [EN, VN, N]),
    Fragment('What is wrong with your {service}?! {symptom} {threat}', [TI, TF], [EN, VN, N]),
    Fragment('My order for {product} still hasn\'t arrived. Can you please give me an update on the status of it?', [TI, TF], [N, NE, P]),
    Fragment('For some reason I can\'t seem to log into your {service}. {symptom} {request}', [TI, TF], [N, NE, P]),
    Fragment('Why does your {service} have to be so damn complicated? All I want to do is {action}, is that really so hard? {threat}', [TI, TF], [EN, VN, N]),
    Fragment('{request} I\'m having a problem with your {service}. {symptom}.', [TI, TF], [VN, N, NE, P]),
    Fragment('I have been waiting on hold now for {duration}. Do you even answer your phones? You should really improve your contact center service, it blows! {request}', [TI], [EN, VN, N]),
    Fragment('{symptom} {request}', [TI, TF], [N, NE, P]),
]

expansions['compliment'] = [
    'Congratulations on providing such a wonderful and convenient service. It is truly an Internet treasure.',
    'Thank you for all your help so far, your staff have been a delight!',
    'You guys are the best, I tell all my friends about how much I love your site. Thanks so much.',
]

expansions['question'] = [
    'Can someone tell me how I go about placing an order?',
    'What\'s your return policy? I just bought {product} for my nephew and he absolutely HATES it. Wondering if I can exchange it for {product}.',
    'Do you deliver internationally? I live in {country} and would really like to order {product} as I can\'t find it anywhere here.',
    'How much does shipping on {product} and {product} cost? Are you able to bundle them together?',
    'Can you please close my account? I am moving to {country} and won\'t have need of your service there.'
]

expansions['symptom'] = [
    'When I log in it gives me a dirty, great big error message! This happens {frequency}.',
    'Even though I\'ve cancelled my order through {service} you guys still charged my credit card.',
    'I\'ve been searching the store for {product} but can\'t find it. It\'s a bestseller so I assume it has to be in stock right?', 
]

expansions['request'] = [
    'Could somebody please help me, I\'m completely lost and don\'t know what to do next.',
    'I just want someone to help me {action}, that\'s all.',
    'How do I go about {action}?',
    'Can you please refund me the correct amount?',
    'Please close my account, I have no further need of this service.'
]

expansions['threat'] = [
    'Fix it before I call {authority}.',
    'If you don\'t fix this immediately I won\'t hesitate to report you to {authority}.',
    'This time you\'ve gone to far! You\'ll be hearing from {authority}, you can count on it.',
    'Give me what I want, or else! You guys are a pack of {insult}.'
    'You better start talking sense you {insult} otherwise I\'m taking my business elsewhere!',
    'I know a lot of people and I plan on telling them all about this little incident.',
    'I\'ve had it up to here with you {insult}. One more problem and I\'m outa here!'
]

expansions['action'] = [
    'make a payment',
    'buy an item',
    'purchase a book',
    'learn how to run a marathon',
    'teach myself to cook',
    'browse',
    'read a book',
    'wash the dog'
]

expansions['service'] = [
    'website',
    'payments system',
    'delivery system',
    'shopping cart',
    'online store',
    'contact center'
]

expansions['duration'] = [
    '10 minutes',
    '30 mintues',
    '45 minutes',
    '1 hour',
    '2 hours',
    '48 hours',
    '3 days',
    'a week',
    '2 weeks',
    'a whole month',
    'almost a year'
]

expansions['frequency'] = [
    'only rarely',
    'only sometimes',
    'every time',
    'every day',
    'most days',
    'every day',
    'at least once a week',
    'every week'
]

expansions['authority'] = [
    'the relevant authority',
    'the ombudsman',
    'my lawyer',
    'the company directors',
    'my mother-in-law'
]

expansions['insult'] = [
    'lousy douchebags',
    'galahs',
    'idiots',
    'morons',
    'dickheads',
    'wankers',
    'monumental fuckups'
]

expansions['product'] = [
    'Gullivers Travels',
    'Humble Pie by Gordon Ramsey',
    'Danielle Steel\'s Wanderlust',
    'How to Win Friend and Influence People',
    'David Allen\'s Getting Things Done',
    'The Belgariad',
    'A Tale of Two Cities by Dickins',
    'Lord of the Rings'
]

expansions['name'] = [
    Fragment('Walter Cronkite', [TF], [EN, VN, N, NE, P, VP]),
    Fragment('Remi Francis', [TF], [EN, VN, N, NE, P, VP]),
    Fragment('Douglas Johnson', [TF], [EN, VN, N, NE, P, VP]),
    Fragment('Pratap Chintoju', [TF], [EN, VN, N, NE, P, VP]),
    Fragment('Margaret Jefferson', [TF], [EN, VN, N, NE, P, VP]),
    Fragment('Art Vandelay', [TF], [EN, VN, N, NE, P, VP]),
    Fragment('Kel Varnsen', [TF], [EN, VN, N, NE, P, VP]),
    Fragment('H.E. Pennypacker', [TF], [EN, VN, N, NE, P, VP]),
    Fragment('Dave', [TI], [EN, VN, N, NE, P, VP]),
    Fragment('Jim', [TI], [EN, VN, N, NE, P, VP]),
    Fragment('Marcus', [TI], [EN, VN, N, NE, P, VP]),
    Fragment('Mary', [TI], [EN, VN, N, NE, P, VP]),
    Fragment('Jane', [TI], [EN, VN, N, NE, P, VP]),
    Fragment('Julia', [TI], [EN, VN, N, NE, P, VP]),
    Fragment('Martin', [TI], [EN, VN, N, NE, P, VP]),
    Fragment('Amber', [TF], [EN, VN, N, NE, P, VP]),
    Fragment('A very angry customer', [TF, TI], [EN, VN]),
    Fragment('A satisfied customer', [TF, TI], [P, VP])
]

expansions['country'] = [
    'Afghanistan',
    'Albania',
    'Germany',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Antilles',
    'Netherlands Antilles',
    'Saudi Arabia',
    'Svalbard',
    'Algeria',
    'Argentina',
    'Armenia',
    'Aruba',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belgium',
    'Belize',
    'Bermuda',
    'Bhutan',
    'Belarus',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina-Faso',
    'Burundi',
    'Cape Verde',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Chad',
    'Chile',
    'China',
    'Cyprus',
    'Vatican City',
    'Colombia',
    'Comoros',
    'Congo',
    'North Korea',
    'South Korea',
    'Costa Rica',
    'Croatia',
    'Cuba',
    'Benin',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'United Arab Emirates',
    'Eritrea',
    'Slovakia',
    'Slovenia',
    'Spain',
    'United States of America',
    'Estonia',
    'Ethiopia',
    'Russian Federation',
    'Malay States',
    'Fiji',
    'Republic of the Philippines',
    'Finland',
    'France',
    'Gabon',
    'Gambia',
    'Georgia',
    'Ghana',
    'Gibraltar',
    'Grenada',
    'Greece',
    'Greenland',
    'Guadeloupe',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Equatorial Guinea',
    'Guiana',
    'French Guiana',
    'Haiti',
    'Honduras',
    'Hong Kong',
    'Hungary',
    'India',
    'Indonesia',
    'Iraq',
    'Iran',
    'Ireland',
    'Isle of Man',
    'Iceland',
    'Channel Islands',
    'Cayman Islands',
    'Cook Islands',
    'Faeroes',
    'Falkland Islands',
    'Northern Mariana Islands',
    'Marshall Islands',
    'Solomon Islands',
    'Turks and Caicos Islands',
    'British Virgin Islands',
    'Wallis and Futuna Islands',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kyrgyzstan',
    'Kiribati',
    'Kuwait',
    'Laos',
    'Lesotho',
    'Latvia',
    'Lebanon',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxemburg',
    'Macao',
    'Macedonia',
    'Madagascar',
    'Malaysia',
    'Malawi',
    'Maldives',
    'Mali',
    'Malta',
    'Morocco',
    'Martinique',
    'Mauritius',
    'Mauritania',
    'Mayotte',
    'Mexico',
    'Micronesia',
    'Monaco',
    'Mongolia',
    'Montserrat',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'New Caledonia',
    'New Zealand',
    'Polynesia',
    'Micronesia',
    'Melanesia',
    'Oman',
    'Netherlands',
    'Pakistan',
    'Palau Islands',
    'Palestine',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Pitcairn Island',
    'French Polynesia',
    'Poland',
    'Portugal',
    'Puerto Rico',
    'Qatar',
    'United Kingdom',
    'Czech Republic',
    'Dominican Republic',
    'Central African Republic',
    'Democratic Republic of the Congo',
    'Rwanda',
    'Romania',
    'Samoa',
    'Saint Christopher-Nevis',
    'Saint Pierre and Miquelon',
    'Saint Vincent and the Grenadines',
    'Saint Helena',
    'Saint Lucia',
    'Senegal',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Syria',
    'Somalia',
    'South Africa',
    'Sri Lanka',
    'Sudan',
    'Sweden',
    'Switzerland',
    'Surinam',
    'Swaziland',
    'Thailand',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'East Timor',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkmenistan',
    'Turkey',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Venezuela',
    'Vietnam',
    'Yemen Republic',
    'Yugoslavia',
    'Zambia',
    'Zimbabwe'
]
