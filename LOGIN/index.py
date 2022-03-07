# importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# Criar Nossa Janela
janela = Tk() 
janela.title('Hunter System - Access Panel')
janela.geometry ('700x400')
janela.configure(background='white')
janela.resizable(width=False , height=False)
janela.attributes("-alpha", 0.7)

#===== Carrega Imagenes =====
logo = PhotoImage(file='LOGIN/icons/índice.png')

#==== Widgets=============================
leftFrame = Frame(janela,width=300 , height=400 , bg='DarkGray',relief='raise')
leftFrame.pack(side=LEFT)

rightFrame = Frame(janela,width=395 , height=400 , bg='MidnightBlue',relief='raise')
rightFrame.pack(side=RIGHT)

LogoLabel = Label(leftFrame, image= logo , bg='DarkGray')
LogoLabel.place(x =41 ,y=90)

#===== Usuario===========
UserLabel = Label(rightFrame, text='Nombre de Usuario: ' , font=('Century Gothic', 15), bg ='MidnightBlue',fg='white')
UserLabel.place(x = 5 , y = 90)

UserEntry = ttk.Entry(rightFrame, width=21)
UserEntry.place (x=210 , y = 91)

#==========Senha ============
Senhalabel = Label(rightFrame , text ='Senha de Usuario: ' , font=('Century Gothic' , 15) ,bg = 'MidnightBlue',fg ='white' )
Senhalabel.place (x = 5 , y = 145)

SenhaEntry = ttk.Entry(rightFrame, width=21)
SenhaEntry.place (x =210 , y= 145 )

# ==========Botoes ===========
LoginButton = ttk.Button(rightFrame , text='Login',width= 35)
LoginButton.place(x = 60 , y = 300)

#====== Register ==============
RegisterButton = ttk.Button(rightFrame , text='Registro',width=30)
RegisterButton.place (x = 80 , y = 335)

janela.mainloop()

