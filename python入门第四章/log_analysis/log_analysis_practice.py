import re
log_name = 'web_logs.txt'

def log_ip_list(log_name):
    file = open(log_name)
    data = file.read()
    data_list = re.findall("(?<![\/(?:\d{1,3}\.){3}\d{1,3}])(?:\d{1,3}\.){3}\d{1,3}", data)
    file.close()
    return data_list

def every_day_pv_uv(log_name):
    data_list = log_ip_list(log_name)
    pv = len(data_list)
    data_set = set(data_list)
    uv = len(data_set)
    return pv, uv

# pv_data, uv_data = every_day_pv_uv(log_name)
# print("PV数为：%d UV数为：%d"%(pv_data, uv_data))

def every_hour_pv_uv(log_name):
    file = open(log_name)
    date_set = set(re.findall("\d{4}\:\d{2}",file.read()))
    for i in sorted(date_set):
        file.seek(0)
        pv_date_list = []
        for line in file:
            if i in line:
                a = re.findall("(?P<IP>(?<![\/(?:\d{1,3}\.){3}\d{1,3}])(?:\d{1,3}\.){3}\d{1,3})", line)
                if len(a):
                    pv_date_list.append(str(a[0]))
        uv_date_set = set(pv_date_list)
        print("%s PV数为：%s UV数为：%s"%(i,len(pv_date_list), len(uv_date_set)))
    file.close()

# every_hour_pv_uv(log_name)

def top10_uv(log_name):
    pv_data_list = log_ip_list(log_name)
    uv_data_set = set(pv_data_list)
    uv_data_dic = {}
    for i in uv_data_set:
        uv_data_dic[pv_data_list.count(i)] = i
    top10_uv_data = sorted(uv_data_dic.keys())[-10:]
    top10_uv_data = top10_uv_data[::-1]
    number = 1
    for k in top10_uv_data:
        print("top%d的UV IP是：%s   点击数为：%d "%(number,uv_data_dic[k],k))
        number +=1


# top10_uv(log_name)






