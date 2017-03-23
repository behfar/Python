__author__ = 'bastanib'

import csv

filename = 'Citrix US grants as of 20150630.csv'
patents = {}

with open(filename, 'r', encoding='utf-8') as f:
  reader = csv.DictReader(f)
  count = 0
  for row in reader:
    patents[row['Patent']] = row
    count = count + 1

  print(count)


