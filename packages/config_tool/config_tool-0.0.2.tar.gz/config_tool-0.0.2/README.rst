config_tool (A simple configuration management tool for JSON files)
===================================================================

#The MIT License (MIT)
#Copyright (c) 2016 Sam Caldwell.
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to 
#deal in the Software without restriction, including without limitation the
#rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#sell copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
#IN THE SOFTWARE.


config-tool is a simple configuration management tool for JSON files.
This tool allows the user to easily read, write and validate a JSON
file from command line as well as from a python script which imports
the Config class.



============================
USAGE (FROM THE COMMANDLINE)
============================



Given a configuration file (sample.json):

-----------------------------------------

{
    "foo":{
        "bar":1
    }
}

-----------------------------------------




We can create a shell script (reader.sh) like this:

---------------------------------------------------

#!/bin/bash

foo_bar="$(config --read --key foo.bar --config ./sample.json)"

echo "foo.bar:$foo_bar"

---------------------------------------------------




Executing this script will return this:

---------------------------------------

root# reader.sh

foo.bar:1

---------------------------------------


