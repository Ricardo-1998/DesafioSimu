import tkinter as tk
from PIL import ImageTk, Image
from imagenes import AnimatedGIF
import os, sys
from tkinter import font as tkFont

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = getattr(sys, '_MEIPASS', os.getcwd())
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def cambiar(titulo,num):
    verificarTitulo()
    cambiarTitulo(titulo)
    olvidar()
    cambiarVar(num)

def cambiar2(titulo):
    global labelBgOpciones
    verificarTitulo()
    cambiarTitulo(titulo)
    labelBgOpciones.place_forget()


def cambiarVar(num):
    global abierta
    abierta=num #variable global que ayudara a ver que widget se esta  mostrando


def olvidar():
    global abierta,siguiente,anterior,l,labelBgOpciones
    
    if(abierta==1 or abierta==2 or abierta==5):
        l.place_forget()
        l.destroy()
    elif(mefVar==9):
        labelBgOpciones.place_forget()
        siguiente.place_forget()
        anterior.place_forget()
    else:
        labelBgOpciones.place_forget()

    
    
    
#############################Funciones para el titulo de cada opcion#########################################
def cambiarTitulo(title):
    global titulo
    helv = tkFont.Font(family='Ink Free', size=20, weight='bold')
    titulo = tk.Label(text=title,image=tituloI,fg='white',compound='center',font=helv)
    titulo.place(x=600,y=10,width=300,height=40)

def verificarTitulo():
    global titulo

    if(abierta!=0):
        titulo.place_forget()
#############################Funciones para el titulo de cada opcion##########################################

#############################Funciones para modelo###########################################################
def dominio():
    global l,mefVar
    mefVar=9
    cambiar('Dominio',1)
    l = AnimatedGIF(ventana, resource_path("images/dominio.gif"))
    l.place(x=190,y=60,width=1089,height=540)
   
#############################Funciones para modelo###########################################################



#############################Funciones para malla###########################################################
def malla():
    global l,mefVar
    mefVar=9
    cambiar('Malla',2)
    l = AnimatedGIF(ventana, resource_path("images/malla.gif"))
    l.place(x=260,y=60)

#############################Funciones para malla###########################################################




#############################Funciones para tabla conectividades##############################################
def tablaConectividades():
    global labelBgOpciones,mefVar
    mefVar=9
    cambiar('Tabla de conectividades',3)
    labelBgOpciones= tk.Label(ventana,borderwidth=4,relief="solid",image=tablaC,bg="black")
    labelBgOpciones.place(x=190,y=60,width=1089,height=540)
#############################Funciones para tabla conectividades############################################## 

def modelo():
    global labelBgOpciones,mefVar
    mefVar=9
    cambiar('Modelo',4)
    labelBgOpciones= tk.Label(ventana,borderwidth=4,relief="solid",image=modeloI,bg="black")
    labelBgOpciones.place(x=190,y=60,width=1089,height=540)


def condiciones():
    global labelBgOpciones,mefVar
    mefVar=9
    cambiar('Condiciones',5)
    labelBgOpciones= tk.Label(ventana,borderwidth=4,relief="solid",image=condicionesI,bg="black")
    labelBgOpciones.place(x=190,y=60,width=1089,height=540)



