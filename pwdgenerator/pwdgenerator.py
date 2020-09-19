import random

liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'y', 'Z',
         '1','2','3','4','5','6','7','8','9','0',
         '&','~','(','-','_',')','?','/',':','!','*']


#for i in range(0,25):  #simple alphabet

#for i in range(25,52):   #Grand alphabet

#for i in range(52, 62): #Numbers

#for i in range(62,72):  #signals

def easypwd(len):

    j =0
    pwd = str()
    for j in range(len):
        i = random.randint(0, 26)

        c = liste[i]
        pwd += c
    return pwd

def mediumpwd(len):

    j =0
    pwd = str()
    for j in range(len):
        i = random.randint(0, 62)

        c = liste[i]
        pwd += c
    return pwd

def hardpwd(len):


    pwd = str()
    for j in range(len):
        i = random.choice(liste)


        pwd += i
    return pwd







