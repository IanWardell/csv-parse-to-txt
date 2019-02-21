# csv-parse-to-txt
Author: Ian A. Wardell

Description: This script intakes a.csv file and outputs the columns into a.txt file; parse a user specified CSV file into one .txt per row

Usage: 
In Bash ./csv_to_txt.py -f sample.csv

Requirements: 
- input file must be a .csv file 
- input file must NOT include column headings 
- column headings must be in the following format:
referencenumber,House/senate,first,last,district,state,party,title,link,title,cleantext,date,tone(manual),criticismtype,Political/Regular,Counter-majoritarian,Democratic Process,Other

How to convert .xlsx (Microsoft Excel) to .csv:
File -> Save As -> Select 'CSV UTF-8 (comma delimated) (*.csv)' from drop down -> Save 

Steps to use:
1) Delete column heading row from the Excel file 
2) Convert .xlsx to .csv
3) Run the python script ./csv_to_txt.py -f sample.csv
4) Open the output folder to view results
