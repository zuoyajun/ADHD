"""
mysql.py
redis
"""

import redis

# 连接数据库
# pool = redis.ConnectionPool(host='192.168.1.241',port=6379)
pool = redis.ConnectionPool(host='49.232.118.115', port=6379)
conn = redis.Redis(connection_pool=pool)

# 所有用户登录密码输入错误次数前缀
PASSWD_ERR_NUM_REDIS = 'passwd_err_'
admin_email = 'liqingsong@66nao.com'
stats = conn.delete(PASSWD_ERR_NUM_REDIS + admin_email)
print(stats)
