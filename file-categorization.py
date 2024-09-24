import os
import PyPDF2
from collections import Counter

def categorize_pdf(file_path):
    ran_keywords = ['RAN', 'Radio Access Network', 'eNodeB', 'gNodeB', 'base station']
    core_keywords = ['Core Network', 'EPC', '5GC', 'MME', 'SGW', 'PGW', 'AMF', 'SMF', 'UPF']
    nr_keywords = ['NR', 'New Radio', '5G NR', 'gNB']
    #lte_keywords = ['LTE', 'Long Term Evolution', 'eNodeB', 'EPC']  ##to be evaluated within the TS documents
    #

    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        content = ''
        for page in reader.pages:
            content += page.extract_text().lower()

    ran_count = sum(content.count(keyword.lower()) for keyword in ran_keywords)
    core_count = sum(content.count(keyword.lower()) for keyword in core_keywords)
    nr_count = sum(content.count(keyword.lower()) for keyword in nr_keywords)

    counts = Counter({'RAN': ran_count, 'Core Network': core_count, 'NR': nr_count})
    category = counts.most_common(1)[0][0]

    return category

def categorize_pdfs_in_directory(directory):
    results = {}
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory, filename)
            category = categorize_pdf(file_path)
            results[filename] = category
    return results

pdf_directory = r"/mnt/c/Users/iccl/tim/test3gpp-local/etsi/"
categorization_results = categorize_pdfs_in_directory(pdf_directory)

for filename, category in categorization_results.items():
    print(f"{filename}: {category}")