import os #--->importing os module to get os data like current directory and files list
from playsound import playsound
a=os.getcwd() #---->
dirName=input("Enter Name of Directory")
workingDir=a+f'\\{dirName}'
files=os.listdir(workingDir)
for i in range(len(files)):
    print(i+1,'-',files[i])
choice=int(input("Enter the index of song that u want to play"))
choice=choice-1
url=workingDir+f'\\{files[choice]}'
print(url)
print(type(url))
newurl=url.replace('\\', '\\\\')
playsound(newurl)
