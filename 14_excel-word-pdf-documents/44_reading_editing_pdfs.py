import pypdf

# Opens a PDF with the "read binary" argument (as PDFs are binary data!): -
pdf_file = open("meetingminutes1.pdf", "rb")

# The below code creates a "reader" object for the PDF: -
reader = pypdf.PdfReader(pdf_file)

# Check how many pages: -
print(len(reader.pages))

# Extract text from a page: -
page = reader.pages[0]
print(page.extract_text())

# # Extract text from all pages: -
# for page_num in range(len(reader.pages)):
#     print(reader.pages[page_num].extract_text())

# Combine 2 PDF files into one: -
pdf_file_1 = open("meetingminutes1.pdf", "rb")
pdf_file_2 = open("meetingminutes2.pdf", "rb")
# Creating reader objects for both PDFs: -
reader_1 = pypdf.PdfReader(pdf_file_1)
reader_2 = pypdf.PdfReader(pdf_file_2)
# Creating writer object to create a new PDF: -
writer = pypdf.PdfWriter()
# Code to loop through pages and add them to the new PDF: -
for page_num in range(len(reader_1.pages)):
    page = reader_1.pages[page_num]
    writer.add_page(page)
for page_num in range(len(reader_2.pages)):
    page = reader_2.pages[page_num]
    writer.add_page(page)

# Creating a new file on disk to write the new PDF to: -
output_file = open("combined_minutes.pdf", "wb")
# Saving the PDF file in program memory to disk: -
writer.write(output_file)

# Closing original PDFs: -
pdf_file_1.close()
pdf_file_2.close()