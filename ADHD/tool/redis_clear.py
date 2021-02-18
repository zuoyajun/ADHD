"""
mysql.py
redis
"""
import redis

from tool.get_logger import GetLogger

log = GetLogger.get_logger()


def redis_clear(email):
    # 连接数据库
    pool = redis.ConnectionPool(host='49.232.118.115', port=6379)
    conn = redis.Redis(connection_pool=pool)

    # 管理员发送邮件次数前缀
    ADMIN_EMAIL_SEND_NUM_REDIS = 'admin_email_send_num_'
    admin_email = email
    stats = conn.delete(ADMIN_EMAIL_SEND_NUM_REDIS + admin_email)
    log.info("邮箱：{}，清除redis：{}".format(email, stats))
