import pymysql, datetime, xlwt, oss2

"""
pip install pymysql
pip install xlwt
pip install cryptography
pip install oss2
解决：RuntimeError: cryptography is required for sha256_password or caching_sha2_password
如果用crontab定时执行程序不能使用相对路径
"""

def get_data(cur, sql):
    try:
        cur.execute(sql)
        return cur.fetchall()
    except Exception as e:
        with open(current_time + 'sql.log', 'w') as log_file:
            log_file.write(e)


def excel_save(field_list, file_name, sql_data):
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('Sheet1')
    for i in range(0, len(field_list)):
        sheet.write(0, i, field_list[i])
    start_row_num = 1
    for data in sql_data:
        start_col_num = 0
        for line in data:
            sheet.write(start_row_num, start_col_num, line)
            start_col_num +=1
        start_row_num +=1
    local_file_path = './data/' + file_name + str(thismonthtoday) + '.xls'
    wb.save(local_file_path)
    oss_file_path = 'data/' + file_name + str(thismonthtoday) + '.xls'

    with open(local_file_path, 'rb') as file_data:
        bucket.put_object(oss_file_path, file_data)


def run(file_dic):
    for file_id in file_dic:
        cur = db.cursor()
        sql = file_dic[file_id][2]
#        print(sql)
        data = get_data(cur, sql)
#        print(data)
        excel_save(file_name=file_dic[file_id][0], field_list=file_dic[file_id][1], sql_data=data)


if __name__ in '__main__':
    try:
        db = pymysql.connect('xxx', 'xxx', 'xxx', 'xxx', charset='utf8')
        thismonthtoday = datetime.date.today() + datetime.timedelta(days= -1)
        current_time = "'%s'"%(thismonthtoday)

        total_sql = """SELECT a.accountid, t.nickname, t.phone, COUNT(*) AS count FROM self_event_team_call_log a LEFT JOIN users t ON a.accountid = t.accountid GROUP BY a.accountid ORDER BY count DESC;"""
        current_sql = """SELECT a.accountid, t.nickname, t.phone, COUNT(*) AS count, %s FROM self_event_team_call_log a LEFT JOIN users t ON a.accountid = t.accountid WHERE LEFT (a.update_time, 10) = %s GROUP BY a.accountid ORDER BY count DESC;"""%(current_time, current_time)

        file_dic = {1: ['total_surface', ['user_id', 'user_name', 'user_phone', 'count'], total_sql],
                    2: ['current_surface', ['user_id', 'user_name', 'user_phone', 'count', 'time'], current_sql]
                    }

        endpoint = 'oss-cn-beijing.aliyuncs.com'
        auth = oss2.Auth('xxx', 'xxx')
        bucket = oss2.Bucket(auth, endpoint, 'xxx')

        run(file_dic)
        db.close()
    except Exception as e:
        with open('./logs/mysql_export.log', 'w') as log_file:
            log_file.write(e)

