password = "a123456"
i = 3
while True:
	code = input("請輸入密碼")
	if code == password:
		print("登入成功")
		break
	else :
		i = i - 1
		print("密碼錯誤還有", i,"次機會")
		if i == 0:
		    print("請過十分鐘後在回來")
		    break




		
			
