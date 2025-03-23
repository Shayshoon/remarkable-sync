# Remarkable sync
This script automatically converts PDF files into `.rmdoc` files.\
It's made out of two tools. [Drawj2d](https://sourceforge.net/p/drawj2d/wiki/reMarkable/) is used to convert single-page PDF files to `.rmdoc` format, and [`rmcat`](https://github.com/kg4zow/rm2-scripts/tree/main/rmcat) is a perl script that merges the result files into a single multipage `.rmdoc`.\
I plan to clean this up someday and host it on some cloud server so I can use upload files to my remarkable tablet from the web. That way it would be easy to use either PC or mobile to sync files.

## Usage
To use this script, first you need java, perl and python installed.\
Then you can install pythons requirements using `pip install -r requirements.txt`.\
To run the script, use `python ./pdf2rmdoc.py <YOUR-PDF>.pdf`. You should see files being created and removed from the working directory, these are the split pages. The result `.rmdoc` file will be named like the input file, only with `.rmdoc` extension of course.

You can sync the resulting `.rmdoc` files with the remarkable tablet like any other document, through the app or api or usb...
