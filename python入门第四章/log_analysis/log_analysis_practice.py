import re
file = open('web_logs.txt')
data = file.read()
print(re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', data))