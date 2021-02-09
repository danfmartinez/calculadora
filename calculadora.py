# -*- coding: utf-8 -*-
"""
@author: danfmartinez
"""
################################      CALCULADORA            ####################
from tkinter import*
import tkinter as tk
"""
Igualar
"""
def igualar(y1,y2) -> tuple:                                             
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

"""
Complemento A1
"""
def comp1(y1) -> str:                             
    c = ''
    for i in range(len(y1)):
        if y1[i] == '0':
            c += '1'
        else:
            c += '0'
    return c
"""
Funciones de binario a otro sistema 
"""
# binario a decimal
def bina_a_decim(binario: int) -> int: 
    y=str(binario)
    y1=0
    l=len(y)-1    
    for i in range(len(y)):
        y1+=int(y[i])*2**l
        l=l-1
    return y1

# binario a octal
def bin_a_oct(bina: int) -> int:
    dict_bin_oct = {"000":"0", "001":"1", "010":"2", "011":"3", "100":"4", "101":"5", "110":"6","111":"7"}
    NumList = str(bina)
    while len(NumList) % 3 != 0:
        A0 = "0"
        A0 += NumList
        NumList = A0
    
    NumOct = []    
    NumList = list(NumList)
    for i in range(0,len(NumList),3):
         num = NumList[i] + NumList[i+1] + NumList[i+2]
         NumOct.append(dict_bin_oct[num]) 
    if len(NumOct) !=1 :
        octal = ""
        for i in NumOct:
            octal += i
    else:
        octal = NumOct[0]
    octal = int(octal)
    return octal

# binario a hexa
def bin_a_hex(bina: int) -> str:
    dict_bin_hexa = {"0000":"0", "0001":"1", "0010":"2", "0011":"3", "0100":"4", "0101":"5",
                    "0110":"6","0111":"7", "1000": "8", "1001":"9", "1010":"A","1011":"B", 
                    "1100":"C", "1101":"D", "1110":"E", "1111":"F"}
    NumList = str(bina)
    while len(NumList) % 4 != 0:
        A0 = "0"
        A0 += NumList
        NumList = A0
    
    NumHexa = []    
    NumList = list(NumList)
    for i in range(0,len(NumList), 4):
         num = NumList[i] + NumList[i+1] + NumList[i+2] + NumList[i+3]
         NumHexa.append(dict_bin_hexa[num]) 
    if len(NumHexa) !=1 :
        Hexa = ""
        for i in NumHexa:
            Hexa += i
    else:
        Hexa = NumHexa[0]
    
    return Hexa

"""
Funciones de otro sistema a binario
"""
# de decimal a binario
def dec_a_bin (decimal: int) -> int:
    binario=''
    while decimal // 2 !=0:
        binario=str(decimal % 2) + binario
        decimal= decimal // 2
    return int ( str(decimal) + binario) 

# de octal a binario
def octal_a_bin(octal: int) -> int:
    dictoct2bin = {'0':'000','1':'001','2':'010','3':'011','4':'100','5':'101','6':'110','7':'111'}
    Numbin = []
    Nlist = list(str(octal))
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
    binario=0
    l=len(Numbin)-1    
    for i in range(len(Numbin)):
        binario += int(Numbin[i])*10**l
        l=l-1
    return binario

#de hexa a binario
def hex_a_bin(hexa: str) -> int:
    dicthex2bin = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110',
                   '7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100',
                   'D':'1101','E':'1110','F':'1111'}
    Numbin = []
    Nlist = list(hexa)
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
    binario=0
    l=len(Numbin)-1    
    for i in range(len(Numbin)):
        binario += int(Numbin[i])*10**l
        l=l-1
    return binario 
   
# confirmar numero binario
def confirmar_bin (binario: int) -> bool:
    num_list = list (str(binario))
    for i in num_list:
        if i != "0" and i != "1":
            return False
    return True    
                
"""
Funciones de operaciones entre binarios
"""

#Suma
def sumbin(n,m) -> str:                          
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
def restabin(a,b) -> str: 
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
def mbin(z1,z2) -> str:
    c = '0'
    while int(z2) != 0:
        c = sumbin(c,z1)
        z2 = restabin(z2,'1')
    return c

#Division
def dbinent(y1,y2) -> str:
    
    c='0'
    if int(y2) == 0:
        return ('INDETERMINACION',"")
    while int(y1) >= int(y2):
        y1 = restabin(y1,y2)
        c = sumbin(c,'1')

    pd=mbin(y1,1100100) #sucecion de restas para decimeales
    w='0'
    while int(pd) >= int(y2):
        pd = restabin(pd,y2)
        w = sumbin(w,'1')
    return (c,w)

"""
Entradas y salidas de la interfaz
"""

