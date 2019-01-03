import csv
import sys
import os

myfile = os.path.join('C:\\USOB', 'F.pdf.pdf')
print (myfile)

directory_with_files_of_interest = "'C:\\USOB"
file_to_convert_to_txt = "F.pdf.pdff"
converted_filename = "F.pdf.pdf.txt"
#scroll over so you don't miss cut off text here
os.system("python pdfminer-20140328/tools/pdf2txt.py -o %s %s/%s" %(converted_filename, directory_with_files_of_interest, file_to_convert_to_txt))

#take a look at the contents
file = open("%s" %(converted_filename), "rt")
for line in file:
     print(line)