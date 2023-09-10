print("#######                                                                          #####                                                         ")
print("   #    ###### #    # #####  ###### #####    ##   ##### #    # #####  ######    #     #  ####  #    # #    # ###### #####  ##### ###### #####  ")
print("   #    #      ##  ## #    # #      #    #  #  #    #   #    # #    # #         #       #    # ##   # #    # #      #    #   #   #      #    # ")
print("   #    #####  # ## # #    # #####  #    # #    #   #   #    # #    # #####     #       #    # # #  # #    # #####  #    #   #   #####  #    # ")
print("   #    #      #    # #####  #      #####  ######   #   #    # #####  #         #       #    # #  # # #    # #      #####    #   #      #####  ")
print("   #    #      #    # #      #      #   #  #    #   #   #    # #   #  #         #     # #    # #   ##  #  #  #      #   #    #   #      #   #  ")
print("   #    ###### #    # #      ###### #    # #    #   #    ####  #    # ######     #####   ####  #    #   ##   ###### #    #   #   ###### #    # ")
                                                                                                                                               








                #######                #####                                    
#####  #   #       #     ####  #####  #     # ######  ####  #####  ###### ##### 
#    #  # #        #    #    # #    # #       #      #    # #    # #        #   
#####    #         #    #    # #    #  #####  #####  #      #    # #####    #   
#    #   #         #    #    # #####        # #      #      #####  #        #   
#    #   #         #    #    # #      #     # #      #    # #   #  #        #   
#####    #         #     ####  #       #####  ######  ####  #    # ######   #   
                                                                                

#Welcome to Temp Converter.
#This app uses functions to convert between temperature units.  
#An interesting way to code these functions is to call one to define another


print("\n\n\n\n\n Welcome to  Temperature Converter by TopSecret")
print("This tool is used to convert a temperature from one format to another (Farenheit, Celcius, and Kelvin)")
print("\nWhat unit are you converting from? (type the corresponding number and hit enter) \n1.)Farenheit\n2.)Celcius\n3.)Kelvin")


#conversion functions

def fToC(farenheit):
    return (farenheit - 32)*(5/9)
def fToK(farenheit):
    #return ((farenheit - 32)*(5/9) + 273.15)
    return (fToC(farenheit)) + 273.15

def cToF(celcius):
    return ((celcius * (9/5)) + 32)
def cToK(celcius):
    return (celcius + 273.15)
    
def kToF(kelvin):
    return ((kelvin - 273.15)*(9/5)+ 32)
def kToC(kelvin): 
    return (kelvin - 273.15)


origUnit = input()
if origUnit == "1":
    print("\n\nYour starting unit is Farenheit.\nWhat unit are you converting to?\n1.)Farenheit\n2.)Celcius\n3.)Kelvin")
    newUnit = input()
elif origUnit == "2":
    print("\n\nYour starting unit is Celcius.\nWhat unit are you converting to?\n1.)Farenheit\n2.)Celcius\n3.)Kelvin")
    newUnit = input()   
elif origUnit == "3":
    print("\n\nYour starting unit is Kelvin.\nWhat unit are you converting to?\n1.)Farenheit\n2.)Celcius\n3.)Kelvin")
    newUnit = input() 
else:
    print("invalid entry")

if newUnit == "1":
    print("\n\nWe will convert your temperature to Farenheit.  What is the numerical temperature to convert?\n")
    temperature = input()
elif newUnit == "2":
    print("\n\nWe will convert your temperature to Celcius.  What is the numerical temperature to convert?\n")
    temperature = input()
elif newUnit == "3":
    print("\n\nWe will convert your temperature to Kelvin.  What is the numerical temperature to convert?\n")
    temperature = int(input())

temperature = int(temperature)


   
if origUnit == "1":
    if newUnit == "2":
        answer = fToC(temperature)
    if newUnit == "3":
        answer = fToK(temperature)

if origUnit == "2":
    if newUnit == "1":
        answer = cToF(temperature)
    if newUnit == "3":
        answer = cToK(temperature)

if origUnit == "3":
    if newUnit == "1":
        answer = kToF(temperature)
    if newUnit == "2":
        answer = kToC(temperature)

print(round(answer, 1))
print("Thank you for using Temperature Converter by TopSecret")

#def fToC(celcius):
    #return (celcius - 32)*(5/9)



