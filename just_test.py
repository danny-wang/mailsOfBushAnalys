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


 