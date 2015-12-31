#测试集合操作和链表操作的时间
# import time
# a=set()
# s=time.time()
# l=[]
# for i in range(10000000):
# 	l.append(i)
# print(time.time()-s)

# s=time.time()
# l=[x for x in range(50000000)]
# print(time.time()-s)


# 布什邮件分析 预处理

# inputfile="d://FinalOutput.txt"
# outputfile='d://out1.txt'
# fpin=open(inputfile,"r",encoding="utf-8")
# lines=fpin.readlines()
# fpin.close()
# w="["
# d="["
# pair=[]
# count=0
# mm=-1
# for line in lines:
# 	datas=line.split("\t")
# 	if( int(datas[1])>800):
# 		count+=1
# 		# w+=('"'+datas[0].rstrip()+'",')
# 		# d+=(datas[1].rstrip()+',')
# 		pair.append(line)
# 		if(int(datas[1])>mm):
# 			mm=int(datas[1])
# w+="]\n"
# d+="]"
# print(mm)
# print(count)
# fout=open(outputfile,'w',encoding='utf-8')
# fout.writelines(pair)
 
# fout.close()
#!-- encoding=utf-8
from __future__ import print_function
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans,MiniBatchKMeans
 
 
def loadDataset():
    '''导入文本数据集'''
    f = open('d://test.txt','r')
    dataset = []
    lastPage = None
    for line in f.readlines():
        if '< title >' in line and '< / title >' in line:
            if lastPage:
                dataset.append(lastPage)
            lastPage = line
        else:
            lastPage += line
    if lastPage:
        dataset.append(lastPage)
    f.close()
    return dataset
 
def transform(dataset,stopword=[],n_features=400):
	# f=open("d://part_raw_output.txt",'r',encoding='UTF-8')
	# lines=f.readlines()
	 
	vectorizer = TfidfVectorizer(max_features=n_features,stop_words=stopword, min_df=2,use_idf=True)
	# print(dataset)
	counts = ['This is the an first document.',
     'This is second second an document.',
      'the is the first a document?',
     'the is third one.',
    ]

	X = vectorizer.fit_transform(dataset)
	# print(vectorizer.get_stop_words())
	print(vectorizer.get_feature_names())
	return X,vectorizer

def train(X,vectorizer,true_k=10,minibatch = False,showLable = False):
    #使用采样数据还是原始数据训练k-means，    
    if minibatch:
        km = MiniBatchKMeans(n_clusters=true_k, init='k-means++', n_init=1,
                             init_size=1000, batch_size=1000, verbose=False)
    else:
        km = KMeans(n_clusters=true_k, init='k-means++', max_iter=300, n_init=1,
                    verbose=False)
    km.fit(X)    
    if showLable:
        print("Top terms per cluster:")
        order_centroids = km.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names()
        print ("stop_word",vectorizer.get_stop_words())
        for i in range(true_k):
            print("Cluster %d:" % i, end='')
            for ind in order_centroids[i, :10]:
                print(' %s' % terms[ind], end='')
            print()
    result = list(km.predict(X))
    print ('Cluster distribution:')
    print (dict([(i, result.count(i)) for i in result]))
    leng=len(result)
    # lists=["" for i in range(100)]
    # for i in range(leng):
    # 	lists[result[i]]+="\t"+str(i+1)
    # print(lists)
    # print(len(result))
    # for i in range(100):
    # 	lists[i]+="\n"
    # f=open("d://cluster_result.txt",'w',encoding='utf-8')
    # f.writelines(lists)
    # f.close()
    return -km.score(X)
     
def test(dataset):
    '''测试选择最优参数'''
    # dataset = loadDataset()    
    print("%d documents" % len(dataset))
    X,vectorizer = transform(dataset,n_features=500)
    true_ks = []
    scores = []
    for i in range(3,80,1):        
        score = train(X,vectorizer,true_k=i)/len(dataset)
        print (i,score)
        true_ks.append(i)
        scores.append(score)
    plt.figure(figsize=(8,4))
    plt.plot(true_ks,scores,label="error",color="red",linewidth=1)
    plt.xlabel("n_features")
    plt.ylabel("error")
    plt.legend()
    plt.show()
     
# print(x.shape)
#!--encoding=utf-8
#coding=utf-8