def imagenMef():
    global mefVar

    if(mefVar==1):
        cambiar2('Paso 1')
        labelBgOpciones= tk.Label(ventana,borderwidth=4,relief="solid",image=mef1,bg="black")
        labelBgOpciones.place(x=190,y=60,width=1089,height=540)
    if(mefVar==2):
        cambiar2('Paso 2')
        labelBgOpciones= tk.Label(ventana,borderwidth=4,relief="solid",image=mef2,bg="black")
        labelBgOpciones.place(x=190,y=60,width=1089,height=540)
    if(mefVar==3):
        cambiar2('Paso 3')
        labelBgOpciones= tk.Label(ventana,borderwidth=4,relief="solid",image=mef3,bg="black")
        labelBgOpciones.place(x=190,y=60,width=1089,height=540)
    if(mefVar==4):
        cambiar2('Paso 4')
        labelBgOpciones= tk.Label(ventana,borderwidth=4,relief="solid",image=mef4,bg="black")
        labelBgOpciones.place(x=190,y=60,width=1089,height=540)
    if(mefVar==5):
        cambiar2('Paso 5')
        labelBgOpciones= tk.Label(ventana,borderwidth=4,relief="solid",image=mef5,bg="black")
        labelBgOpciones.place(x=190,y=60,width=1089,height=540)
    if(mefVar==6):
        cambiar2('Paso 6')
        labelBgOpciones= tk.Label(ventana,borderwidth=4,relief="solid",image=mef6,bg="black")
        labelBgOpciones.place(x=190,y=60,width=1089,height=540)
    if(mefVar==7):
        cambiar2('Material')
        labelBgOpciones= tk.Label(ventana,borderwidth=4,relief="solid",image=mef7,bg="black")
        labelBgOpciones.place(x=190,y=60,width=1089,height=540)
    if(mefVar==8):
        cambiar2('Componente C')
        labelBgOpciones= tk.Label(ventana,borderwidth=4,relief="solid",image=mef8,bg="black")
        labelBgOpciones.place(x=190,y=60,width=1089,height=540) 
    if(mefVar==9):
        cambiar2('Componente M')
        labelBgOpciones= tk.Label(ventana,borderwidth=4,relief="solid",image=mef9,bg="black")
        labelBgOpciones.place(x=190,y=60,width=1089,height=540)    
    if(mefVar==10):
        cambiar2('Componente L')
        labelBgOpciones= tk.Label(ventana,borderwidth=4,relief="solid",image=mef10,bg="black")
        labelBgOpciones.place(x=190,y=60,width=1089,height=540)
    if(mefVar==11):
        cambiar2('Componente K')
        labelBgOpciones= tk.Label(ventana,borderwidth=4,relief="solid",image=mef11,bg="black")
        labelBgOpciones.place(x=190,y=60,width=1089,height=540)
    if(mefVar==12):
        cambiar2('Componentes G y H')
        labelBgOpciones= tk.Label(ventana,borderwidth=4,relief="solid",image=mef12,bg="black")
        labelBgOpciones.place(x=190,y=60,width=1089,height=540)  


def nextMef():
    global mefVar
    mefVar=mefVar+1
    if(mefVar>12):
        mefVar=1
    imagenMef()
    

def antMef():
    global mefVar
    mefVar=mefVar-1
    if(mefVar<1):
        mefVar=12
    imagenMef()
    
    
    print("Sali: "+str(mefVar))




def mef():
    global labelBgOpciones,mefVar
    mefVar=1
    siguiente.place(x=1215,y=610,width=60,height=40)
    anterior.place(x=1115,y=610,width=60,height=40)
 
    imagenMef()


def ensamblaje():
    global l,mefVar
    mefVar=9
    cambiar('Ensamblaje',5)
    l = AnimatedGIF(ventana, resource_path("images/ensamblaje.gif"))
    l.place(x=190,y=60)

def crearWidgetsPrincipales():
    global mefVar,siguiente,anterior
    helv1 = tkFont.Font(family='Ink Free', size=13, weight='bold')
    helv2 = tkFont.Font(family='Ink Free', size=12, weight='bold')
    fondo =tk.Label(ventana,image=fondoI)
    fondo.pack(fill="both") 

    label=tk.Label(ventana,borderwidth=4,relief="solid",bg="#1d1d1d", image=inicioI)
    label.place(x=190,y=60,width=1089,height=540)
    ##########################Botones##############################
    
    dominioB=tk.Button(ventana,command=dominio,image=botonI,text='Dominio',bg='black',compound="center",fg='black',font=helv1)
    dominioB.place(x=40,y=17,width=120,height=60)

    mallaB=tk.Button(ventana,command=malla,text='Malla',image=botonI,bg='black',compound="center",fg='black',font=helv1)
    mallaB.place(x=40,y=94,width=120,height=60)

    tablacB=tk.Button(ventana,command=tablaConectividades,text='Tabla de \nConectividades',image=botonI,bg='black',compound="center",fg='black',font=helv2)
    tablacB.place(x=40,y=171,width=120,height=60)

    modeloB=tk.Button(ventana,command=modelo,text='Modelo',image=botonI,bg='black',compound="center",fg='black',font=helv1)
    modeloB.place(x=40,y=248,width=120,height=60)

    mefB=tk.Button(ventana,command=mef,text='MEF',image=botonI,bg='black',compound="center",fg='black',font=helv1)
    mefB.place(x=40,y=325,width=120,height=60)

    ensamblajeB=tk.Button(ventana,command=ensamblaje,text='Ensamblaje',image=botonI,bg='black',compound="center",fg='black',font=helv1)
    ensamblajeB.place(x=40,y=402,width=120,height=60)

    condicionesB=tk.Button(ventana,command=condiciones,text='Condiciones \nde Contorno',image=botonI,bg='black',compound="center",fg='black',font=helv1)
    condicionesB.place(x=40,y=479,width=120,height=60)

    salirB=tk.Button(ventana,command=lambda:ventana.destroy(),text='Salir',image=botonI,bg='black',compound="center",fg='black',font=helv1)
    salirB.place(x=40,y=556,width=120,height=60)
    
    siguiente=tk.Button(ventana,command=lambda:nextMef(),image=siguienteI,bg='black',border=0)
    anterior=tk.Button(ventana,command=lambda:antMef(),image=anteriorI,bg='black',border=0)

    

    

