def main():
    mass = float(input("Enter a weight of earth? "))
    planet = str(input("Enter a planet: "))
    if(planet.lower() == "mars"):
        gravity_constant = 0.378
    elif(planet.lower() == "mercury"):
        gravity_constant = 0.376
    elif(planet.lower() == "venus"):
        gravity_constant = 0.889
    elif(planet.lower() == "jupiter"):
        gravity_constant = 2.36
    elif(planet.lower() == "saturn"):
        gravity_constant = 1.081
    elif(planet.lower() == "uranus"):
        gravity_constant = 0.815
    elif(planet.lower() == "neptune"):
        gravity_constant = 1.081
    else:
        gravity_constant = 1.081

    planet_weight = mass * gravity_constant
    rounded_planet_weight = round(planet_weight, 2)


    print("The equivalent weight on " + planet + ":  " + str(rounded_planet_weight))
if __name__ == '__main__':
    main()