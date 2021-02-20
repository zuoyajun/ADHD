import pymysql


def get_select_mysql(sql):
    # 连接数据库
    db = pymysql.connect(host='49.232.118.115',
                         port=3306,
                         user='root',
                         password='bj66nao',
                         database='66nao_ccat',
                         charset='utf8')
    # 创建游标
    cur = db.cursor()
    # 执行sql语句
    cur.execute(sql)
    # 输出全部数据
    data = cur.fetchall()
    # 关闭游标
    cur.close()
    # 关闭数据库
    db.close()
    return data


def get_mysql(sql):
    # 连接数据库
    db = pymysql.connect(host='49.232.118.115',
                         port=3306,
                         user='root',
                         password='bj66nao',
                         database='66nao_ccat',
                         charset='utf8')
    # 创建游标
    cur = db.cursor()
    try:
        # 执行sql语句
        cur.execute(sql)
        # 提交到数据库执行
        db.commit()
    except AssertionError:
        # 回滚
        db.rollback()
    # 关闭游标
    cur.close()
    # 关闭数据库
    db.close()


if __name__ == '__main__':
    # 按创建日期升序：
    data_asc = "select name from ccat_doctor order by create_time desc limit 3;"
    print(get_select_mysql(data_asc))

    # print(get_mysql(data_asc)[0][0])
