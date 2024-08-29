import pymupdf

doc = pymupdf.open("pdf/test.pdf")

first_page = doc.load_page(0)
text = first_page.get_text()

out = open("output.txt", "wb")

for page in doc:
    text = page.get_text().encode("utf8")
    out.write(text)
    out.write(bytes((12,)))

out.close()
