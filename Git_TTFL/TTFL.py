#---
#       IMPORT LIBRARIES
#---
#import os
import numpy as np
import matplotlib.pyplot as plt
#from scipy.interpolate import interp1d


#---
#       FUNCTIONS
#---

def dataSaison(name):
    with open(name,"r", encoding="utf-8") as f:
        lines = [line.strip().split(" ") for line in f]
    res = []
    res.append([int(k[0]) for k in lines[::-1]])
    res.append([k[1] for k in lines[::-1]])
    res.append([int(k[2]) for k in lines[::-1]])
    return (res)

def somme(l):
    res = [0]
    for i in l:
        res.append(res[-1]+i)
    return(res)


def plotbar(x,l,c,text):
    plt.bar([x],[l], color=c)
    plt.text(x-0.2,l+1,text,rotation=90,color=c,fontsize=10)

def singlePoint(a,b,c,line=':',mark='*',text='',moy=False):
    plt.plot([a],[b],mark,color=c)
    if moy:plt.plot([0,a],[0,b],line,color=c)
    plt.text(a+0.5,b+0.5,text,color=c,fontsize=15)

#---
#       DICTIONNNAIRES
#---



#---
#       PROGRAM
#---
#os.chdir("/Users/Louis/Desktop/TTFL")


Louis2021 = dataSaison('TTFLLouis.txt')
Romain2021 = dataSaison('TTFLRomain.txt')
Pierre2021 = dataSaison('TTFLPierre.txt')

Louis1920 = dataSaison('TTFLLouis1920.txt')
Romain1920 = [dataSaison('TTFLRomain1920.txt')[0][::-1],dataSaison('TTFLRomain1920.txt')[2][::-1]]
Pierre1920 = [dataSaison('TTFLPierre1920.txt')[0][::-1],dataSaison('TTFLPierre1920.txt')[2][::-1]]

Louis1819 = [dataSaison('TTFLLouis1819.txt')[0][::-1],dataSaison('TTFLLouis1819.txt')[2][::-1]]
Romain1718 = [dataSaison('TTFLRomain1718.txt')[0][::-1],dataSaison('TTFLRomain1718.txt')[2][::-1]]
Romain1819 = [dataSaison('TTFLRomain1819.txt')[0][::-1],dataSaison('TTFLRomain1819.txt')[2][::-1]]
Louis1718 = [dataSaison('TTFLLouis1718.txt')[0][::-1],dataSaison('TTFLLouis1718.txt')[2][::-1]]
Pierre1819 = [dataSaison('TTFLPierre1819.txt')[0][::-1],dataSaison('TTFLPierre1819.txt')[2][::-1]]
Pierre1718 = [dataSaison('TTFLPierre1718.txt')[0][::-1],dataSaison('TTFLPierre1718.txt')[2][::-1]]



MoyLouis2021TOP = np.average(Louis2021[2][:8])


NbPick = len(Louis2021[2])

PremGene = 2111

plt.close('all')
fig=plt.figure(figsize=(15,8))
fig.set_facecolor('white')


singlePoint(NbPick,PremGene,'silver','-.','*',r'NicJD',True)

plt.plot(Romain1920[0],Romain1920[1],'.-',linewidth=1,markersize=2, color='lightskyblue')
plt.plot(Pierre1920[0],Pierre1920[1],'.-',linewidth=1,markersize=2, color='lightgreen')

for i in range(0,len(Louis1718[1])):
    singlePoint(Louis1718[0][i],Louis1718[1][i],'red','-','^')
for i in range(0,len(Romain1718[1])):
    singlePoint(Romain1718[0][i],Romain1718[1][i],'dodgerblue','-','^')
for i in range(0,len(Pierre1718[1])):
    singlePoint(Pierre1718[0][i],Pierre1718[1][i],'lime','-','^')
for i in range(0,len(Louis1819[1])):
    singlePoint(Louis1819[0][i],Louis1819[1][i],'red','-','p')
