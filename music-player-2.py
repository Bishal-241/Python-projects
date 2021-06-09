import os
from playsound import playsound
dir=list()
content=os.listdir()
def showdir(dir):
    for i in dir:
        print(f"{dir.index(i)+1}-{i}")
def play(url):
    a=os.listdir(url)
    b=int(input('Enter the index of song that u want to play'))
    c=f'\\{a[b-1]}'
    fullurl=url + c
    print(type(fullurl))
    playsound(fullurl)
    print(fullurl)

def showfiles(url): #i is use to show file in the irectory of the passed url
    a=os.listdir(url)
    for i in a:
        print(f'{a.index(i)+1}-{i}')

for i in content:
    if '.mp3'  in i:
        pass
    elif '.py' in i:
        pass
    else:
        dir.append(i)
while 1==1:
    showdir(dir)
    a=int(input('Enter the index of drectory that u want to open'))
    a-=1
    c=dir[a]
    newurl=os.getcwd()+f'\\{c}' # --->url of selected directory
    print(newurl)
    showfiles(newurl) 
    play(newurl)
    d=int(input("Enter 1 to restart and 0 to exit"))
    if d==1:
        continue
    elif d==0:
        break
    

