#!/usr/bin/env python
# coding: utf-8

# In[3]:

import matplotlib.pyplot as plt
################################      CALCULADORA            ####################
###################
# Igualar
###################
def igualar(y1,y2):                                             
    y1=str(y1)
    y2=str(y2)
    while len(y1) != len(y2):
        if len(y1) < len(y2):
            x0 = '0'
            x0 += y1
            y1 = x0
        else:
            y0 = '0'
            y0 += y2
            y2 = y0
    return (y1,y2)
##################
# Complemento A1
##################
def comp1(y1):                             
    c = ''
    for i in range(len(y1)):
        if y1[i] == '0':
            c += '1'
        else:
            c += '0'
    return c
#####################################
# Funciones de binario a otro sistema 
####################################
def bina_a_decim(y): 
    y=str(y)
    y1=0
    l=len(y)-1    
    for i in range(len(y)):
        y1+=int(y[i])*2**l
        l=l-1
    return y1

def bin_a_oct(n):
    n=str(n)
    dec=int(n,2)
    octa=oct(dec).split('o')[1]
    return (octa)

def bin_a_hex(y1):
    y1=str(y1)
    dec=int(y1,2)
    hexa=hex(dec).split('x')[1]
    return hexa
    #print(hexa)

#########################################
# Funciones de operaciones entre binarios
#########################################

#Suma
def sumbin(n,m):                          
    z1, z2 = igualar(n,m)
    c = ''
    n = '0'                                    
    for i in range(len(z1)):
        i = len(z1)-(1+i)
        if z1[i] == z2[i] and n == '1':
            c += '1'
            if z1[i] == '0':
                n = '0'
        elif z1[i] == z2[i] and n == '0':
            c += '0'
            if z1[i] == '1':
                n = '1'
        else:
            if n == '0':
                c += '1'
            else:
                c += '0'
                n = '1'
    if n == '1':
        c += '1'
    cc = ''
    for i in range(len(c)):             
        i = len(c)-(1+i)
        cc += c[i]
    c = cc                          
    return c

#Resta
def restabin(a,b): 
    x=str(a)
    y=str(b)
    if len(x) > len(y):
        n, m = igualar(a,b)
        cob = comp1(m)
        pas2 = sumbin(n,cob)   
        if len(pas2) == len(n):
            r = ['1', comp1(pas2)]
            if int(comp1(pas2)) == 0:
                r = '0'
            return r
        else:
            r = ''
            for i in range(len(pas2)): 
                i = i + 1
                if i != len(pas2):
                    r += pas2[i]
            r = sumbin(r,'1')
            return r
    else:
        m, n = igualar(a,b)
        cob = comp1(m)
        pas2 = sumbin(n,cob)   
        if len(pas2) == len(n):
            r = ['1', comp1(pas2)]
            if int(comp1(pas2)) == 0:
                r = '0'
            return r
        else:
            r = ''
            s = ''
            for i in range(len(pas2)): 
                i = i + 1
                if i != len(pas2):
                    r += pas2[i]
            r = sumbin(r,'1')
            s = '-'
            return r
        
#Multiplicacon
def mbin(z1,z2):
    c = '0'
    while int(z2) != 0:
        c = sumbin(c,z1)
        z2 = restabin(z2,'1')
    return c

#Division
def dbinent(y1,y2):
    
    c='0'
    if int(y2) == 0:
        return ('Indeterminación',0)
    while int(y1) >= int(y2):
        y1 = restabin(y1,y2)
        c = sumbin(c,'1')

    pd=mbin(y1,1100100) #sucecion de restas para decimeales
    w='0'
    while int(pd) >= int(y2):
        pd = restabin(pd,y2)
        w = sumbin(w,'1')
    return (c,w)
###################
# Entradas
###################
import numpy as np
#selecionar el sistema numerico de la primera entrada
def entrada1(): #de decimal a binario
    E1=selec.get()
    if  E1==1:
        def dec_a_bin (decimal):
            binario=''
            while decimal // 2 !=0:
                binario=str(decimal % 2) + binario
                decimal= decimal // 2
            return str(decimal) + binario 
        num= int(vartxt1.get())
        varbin1.set(int(dec_a_bin (num))) #interfaz

