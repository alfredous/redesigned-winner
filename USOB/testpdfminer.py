import os
import pdfminer
print(pdfminer.__version__)
##from pdfminer.pdfinterp import PDFResourceManager, process_pdf
##from pdfminer.converter import TextConverter
myfile = os.path.join('C:\\USOB', 'F.pdf.pdf')
print (myfile)
fp = open(myfile, 'rb')
outfp = open('C:\\USOB\\F.txt', 'wb')
rsrc = PDFResourceManager()
pdfminer
device =TextConverter(rsrc, outfp)

process_pdf(rsrc, device, fp, maxpages=2)

fp.close()
outfp.close()