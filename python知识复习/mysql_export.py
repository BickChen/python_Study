import pymysql, datetime, xlwt

"""
pip install pymysql
pip install xlwt
pip install cryptography
解决：RuntimeError: cryptography is required for sha256_password or caching_sha2_password
"""

db = pymysql.connect('xxx', 'xxxx', 'xxxx', 'xxxx', charset='utf8')
cur = db.cursor()
def get_data(cur, sql):
    try:
        cur.execute(sql)
        return cur.fetchall()
    except Exception as e:
        with open('sql.log', 'w') as log_file:
            log_file.write(e)

def excel_save(*args, file_name, sql_data):
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('Sheet1')
    for i in range(0, len(args)):
        sheet.write(0, i, args[i])




if __name__ in '__main__':
    thismonthtoday = datetime.date.today()
    total_sql = """SELECT a.team_id, t.team_name , COUNT(*) as count FROM self_event_team_call_log a LEFT JOIN self_event_teams t ON a.team_id = t.id GROUP BY a.team_id ORDER BY count desc;"""
    data = get_data(cur, total_sql)
    print(data)



