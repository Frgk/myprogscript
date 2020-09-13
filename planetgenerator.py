

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

def planet_name(name):

    if name == '':
        pre = ["Me","Mo","Ma","Mu","Re","Ra","Ro","Ru","Yo","Pa","Pu","Pr","Za","We","Gr","Gu","Gy","Ko","Ke","Be","Ba","Br","Bo"]
        mid = ["is","eos","eor","eo","br","rr","r","mm","m","nn","n","ety","ci","ta","la","pp","p"]
        end = ["sir","ber","ler","per","era","ero","ro","ver","vo","yst","st","sto"]
        return random.choice(pre) + random.choice(mid) + random.choice(end)

    else :
        return name

def planet_size():

    return random.randint(1900,70000)      #Based on the size of Kepler 37b(3900km) and Jupiter(139822km)

def number_moons():
    return random.randint(0, 82)        #Based on the 82 Saturn's moons

def planet_number():
    chance = random.randint(0, 100)

    if chance >=70:
        teles = random.randint(1,22)        #Based on the 22 stars discovered by Kepler
        num = ['b','c','d','e','f','g']     #Based on from Kepler-11b to Kepler-11g
        return "-"+str(teles)+" "+random.choice(num)
    else:
        return ''

def planet_age():
    return random.randint(10000,50000000)



def story_planet(name,number,temperature,type,size,moon,age):

    pre = [
           "This planet called "+name,
           "Also called as "+name+", this planet",
           "This planet discovered by the telescope "+name+",",
           "We know that "+name,
           "Situated near our system SOL,"+name,
           "Aged of "+str(age)+" years,"+ name
           ]

    pre2 = [
        "is totally "+type,
        "is entirely "+type,
        "has an "+type+" environment",
        "is in an "+type+" era"
    ]

    pre3=["and has a temperature surrounding " + str(temperature) + " °C",
          "with a temperature of " + str(temperature) + " °C",
          "due to temperatures approaching " + str(temperature) + " °C",
    ]

    if temperature >= -300 and temperature < 0:
        mid = [name + " is a telluric planet, covered with ice",
               "The planet " + name + "is mostly composed of ice",
               name + " can be considered like a liquid planet, because of the presence of liquid nitrogen on surface",
               name + " is like Earth, it's a telluric planet, but with ice on surface"
        ]

    elif temperature >= 0 and temperature < 40:
        mid=[name + " has a temperature at a temperature that would allow humans to live there",
           "Thanks to his proximity with his sun, "+name+" is a telluric planet with a correct temperature",
           name + " is an uncommon planet, with a good ambient temperature but it's a gas planet",
           "Due to proximity with his star, " + name + " is a liquid planet heat to a boil"
        ]
    elif temperature >= 40 and temperature <= 300:
        mid=[name + " is an old telluric planet that has been heat with the core heat. Now it's a magmatic planet reaching unthinkable temperatures",
             name + " can be considered like a liquid planet, with the presence of lava on surface"
        ]

    mid2 = [", with " + str(moon) + "moons orbiting around.",
            ", counting at least " + str(moon) +" moons around.",
            ". Moreover, among these " + str(moon) + " moons, one looks like the planet itself, and has an elliptical orbit approaching the planet each year.",
            ". "+ name + "  has " + str(moon) + " moons having been destroyed by meteorites over the past centuries. These moons are now, fields of lunar debris orbiting around " + name,
    ]






    return random.choice(pre) +" "+random.choice(pre2) + " "+random.choice(pre3)+".\n"+random.choice(mid) + random.choice(mid2)





def create_planet(name):

    planetname = planet_name(name)
    planetnumber = planet_number()
    print("Planet Name : " + planetname+planetnumber)


    temperature = temp_planet()
    print("Temperature on surface : " + str(temperature) +" °C")
    print("Type of the planet :  " + planet_type(temperature))


    planetsize = planet_size()
    print("Planet Diameter : " + str(planetsize) + " km")

    numbermoon = number_moons()
    print("Number of moons : " + str(numbermoon))

    planetage = planet_age()



    planetstory = story_planet(planetname,planetnumber,temperature,planet_type(temperature),planetsize,numbermoon,planetage)
    print("\n\n"+planetstory)








nom = str(input("Enter the name of the planet ( Leave it blank for a random name ) : "))

create_planet(nom)
