l1=['my name is rajeswar']
l2=['   i am from class 12']
l3=['  school name is kendriya vidyalaya malanjkhand']
f=open('detail.txt','w')
f.writelines(l1)
f.writelines(l2)
f.writelines(l3)
f.close()


f=open('detail.txt','r')
x=f.readlines()
print(x)
f.close()