abierta=0

ventana= tk.Tk()
ventana.geometry("1285x660")


labelBgOpciones=tk.Label(ventana,bg="black")
labelBgOpciones.place(x=190,y=60,width=1090,height=540)
#######################Load Images###########################
img=Image.open(resource_path("images/conectividades.png"))
tablaC= ImageTk.PhotoImage(img)  

img=Image.open(resource_path("images/modelo.png"))
modeloI= ImageTk.PhotoImage(img)  

#####Mef
img=Image.open(resource_path("images/paso1.png"))
img= img.resize((1090,540),Image.ANTIALIAS)
mef1= ImageTk.PhotoImage(img) 

img=Image.open(resource_path("images/paso2.png"))
img= img.resize((1090,540),Image.ANTIALIAS)
mef2= ImageTk.PhotoImage(img) 

img=Image.open(resource_path("images/paso3.png"))
img= img.resize((1090,540),Image.ANTIALIAS)
mef3= ImageTk.PhotoImage(img) 

img=Image.open(resource_path("images/paso4.png"))
img= img.resize((1090,540),Image.ANTIALIAS)
mef4= ImageTk.PhotoImage(img) 

img=Image.open(resource_path("images/paso5.png"))
img= img.resize((1090,540),Image.ANTIALIAS)
mef5= ImageTk.PhotoImage(img) 

img=Image.open(resource_path("images/paso6.png"))
img= img.resize((1090,540),Image.ANTIALIAS)
mef6= ImageTk.PhotoImage(img) 

img=Image.open(resource_path("images/material.png"))
img= img.resize((1090,540),Image.ANTIALIAS)
mef7= ImageTk.PhotoImage(img) 

img=Image.open(resource_path("images/componenteC.png"))
img= img.resize((1090,540),Image.ANTIALIAS)
mef8= ImageTk.PhotoImage(img) 

img=Image.open(resource_path("images/componenteM.png"))
img= img.resize((1090,540),Image.ANTIALIAS)
mef9= ImageTk.PhotoImage(img) 

img=Image.open(resource_path("images/componenteL.png"))
img= img.resize((1090,540),Image.ANTIALIAS)
mef10= ImageTk.PhotoImage(img) 

img=Image.open(resource_path("images/componenteK.png"))
img= img.resize((1090,540),Image.ANTIALIAS)
mef11= ImageTk.PhotoImage(img) 

img=Image.open(resource_path("images/componenteGH.png"))
img= img.resize((1090,540),Image.ANTIALIAS)
mef12= ImageTk.PhotoImage(img) 

####Fin Mef

img=Image.open(resource_path("images/condiciones.png"))
img= img.resize((1090,540),Image.ANTIALIAS)
condicionesI= ImageTk.PhotoImage(img)  



img=Image.open(resource_path("images/fondo.png"))
fondoI=ImageTk.PhotoImage(img)  

img=Image.open(resource_path("images/botones.png"))
botonI=ImageTk.PhotoImage(img)  

img=Image.open(resource_path("images/titulos.png"))
tituloI=ImageTk.PhotoImage(img)  

img=Image.open(resource_path("images/siguiente.png"))
siguienteI=ImageTk.PhotoImage(img)  

img=Image.open(resource_path("images/anterior.png"))
anteriorI=ImageTk.PhotoImage(img)  

img=Image.open(resource_path("images/welcome.png"))
img= img.resize((430,540),Image.ANTIALIAS)
inicioI=ImageTk.PhotoImage(img)  

crearWidgetsPrincipales()

ventana.resizable(0,0)
ventana.mainloop()

#pyinstaller -w -F --add-Data 'images/*.png;images' --add-Data 'images/*.gif;images' 00004817.py
