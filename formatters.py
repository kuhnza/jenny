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

def get_formatter(format):
    """Factory function for obtaining new formatter objects."""
    if format == 'plain':
        return PlainFormatter()
    elif format == 'pretty':
        return PrettyFormatter()
    elif format == 'csv':
        return CSVFormatter()
    else:
        raise FormatterDoesNotExistError('Formatter: %s does not exist.' % format)

class FormatterDoesNotExistError(Exception):
    pass

class Formatter(object):
    
    def format(self, obj):
        raise NotImplementedError()
    
class PlainFormatter(Formatter):
    
    def format(self, obj):
        return obj.__str__()
    
class PrettyFormatter(Formatter):
    
    def format(self, obj):
        s = []
        s.append('Tone: {tone}, Mood: {mood}\n\n'.format(tone=obj.tone, mood=obj.mood))
        s.append(obj.text)
        s.append('\n--------\n')    
        return ''.join(s)
    
class CSVFormatter(Formatter):
    
    def format(self, obj):
        raise NotImplementedError()