# from multiprocessing import Process
# import time
# import random
#
#
# def task(n):
#     time.sleep(random.randint(1,3))
#     print('-------->%s' %n)
#
#
# if __name__ == '__main__':
#     p1 = Process(target=task, args=(1,))
#     p2 = Process(target=task, args=(2,))
#     p3 = Process(target=task, args=(3,))
#
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     p3.start()
#     p3.join()
#
#     print('-------->4')

# from multiprocessing import Process
# n=100 #在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了
# def work():
#     print('子进程内: ',n)
#
#
# if __name__ == '__main__':
#     p=Process(target=work)
#     p.start()
#     print('主进程内: ',n)

# import socket
# from multiprocessing import Process
#
# host_post = ('0.0.0.0', 8080)
# phone=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.bind((host_post))
# # phone.listen(5)
# def connt():
#     coon, cilent_addr = phone.accept()
#     print(coon, cilent_addr)
#
# if __name__ == "__main__":
#     p1 = Process(target=connt,)
#     p2 = Process(target=connt,)

#!/usr/local/python3.6.7/bin/python3
# author: momaekshi
# time: 2020/04/21

import pymysql
import datetime
from influxdb import InfluxDBClient, SeriesHelper
import logging


logging.basicConfig(
    filename='/tmp/job_monitor811.log',
    format='%(asctime)s|%(filename)s|line:%(lineno)d|%(name)s|%(levelname)s|%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)


class ParseEntry(SeriesHelper):
    class Meta:
        series_name = 'monitor_811'
        fields = [
            'time',
            'count']
        tags = ['country', 'isp', 'bg']


class Monitor811(object):

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.r_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:00")

    def parse_sql_data(self, sql):
        try:
            conn = pymysql.connect(host="10.80.21.159", port=3306, user="moba", password="moba2016",
                                   database="db_log_report", charset="utf8")
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute(sql)
            data = cursor.fetchall()
            cursor.close()
            conn.close()
            return data
        except Exception as e:
            logging.error(u"Conn Mysql Error：{}".format(e))
            raise e

    def get_reconnect_table_name(self):
        sql = """
            show tables;
        """
        data = self.parse_sql_data(sql)
        now_time = datetime.datetime.now()
        try:
            table_time = []
            for table in data:
                if 'client_battle_reconnect_' in table["Tables_in_db_log_report"]:
                    table_time.append(table["Tables_in_db_log_report"].split("_")[-1])
            return 'client_battle_reconnect_' + str(max(table_time))

        except Exception:
            pass