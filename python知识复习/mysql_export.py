import pymysql, datetime, xlwt

"""
pip install pymysql
pip install xlwt
pip install cryptography
解决：RuntimeError: cryptography is required for sha256_password or caching_sha2_password
"""

def get_data(cur, sql):
    try:
        cur.execute(sql)
        return cur.fetchall()
    except Exception as e:
        with open(current_time + 'sql.log', 'w') as log_file:
            log_file.write(e)

def excel_save(*args, file_name, sql_data):
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('Sheet1')
    for i in range(0, len(args)):
        sheet.write(0, i, args[i])
    start_row_num = 1
    for data in sql_data:
        start_col_num = 0
        for line in data:
            sheet.write(start_row_num, start_col_num, line)
            start_col_num +=1
        start_row_num +=1
    wb.save(file_name + str(thismonthtoday) + '.xls')


if __name__ in '__main__':
    db = pymysql.connect('xxx', 'xxx', 'xxx', 'xxx', charset='utf8')
    thismonthtoday = datetime.date.today()
    current_time = "'%s'"%(thismonthtoday)
    total_sql = """SELECT a.team_id, t.team_name , COUNT(*) as count FROM self_event_team_call_log a LEFT JOIN self_event_teams t ON a.team_id = t.id GROUP BY a.team_id ORDER BY count desc;"""
    cur_01 = db.cursor()
    total_data = get_data(cur_01, total_sql)
    excel_save('team_id', 'team_name', 'votes_num', file_name='total_surface', sql_data=total_data)
    print(total_data)
    current_sql = """SELECT a.team_id, t.team_name , COUNT(*), %s FROM self_event_team_call_log a LEFT JOIN self_event_teams t ON a.team_id = t.id WHERE left(a.update_time, 10)=%s GROUP BY a.team_id;"""%(current_time, current_time)
    cur_02 = db.cursor()
    current_data = get_data(cur_02, current_sql)
    excel_save('team_id', 'team_name', 'votes_num', 'time', file_name='current_surface', sql_data=current_data)
    print(current_data)
    db.close()



