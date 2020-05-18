file_name = 'stock_data'
screen = ["最新价", "涨跌幅", "换手率"]
f = open(file_name, 'r', encoding="UTF-8")
keys = f.readline().strip().split(',')
number = 0
while True:
    user_input = input("股票查询接口>>: ")
    for line in f:
        line = line.strip().split(',')
        dic = dict(zip(keys, line))
        print(dic)
#        print(dic)
        if '>' in user_input:
            q_name, q_val = user_input.split('>')
            if q_val.isdigit() and q_name in screen:
                q_val = int(q_val)
                condition = dic[q_name]
                condition = int(float(condition))
                if condition > q_val:
                    print(line)
                    number += 1
            else:
                print('您输入的筛选条件不支持！')
                break
        elif '<' in user_input:
            q_name, q_val = user_input.split('>')
            if q_val.isdigit() and q_name in screen:
                q_val = int(q_val)
                condition = dic[q_name]
                condition = int(float(condition))
                if int(dic[q_name]) < q_val:
                    print(line)
                    number += 1
            else:
                print('您输入的筛选条件不支持！')
                break
        else:
            if user_input in dic['名称']:
                print(line)
                number +=1
    print('找到%d条'%number)
    number = 0
