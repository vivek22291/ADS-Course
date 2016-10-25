import glob
import os
import io
import PyPDF2
import csv
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
i=0
token=[]
path = 'D:\Scrapper2\\'

for filename in glob.glob(os.path.join(path, '*.pdf')):
    filePath = open(filename, 'rb')
    #breaking paths
    token = filename.split('\\')
    fToken=token[-1].split('.')
    #Parameters for Reading PDFs
    codec = 'utf-8'
    retString=io.StringIO()
    laparameters = LAParams()
    resourceManager = PDFResourceManager()
    device = TextConverter(resourceManager, retString, codec=codec, laparams=laparameters)

    interpreter = PDFPageInterpreter(resourceManager, device)
    fileToWrite =fToken[0]+".txt"
    fileToWriteCSV=fToken[0]+".csv"
    baseLocationText="D:\Scrapper2\TextFolder\\"+fileToWrite
    baseLocationCSV="D:\Scrapper2\CSVs\\"+fileToWriteCSV
    #Traversing the pages
    for page in PDFPage.get_pages(filePath):
        interpreter.process_page(page)
        data = retString.getvalue()
    #Opening a text file to convert PDF to Text
    file = open(baseLocationText,'w')
    file.write(data)
    file.close()

#Read the text file and Open the CSV file to write
    reads=open(baseLocationText,"rt")
    with open(baseLocationCSV,"w") as out_file:
     for line in reads:
      listwords=line.split("   ")
      while '' in listwords[1:]:
        listwords.remove('')
      out_csv = csv.writer(out_file)
      out_csv.writerow(listwords)
     out_file.close()


