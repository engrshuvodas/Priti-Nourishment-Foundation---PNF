import sys
import pypdf
with open(sys.argv[1], 'rb') as file:
    reader = pypdf.PdfReader(file)
    for i, page in enumerate(reader.pages):
        print(f"\n--- Page {i+1} ---\n")
        print(page.extract_text())
