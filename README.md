# LinesOfCodeCounter
A simple python script that counts the number of lines of code in your project. Can filter by file type.

Ever wonder how many lines of code your project has grown to? Well now you can find out! Simply provide the script your root directory and the file types to include and it will calculate the total lines of code in your project

# Usage
To run from command prompt:
* python LinesOfCodeCounter.py [root_dir] [file_types_to_count]
* [root_dir] the relative/absolute path to the root directory containing your project
* [file_types_to_count]  a comma separated list of file extensions to include in the count.

Example count lines of code in .c, .py and .h files with current directory as root:
python LinesOfCodeCounter.py . .c,.py,.h

OR

Run the python script and enter the directory and file types when requested.

## Copyright & License

Copyright 2016 Krugaroo 

License: MIT License

Copyright (c) 2016 Michael Kruger, Krugaroo Interactive Technology

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE
