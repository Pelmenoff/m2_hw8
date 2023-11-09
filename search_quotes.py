from models import Quote
import connect

while True:
    command = input("/// Enter a command (e.g., name: Steve Martin, tag:life, tags:life,live, exit): ")

    if command == 'exit' or command == 'q':
        break

    parts = command.split(':')
    if len(parts) != 2:
        print("/// Invalid command format. Please use format 'command: value'.")
        continue

    query_type, value = parts
    query = {}

    if query_type == 'name':
        query['author__fullname'] = value
    elif query_type == 'tag':
        query['tags'] = value
    elif query_type == 'tags':
        query['tags__in'] = value.split(',')

    quotes = Quote.objects(**query)

    if quotes:
        for quote in quotes:
            print(f"/// Author: {quote.author.fullname}, Quote: {quote.quote}, Tags: {', '.join(quote.tags)}")
    else:
        print("/// No quotes found for the given criteria.")
