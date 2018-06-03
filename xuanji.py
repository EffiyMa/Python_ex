# -*- coding:utf-8 -*-
#折叠四围四角红书读法
count=1


def Poem(TList,posr,posc,num):#四围四角红字读法
        pcList=[]
        prList=[]
        for i in range(num):
                row1=TList[posr+i]
                pcList.append(row1[posc]) #右
                row2=TList[posr+num]
                prList.append(row2[posc-i])#下

        for j in range(num-1,-1,-1):
                col1=TList[posr+j+1]
                pcList.append(col1[posc-num])#左
                
                col2=TList[posr]
                prList.append(col2[posc-j-1])

        string1=''.join ( (pcList)[:num]+(prList)[:num]+(pcList)[num:]+(prList)[num:] )
        OutPut(string1,num)
        OutPut(string1[::-1],num)

        string2=''.join ( (prList)[:num]+(pcList)[num:]+(prList)[num:]+(pcList)[:num] )
        OutPut(string2,num)
        OutPut(string2[::-1],num)

        string3=''.join ( (pcList)[num:]+(prList)[num:]+(pcList)[:num]+(prList)[:num] )
        OutPut(string3,num)
        OutPut(string3[::-1],num)

        string4=''.join ( (prList)[num:]+(pcList)[:num]+(prList)[:num]+(pcList)[num:] )
        OutPut(string4,num)
        OutPut(string4[::-1],num)

def OutPut(string,num):
        global count
        print('\n','===========POEM',count,'=========')
        for i in range(len(string)):
                print(string[i],end='')
                if ( (i+1)/num )%2 == 1:
                        print('。')
                elif ( (i+1)/num )%2 == 0:
                        print('，')

        count+=1
                





import codecs
TotalList=[]
count=1

fp=codecs.open("poem.txt","r+",encoding='utf-8')
fp=open("poem.txt",'r')
for line in fp:
        x=list(line.strip('\n'))
        TotalList.append(x) # Model as [[line1],[line2]...]

print("*****"*5,'左上',"*****"*5)
Poem(TotalList,0,7,7)

print("*****"*5,'右上',"*****"*5)
Poem(TotalList,0,28,7)

print("*****"*5,'左下',"*****"*5)
Poem(TotalList,21,7,7)

print("*****"*5,'右下',"*****"*5)
Poem(TotalList,21,28,7)
