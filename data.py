import codecs

with codecs.open('001.txt', 'r', 'utf-8') as file:
    
    content = file.read()
    
    print(content)
    
    