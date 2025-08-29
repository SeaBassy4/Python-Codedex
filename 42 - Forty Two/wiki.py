import wikipedia

# Search for a page
result = wikipedia.summary("Python (programming language)", sentences=2)

print(result)