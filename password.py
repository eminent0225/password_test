password = "a123456"
i = 3
while i > 0:
	code = input("請輸入密碼")
	if code == password:
		print("登入成功")
		break
	else :
		i = i - 1
		print("密碼錯誤還有", i,"次機會")




		
			
