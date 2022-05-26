#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
#python3 /home/riyaz/git/summary.txt file /home/riyaz/Downloads/google-python-exercises/babynames/baby1990.html
#./baby3.py /home/riyaz/git/summary.txt file /home/riyaz/Downloads/google-python-exercises/babynames/baby1990.html
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise
[1-9] [0-9]*
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
  d = {}
  list_ = []
  file_ = open(filename, 'r')
  text = file_.read()
  match = re.search(r'(Popularity\sin\s)(\d{4})', text)
  print (match.group(2))
  name_rank = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
  for rank,name1,name2 in name_rank:
    first = name1 + ' ' + rank
    second = name2 + ' ' + rank
    list_.append(first)
    list_.append(second)
  s = [match.group(2)] + sorted(list_)
  file_.close()
  return s
  

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  filename = args[1]
  print(filename)
  summary_filename = "summary_"+filename+".txt"
  extracted_names = extract_names(filename)
  file_ = open(summary_filename, 'w')
  file_.write('\n'.join(extracted_names))
  print(file_)
  
  file_.close()
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()