for i in range(0,len(Romain1819[1])):
    singlePoint(Romain1819[0][i],Romain1819[1][i],'dodgerblue','-','p')
for i in range(0,len(Pierre1819[1])):
    singlePoint(Pierre1819[0][i],Pierre1819[1][i],'lime','-','p')

plt.plot([],[],'^',color='black',label='17/18')
plt.plot([],[],'p',color='black',label='18/19')


plt.plot(np.arange(len(Louis1920[2])+1),somme(Louis1920[2]),'.-',linewidth=1, markersize=2,color='lightsalmon')
plt.plot(np.arange(len(Louis2021[2])+1),somme(Louis2021[2]),'o-',markersize=3,label='Louis', color='red')
plt.plot(np.arange(len(Romain2021[2])+1),somme(Romain2021[2]),'o-',markersize=3,label='Romain', color='blue')
plt.plot(np.arange(len(Pierre2021[2])+1),somme(Pierre2021[2]),'o-',markersize=3,label='Pierre', color='green')



plt.title('saison 2020/21',fontsize=15)
plt.xlabel('pick n°', fontsize=15)
plt.ylabel('Score TTFL', fontsize=15)
plt.legend(fontsize=15,loc=2)
plt.axis([NbPick-27,NbPick+13,PremGene-1400,PremGene+50])
#plt.axis([0,180,0,6500])
plt.grid()
plt.show()


fig=plt.figure(figsize=(5,5))
fig.set_facecolor('white')

moyz = [[Louis1718[1][-1]/Louis1718[0][-1],'Louis - 17/18','red'],
[Louis1819[1][-1]/Louis1819[0][-1],'pick 114 - 18/19','red'],
[somme(Louis1920[2])[-1]/(len(somme(Louis1920[2]))-1),'Louis - 19/20','red'],
[somme(Louis2021[2])[-1]/(len(somme(Louis2021[2]))-1),'Louis - 20/21','red'],
[Romain1718[1][-1]/Romain1718[0][-1],'Romain - 17/18','blue'],
[Romain1819[1][-1]/Romain1819[0][-1],'pick 114 - 18/19','blue'],
[Romain1920[1][-1]/Romain1920[0][-1],'Romain - 19/20','blue'],
[somme(Romain2021[2])[-1]/(len(somme(Romain2021[2]))-1),'Romain - 20/21','blue'],
[Pierre1718[1][-1]/Pierre1718[0][-1],'Pierre - 17/18','green'],
[Pierre1819[1][-1]/Pierre1819[0][-1],'pick 114 - 18/19','green'],
[Pierre1920[1][-1]/Pierre1920[0][-1],'Pierre - 19/20','green'],
[somme(Pierre2021[2])[-1]/(len(somme(Pierre2021[2]))-1),'Pierre - 20/21','green']]

for m in range(0,len(moyz)):
    plotbar(m,moyz[m][0],moyz[m][2],moyz[m][1])
#    plotbar(m,somme(Louis1920[2])[-1]/len(somme(Louis1920[2])),c,text)

plt.title('Moyennes',fontsize=15)
plt.ylabel('score moyen par pick', fontsize=15)
plt.axis([-0.7,11.7,30,47])
plt.grid()
plt.show()


EcartPiLou2021=[somme(Louis2021[2])[i]-somme(Pierre2021[2])[i] for i in range (0,len(Pierre2021[2])+1)]

fig=plt.figure(figsize=(10,5))
fig.set_facecolor('white')

plt.plot(np.arange(len(EcartPiLou2021)),EcartPiLou2021,'o-',markersize=3, color='orange')
plt.plot([0,len(EcartPiLou2021)],[0,0],':',linewidth=3,color='red')
plt.title('Ecart avec Pierre 2020-21',fontsize=15)
plt.xlabel('pick n°', fontsize=15)
plt.grid()
plt.show()

