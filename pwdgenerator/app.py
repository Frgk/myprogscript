
#I coded an "application" with Tkinter to adapt my pwd generator script

from tkinter import *
from tkinter import ttk

from pwdgenerator import *





def generate_pwd():

    if listeCombo.get() == "Easy" :
        pwd = easypwd(5)
        pwd_display['text'] = pwd
        print(pwd)

    if listeCombo.get() == "Medium":
        pwd = mediumpwd(5)
        pwd_display['text'] = pwd
        print(pwd)

    if listeCombo.get() == "Hard":
        pwd = hardpwd(5)
        pwd_display['text'] = pwd
        print(pwd)






###########################################
background_color = 'black'
window = Tk()
###########################################

#Personnaliser cette fenêtre
window.title("My Application")
window.geometry('720x480')
window.minsize(480, 360)
window.iconbitmap("library.ico")
window.config(background=background_color)


###########################################
middle_frame = Frame(window, bg=background_color)
labelChoix = Label(middle_frame,text='Choisissez la difficulté', font = ("Courrier, 15"), bg=background_color, fg='white')
labelChoix.pack()
listeProduits = ["Easy", "Medium", "Hard"]  #Créer la liste Python contenant les éléments de la liste Combobox
listeCombo = ttk.Combobox(middle_frame, values=listeProduits)   #Création de la Combobox via la méthode ttk.Combobox()
listeCombo.current(0)   #Choisir l'élément qui s'affiche par défaut
listeCombo.pack()
pwd_display = Label(middle_frame,text='...', font = ("Courrier, 25"), bg=background_color, fg='white')
pwd_display.pack()
middle_frame.pack(side=TOP)
###########################################


###########################################
title_frame = Frame(window, bg=background_color)
label_title = Label(title_frame, text='Password Generator', font = ("Courrier, 40"), bg=background_color, fg='white')
label_title.pack()
label_subtitle = Label(title_frame, text='Press the button', font = ("Courrier, 25"), bg=background_color, fg='white')
label_subtitle.pack()
button = Button(title_frame, text='Generate', font = ("Courrier, 25"), bg='white', fg=background_color,command=generate_pwd)
button.pack()
title_frame.pack(side=BOTTOM)
###########################################




#Afficher
window.mainloop()
