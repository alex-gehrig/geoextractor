# geoextractor
This is my first little repository. It contains only a
small Python-script.

# Purpose of the script
You have got a bunch of textfiles containing the
results of a whois-lookup, perhaps because you had a look
at the logfile of your website and you grabbed all the
IP-addresses in there? And now you want to know, from
which countries the IP-addresses come from? Of course
this is not so much work, but this script does it for you.

# Usage
Create a new folder, throw in all the "whois"-files (each
containing the result of a whois-lookup of one IP-address)
and add the script also.

Then open the terminal, navigate to that folder and start
the script using

`python3 geoextractor.py`

The result will be a file named "countries.csv".

This file contains two columns: the number of occurance and
the abbreviation of the country. The list is sorted by
the number of the occurance of the country-code in
descending order. In the last line you see the total.

The script only uses the first country-code to be found,
as this is usually the physical location of the server.

# Hint
The script processes only those files, whose filenames
match the pattern "whois*.txt"
