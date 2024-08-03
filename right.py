file = open("simple.txt", 'r')
content = file.read()
file.close()
print(f"content of 'simple.txt':{content}")