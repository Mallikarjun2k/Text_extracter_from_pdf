from PyPDF2 import PdfFileReader, PdfFileWriter

file_path = 'Infosys Paper.pdf'
pdf = PdfFileReader(file_path)

with open('New text file.txt', 'w') as f:
    for page_num in range(pdf.numPages):
        pageObj = pdf.getPage(page_num)

        try: 
            txt = pageObj.extractText()
            print(''.center(100, '-'))
        else:
            f.write('Page {0}\n'.format(page_num+1))
            f.write(''.center(100, '-'))
            f.write(txt)
    f.close()