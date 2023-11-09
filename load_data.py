import json
import connect
from models import Author, Quote

with open('authors.json', 'r', encoding='utf-8') as author_file:
    authors_data = json.load(author_file)

with open('quotes.json', 'r', encoding='utf-8') as quote_file:
    quotes_data = json.load(quote_file)


for author_info in authors_data:
    author = Author(**author_info)
    author.save()

for quote_info in quotes_data:
    author = Author.objects(fullname=quote_info['author']).first()
    if author:
        quote_info['author'] = author
        quote = Quote(**quote_info)
        quote.save()
