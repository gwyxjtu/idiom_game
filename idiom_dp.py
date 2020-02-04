import json
import pypinyin
import unicodedata

#广搜，用队列
flag = 0
str(unicodedata.normalize('NFKD', pypinyin.lazy_pinyin("bǎi")[0]).encode('ascii','ignore'))[2:-1]

def judge(a,b):
	if(unicodedata.normalize('NFKD', pypinyin.lazy_pinyin(a)[0]).encode('ascii','ignore') == unicodedata.normalize('NFKD', pypinyin.lazy_pinyin(b)[0]).encode('ascii','ignore')):
		return True
	else:
		return False

def display(c):#传进来一个字符串
	list_play = c.split("+")
	global s
	print("-------------------------------")
	print("第"+str(0)+"个成语："+e)
	for i in range(len(list_play)-1):
		print("第"+str(i+1)+"个成语：",end = "")
		print(file_json[int(list_play[i])]["word"])
	print("第"+str(i+2)+"个成语："+s)
	print("-------------------------------")
def degrade(a):#数据降维
	b = str(a)
	b = b.replace('[','')
	b = b.replace(']','')
	b = b.replace("'",'')
	#print(b)
	a = b.split(",")
	return a

def search_idiom(p):
	#进来一个拼音，返回一个list，是以传进来的拼音结尾的
	global flag
	ans1=[]
	ans2=[]
	for iiii in range(l):#json
		ll = len(file_json[iiii]["word"])
		#print(file_json[iiii]["pinyin"].split(" "))
		if(judge(file_json[iiii]["pinyin"].split(" ")[-1] ,p)):
			#print(file_json[iiii]["pinyin"].split(" ")[0])
			ans1.append(file_json[iiii]["pinyin"].split(" ")[0].replace("'",""))#返回首字的拼音和索引
			ans2.append(str(iiii)+"+")
			#print("-------------------------------------\n")
			#print(file_json[iiii]["pinyin"].split(" ")[0],pinyin2)
			#print(file_json[iiii]["pinyin"].split(" ")[0] == pinyin2)
			#print("-------------------------------------\n")
			if(judge(file_json[iiii]["pinyin"].split(" ")[0],pinyin2)):
				flag = 1
				#print(ans1,ans2)
				return ans1,ans2
	#print(ans1)
	return ans1,ans2


def traverse(list_idiom,list_index):
	idiom_tmp = degrade(list_idiom)
	index_tmp = degrade(list_index)
	#print(idiom_tmp)
	global dp
	global index 
	global flag
	#l = len(np.array(list_idiom).shape)
	l_tmp = len(idiom_tmp)

	for i in range(l_tmp):
		tmp1,tmp2 = search_idiom(idiom_tmp[i])
		for j in range(len(tmp1)):
			#print(tmp2[j])
			tmp2[j]=tmp2[j]+index_tmp[i]
			#print(tmp2[j])
		if(flag !=0):
			#print(tmp2[i])
			print("成功了")
			flag =1;
			display(tmp2[-1])
			break
			
		if(len(tmp1)>0):
			dp.append(tmp1)
		#print(dp)
		if(len(tmp2)>0):
			index.append(tmp2)


file = open("H:/2020/idiom/idiom.json","rb")
file_json = json.load(file)
l = len(file_json)
while(1):
	s = input("想要接龙到的成语(输入exit退出程序):")
	if(s == ""):
		continue
	if(s == "exit"):
		break
	pinyin1 = pypinyin.pinyin(s)[0][0]#
	#print(pinyin1)

	while(1):
		e = input("开始的成语(exit退出到上一级)：")
		if(e == ""):
			continue
		if(e == "exit"):
			break
		pinyin2 = pypinyin.pinyin(e)[-1][0]
		#print(pinyin2)

		#转为拼音
		dp=[]#核心要维护的队列
		index = []#对应dp的队列
		dp.append(pinyin1)
		index.append("")
		times = 0
		flag = 0
		while(times < 10 and flag == 0):
			for ii in range(len(dp)):
				traverse(dp.pop(0),index.pop(0))
				if(len(dp) == 0):
					#print("dp=0")
					flag =1

				
				times+=1
				print("第"+str(times)+"轮广搜查询")
				# if(len(index)>0):
				# 	for ij in range(len(index)):
				# 		for ji in range(len(index[ij])):

				# 			display(index[ij][ji])
				# 			print("-------------------------------------\n")
