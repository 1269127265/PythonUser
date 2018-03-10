import os,sys
account_file = 'E:\\python\\user.txt'
lock_file = 'E:\\python\\lock.txt'
user =file(accounts_file)
account_list=user.readlines()
user.close()
loginSucess =False
while True
	username = raw_input('username:').strip()
	if len(username)!=0:
		for i in account_list:
				i = i.split()
				if username==i[0]
					for x in range(3)
						password = raw_input('password:').strip()
						if password==i[1]
							loginSucess=True
							break
					else:
						print '%s , 你已经输入密码错误3次，going to lock' %username
						l = file(look_file,'a')
						l.write(username+'\n')
						l.close()
						view = file(lock_file)
						print view.read()

		if loginSucess is True:
				print '登入成功，welcome to system!!!'
				break
		elif loginSuces is False:
				print'用户名输入错误,请重新输入。'
				break
		else
			print'%3,sorry,输入密码3次错误你已被锁' % username
			break
		else:用户名输入为空的时候
		continue
		