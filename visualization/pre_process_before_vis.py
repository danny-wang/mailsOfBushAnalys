inputfile="d://FinalOutput.txt"
outputfile='d://out1.txt'
fpin=open(inputfile,"r",encoding="utf-8")
lines=fpin.readlines()
fpin.close()
w="["
d="["
pair=[]
count=0
mm=-1
for line in lines:
	datas=line.split("\t")
	if( int(datas[1])>800):
		count+=1
		# w+=('"'+datas[0].rstrip()+'",')
		# d+=(datas[1].rstrip()+',')
		pair.append(line)
		if(int(datas[1])>mm):
			mm=int(datas[1])
w+="]\n"
d+="]"
print(mm)
print(count)
fout=open(outputfile,'w',encoding='utf-8')
fout.writelines(pair)
 
fout.close()