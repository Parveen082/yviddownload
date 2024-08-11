import pdf2docx

def pdf_to_docx(pdf_file, docx_file):
   
    converter = pdf2docx.Converter(pdf_file)
    converter.convert(docx_file)

# Example usage
pdf_file = 'input.pdf'
docx_file = 'output.docx'
pdf_to_docx(pdf_file, docx_file)