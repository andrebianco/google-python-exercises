#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++

    filehtml = open(filename, 'r')
    doc = filehtml.read()

    year = re.search(r'<input type="text" name="year" id="yob" size="4" value="(.*?)">', doc, re.S).group(1).split(' ')[-1]
    babynamesdata = [year]

    table = re.search(r'<th scope="col" bgcolor="pink" width="41%">Female name</th></tr>.*?<tr><td colspan="3"><small>',
                      doc, re.S).group(0)[64:-27]

    table = list(set(table.split('\n')))

    listnames = list()

    for row in table:
        if len(row) > 5:
            datarow = (re.findall(r'<tr align="right"><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>', row, re.S))
            malename = datarow[0][1] + ' ' + datarow[0][0]
            femalename = datarow[0][2] + ' ' + datarow[0][0]
            babynamesdata.append(malename)
            babynamesdata.append(femalename)

    babynamesdata.sort()

    return babynamesdata


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

        for i in range(0, len(args)):
            print(extract_names(args[i]))

        # +++your code here+++
        # For each filename, get the names, then either print the text output
        # or write it to a summary file


if __name__ == '__main__':
    main()
