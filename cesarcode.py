
#NEED TO IMPROVE THE PROGRAM




mess = input("Enter the text to code : ")    #Enter the text to code
key = int(input("Entrez the key : ")) #Enter the key

alphabet = ['a', 'b', 'c', 'd', 'f', 'e', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def letter_reco(letter, liste, key):  #Defining a function used to code a letter
    key = key % 26
    i = 0
    while letter != liste[i]:
        i += 1

    j = i + key
    if j >= 26:
        j -= 26
    elif j < 0:
        j += 26

    return j


def main():
    new_message = str()

    for i in range(len(mess)):  # execute a "for" loop on each letter of the message
        if mess[i] == ' ':  #make the exception of the space character
            new_letter = ' '
        else :
            new_letter = alphabet[letter_reco(mess[i], alphabet, key)]
        new_message += new_letter

    print("Coded message : ",new_message)


main()
