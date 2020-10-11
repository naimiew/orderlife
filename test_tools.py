#-*- coding:utf-8 -*-
import paramiko
import pymysql
from sshtunnel import SSHTunnelForwarder

'''
class ExecuteSQL(object):
	def __init__(self):
		SSHTunnelForwarder(ssh_address_or_host=('jms.jindanfenqi.com', 4231),
		                   # 设置密钥
		                   ssh_pkey=paramiko.RSAKey.from_private_key_file(
			                   'C:/Users/kte/Desktop/金蛋/分期/huhaiyang.pem', 'dTQtRjoxvKSVMj9_'),
		                   # 如果是通过密码访问，可以把下面注释打开，将密钥注释即可。
		                   # ssh_password="password",
		                   # 设置用户
		                   ssh_username='huhaiyang',
		                   # 设置数据库服务地址及端口
		                   remote_bind_address=('39.105.213.16', 3306))

		self.connection = pymysql.connect(database='ijindantest',
		                                  user='jdfqtest',
		                                  password='jdfqtest123',
		                                  host='39.105.213.16',
		                                  # 因为上面没有设置 local_bind_address,所以这里必须是127.0.0.1,如果设置了，取设置的值就行了。
		                                  port=3306,  # 这里端口也一样，上面的server可以设置，没设置取这个就行了
		                                  cursorclass=pymysql.cursors.DictCursor)
		self.cursor = self.connection.cursor()

	def __enter__(self):
		return self.cursor

	def __exit__(self, *exc_info):
		self.cursor.close()
		self.connection.close()

	def execute_sql(self, sql):
		results = ''
		try:
			self.cursor.execute(sql)
			# str = sql
			print(f'开始执行:{sql}')
			results = self.cursor.fetchall()
		except Exception as data:
			print(f'Error: 执行查询失败，{data}')
			self.cursor.close()
			self.connection.close()
		return results
'''