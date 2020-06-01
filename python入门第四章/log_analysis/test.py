import re
# file = open("web_logs.txt")
# file_line = file.readline()
# print(file_line)
# # data_list = re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', file_line)
# file_list = re.findall("(?<![\/(?:\d{1,3}\.){3}\d{1,3}])(?:\d{1,3}\.){3}\d{1,3}", file_line)
# file.close()
# print(file_list)

# print(re.findall("(?=test)", "pythonretest"))

file = open("web_logs.txt")
file_line = file.readline()
print(file_line)
#可以获取IP地址
# file_list = re.search("(?P<IP>(?<![\/(?:\d{1,3}\.){3}\d{1,3}])(?:\d{1,3}\.){3}\d{1,3})", file_line).group()
# print(file_list)
#可以获取时间
# file_list = re.search("(?P<Time>\d{4}\:\d{2})", file_line).groupdict()
# print(file_list)
#不能同时获取IP地址和时间,因为IP地址和时间不是相连的所以无法匹配到数据
# file_list = re.search("(?P<IP>(?<![\/(?:\d{1,3}\.){3}\d{1,3}])(?:\d{1,3}\.){3}\d{1,3})(?P<Time>\d{4}\:\d{2})", file_line)
# print(file_list)

# file_A = re.findall("Android", file.read())
# print(len(file_A))
# file.seek(0)
# file_I = re.findall(r"iPhone OS", file.read())
# print(len(file_I))
# file.seek(0)
# file_W = re.findall(r"Windows NT", file.read())
# print(len(file_W))
# file.seek(0)
# file_M = re.findall(r"Intel Mac OS", file.read())
# print(len(file_M))
# file_D = re.findall(r"iPad", file.read())
# print(len(file_D))
# total = len(file_A) + len(file_I) + len(file_W) + len(file_M) + len(file_D)
# print(total)

# Mozilla/5.0 (Linux; Android 8.1.0;
# file.seek(0)
# equipment = re.findall(r"Mozilla/5.0..\w{5}.........", file.read())
# equipment = set(equipment)
# print(equipment)