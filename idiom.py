import json
import pypinyin
import unicodedata

def judge(a,b):
	if(unicodedata.normalize('NFKD', pypinyin.lazy_pinyin(a)[0]).encode('ascii','ignore') == unicodedata.normalize('NFKD', pypinyin.lazy_pinyin(b)[0]).encode('ascii','ignore')):
		return True
	else:
		return False
file = open("H:/2020/idiom/idiom.json","rb")
file_json = json.load(file)
l = len(file_json)
while(1):
	s = input("目前要开始的字符：(输入exit退出):")
	if(s == ""):
		continue
	if(s == "exit"):
		break
	pinyin1 = pypinyin.pinyin(s)[-1][0]
	print(pinyin1)
	#转为拼音
	e = input("想要结尾的字符,不要求的输入nothing：")
	if e == "" or e =="nothing":
		for i in range(l):
			ll = len(file_json[i]["word"])
			if(judge(file_json[i]["pinyin"].split(" ")[0] , pinyin1)):
				print("-----------------------------------------------------------------------------------------------------")
				print(file_json[i]["word"],end = "")
				print(" ||拼音：",end = "")
				print(file_json[i]["pinyin"],end = "")
				print(" ||释意：",end = "")
				print(file_json[i]["derivation"])
	else:
		for i in range(l):
			ll = len(file_json[i]["word"])
			if(judge(file_json[i]["pinyin"].split(" ")[0] , pinyin1) and judge(file_json[i]["word"][ll-1] , e)):
				print("----------------------------------------------------------------------------------------")
				print(file_json[i]["word"],end = "")
				print(" ||拼音：",end = "")
				print(file_json[i]["pinyin"],end = "")
				print(" ||释意：",end = "")
				print(file_json[i]["derivation"])
print(file_json[9356]["derivation"])



# for i in range(l):#给结尾的成语
# 	ll = len(file_json[i]["word"])
# 	if(file_json[i]["word"] == "侯门似海"):
# 		print(file_json[i])
# 		print(i)
