Benjamin Ferraro -- Releaf Coding Assignment

This python script parses allAfrica.com's 141 RSS feeds, and scrubs each article link within the feeds.
This comes out to just over 3300 total articles scrubbed.

After reading all of the company names in the first column of rev_rest_africa.xlsx, I sanitize the articles html page and see if any of the company names appear within the html page. If so, I add the current artical's URL to a dictionary of URLs for each company. 
Finally, I write these URLs to rev_rest_africa.xlsx.

I used several python libraries in order to carry out this task, all of which are included in the script's directory. 

HOW TO RUN:
1. Open a terminal window and change to the ReleafChallenge/ directory
2. chmod 700 installLibs.command
3. ./installLibs.command - this will install all of the needed libraries
4. python ReleafChallenge.py
	- The current RSS feed and article being parsed is printed out to the console window. Once it is done running, all of the URLs will have been added to the .xlsx file.


NOTE: After scrubbing all RSS articals, I recieved no results for any of the orignal companies given in rev_rest_africa.xlsx.
	  I went and looked for some company names mentioned in various articals on allAfrica.com, here is what I added to the excel file:
	  
African Development Bank
Stanbic Bank Uganda
British American Tobacco 
Bank of Baroda
National Insurance Corporation
Uganda Clays 
World Food Programme
Thomson Reuters Foundation
FIFA
Tibet Hima Mining
Zimbabwe Environmental Law Association