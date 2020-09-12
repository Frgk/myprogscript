

import random
from termcolor import colored


def temp_planet():
    return random.randint(-300, 300)


def planet_type(temperature):
    if temperature >= -300 and temperature < -100:
        return "Icy"
    elif temperature >= -100 and temperature < -50:
        return "Frosted"
    elif temperature >= -50 and temperature < 0:
        return "Cold"
    elif temperature >= 0 and temperature < 40:
        return "Temperate"
    elif temperature >= 40 and temperature < 100:
        return "Burned"
    elif temperature >= 100 and temperature < 300:
        return "Calcined"

def random_name():
    pre = ["Me","Mo","Ma","Mu","Re","Ra","Ro","Ru","Yo","Pa","Pu","Pr","Za","We","Gr","Gu","Gy","Ko","Ke","Be",]
    mid = ["is","eos","eor","eo","br","rr","r","mm","m","nn","n","ty","ci","ta","la","pp","p"]
    end = ["sir","ber","ler","per","era","ero","ro","ver","vo","yst","st","sto"]



    return random.choice(pre) + random.choice(mid) + random.choice(end)

def planet_size():

    return random.randint(1900,70000)      #Based on the size of Kepler 37b(3900km) and Jupiter(139822km)




def create_planet(name):
    planet_name = str()
    if name == '':
        planet_name = random_name()
    else:
        planet_name = name

    print("Planet Name : " + planet_name)


    temp = temp_planet()

    print("Temperature on surface : " + str(temp) +" °C")
    print("This planet is " + planet_type(temp))


    print("Planet Diameter : " + str(planet_size()) + " km")








nom = input("Enter the name of the planet ( Leave it blank for a random name ) : ")

create_planet(nom)