def entrada1():
    maximo =  11000011010100000 # numero maximo soportado (cien mil) en binario
    E1 = selec.get()
    num1 = vartxt1.get()
    convertido = 0
    try:
        if E1 == 1: # decimal a binario
            convertido = dec_a_bin(int(num1))
        
        elif E1 == 2: # binario a binario
            confirmar = confirmar_bin(int(num1))
            if confirmar == True:
                convertido = int(num1)
            else:
                raise Exception
        
        elif E1 == 3: # octal a binario
            convertido = octal_a_bin(int(num1))
        
        elif E1 == 4: # hexadecimal binario
            convertido = hex_a_bin(num1.upper())
        
        if convertido < maximo:
            varbin1.set(convertido)
        else:
            varbin1.set("math ERROR")    
    except:
        varbin1.set("syntx ERROR")
        
def entrada2():
    maximo2 =  11000011010100000 # numero maximo soportado (cien mil) en binario
    E2 = selec2.get()
    num2= vartxt2.get()
    convertido2 = 0
    try:
        if E2 == 1: # decimal a binario
            convertido2 = dec_a_bin(int (num2) )
        
        elif E2 == 2: # binario a binario
            confirmar = confirmar_bin(int(num2))
            if confirmar == True:
                convertido = int(num2)
            else:
                raise Exception
        elif E2 == 3: # octal a binario
            convertido2 = octal_a_bin(int(num2))
        
        elif E2 == 4: # hexadecimal binario
            convertido2 = hex_a_bin(num2.upper())
    
        if convertido2 < maximo2:
            varbin2.set(convertido2)
        else:
            varbin2.set("math ERROR")
    except: 
        varbin2.set("syntx ERROR")
"""
operaciones
"""
def sumar():
    if ("ERROR" in varbin1.get() or "ERROR" in varbin2.get() ):
        varres.set("ERROR")
    else :    
        varres.set(str(sumbin(varbin1.get(),varbin2.get())))
        conver.set('')
        conver2.set('')
        varres2.set('')
def restar():
    if ("ERROR" in varbin1.get() or "ERROR" in varbin2.get() ):
        varres.set("ERROR")
    else:
        varres.set(str(restabin(varbin1.get(),varbin2.get())))
        conver.set('')
        conver2.set('')
        varres2.set('')
def multiplicar():
    if ("ERROR" in varbin1.get() or "ERROR" in varbin2.get() ):
        varres.set("ERROR")
    else:
        varres.set(str(mbin(varbin1.get(),varbin2.get())))
        conver.set('')
        conver2.set('')
        varres2.set('')
def dividir():
    if ("ERROR" in varbin1.get() or "ERROR" in varbin2.get()):
        varres.set("ERROR")
    else:
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

"""
Salida convertida a un sistema seleccionado 
"""

def entrada3(): 
    E3=selec3.get()
    if "ERROR" in varres.get():
        conver.set("ERROR")
    else:
        if  E3 == 2:
            conver.set(str(varres.get()))
            if varres2.get() != "":
                conver2.set(str(varres2.get()))
        elif E3 == 1:
            conver.set(str(bina_a_decim(varres.get())))
            if varres2.get() != "":
                conver2.set(str(bina_a_decim(varres2.get())))
        elif E3 == 3:
            conver.set(str(bin_a_oct(varres.get())))
            if varres2.get() != "":
                conver2.set(str(bin_a_oct(varres2.get())))
        elif E3 == 4:
            conver.set(str(bin_a_hex(varres.get())))
            if varres2.get() != "":
                conver2.set(str(bin_a_hex(varres2.get())))       

"""
interfaz
"""
ventana = Frame(height=480,width=280)
ventana.pack(padx=10,pady=10)
ventana.configure(background="#CD6155")

vartxt1=StringVar() #entrada 1
txt1= Entry(ventana,textvariable=vartxt1).place(x=10,y=10)
vartxt2=StringVar() #entrada 2
txt2= Entry(ventana,textvariable=vartxt2).place(x=150,y=10)

varbin1=StringVar()  #binario 1
txtb1= Entry(ventana,textvariable=varbin1, state=DISABLED).place(x=10,y=110)
varbin2=StringVar()   #binario 2
txtb2= Entry(ventana,textvariable=varbin2, state=DISABLED).place(x=150,y=110)


varres=StringVar() # respuesta en binario
txtres= Entry(ventana,textvariable=varres,width=42, state=DISABLED).place(x=10,y=295)
varres2=StringVar() # respuesta en binario DECIMALES
txtres2= Entry(ventana,textvariable=varres2,width=23, state=DISABLED).place(x=120,y=315)
conver=StringVar() # respuesta convertida
txconver= Entry(ventana,textvariable=conver,width=42, state=DISABLED).place(x=10,y=430)
conver2=StringVar() # respuesta convertida DECIMALES
txconver2= Entry(ventana,textvariable=conver2,width=23, state=DISABLED).place(x=120,y=450)


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
