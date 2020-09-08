#NEED TO IMPROVE THE PROGRAM

text = input("Enter the text to decrypt : ")    #Enter the text to code

alphabet = ['a', 'b', 'c', 'd', 'f', 'e', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']




def main():

    for key in range(1,25):  #Try to decode the message with all the possible key from 1 to 25

        new_message = str()

        for i in range(len(text)):  # execute a "for" loop on each letter of the message



            if text[i] == ' ':  #make the exception of the space character
                new_letter = ' '
            else :
                j = 0
                while mess[i] != alphabet[j]:
                    j += 1
                j = j - key

                if j >= 26:
                    j -= 26
                elif j < 0:
                    j += 26

                new_letter = alphabet[j]
            new_message += new_letter

        print("Try with a key value of " + str(key) + " : " + new_message)   #Print a string with the value of the key and the message decoded with this key


main()
