# -*- coding:utf-8 -*-
CSRF_ENABLED = True
SECRET_KEY = 'orderlife_v0.1@123$%^'

FROM_PRIVATE_KEY_FILE = ('D:/Study Test/orderlife-v2.1显示sql版/huhaiyang.pem', 'mcWPi9vKuo1HXKQx')
FROM_PRIVATE_KEY_FILE_PEM = 'D:/Study Test/orderlife-v2.1显示sql版/huhaiyang.pem'
FROM_PRIVATE_KEY_FILE_CIPHER ='mcWPi9vKuo1HXKQx'
SSH_ADDRESS_OR_HOST = ('jms.jindanfenqi.com', 4231)
SSH_USERNAME = 'huhaiyang'
#TEST_REMOTE_BIND_ADDRESS = ('47.94.175.76', 3306) #渠道01
#TEST_REMOTE_BIND_ADDRESS = ('39.106.35.160', 3306) #渠道02
TEST_REMOTE_BIND_ADDRESS = ('39.105.213.16', 3306) #渠道03
DATABASE = 'ijindantest'
USER = 'jdfqtest'
PASSWORD = 'jdfqtest123'
#TEST_HOST = '47.94.175.76' #渠道01
#TEST_HOST = '39.106.35.160' #渠道02
TEST_HOST = '39.105.213.16' #渠道03
PORT = 3306
