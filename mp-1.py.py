import os #--->importing os module to get os data like current directory and files list
from playsound import playsound
import subprocess
menu=('Show directory','Show FIles')
def menuList():
    menu=('Show directory','Show FIles')
    print('#*#*---------->Menus<------------*#*#')
    for i in menu:
        index=menu.index(i)
        num=(menu.index(i))+1
        print(f'{num}-{menu[index]}')
def printfiles():
    a=sortFiles()
    for i in a:
        print(f'{a.index(i)+1}-{i}')
def showcontent():
    pass
    a=os.listdir()
    num=len(a)+1
    print('--->Contents')
    for i in a:
        print(f'{a.index(i)+1}-{i}')
def showfiles():
    pass
def sortFiles():
    File=os.listdir()
    musicList=list()
    for i in File:
        if '.mp3' in i:
            musicList.append(i)
    return musicList        
def sortDir():
    a=os.listdir()
    dir=list()
    for i in a:
        if '.mp3' in i:
           continue
        else:
            dir.append(i)
    return dir
def printDir():
    a=sortDir()
    for i in a:
        print(f'{a.index(i)+1}-{i}')

def main():
    files=sortFiles()
    dir=sortDir()
    print(f'Hello Mr/Mrs-{os.getlogin()}-It"s me Bishal Kr Shah And this is one of my first and dream project So Lets Enjoy it')
    run=True
    print("So at first What U want to do:")
    for i in menu:
        menuList()
        choice=int(input("Enter index of your choice: "))
        if choice==1:
            printDir()
            continue
        elif choice ==2:
            printfiles()
            choiceinfiles=input('Wanna Go back or playsong[G/P] :')
            if choiceinfiles=='G' or choiceinfiles=='g':
                continue
            if choiceinfiles=='P'or choiceinfiles=='p':
                choicetoplay=int(input("Enter index of song that u want to play: "))
                playsound(files[choicetoplay-1])

                
        
main()

    

