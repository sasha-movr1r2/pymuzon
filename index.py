#programma dlja sostavlenija spiskov direktorij

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
import sys
if len(sys.argv)==1:
    print('posle imeni programmy nado zapisat imja kornevoj direktorii s muzykalnymi fajlami!!!') 
else:	
    papka= sys.argv[1] 
	
#raskrytie na pervom urovne

def spis(papka):
    lst=os.listdir(papka)
    lang=len(lst)
#  dobavljaem absolutnyj put

    for i in range(lang):
        lst[i]=papka +lst[i] +'/' + ' '
    lang=len(lst)
        
		
#  delaem iz spiska stroku

    stroka=''

    for i in range(lang):
        stroka+=lst[i]
    return(stroka)
	
#vypolnjaem

stroka=spis(papka)
#glubina vlojenija
 
n=int(input("vvedite glubinu  1 or 2:"))
if  n==1:
#Pishem v fajl

    with open('index.txt', mode='w' ,encoding="utf-8") as f:
                f.write(stroka)
if n==2:
    a=''
    lstdir=stroka.split(' ')
    lang=len(lstdir)
    for i in range((lang - 1)):
        a+=spis(lstdir[i])
    print(a)
    with open('index.txt', mode='w' ,encoding="utf-8") as f:
        f.write(a)