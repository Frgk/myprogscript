import random

liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'y', 'Z',
         '1','2','3','4','5','6','7','8','9','0',
         '&','~','(','-','_',')','?','/',':','!','*']


#for i in range(0,25):  #simple alphabet

#for i in range(25,52):   #Grand alphabet

#for i in range(52, 62): #Numbers

#for i in range(62,73):  #signals

def easypwd():

    j =0
    pwd = str()
    for j in range(15):
        i = random.randint(0, 26)

        c = liste[i]
        pwd += c
    return pwd

def mediumpwd():

    j =0
    pwd = str()
    for j in range(15):
        i = random.randint(0, 62)

        c = liste[i]
        pwd += c
    return pwd

def hardpwd():

    j =0
    pwd = str()
    for j in range(15):
        i = random.randint(0, 72)

        c = liste[i]
        pwd += c
    return pwd



def main():
    print("Choose the complexity of the password by typing : easy | medium | hard \n")
    diff = input("What's the difficulty of the pwd : ")

    pwd = str()

    if diff == 'easy' :
        pwd = easypwd()
    if diff == 'medium':
        pwd = mediumpwd()
    if diff == "hard":
        pwd = hardpwd()

    else :
        print("Don't recognise this word !")


    print("The generated password is : ", pwd)
main()



