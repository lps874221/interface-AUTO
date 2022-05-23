
import pymysql

from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_config import conf

class HandleDB:

    def __init__(self):
        self.conn = pymysql.connect(
            host=conf.get("mysql","host"),
            port=conf.getint("mysql","port"),
            user=conf.get("mysql","user"),
            password=conf.get("mysql","password"),
            database=conf.get("mysql","database"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
     
        self.cur = self.conn.cursor()

    def select_one_data(self,sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def select_all_data(self,sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_count(self,sql):
        self.conn.commit()
        return self.cur.execute(sql)

    def update(self,sql):
        self.cur.execute(sql)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    # sql = 'select * from member LIMIT 3'
    # db = HandleDB()
    # count = db.get_count(sql)
    # print("结果个数为：",count)
    # data = db.select_one_data(sql)
    # print("一条数据：",data)
    # all = db.select_all_data(sql)
    # print("所有的数据：",all)
    # db.close()
    # 初始化数据库对象
    db = HandleDB()
    sql = 'select * from member where mobile_phone="18600001120"'
    from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_requests import send_requests
    case = {
        "method":"POST",
        "url":"http://api.lemonban.com/futureloan/member/register",
        "request_data":{"mobile_phone":"18600001120","pwd":"123456789","type":1,"reg_name":"美丽可爱的小简"}
    }
    response = send_requests(case["method"], case["url"], case["request_data"])
    print("响应结果：",response.json())
   
    count = db.get_count(sql)
    print("获取到的结果为：",count)

