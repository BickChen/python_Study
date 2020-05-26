from openpyxl import Workbook
"""
10： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
  "1":["张三",150,120,100],
  "2":["李四",90,99,95],
  "3":["王五",60,66,68]
}
存储到xlsx文件里
"""
with open("student", encoding='utf-8') as file_obj:
    content = file_obj.read()
content = eval(content)

wb = Workbook()
ws = wb.active
for i in content:
    list_info = content[i]
    list_info.insert(0, i)
    ws.append(list_info)
path = './student.xlsx'
wb.save(path)