# Bin- esta entrada es en base 2 (binario) y se debe pasar a base 2 (binario)
    elif E1==2:
        x=list(vartxt1.get())
        y1=0
        l=len(x)-1    
        for i in range(len(x)):
            y1+=int(x[i])*10**l
            l=l-1
        #print(y1)
        #a=str(x)
        #print(a)
        varbin1.set(int(y1)) #interfaz
    
# Oct- esta entrada es en base 8 (octal) y se debe pasar a base 2 (binario)
    elif E1==3:
        x= int(vartxt1.get())
        dictoct2bin = {'0':'000','1':'001','2':'010','3':'011','4':'100','5':'101','6':'110','7':'111'}
        Numbin = []
        Num = str(x)
        Nlist = list(Num)
        for i in Nlist:
            Numbin.append(dictoct2bin[i])
        if len(Numbin) != 1:
            Nbb = ''
            for i in range(0,len(Numbin)):
                Nbb = Nbb+ Numbin[i]
        else:
            Nbb = str(Numbin[0])
        Numbin = list(Nbb)
        for i in range(0,len(Numbin)):
            Numbin[i] = int(Numbin[i])
        y1=0
        l=len(Numbin)-1    
        for i in range(len(Numbin)):
            y1+=int(Numbin[i])*10**l
            l=l-1
        #print(y1)
        #print(Numbin)
        varbin1.set(int(y1)) #interfaz 
    
# Hex- esta entrada es en base 16 (hexadecimal) y se debe pasar a base 2 (binario)
    elif E1==4:
        x= str(vartxt1.get())
        dicthex2bin = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110',
                       '7':'0111','8':'1000','9':'1001','a':'1010','b':'1011','c':'1100','d':'1101','e':'1110','f':'1111'}
        Numbin = []
        Num = str(x)
        Nlist = list(Num)
        for i in Nlist:
            Numbin.append(dicthex2bin[i])
        if len(Numbin) != 1:
            Nbb = ''
            for i in range(0,len(Numbin)):
                Nbb = Nbb+ Numbin[i]
        else:
            Nbb = str(Numbin[0])
        Numbin = list(Nbb)
        for i in range(0,len(Numbin)):
            Numbin[i] = int(Numbin[i])
        y1=0
        l=len(Numbin)-1    
        for i in range(len(Numbin)):
            y1+=int(Numbin[i])*10**l
            l=l-1
        #print(y1)
        #print(Numbin)
        varbin1.set(int(y1))
################################################################################################
#selecionar el sistema numerico de la segunda entrada
def entrada2(): #de decimal a binario
    E2=selec2.get()
    if  E2==1:
        def bin_a_dec (decimal):
            binario=''
            while decimal // 2 !=0:
                binario=str(decimal % 2) + binario
                decimal= decimal // 2
            return str(decimal) + binario 
        
        num = int(vartxt2.get())
        #print(binarizar(numero))
        varbin2.set(int(bin_a_dec (num)))

# Bin- esta entrada es en base 2 (binario) y se debe pasar a base 2 (binario)
    elif E2==2:
        x=list(vartxt2.get())
        y2=0
        l=len(x)-1    
        for i in range(len(x)):
            y2+=int(x[i])*10**l
            l=l-1
        #print(y2)
        #a=str(x)
        #print(a)
        varbin2.set(int(y2))
    
