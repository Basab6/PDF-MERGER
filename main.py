import PyPDF2


pdf_files=["pdf1.pdf","pdf2.pdf"]
merger=PyPDF2.PdfMerger()

for filenames in pdf_files:
    pdfFile=open(filenames,'rb')
    pdfreader=PyPDF2.PdfReader(pdfFile)
    merger.append(pdfreader)

pdfFile.close()
merger.write('merged.pdf')




