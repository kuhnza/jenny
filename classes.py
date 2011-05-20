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

class Fragment():
        
    def __init__(self, text='', tones=None, moods=None, subject=None):
        self.text = text
        self.tones = [] if tones == None else tones
        self.moods = [] if moods == None else moods
        self.subject = '' if subject == None else subject
        
    def __str__(self):
        return self.text
