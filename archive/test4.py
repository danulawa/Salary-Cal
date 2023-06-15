import requests
from PyPDF2 import PdfReader
import re

# Define the URL of the PDF
pdf_url = "https://www.hsbc.lk/content/dam/hsbc/lk/documents/tariffs/foreign-exchange-rates.pdf"

# Send a GET request to fetch the PDF content
response = requests.get(pdf_url)

# Save the PDF locally
with open("exchange_rates.pdf", "wb") as file:
    file.write(response.content)

# Open the PDF file
with open("exchange_rates.pdf", "rb") as file:
    pdf_reader = PdfReader(file)

    # Extract text from each page
    num_pages = len(pdf_reader.pages)
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        page_text = page.extract_text()

        # Search for the USD selling rate
        if "Pound Sterling" in page_text:
            selling_rate_index = page_text.index("Pound Sterling")
            selling_rate_text = page_text[selling_rate_index:]

            matches = re.findall(r"\d+\.\d+", selling_rate_text)

print(matches[1])
