#!/usr/bin/python
# -*- coding: UTF-8 -*-

import glob
import csv

"""Grab the country-codes out of already existing txt-files which
contain the results of 'whois' and write them in a csv-file ordered
descending by occurance"""

# define an empty list to store the temporary results
country_list = []

# assuming that every file containing the whois-data has a filename
# of the type in the brackets of glob.glob
for file in glob.glob('whois*.txt'):
    with open(file) as source:
        data = source.readlines() # all the lines will be read at once
        for line in data:
            line = line.strip()
            # we want only the lines starting with "country:"
            if line.startswith('country:') or line.startswith('Country:'):
                country_list.append(line)

#defining an empty dictionary for counting the country-codes
lst = {}

# looping through the list, splitting them and exctracting only the country-code
for item in country_list:
    pieces = item.strip().split(":")
    c_code = pieces[1].strip()
    # print(c_code) # for debugging purposes
    lst[c_code] = lst.get(c_code, 0) + 1

# creating an empty list as "hitlist"
hitlist = []

# loop through the dictionary, write the tuples within the created list with the count
# as the first entry followed by the corresponding country-code
for c_code, count in lst.items():
    hitlist.append((count, c_code))

# sort the hitlist in descending order based on how often the ip-address was detected
hitlist.sort(reverse=True)

# write results in a csv-file
target = open("countries.csv", "w")
for item in hitlist:
    csv.writer(target).writerow(item)

last_row = [len(country_list), "Total"]
csv.writer(target).writerow(last_row)

target.close() # close the target-file when work is done