# 信息检索 代码
# import codecs
# f= codecs.open("d://news.txt",'r',"utf-8",errors='ignore')  
# lines=f.readlines()
# f.close()
# count=0
# dataset=[]
# temp=""
# for line in lines:
# 	try:
# 		# print(line)
# 		if(line.strip()=="******"):
# 			dataset.append(temp)
# 			temp=""
# 			count+=1

# 		else:
# 			temp+=line
# 	except:
# 		pass
	 
# print(len(lines))
# print(count,"zz")


# x,vectorizer=transform(dataset)
                                         
# print(x.toarray())             
# print(x.shape)
# score = train(x,vectorizer,true_k=100,showLable=True)/len(dataset)
# print(score)
 
# 信息检索代码结束


import codecs
import os
dir="D:\课程\中国科学院大学\软件系统安全与分析\\test"
for root,dirs,files in os.walk(dir):
	for file in files:
		print(os.path.join(root,file))
fstop=codecs.open("D:\development\python\data\english_stop_word.txt",'r','utf-8')
lines=fstop.readlines()
fstop.close()
stop_word=[]
for line in lines:
	stop_word.append(line.strip())

count=0
dataset=[]
for root,dirs,files in os.walk(dir):
	for file in files:
		f= codecs.open(os.path.join(root,file),'r',"utf-8",errors='ignore')  
		lines=f.readlines()
		f.close()
		temp=""
		flag=False
		for line in lines:
			if(line[0:7]=='Subject'):
				flag=True
			if(line[0:4]=="From"):
				dataset.append(temp)
				count+=1
				temp=""
				flag=False
			if(flag==True):
				temp+=line
		print(len(lines)," ",count) 
print(len(lines))
print(len(dataset))

print(stop_word)
x,vectorizer=transform(dataset,stop_word)

print(x.toarray())
print(x.shape)


score = train(x,vectorizer,true_k=30,showLable=True)/len(dataset)
print (score)


 

#程序运行结果
#  Cluster 0: fw original message subject attachments florida insurance county request beach
# Cluster 1: school schools children education students parents support board public county
# Cluster 2: god jesus people life lord christ subject love america don
# Cluster 3: email response subject message address original click send net http
# Cluster 4: property tax taxes county florida subject fw original message pay
# Cluster 5: insurance homeowners florida companies damage property citizens governor increase bush
# Cluster 6: subject terri fl county attachments 2003 notice dear click beach
# Cluster 7: child support fw original message subject children enforcement court florida
# Cluster 8: fwd attachments subject fw message 2003 development read god bush
# Cluster 9: myflorida jeb bush governor 2003 florida html http change women
# Cluster 10: attorney florida office governor legal court services assistance criminal writing
# Cluster 11: gif attachments http message fw original subject news net 2004
# Cluster 12: water florida subject district county st fl protection food original
# Cluster 13: governor office bush assistance united building senate washington florida federal
# Cluster 14: http gulf1 org htm html subject news attachments net click
# Cluster 15: people time children family care told don life money florida
# Cluster 16: bush jeb governor subject message sincerely fl dear writing news
# Cluster 17: racing industry bill governor florida street bush required hours efforts
# Cluster 18: original message fw subject attachments florida county letter insurance governor
# Cluster 19: governor office services citizens respond writing concerns behalf bush sincerely
# Cluster 20: israel peace war people middle land president american military west
# Cluster 21: illegal law florida subject country foreign people drug government laws
# Cluster 22: president war american iraq bush america people united country government
# Cluster 23: subject bush israel 11 war day read family contact attachments
# Cluster 24: mail message subject address received original reply response office fl
# Cluster 25: de la el en por los del se las al
# Cluster 26: bill governor house bush senate subject florida legislation message phone
# Cluster 27: florida governor bush subject county dear fl support office time
# Cluster 28: license foreign florida legislation governor subject national original insurance message
# Cluster 29: yahoo _____ http mail subject note fwd web free bush
# Cluster distribution:
# {0: 11847, 1: 4189, 2: 3490, 3: 3437, 4: 1992, 5: 3722, 6: 26405, 7: 2425, 8: 5828, 9: 616, 10: 1777, 11: 548, 12: 1455, 13: 747, 14: 5582, 15: 17466, 16: 6266, 17: 1062, 18: 7866, 19: 4084, 20: 1256, 21: 1300, 22: 9741, 23: 861, 24: 3185, 25: 1613, 26: 2953, 27: 8480, 28: 1104, 29: 4198}
# 0.6924093369903555