# Oct- esta entrada es en base 8 (octal) y se debe pasar a base 2 (binario)
    elif E2==3:
        x= int(vartxt2.get())
        dictoct2bin = {'0':'000','1':'001','2':'010','3':'011','4':'100','5':'101','6':'110','7':'111'}
        Numbin = []
        Num = str(x)
        Nlist = list(Num)
        for i in Nlist:
            Numbin.append(dictoct2bin[i])
        if len(Numbin) != 1:
            Nbb = ''
            for i in range(0,len(Numbin)):
                Nbb = Nbb+ Numbin[i]
        else:
            Nbb = str(Numbin[0])
        Numbin = list(Nbb)
        for i in range(0,len(Numbin)):
            Numbin[i] = int(Numbin[i])
        y2=0
        l=len(Numbin)-1    
        for i in range(len(Numbin)):
            y2+=int(Numbin[i])*10**l
            l=l-1
        #print(y2)
        #print(Numbin)
        varbin2.set(int(y2))
    
# Hex- esta entrada es en base 16 (hexadecimal) y se debe pasar a base 2 (binario)
    elif E2==4:
        x= str(vartxt2.get())
        dicthex2bin = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110',
                       '7':'0111','8':'1000','9':'1001','a':'1010','b':'1011','c':'1100','d':'1101','e':'1110','f':'1111'}
        Numbin = []
        Num = str(x)
        Nlist = list(Num)
        for i in Nlist:
            Numbin.append(dicthex2bin[i])
        if len(Numbin) != 1:
            Nbb = ''
            for i in range(0,len(Numbin)):
                Nbb = Nbb+ Numbin[i]
        else:
            Nbb = str(Numbin[0])
        Numbin = list(Nbb)
        for i in range(0,len(Numbin)):
            Numbin[i] = int(Numbin[i])
        y2=0
        l=len(Numbin)-1    
        for i in range(len(Numbin)):
            y2+=int(Numbin[i])*10**l
            l=l-1
        #print(y2)
        #print(Numbin)
        varbin2.set(int(y2))

###################
## operaciones
##################

def sumar():
    varres.set(str(sumbin(varbin1.get(),varbin2.get())))
    conver.set('')
    conver2.set('')
    varres2.set('')
def restar():
    varres.set(str(restabin(varbin1.get(),varbin2.get())))
    conver.set('')
    conver2.set('')
    varres2.set('')
def multiplicar():
    varres.set(str(mbin(varbin1.get(),varbin2.get())))
    conver.set('')
    conver2.set('')
    varres2.set('')
def dividir():
    E=dbinent(varbin1.get(),varbin2.get())
    varres.set(str(E[0]))
    varres2.set(str(E[1]))
    conver.set('')
    conver2.set('')
def limpiar():
    varres.set('')
    varres2.set('')
    vartxt1.set('')
    vartxt2.set('')
    varbin1.set('')
    varbin2.set('')
    conver.set('')
    conver2.set('')
####################
# Salida convertida
####################

def entrada3(): 
    E3=selec3.get()
    
    if  E3 == 2:
        conver.set(str(varres.get()))
        conver2.set(str(varres2.get()))
    elif E3 == 1:
        conver.set(str(bina_a_decim(varres.get())))
        conver2.set(str(bina_a_decim(varres2.get())))
    elif E3 == 3:
        conver.set(str(bin_a_oct(varres.get())))
        conver2.set(str(bin_a_oct(varres2.get())))
    elif E3 == 4:
        conver.set(str(bin_a_hex(varres.get())))
        conver2.set(str(bin_a_hex(varres2.get())))

########################################
## Interfaz
########################################
from tkinter import*
import tkinter as tk
ventana = Frame(height=480,width=280)
ventana.pack(padx=10,pady=10)
ventana.configure(background="#CD6155")

vartxt1=StringVar() #entrada 1
txt1= Entry(ventana,textvariable=vartxt1).place(x=10,y=10)
vartxt2=StringVar() #entrada 2
txt2= Entry(ventana,textvariable=vartxt2).place(x=150,y=10)

varbin1=StringVar()  #binario 1
txtb1= Entry(ventana,textvariable=varbin1).place(x=10,y=110)
varbin2=StringVar()   #binario 2
txtb2= Entry(ventana,textvariable=varbin2).place(x=150,y=110)


