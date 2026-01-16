# CM is way to manage resource using "with" statement and ensures file automatically closed even if error occurs.

with open("file.txt", "r") as f:
    data = f.read()
    print(data)