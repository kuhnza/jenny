Jenny - The Moody Message Generator
===================================

About Jenny
-----------

Jenny is a command-line application that can be used to randomly generate a corpus of messages with variable content and tone.

Usage
-----

It's real easy. Just type `python main.py [# messages]` at the prompt and Jenny will spit out the required number of messages to the console. If you want to change the output format to csv then use the `-f --format` flag followed by the format (e.g. csv).

Grammers
--------

Jenny creates messages based on statements contained in `grammers.py`. If you wish to expand the range of possible messages or change the types of messages then simply add to/edit this file. Substitutions are denoted by curly braces (i.e.`{` and `}`).
 
