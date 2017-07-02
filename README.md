# geoextractor
This is my first little repository. It contains only a small Python-script.

# Purpose of the script
You have got one textfile or many textfiles containing the results of a whois-lookup, perhaps because you had a look at the logfile of your website and you grabbed all the IP-addresses in there? And now you want to know, from which countries the IP-addresses come? Of course this is not so much work, but this script does it for you.

# Usage
Create a new folder, throw in all the "whois"-files and add the script also.
Then open the Terminal, navigate to that folder and start the script using "python3 geoextractor.py". The result will be afile named "countries.csv".

This file contains two columns: the number of occurance and the abbreviation of the country. The list is sorted bey the number of the occurence of the country-code in descending order. In the last line you see the total.

# Hint
The script processes only those files, whose filenames match the pattern "whois*.txt"
