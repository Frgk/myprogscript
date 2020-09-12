import random

liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'y', 'Z',
         '1','2','3','4','5','6','7','8','9','0',
         '&','~','(','-','_',')','?','/',':','!','*']          #The list of all the characters possible in the pwd


#for i in range(0,25):  #lower cases

#for i in range(25,52):   #Upper cases

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

def hardpwd(len):          #Function used to generate the hard pwd

    j =0
    pwd = str()
    for j in range(len):
        i = random.choice(liste)

        
        pwd += i
    return pwd



def main():
    print("Choose the complexity of the password by typing : easy | medium | hard \n")
    diff = input("What's the difficulty of the pwd : ")
    leng = int(input("Choose the length of the pwd : "))

    pwd = str()

    if diff == 'easy' :
        pwd = easypwd(leng)
    if diff == 'medium':
        pwd = mediumpwd(leng)
    if diff == "hard":
        pwd = hardpwd(leng)




    print("The generated password is : ", pwd)        #Print the pwd 
main()



