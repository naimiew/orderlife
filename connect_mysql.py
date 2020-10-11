# -*- coding:utf-8 -*-
import config
import paramiko
import pymysql
from sshtunnel import SSHTunnelForwarder


def connect_mysql_third_order_no(third_order_no):
	private_key = paramiko.RSAKey.from_private_key_file(config.FROM_PRIVATE_KEY_FILE_PEM,
	                                                    config.FROM_PRIVATE_KEY_FILE_CIPHER)
	with SSHTunnelForwarder(ssh_address_or_host=config.SSH_ADDRESS_OR_HOST, ssh_pkey=private_key,
	                        ssh_username=config.SSH_USERNAME,
	                        remote_bind_address=config.TEST_REMOTE_BIND_ADDRESS) as server:
		conn = pymysql.connect(database=config.DATABASE, user=config.USER, password=config.PASSWORD,
		                       host=config.TEST_HOST, port=config.PORT, cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		print(f'获取到third_order_no:{third_order_no} 查询开始')
		sql_str_third_order = f"SELECT toi.*,cp.product_code,cp.product_name,cb.state FROM cl_product cp,third_order_info toi LEFT JOIN cl_borrow cb on  toi.order_no = cb.order_no where toi.third_order_no = '{third_order_no}' and toi.source = cp.platform_code ORDER BY id desc"
		sql_str_borrow = f"SELECT * from cl_borrow where order_no = (SELECT order_no FROM third_order_info toi where third_order_no = '{third_order_no}'  ORDER BY id desc)"
		sql_str_borrow_extended_info = f"SELECT * FROM cl_borrow_extended_info where borrow_id = (SELECT id from cl_borrow where order_no = (SELECT order_no FROM third_order_info toi where third_order_no = '{third_order_no}'  ORDER BY id desc))"
		sql_str_borrow_repay = f"SELECT * from cl_borrow_repay where borrow_id = (SELECT id from cl_borrow where order_no = (SELECT order_no FROM third_order_info toi where third_order_no = '{third_order_no}'  ORDER BY id desc))"
		sql_str_borrow_repay_detail = f"SELECT * from cl_borrow_repay_detail where borrow_id = (SELECT id from cl_borrow where order_no = (SELECT order_no FROM third_order_info toi where third_order_no = '{third_order_no}'  ORDER BY id desc))"
		sql_str_pay_apply = f"SELECT * from pay_apply where borrow_id = (SELECT id from cl_borrow where order_no = (SELECT order_no FROM third_order_info toi where third_order_no = '{third_order_no}'  ORDER BY id desc))"
		sql_str_fund_in_order_info = f"SELECT * from fund_in_order_info where borrow_id = (SELECT id from cl_borrow where order_no = (SELECT order_no FROM third_order_info toi where third_order_no = '{third_order_no}'  ORDER BY id desc))"
		sql_str_policy_apply_qa = f"SELECT * FROM policy_apply_qa where borrow_id = (SELECT id from cl_borrow where order_no = (SELECT order_no FROM third_order_info toi where third_order_no = '{third_order_no}'  ORDER BY id desc))"
		sql_str_mq_record_credit = f"SELECT * FROM cl_mq_record WHERE body like CONCAT('%:',(SELECT id FROM cl_jdcredit_req_log where user_id = (SELECT user_id FROM third_order_info toi where third_order_no = '{third_order_no}')ORDER BY id desc LIMIT 1),'%') "
		sql_str_mq_record_fico = f"SELECT * FROM cl_mq_record WHERE body like CONCAT('%',(SELECT order_no FROM third_order_info toi where third_order_no = '{third_order_no}'),'%')"
		sql_str_mq_record_loan = f"SELECT * FROM cl_mq_record WHERE body like CONCAT('%',(SELECT id from cl_borrow where order_no = (SELECT order_no FROM third_order_info toi where third_order_no = '{third_order_no}')),'%')"
		sql_str_notify_callback = f"SELECT * from cl_notify_callback where nc_entry_id = (SELECT order_no FROM third_order_info toi where third_order_no = '{third_order_no}'  ORDER BY id desc)"
		sql_str_req_record_credit_sign = f"select *from req_record_credit_sign where order_no = (SELECT order_no FROM third_order_info toi where third_order_no = '{third_order_no}'  ORDER BY id desc)"
		sql_str_product = f"SELECT * FROM cl_product t WHERE t.id = (SELECT product_id FROM third_order_info toi where third_order_no = '{third_order_no}')"
		sql_str_product_fee = f"SELECT * FROM cl_product_fee t WHERE t.product_id = (SELECT product_id FROM third_order_info toi where third_order_no = '{third_order_no}')"
		sql_str_product_interest_rate = f"SELECT * FROM cl_product_interest_rate t WHERE t.product_id = (SELECT product_id FROM third_order_info toi where third_order_no = '{third_order_no}')"
		sql_str_repay_apply = f"SELECT * FROM repay_apply where borrow_id = (SELECT id from cl_borrow where order_no = (SELECT order_no FROM third_order_info toi where third_order_no = '{third_order_no}'))"
		try:
			print(f'开始执行:{sql_str_third_order}')
			cur.execute(sql_str_third_order)
			third_order_info = cur.fetchall()
			
			print(f'开始执行:{sql_str_borrow}')
			cur.execute(sql_str_borrow)
			borrow = cur.fetchall()
			
			print(f'开始执行:{sql_str_borrow_extended_info}')
			cur.execute(sql_str_borrow_extended_info)
			borrow_extended_info = cur.fetchall()
			
			print(f'开始执行:{sql_str_borrow_repay}')
			cur.execute(sql_str_borrow_repay)
			borrow_repay = cur.fetchall()
			
			print(f'开始执行:{sql_str_borrow_repay_detail}')
			cur.execute(sql_str_borrow_repay_detail)
			borrow_repay_detail = cur.fetchall()
			
			print(f'开始执行:{sql_str_pay_apply}')
			cur.execute(sql_str_pay_apply)
			pay_apply = cur.fetchall()
			
			print(f'开始执行:{sql_str_fund_in_order_info}')
			cur.execute(sql_str_fund_in_order_info)
			fund_in_order_info = cur.fetchall()
			
			print(f'开始执行:{sql_str_policy_apply_qa}')
			cur.execute(sql_str_policy_apply_qa)
			policy_apply_qa = cur.fetchall()
			
			print(f'开始执行:{sql_str_mq_record_credit}')
			cur.execute(sql_str_mq_record_credit)
			mq_record_credit = cur.fetchall()
			
			print(f'开始执行:{sql_str_mq_record_fico}')
			cur.execute(sql_str_mq_record_fico)
			mq_record_fico = cur.fetchall()
			
			print(f'开始执行:{sql_str_mq_record_loan}')
			cur.execute(sql_str_mq_record_loan)
			mq_record_loan = cur.fetchall()
			
			print(f'开始执行:{sql_str_notify_callback}')
			cur.execute(sql_str_notify_callback)
			notify_callback = cur.fetchall()
			
			print(f'开始执行:{sql_str_req_record_credit_sign}')
			cur.execute(sql_str_req_record_credit_sign)
			req_record_credit_sign = cur.fetchall()
			
			print(f'开始执行:{sql_str_product}')
			cur.execute(sql_str_product)
			product = cur.fetchall()
			
			print(f'开始执行:{sql_str_product_fee}')
			cur.execute(sql_str_product_fee)
			product_fee = cur.fetchall()
			
			print(f'开始执行:{sql_str_product_interest_rate}')
			cur.execute(sql_str_product_interest_rate)
			product_interest_rate = cur.fetchall()
			
			print(f'开始执行:{sql_str_repay_apply}')
			cur.execute(sql_str_repay_apply)
			repay_apply = cur.fetchall()
			
			print(f'获取到third_order_no:{third_order_no} 查询结束！！')
			conn.close()
			return sql_str_third_order, third_order_info, \
			       sql_str_borrow, borrow, \
			       sql_str_borrow_extended_info, borrow_extended_info, \
			       sql_str_borrow_repay, borrow_repay, \
			       sql_str_borrow_repay_detail, borrow_repay_detail, \
			       sql_str_pay_apply, pay_apply, \
			       sql_str_fund_in_order_info, fund_in_order_info, \
			       sql_str_policy_apply_qa, policy_apply_qa, \
			       sql_str_mq_record_credit, mq_record_credit, \
			       sql_str_mq_record_fico, mq_record_fico, \
			       sql_str_mq_record_loan, mq_record_loan, \
			       sql_str_notify_callback, notify_callback, \
			       sql_str_req_record_credit_sign, req_record_credit_sign, \
			       sql_str_product, product, \
			       sql_str_product_fee, product_fee, \
			       sql_str_product_interest_rate, product_interest_rate, \
			       sql_str_repay_apply, repay_apply
		except Exception as data:
			print(f'Error: 执行查询失败，{data}')
			conn.close()


# 提速 mq  callback  还款  先查到未执行  再提速
# update repay_apply set ra_accept_time = DATE_SUB(ra_accept_time,INTERVAL 10 MINUTE) where user_id in (SELECT id from cl_user WHERE login_name='15810079826')  ORDER BY ra_id;

def connect_mysql_id_no(id_no):
	private_key = paramiko.RSAKey.from_private_key_file(config.FROM_PRIVATE_KEY_FILE_PEM,
	                                                    config.FROM_PRIVATE_KEY_FILE_CIPHER)
	with SSHTunnelForwarder(ssh_address_or_host=config.SSH_ADDRESS_OR_HOST, ssh_pkey=private_key,
	                        ssh_username=config.SSH_USERNAME,
	                        remote_bind_address=config.TEST_REMOTE_BIND_ADDRESS) as server:
		conn = pymysql.connect(database=config.DATABASE, user=config.USER, password=config.PASSWORD,
		                       host=config.TEST_HOST, port=config.PORT, cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		print(f'获取到id_no:{id_no} 查询开始')
		# updata 相关
		sql_str_can_loan = f"SELECT ucld.*,cp.platform_code as cppc ,cp.product_code,cp.product_name,(unix_timestamp(CURRENT_DATE())*1000) as timestamp_now,CURRENT_DATE() as date_now from user_can_loan_date ucld,cl_product cp WHERE ucld.id_no = '{id_no}' and ucld.platform_code = cp.platform_code"
		sql_str_id_no = f"SELECT cubi.*,cp.product_code,cp.product_name FROM cl_user_base_info cubi,cl_product cp where cubi.id_no = '{id_no}' and cubi.source = cp.platform_code ORDER BY id desc"
		try:
			print(f'开始执行:{sql_str_can_loan}')
			cur.execute(sql_str_can_loan)
			can_loan = cur.fetchall()
			
			print(f'开始执行:{sql_str_id_no}')
			cur.execute(sql_str_id_no)
			id_no_info = cur.fetchall()
			
			print(f'获取到id_no:{id_no} 查询结束！！')
			conn.close()
			return sql_str_can_loan, can_loan, \
			       sql_str_id_no, id_no_info
		except Exception as data:
			print(f'Error: 执行查询失败，{data}')
			conn.close()


def connect_mysql_user_info(user_id):
	private_key = paramiko.RSAKey.from_private_key_file(config.FROM_PRIVATE_KEY_FILE_PEM,
	                                                    config.FROM_PRIVATE_KEY_FILE_CIPHER)
	with SSHTunnelForwarder(ssh_address_or_host=config.SSH_ADDRESS_OR_HOST, ssh_pkey=private_key,
	                        ssh_username=config.SSH_USERNAME,
	                        remote_bind_address=config.TEST_REMOTE_BIND_ADDRESS) as server:
		conn = pymysql.connect(database=config.DATABASE, user=config.USER, password=config.PASSWORD,
		                       host=config.TEST_HOST, port=config.PORT, cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		print(f'获取到user_id:{user_id} 查询开始')
		
		sql_str_user_id = f"SELECT cu.*,cp.product_code,cp.product_name FROM cl_user cu,cl_product cp where cu.id = '{user_id}' and cu.source = cp.platform_code"
		sql_str_third_order_info = f"SELECT toi.*,cp.product_code,cp.product_name,cb.state FROM cl_product cp,third_order_info toi LEFT JOIN cl_borrow cb on  toi.order_no = cb.order_no where toi.user_id = '{user_id}'  and toi.source = cp.platform_code ORDER BY id desc"
		sql_str_user_push_data = f"SELECT * from qc_borrow_data where id in (SELECT data_id from third_order_info where user_id = '{user_id}' ) ORDER BY id desc"
		sql_str_credit_account_data = f"SELECT uca.*,cp.platform_code,cp.product_code,cp.product_name FROM user_credit_account uca,cl_product cp,cl_jdcredit_req_log  cjrl WHERE uca.user_id  = '{user_id}' and uca.user_id = cjrl.user_id and uca.product_id = cp.product_code"
		sql_str_credit_account_info = f"select * from user_credit_account_info where user_credit_account_id in (SELECT id FROM user_credit_account WHERE user_id='{user_id}')"
		sql_str_credit_account_change_detail = f"select * from user_credit_account_change_detail where user_credit_account_id in (SELECT id FROM user_credit_account WHERE user_id='{user_id}')"
		sql_str_bank_card_list = f"SELECT * from cl_bank_card WHERE user_id= '{user_id}'"
		sql_depository_register_info = f"SELECT * from cl_depository_register_info where id_no = (SELECT id_no from cl_user_base_info WHERE user_id = '{user_id}')"
		sql_str_jdcredit_req_log = f"SELECT * FROM cl_jdcredit_req_log WHERE user_id  = '{user_id}' ORDER BY id DESC"
		try:
			print(f'开始执行:{sql_str_user_id}')
			cur.execute(sql_str_user_id)
			user_id_info = cur.fetchall()
			
			print(f'开始执行:{sql_str_third_order_info}')
			cur.execute(sql_str_third_order_info)
			third_order_info = cur.fetchall()
			
			print(f'开始执行:{sql_str_user_push_data}')
			cur.execute(sql_str_user_push_data)
			user_push_data = cur.fetchall()
			
			print(f'开始执行:{sql_str_credit_account_data}')
			cur.execute(sql_str_credit_account_data)
			credit_account_data = cur.fetchall()
			
			print(f'开始执行:{sql_str_credit_account_info}')
			cur.execute(sql_str_credit_account_info)
			credit_account_info = cur.fetchall()
			
			print(f'开始执行:{sql_str_credit_account_change_detail}')
			cur.execute(sql_str_credit_account_change_detail)
			credit_account_change_detail = cur.fetchall()
			
			print(f'开始执行:{sql_str_bank_card_list}')
			cur.execute(sql_str_bank_card_list)
			bank_card_list = cur.fetchall()
			
			print(f'开始执行:{sql_depository_register_info}')
			cur.execute(sql_depository_register_info)
			depository_register_info = cur.fetchall()
			
			print(f'开始执行:{sql_str_jdcredit_req_log}')
			cur.execute(sql_str_jdcredit_req_log)
			jdcredit_req_log = cur.fetchall()
			
			print(f'获取到user_id:{user_id} 查询结束！！')
			conn.close()
			return sql_str_user_id, user_id_info, \
			       sql_str_third_order_info, third_order_info, \
			       sql_str_user_push_data, user_push_data, \
			       sql_str_credit_account_data, credit_account_data, \
			       sql_str_credit_account_info, credit_account_info, \
			       sql_str_credit_account_change_detail, credit_account_change_detail, \
			       sql_str_bank_card_list, bank_card_list, \
			       sql_depository_register_info, depository_register_info, \
			       sql_str_jdcredit_req_log, jdcredit_req_log
		except Exception as data:
			print(f'Error: 执行查询失败，{data}')
			conn.close()


def connect_mysql_update_bindcard(card_no, user_id, phone):
	private_key = paramiko.RSAKey.from_private_key_file(config.FROM_PRIVATE_KEY_FILE_PEM,
	                                                    config.FROM_PRIVATE_KEY_FILE_CIPHER)
	with SSHTunnelForwarder(ssh_address_or_host=config.SSH_ADDRESS_OR_HOST, ssh_pkey=private_key,
	                        ssh_username=config.SSH_USERNAME,
	                        remote_bind_address=config.TEST_REMOTE_BIND_ADDRESS) as server:
		conn = pymysql.connect(database=config.DATABASE, user=config.USER, password=config.PASSWORD,
		                       host=config.TEST_HOST, port=config.PORT, cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		print(f'获取到update_bindcard:{card_no},{user_id},{phone}- 查询开始')
		sql_str_update_bindcard_all = f"update cl_bank_card set default_pay = 0 , default_repay = 0 where user_id = '{user_id}'"
		sql_str_update_bindcard_target = f"update cl_bank_card set default_pay = 1 , default_repay = 1 where user_id = '{user_id}' and phone = '{phone}' and card_no = '{card_no}'"
		sql_str_bank_card_list = f"SELECT * from cl_bank_card WHERE user_id= '{user_id}'"
		try:
			print(f'开始执行:{sql_str_update_bindcard_all}')
			try:
				cur.execute(sql_str_update_bindcard_all)
				conn.commit()
			except:
				conn.rollback()
			
			print(f'开始执行:{sql_str_update_bindcard_target}')
			try:
				cur.execute(sql_str_update_bindcard_target)
				conn.commit()
			except:
				conn.rollback()
			
			print(f'开始执行:{sql_str_bank_card_list}')
			cur.execute(sql_str_bank_card_list)
			bank_card_list = cur.fetchall()
			
			print(f'获取到update_bindcard:{card_no},{user_id},{phone} 查询结束！！')
			conn.close()
			return sql_str_bank_card_list, bank_card_list
		except Exception as data:
			print(f'Error: 执行查询失败，{data}')
			conn.close()

def connect_mysql_update_repay_apply(third_order_no):
	private_key = paramiko.RSAKey.from_private_key_file(config.FROM_PRIVATE_KEY_FILE_PEM,
	                                                    config.FROM_PRIVATE_KEY_FILE_CIPHER)
	with SSHTunnelForwarder(ssh_address_or_host=config.SSH_ADDRESS_OR_HOST, ssh_pkey=private_key,
	                        ssh_username=config.SSH_USERNAME,
	                        remote_bind_address=config.TEST_REMOTE_BIND_ADDRESS) as server:
		conn = pymysql.connect(database=config.DATABASE, user=config.USER, password=config.PASSWORD,
		                       host=config.TEST_HOST, port=config.PORT, cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		print(f'获取到update_repay_apply:{third_order_no}- 开始')
		sql_str_update_repay_apply = f"update repay_apply set ra_accept_time = DATE_SUB(ra_accept_time,INTERVAL 10 MINUTE) where user_id in (SELECT user_id from third_order_info WHERE third_order_no = '{third_order_no}')  ORDER BY ra_id"
		try:
			print(f'开始执行:{sql_str_update_repay_apply}')
			try:
				cur.execute(sql_str_update_repay_apply)
				conn.commit()
			except:
				conn.rollback()
			print(f'获取到update_repay_apply:{third_order_no}- 结束！！')
			conn.close()
		except Exception as data:
			print(f'Error: 执行查询失败，{data}')
			conn.close()
			
def connect_mysql_update_borrow_state(third_order_no,borrow_state):
	private_key = paramiko.RSAKey.from_private_key_file(config.FROM_PRIVATE_KEY_FILE_PEM,
	                                                    config.FROM_PRIVATE_KEY_FILE_CIPHER)
	with SSHTunnelForwarder(ssh_address_or_host=config.SSH_ADDRESS_OR_HOST, ssh_pkey=private_key,
	                        ssh_username=config.SSH_USERNAME,
	                        remote_bind_address=config.TEST_REMOTE_BIND_ADDRESS) as server:
		conn = pymysql.connect(database=config.DATABASE, user=config.USER, password=config.PASSWORD,
		                       host=config.TEST_HOST, port=config.PORT, cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		print(f'获取到update_repay_apply:{third_order_no},{borrow_state}- 开始')
		sql_str_update_borrow_state = f"UPDATE cl_borrow set state = '{borrow_state}' where order_no = (SELECT order_no from third_order_info WHERE third_order_no = '{third_order_no}')"
		try:
			print(f'开始执行:{sql_str_update_borrow_state}')
			try:
				cur.execute(sql_str_update_borrow_state)
				conn.commit()
			except:
				conn.rollback()
			print(f'获取到update_repay_apply:{third_order_no},{borrow_state}- 结束！！')
			conn.close()
		except Exception as data:
			print(f'Error: 执行查询失败，{data}')
			conn.close()
			
def connect_mysql_update_repay_time(update_repay_time_day,third_order_no,borrow_repay_id):
	private_key = paramiko.RSAKey.from_private_key_file(config.FROM_PRIVATE_KEY_FILE_PEM,
	                                                    config.FROM_PRIVATE_KEY_FILE_CIPHER)
	with SSHTunnelForwarder(ssh_address_or_host=config.SSH_ADDRESS_OR_HOST, ssh_pkey=private_key,
	                        ssh_username=config.SSH_USERNAME,
	                        remote_bind_address=config.TEST_REMOTE_BIND_ADDRESS) as server:
		conn = pymysql.connect(database=config.DATABASE, user=config.USER, password=config.PASSWORD,
		                       host=config.TEST_HOST, port=config.PORT, cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		print(f'获取到update_repay_time:{update_repay_time_day},{third_order_no},{borrow_repay_id}- 开始')
		sql_str_update_repay_time = f"update cl_borrow_repay set repay_time = DATE_SUB(repay_time,INTERVAL '{update_repay_time_day}' DAY) where borrow_id in (SELECT id FROM cl_borrow where order_no = (SELECT order_no from third_order_info WHERE third_order_no = '{third_order_no}')) and id = '{borrow_repay_id}'"
		try:
			print(f'开始执行:{sql_str_update_repay_time}')
			try:
				cur.execute(sql_str_update_repay_time)
				conn.commit()
			except:
				conn.rollback()
			print(f'获取到update_repay_time:{update_repay_time_day},{third_order_no},{borrow_repay_id}- 结束！！')
			conn.close()
		except Exception as data:
			print(f'Error: 执行查询失败，{data}')
			conn.close()
			
def connect_mysql_update_mq_record_credit(third_order_no,mq_record_credit_id):
	private_key = paramiko.RSAKey.from_private_key_file(config.FROM_PRIVATE_KEY_FILE_PEM,
	                                                    config.FROM_PRIVATE_KEY_FILE_CIPHER)
	with SSHTunnelForwarder(ssh_address_or_host=config.SSH_ADDRESS_OR_HOST, ssh_pkey=private_key,
	                        ssh_username=config.SSH_USERNAME,
	                        remote_bind_address=config.TEST_REMOTE_BIND_ADDRESS) as server:
		conn = pymysql.connect(database=config.DATABASE, user=config.USER, password=config.PASSWORD,
		                       host=config.TEST_HOST, port=config.PORT, cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		print(f'获取到update_mq_record_credit:{third_order_no},{mq_record_credit_id}- 开始')
		sql_str_update_mq_record_credit = f"update cl_mq_record set gmt_modified = DATE_SUB(gmt_modified,INTERVAL 20 MINUTE) where id = '{mq_record_credit_id}' and body like CONCAT('%:',(SELECT id FROM cl_jdcredit_req_log where user_id = (SELECT user_id FROM third_order_info toi where third_order_no = '{third_order_no}')ORDER BY id desc LIMIT 1),'%')"
		try:
			print(f'开始执行:{sql_str_update_mq_record_credit}')
			try:
				cur.execute(sql_str_update_mq_record_credit)
				conn.commit()
			except:
				conn.rollback()
			print(f'获取到update_mq_record_credit:{third_order_no},{mq_record_credit_id}- 结束！！')
			conn.close()
		except Exception as data:
			print(f'Error: 执行查询失败，{data}')
			conn.close()
			
def connect_mysql_update_mq_record_fico(third_order_no,mq_record_fico_id):
	private_key = paramiko.RSAKey.from_private_key_file(config.FROM_PRIVATE_KEY_FILE_PEM,
	                                                    config.FROM_PRIVATE_KEY_FILE_CIPHER)
	with SSHTunnelForwarder(ssh_address_or_host=config.SSH_ADDRESS_OR_HOST, ssh_pkey=private_key,
	                        ssh_username=config.SSH_USERNAME,
	                        remote_bind_address=config.TEST_REMOTE_BIND_ADDRESS) as server:
		conn = pymysql.connect(database=config.DATABASE, user=config.USER, password=config.PASSWORD,
		                       host=config.TEST_HOST, port=config.PORT, cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		print(f'获取到update_mq_record_fico:{third_order_no},{mq_record_fico_id}- 开始')
		sql_str_update_mq_record_fico = f"update cl_mq_record set gmt_modified = DATE_SUB(gmt_modified,INTERVAL 20 MINUTE) where id = '{mq_record_fico_id}' and body like CONCAT('%',(SELECT order_no FROM third_order_info toi where third_order_no = '{third_order_no}'),'%')"
		try:
			print(f'开始执行:{sql_str_update_mq_record_fico}')
			try:
				cur.execute(sql_str_update_mq_record_fico)
				conn.commit()
			except:
				conn.rollback()
			print(f'获取到update_mq_record_fico:{third_order_no},{mq_record_fico_id}- 结束！！')
			conn.close()
		except Exception as data:
			print(f'Error: 执行查询失败，{data}')
			conn.close()

def connect_mysql_update_mq_record_loan(third_order_no, mq_record_loan_id):
	private_key = paramiko.RSAKey.from_private_key_file(config.FROM_PRIVATE_KEY_FILE_PEM,
	                                                    config.FROM_PRIVATE_KEY_FILE_CIPHER)
	with SSHTunnelForwarder(ssh_address_or_host=config.SSH_ADDRESS_OR_HOST, ssh_pkey=private_key,
	                        ssh_username=config.SSH_USERNAME,
	                        remote_bind_address=config.TEST_REMOTE_BIND_ADDRESS) as server:
		conn = pymysql.connect(database=config.DATABASE, user=config.USER, password=config.PASSWORD,
		                       host=config.TEST_HOST, port=config.PORT, cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		print(f'获取到update_mq_record_loan:{third_order_no},{mq_record_loan_id}- 开始')
		sql_str_update_mq_record_loan = f"update cl_mq_record set gmt_modified = DATE_SUB(gmt_modified,INTERVAL 20 MINUTE) where id = '{mq_record_loan_id}' and body like CONCAT('%',(SELECT id from cl_borrow where order_no = (SELECT order_no FROM third_order_info toi where third_order_no = '{third_order_no}')),'%')"
		try:
			print(f'开始执行:{sql_str_update_mq_record_loan}')
			try:
				cur.execute(sql_str_update_mq_record_loan)
				conn.commit()
			except:
				conn.rollback()
			print(f'获取到update_mq_record_loan:{third_order_no},{mq_record_loan_id}- 结束！！')
			conn.close()
		except Exception as data:
			print(f'Error: 执行查询失败，{data}')
			conn.close()
			
def connect_mysql_cl_notify_callback(third_order_no, cl_notify_callback_id):
	private_key = paramiko.RSAKey.from_private_key_file(config.FROM_PRIVATE_KEY_FILE_PEM,
	                                                    config.FROM_PRIVATE_KEY_FILE_CIPHER)
	with SSHTunnelForwarder(ssh_address_or_host=config.SSH_ADDRESS_OR_HOST, ssh_pkey=private_key,
	                        ssh_username=config.SSH_USERNAME,
	                        remote_bind_address=config.TEST_REMOTE_BIND_ADDRESS) as server:
		conn = pymysql.connect(database=config.DATABASE, user=config.USER, password=config.PASSWORD,
		                       host=config.TEST_HOST, port=config.PORT, cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		print(f'获取到cl_notify_callback:{third_order_no},{cl_notify_callback_id}- 开始')
		sql_str_update_cl_notify_callback = f"update cl_notify_callback set nc_next_time = DATE_SUB(nc_next_time,INTERVAL 20 MINUTE) where nc_id = '{cl_notify_callback_id}' and nc_entry_id = (SELECT order_no FROM third_order_info toi where third_order_no = '{third_order_no}'  ORDER BY id desc)"
		try:
			print(f'开始执行:{sql_str_update_cl_notify_callback}')
			try:
				cur.execute(sql_str_update_cl_notify_callback)
				conn.commit()
			except:
				conn.rollback()
			print(f'获取到cl_notify_callback:{third_order_no},{cl_notify_callback_id}- 结束！！')
			conn.close()
		except Exception as data:
			print(f'Error: 执行查询失败，{data}')
			conn.close()

def connect_mysql_cl_notify_callback_re(third_order_no, cl_notify_callback_re_id):
	private_key = paramiko.RSAKey.from_private_key_file(config.FROM_PRIVATE_KEY_FILE_PEM,
	                                                    config.FROM_PRIVATE_KEY_FILE_CIPHER)
	with SSHTunnelForwarder(ssh_address_or_host=config.SSH_ADDRESS_OR_HOST, ssh_pkey=private_key,
	                        ssh_username=config.SSH_USERNAME,
	                        remote_bind_address=config.TEST_REMOTE_BIND_ADDRESS) as server:
		conn = pymysql.connect(database=config.DATABASE, user=config.USER, password=config.PASSWORD,
		                       host=config.TEST_HOST, port=config.PORT, cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		print(f'获取到cl_notify_callback_re:{third_order_no},{cl_notify_callback_re_id}- 开始')
		sql_str_update_cl_notify_callback_re = f"update cl_notify_callback set nc_send_status = '0',nc_execute_num = '0',nc_next_time = DATE_SUB(nc_next_time,INTERVAL 20 MINUTE) where nc_id = '{cl_notify_callback_re_id}' and nc_entry_id = (SELECT order_no FROM third_order_info toi where third_order_no = '{third_order_no}'  ORDER BY id desc)"
		try:
			print(f'开始执行:{sql_str_update_cl_notify_callback_re}')
			try:
				cur.execute(sql_str_update_cl_notify_callback_re)
				conn.commit()
			except:
				conn.rollback()
			print(f'获取到cl_notify_callback_re:{third_order_no},{cl_notify_callback_re_id}- 结束！！')
			conn.close()
		except Exception as data:
			print(f'Error: 执行查询失败，{data}')
			conn.close()