varres=StringVar() # respuesta en binario
txtres= Entry(ventana,textvariable=varres,width=42).place(x=10,y=295)
varres2=StringVar() # respuesta en binario DECIMALES
txtres2= Entry(ventana,textvariable=varres2,width=23).place(x=120,y=315)
conver=StringVar() # respuesta convertida
txconver= Entry(ventana,textvariable=conver,width=42).place(x=10,y=430)
conver2=StringVar() # respuesta convertida DECIMALES
txconver2= Entry(ventana,textvariable=conver2,width=23).place(x=120,y=450)


bsum = Button(ventana,command=sumar,text='Sumar',padx=42,pady=5,background="#D5D8DC").place(x=10,y=150) #boton suma
bres = Button(ventana,command=restar,text='Restar',padx=41,pady=5,background="#D5D8DC").place(x=150,y=150) #boton resta
bmul = Button(ventana,command=multiplicar,text='Multiplicar',padx=30,pady=5,background="#D5D8DC").place(x=10,y=190) # boton mult
bdiv = Button(ventana,command=dividir,text='Dividir',padx=40,pady=5,background="#D5D8DC").place(x=150,y=190) #  boton divi
blim = Button(ventana,command=limpiar,text='Limpiar',padx=100,pady=5,background="#F7DC6F").place(x=17,y=230) # boton limpiar

selec=IntVar()
Cdec= Radiobutton(ventana,command=entrada1,text='Dec',fg="white",value=1,variable=selec,background="#CD6155").place(x=10,y=30) 
Cbin= Radiobutton(ventana,command=entrada1,text='Bin',fg="white",value=2,variable=selec,background="#CD6155").place(x=60,y=30)
Coct= Radiobutton(ventana,command=entrada1,text='Oct',fg="white",value=3,variable=selec,background="#CD6155").place(x=10,y=50)
Chex= Radiobutton(ventana,command=entrada1,text='Hex',fg="white",value=4,variable=selec,background="#CD6155").place(x=60,y=50)

selec2=IntVar()
Cdec2= Radiobutton(ventana,command=entrada2,text='Dec',fg="white",value=1,variable=selec2,background="#CD6155").place(x=160,y=30)
Cbin2= Radiobutton(ventana,command=entrada2,text='Bin',fg="white",value=2,variable=selec2,background="#CD6155").place(x=210,y=30)
Coct2= Radiobutton(ventana,command=entrada2,text='Oct',fg="white",value=3,variable=selec2,background="#CD6155").place(x=160,y=50)
Chex2= Radiobutton(ventana,command=entrada2,text='Hex',fg="white",value=4,variable=selec2,background="#CD6155").place(x=210,y=50)

selec3=IntVar()
Cdec3= Radiobutton(ventana,command=entrada3,text='Dec',fg="white",value=1,variable=selec3,background="#CD6155").place(x=90,y=380)
Cbin3= Radiobutton(ventana,command=entrada3,text='Bin',fg="white",value=2,variable=selec3,background="#CD6155").place(x=140,y=380)
Coct3= Radiobutton(ventana,command=entrada3,text='Oct',fg="white",value=3,variable=selec3,background="#CD6155").place(x=90,y=400)
Chex3= Radiobutton(ventana,command=entrada3,text='Hex',fg="white",value=4,variable=selec3,background="#CD6155").place(x=140,y=400)

etiqueta2=tk.Label(ventana,text='Resultado en Binario',fg="white",padx=10,pady=5,background="#CD6155").place(x=10,y=265)
etiqueta3=tk.Label(ventana,text='Elija el sistema al que desea convertir',
                   fg="white",padx=10,pady=5,background="#CD6155").place(x=10,y=355)
etiqueta4=tk.Label(ventana,text='punto decimal',
                   fg="white",padx=10,pady=5,background="#CD6155").place(x=10,y=315)
etiqueta5=tk.Label(ventana,text='punto decimal',
                   fg="white",padx=10,pady=5,background="#CD6155").place(x=10,y=450)
etiqueta1=tk.Label(ventana,text='Entradas convertidas a binario ',
                   fg="white",padx=10,pady=5,background="#CD6155").place(x=10,y=80)

ventana.mainloop()
