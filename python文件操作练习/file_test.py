f = open ("stock_data", "r",encoding="utf-8")
query_columns = ["最新价", "涨跌幅", "换手率"]
columns = f.readline().strip().split(',')
stock_data = {}

for line in f:
    line = line.strip().split(',')
    name = line[2]
    stock_data[name] = line # 创建股票数据dict{name：data...}

while True:
    count = 0
    cmd = input("输入查询指令>>:").strip()
    if len(cmd) == 0:
        continue
    print(columns)
    for s_name in stock_data:
        if cmd in s_name:
            print(stock_data[s_name])
            count += 1

    if ">" in cmd:
        q_name,q_val = cmd.split('>')
        q_name = q_name.strip()
        q_val = float(q_val)
        if q_name in query_columns:
            q_name_index = columns.index(q_name)
            for s_name,s_vals in stock_data.items():
                if float(s_vals[q_name_index].strip('%')) > q_val:
                    print(s_vals)
                    count += 1
    elif "<" in cmd:
        pass
    if count > 0:
        print("匹配到%s条" % count)