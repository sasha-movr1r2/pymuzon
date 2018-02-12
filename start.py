#player

#*****************************************
#Copyright 2015 Sasha <movr1r2@gmail.com>

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT
#WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
#INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY,FITNESS FOR A PARTICULAR
#PURPOSE AND NONINFRINGEMENT. IN NO EVENT 
#SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
#LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR 
#OTHER DEALINGS IN THE SOFTWARE.
#*******************************************

import os
import glob
import subprocess
import random
#*******************
def zap(j ,i):
    j1=str(j) + '\n'
    i1=str(i) + '\n'
    igr=os.getcwdb()
    os.chdir(cur)
    with open('pam.txt', mode='w' ,encoding="utf-8") as f:
        f.write(j1)
        f.write(i1)
    os.chdir(igr)

#********************
#os.path.exists(path)

def playpam(player,spisok):
    print('igraem i pomnim!')
    if os.path.exists('pam.txt')==True:
        with open('pam.txt', mode='r' ,encoding="utf-8") as f:
            dir=int(f.readline())
            
            song=int(f.readline())
            
        with open(spisok, mode='r' ,encoding="utf-8") as f:
            a=f.read()
        lstdir=a.split(' ')
        lang=len(lstdir)
        
        k=0
    
        for j in  range(dir ,lang , 1):
            os.chdir(lstdir[j])
            fajlo=glob.glob('*.mp3')
            langs=len(fajlo)
            if k>0:
                song=0
    
            for i in range(song ,langs , 1):
                print(fajlo[i])
                zap(j ,i)
                k+=1
                subprocess.call([player , fajlo[i] ])
        os.chdir(cur)
        os.remove('pam.txt')
        osnova(lst)

        
            
    if os.path.exists('pam.txt')==False:
        dir=0
        song=0
        with open(spisok, mode='r' ,encoding="utf-8") as f:
            a=f.read()
        lstdir=a.split(' ')
        lang=len(lstdir)
        for j in  range(dir ,lang , 1):
            os.chdir(lstdir[j])
            fajlo=glob.glob('*.mp3')
            langs=len(fajlo)
            for i in range(song ,langs , 1):
                print(fajlo[i])
                zap(j ,i)
                subprocess.call([player , fajlo[i] ])
        os.chdir(cur)
        os.remove('pam.txt')
        osnova(lst)

#*******************

def playuno(player,spisok):
    print('igraem po odnoj!')
    with open(spisok, mode='r' ,encoding="utf-8") as f:
        a=f.read()
    lstdir=a.split(' ')
    print(lstdir)
    random.shuffle(lstdir)
    lang=len(lstdir)
    
    for j in  range(lang):
        os.chdir(lstdir[j]) 
        fajlo=glob.glob('*.mp3')
        random.shuffle(fajlo)	
        print(fajlo[1])
        subprocess.call([player , fajlo[1] ])
    os.chdir(cur)
    osnova(lst) 
#*******************
def playrandom(player,spisok):
    print("random player!!!")
    with open(spisok, mode='r' ,encoding="utf-8") as f:
        a=f.read()
    lstdir=a.split(' ')
    random.shuffle(lstdir)
    lang=len(lstdir)
    
    for j in  range(lang):
        os.chdir(lstdir[j]) 
        fajlo=glob.glob('*.mp3')
        random.shuffle(fajlo)	
        for i in fajlo:
            print(i)
            subprocess.call([player , i ])
    os.chdir(cur)
    osnova(lst) 
	
#*******************
def  play(player , spisok):
    print("regular player!!!")
    with open(spisok, mode='r' ,encoding="utf-8") as f:
        a=f.read()
    lstdir=a.split(' ')
    lang=len(lstdir)
    
    
    for j in  range(lang):
        os.chdir(lstdir[j])
        fajlo=glob.glob('*.mp3')
    
        for i in fajlo:
            print(i)
            subprocess.call([player , i ])
    os.chdir(cur)
    osnova(lst)
#*******************
def osnova(lst):
    player=lst[0]
    dl=len(lst)
    for i in range(1 ,dl ,1):
        print('{:>4} {}'.format(i ,lst[i]))       
    n=int(input("vvedite nomer spiska!:"))
    spisok=lst[n]
    rejim=['regular','random','uno-random','memor']
    for i in range(4):
        print('{:>4} {}'.format(i ,rejim[i]))
    r=int(input("vvedite nomer rejima:"))
    if r<0:
        quit()
    if r>3:
        quit()
    if r==0:
        play(player ,spisok)
    if r==1:
        playrandom(player ,spisok)
    if r==2:
        playuno(player ,spisok)
    if r==3:
        playpam(player,spisok)
#********************
lst=[ ]
with open("muz.conf", mode='r' ,encoding="utf-8") as f:
        for i in f:
            lst.append(i.rstrip())
cur=os.getcwdb()
osnova(lst)


