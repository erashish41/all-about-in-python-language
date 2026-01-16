with open('file.txt', 'r') as f:
    data = f.read()
    
f = open('file.txt', 'r')
try:
    data = f.read()
finally:
    f.close()