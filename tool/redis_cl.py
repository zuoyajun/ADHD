import redis

# 清除redis文件

# 连接数据库
pool = redis.ConnectionPool(host='49.232.118.115', port=6379)
conn = redis.Redis(connection_pool=pool)

# 管理员发送邮件次数前缀
ADMIN_EMAIL_SEND_NUM_REDIS = 'admin_email_send_num_'
admin_email = '18538192813@163.com'
# admin_email = 'zuoyajun@66nao.com'
stats = conn.delete(ADMIN_EMAIL_SEND_NUM_REDIS + admin_email)
print(stats)
