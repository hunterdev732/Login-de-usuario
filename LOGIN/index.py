# importar as bibliotecas

from cgitb import text
from pydoc import plain
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font


# Criar Nossa Janela
janela = Tk() 
janela.title('Hunter System - Access Panel')
janela.geometry ('700x400')
janela.configure(background='white')
janela.resizable(width=False , height=False)


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
UserLabel = Label(rightFrame, text='Username:' , font=('Century Gothic', 18), bg ='MidnightBlue',fg='white')
UserLabel.place(x = 18 , y = 170)

UserEntry = ttk.Entry(rightFrame, width=22)
UserEntry.place (x=170 , y = 174)

#==========Senha ============
Senhalabel = Label(rightFrame , text ='Password: ' , font=('Century Gothic' , 18) ,bg = 'MidnightBlue',fg ='white' )
Senhalabel.place (x = 18 , y = 220)

SenhaEntry = ttk.Entry(rightFrame, width=22, show='*')
SenhaEntry.place (x =170 , y= 224 )

# ==========Botoes ===========
LoginButton = ttk.Button(rightFrame , text='Login',width= 35)
LoginButton.place(x = 60 , y = 300)

def register():
    #===== Removendo widgets de login
    LoginButton.place(x=5000)
    RegisterButton.place(x= 5000)

    #Inserindo widgets de Cadastro
    NomeLabel = Label(rightFrame , text='Name: ', font=('Century Gothic',18),bg ='MidnightBlue' , fg='white')
    NomeLabel.place(x = 18 , y = 10)

    NomeEntry = Entry(rightFrame, width=22)
    NomeEntry.place(x = 170 , y = 14)

    GmailLabel = Label(rightFrame , text ='Gmail: ', font=("Century Gothic ", 18),bg = 'MidnightBlue', fg='White')
    GmailLabel.place (x =18 ,y = 60  )

    GmailEntry = Entry(rightFrame,width=22)
    GmailEntry.place (x = 170 , y = 64)

    Register = ttk.Button(rightFrame ,text='Register', width=30)
    Register.place (x = 70 , y =320)

    def BacktoLogin():
        #=== Removendo widgets de cadastro====
        NomeLabel.place(x = 5000)
        NomeEntry.place(x = 5000)
        GmailEntry.place(x = 5000)
        GmailLabel.place (x = 5000)
        Register.place (x = 5000)
        Back.place (x = 5000)
        #==== Trazendo de volta os widgets de login
        LoginButton.place(x=60)
        RegisterButton.place(x= 80)

    Back = ttk.Button(rightFrame, text='Back', width=15 , command=BacktoLogin) 
    Back.place (x =127 , y = 355 )

#====== Register ==============
RegisterButton = ttk.Button(rightFrame , text='Registro',width=30 , command=register)
RegisterButton.place (x = 80 , y = 335)


janela.mainloop()

