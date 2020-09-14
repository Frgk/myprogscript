

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


text = input("Enter the text to code : ")
key = input("Enter the key : ")



def letter_reco(letter, liste):
    i = 0
    while letter != liste[i]:
        i += 1
    return i

def main():
    new_message = str()
    j = 0
    for i in range(len(text)):

        coord = letter_reco(text[i], alphabet) - letter_reco(key[j], alphabet)

        if coord <= 0:
            coord +=26


        #print(alphabet[letter_reco(text[i],alphabet)] + " - ",letter_reco(text[i],alphabet)+1)
        char = alphabet[coord]
        new_message += char

        if j == len(key)-1:
            j = 0
        else :
            j += 1
    print("Coded message : " +new_message)
main()
