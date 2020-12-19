# program that breaks down customized health data

import os

def main():

    name = ''
    outfile = ''
    nameCondition = False
    height = 0
    weight = 0
    age = 0
    gender = 0
    genderCondition = False
    activityLevel = 0
    activityLevelCondition = False
    goalWeight = 0
    goalSpeed = 0
    goalSpeedCondition = False
    macroNutrients = 0
    macroNutrientsCondition = False
    carbohydrate = 0
    protein = 0
    fat = 0

    print("Welcome to MyHealth!\nPlease fill out the requested information to get started.\n")

    while (nameCondition == False):
        try:
            name = input("(1) Your name: ")
            outfile = open(name + "'s Personal Profile", 'w')
            outfile.write(
                "please enter all information")
            outfile.close()
        except:
            print("Try again.")
            print()
            nameCondition = False
        else:
            print('Nice to meet you', name, '\b!')
            nameCondition = True
    print()

    while not (height > 0):
        try:
            height = int(input("(2) Height in centimeters: "))
        except:
            print("Try again.")
            print()
        else:
            if not (height > 0):
                print("Try again.")
                print()
    print()

    while not (weight > 0):
        try:
            weight = int(input("(3) Weight in pounds: "))
        except:
            print("Try again.")
            print()
        else:
            if not (weight > 0):
                print("Try again.")
                print()
    print()

    while not (age > 0):
        try:
            age = int(input("(4) Age: "))
        except:
            print("Try again.")
            print()
        else:
            if not (age > 0):
                print("Try again.")
                print()
    print()

    print("0 for Male")
    print("1 for Female")
    print()

    while (genderCondition == False):
        try:
            gender = int(input("(5) Gender: "))
        except:
            print("Try again.")
            print()
            genderCondition = False
        else:
            if (gender == 0):
                genderCondition = True
            elif (gender == 1):
                genderCondition = True
            else:
                genderCondition = False
                print("Try again.")
                print()
    print()

    print("1 -- No exercise")
    print("2 -- Low exercise")
    print("3 -- Moderate exercise")
    print("4 -- Heavy exercise")
    print("5 -- Vigorous exercise")
    print()

    while (activityLevelCondition == False):
        try:
            activityLevel = int(input("(6) Activity Level (1-5): "))
        except:
            print("Try again.")
            print()
            activityLevelCondition = False
        else:
            if (activityLevel == 1) or (activityLevel == 2) or (activityLevel == 3) or (activityLevel == 4) or (
                    activityLevel == 5):
                activityLevelCondition = True
            else:
                activityLevelCondition = False
                print("Try again.")
                print()
    print()

    while not (goalWeight > 0):
        try:
            goalWeight = int(input("(7) Goal Weight in pounds: "))
        except:
            print("Try again.")
            print()
        else:
            if not (goalWeight > 0):
                print("Try again.")
                print()
    print()

    if (goalWeight < weight):

        print("1 -- I'd like to lose half a pound per week")
        print("2 -- I'd like to lose a pound per week")
        print()

        while (goalSpeedCondition == False):
            try:
                goalSpeed = int(input("Select goal (1 or 2): "))
            except:
                goalSpeedCondition = False
                print("Try again.")
                print()
            else:
                if (goalSpeed == 1) or (goalSpeed == 2):
                    goalSpeedCondition = True

    elif (goalWeight > weight):

        print("3 -- I'd like to gain half a pound per week")
        print("4 -- I'd like to gain a pound per week")
        print()

        while (goalSpeedCondition == False):
            try:
                goalSpeed = int(input("Select goal (3 or 4): "))
            except:
                goalSpeedCondition = False
                print("Try again.")
                print()
            else:
                if (goalSpeed == 3) or (goalSpeed == 4):
                    goalSpeedCondition = True

    else:
        print("Maintain weight")
        goalSpeed = 5
    print()

    print("1 -- I'd like the recommended macronutrient diet plan")
    print("2 -- I'd like to do a high carb / low fat diet")
    print("3 -- I'd like to do a low carb ketogenic diet")
    print("4 -- I'd like to create my own macronutrient profile")
    print()

    while (macroNutrientsCondition == False):
        try:
            macroNutrients = int(input("Select Diet (1-4): "))
        except:
            macroNutrientsCondition = False
            print("Try again.")
            print()
        else:
            if (macroNutrients == 1) or (macroNutrients == 2) or (macroNutrients == 3) or (macroNutrients == 4):
                macroNutrientsCondition = True
    print()

    if (macroNutrients == 1):
        carbohydrate = 60
        fat = 25
        protein = 15

    elif (macroNutrients == 2):
        carbohydrate = 80
        fat = 10
        protein = 10

    elif (macroNutrients == 3):
        carbohydrate = 10
        fat = 60
        protein = 30

    elif (macroNutrients == 4):
        while not (carbohydrate + protein + fat == 100):
            try:
                carbohydrate = int(input("Enter percent of diet that is carbohydrate: "))
                fat = int(input("Enter percent of diet that is fat: "))
                protein = int(input("Enter percent of diet that is protein: "))
            except:
                carbohydrate = 100
                fat = 100
                protein = 100
                print("Make sure they add up to 100%)")
                print()
            else:
                if not (carbohydrate + protein + fat == 100):
                    print("Try again.")
                    print()

    (BMR, TDEE) = TDEEcalculator(height, weight, gender, age, activityLevel)

    (BMI, NewBMI) = BMIcalculator(height, weight, goalWeight)

    calPerDay = calPerDaycalculculator(TDEE, goalSpeed)

    timeTaken = timeTakencalculator(goalWeight, goalSpeed, weight)

    (carbohydrateGrams, fatGrams, proteinGrams) = macroNutrientscalculator(macroNutrients, carbohydrate, fat, protein,
                                                                           calPerDay)

    print("Your customized health data has been generated.")

    outfile = open(name + "'s Data", 'w')

    outfile.write("MyHealth" + '\n')

    outfile.write(name + "'s Data" + '\n')
    outfile.write('\n')

    outfile.write("Age:                 " + str(age) + " years")
    outfile.write('\n')

    outfile.write("Height:              " + str(height) + " cm")
    outfile.write('\n')

    if (gender == 0):
        outfile.write("Gender:              Male")
    elif (gender == 1):
        outfile.write("Gender:              Female")
    outfile.write('\n')

    if (activityLevel == 1):
        outfile.write("Your Exercise level: Sedentary - 0 to 1 day of exercise per week")
    elif (activityLevel == 2):
        outfile.write("Your Exercise level: Lightly active - 1 to 3 days of exercise per week)")
    elif (activityLevel == 3):
        outfile.write("Your Exercise level: moderately active - 3 to 5 days of exercise per week)")
    elif (activityLevel == 4):
        outfile.write("Your Exercise level: Very active - 6 to 7 days of exercise per week)")
    elif (activityLevel == 5):
        outfile.write("Your Exercise level: Vigorously active - daily exercise, even multiple times")
    outfile.write('\n')

    outfile.write("Current Weight:      " + str(weight) + " lbs")
    outfile.write('\n')
    outfile.write("Goal Weight:         " + str(goalWeight) + " lbs" + '\n')

    if (goalSpeed == 1):
        outfile.write("Weight progression:  I'd like to lose half a pound per week")
    elif (goalSpeed == 2):
        outfile.write("Weight progression:  I'd like to lose a pound per week")
    elif (goalSpeed == 3):
        outfile.write("Weight progression:  I'd like to gain half a pound per week")
    elif (goalSpeed == 4):
        outfile.write("Weight progression:  I'd like to gain a pound per week")
    elif (goalSpeed == 5):
        outfile.write("Weight progression:  Maintain weight")
    outfile.write('\n')

    outfile.write('\n')

    outfile.write("Current BMI: " + str(BMI) + "                          |Underweight: BMI is less than 18.5.")
    outfile.write('\n')
    outfile.write("Goal BMI:    " + str(NewBMI) + "                          |Normal weight: BMI is 18.5 to 24.9.")
    outfile.write('\n')
    outfile.write('                                           |Overweight: BMI is 25 to 29.9.')
    outfile.write('\n')
    outfile.write('                                           |Obese: BMI is 30 or more.')
    outfile.write('\n')

    outfile.write('\n')

    outfile.write("Basal Metabolic Rate (BMR) is the number of calories burned at rest")
    outfile.write('\n')
    outfile.write("BMR:  " + str(BMR))
    outfile.write('\n')

    outfile.write('\n')

    outfile.write("Total Daily Energy Expenditure (TDEE) is the total numbers of calories burned daily")
    outfile.write('\n')
    outfile.write("TDEE: " + str(TDEE))
    outfile.write('\n')

    outfile.write('\n')
    outfile.write("Recommended number of calories per day to reach goal: " + str(calPerDay))
    outfile.write('\n')

    outfile.write("Approximate number of days until goal is reached:     " + str(timeTaken))
    outfile.write('\n')
    outfile.write('\n')

    if (macroNutrients == 1):
        outfile.write("Recommended Diet (60% carb, 25% fat, 15% protein)")
        outfile.write('\n')
        outfile.write('\n')
        outfile.write("Carbohydrate intake in grams per day: " + str(carbohydrateGrams))
        outfile.write('\n')
        outfile.write("Fat intake in grams per day:          " + str(fatGrams))
        outfile.write('\n')
        outfile.write("Protein intake in grams per day:      " + str(proteinGrams))
    elif (macroNutrients == 2):
        outfile.write("High Carb, Low Fat Diet (80% carb, 10% fat, 10% protein)")
        outfile.write('\n')
        outfile.write('\n')
        outfile.write("Carbohydrate intake in grams per day: " + str(carbohydrateGrams))
        outfile.write('\n')
        outfile.write("Fat intake in grams per day:          " + str(fatGrams))
        outfile.write('\n')
        outfile.write("Protein intake in grams per day:      " + str(proteinGrams))
    elif (macroNutrients == 3):
        outfile.write("Low Carb, Ketogenic Diet (10% carb, 60% fat, 30% protein)")
        outfile.write('\n')
        outfile.write('\n')
        outfile.write("Carbohydrate intake in grams per day: " + str(carbohydrateGrams))
        outfile.write('\n')
        outfile.write("Fat intake in grams per day:          " + str(fatGrams))
        outfile.write('\n')
        outfile.write("Protein intake in grams per day:      " + str(proteinGrams))
    elif (macroNutrients == 4):
        outfile.write("Customized Diet (" + str(carbohydrate) + "% carb, " + str(
            fat) + "% fat, " + str(protein) + "% protein)")
        outfile.write('\n')
        outfile.write('\n')
        outfile.write("Carbohydrate intake in grams per day: " + str(carbohydrateGrams))
        outfile.write('\n')
        outfile.write("Fat intake in grams per day:          " + str(fatGrams))
        outfile.write('\n')
        outfile.write("Protein intake in grams per day:      " + str(proteinGrams))

    outfile.close()

    os.startfile(name + "'s Data", 'w')

def BMIcalculator(height, weight, goalWeight):
    # Declare local variables
    BMI = 0
    NewBMI = 0

    # calculate BMI
    BMI = ((weight / 2.2) / (height / 100) ** 2)
    NewBMI = ((goalWeight / 2.2) / (height / 100) ** 2)

    # Round numbers
    BMI = round(BMI, 1)
    NewBMI = round(NewBMI, 1)

    # Return values
    return (BMI, NewBMI)

def TDEEcalculator(height, weight, gender, age, activityLevel):
    # Declare local variables
    TDEE = 0
    BMR = 0

    # Check gender
    if (gender == 0):
        BMR = (66 + (13.7 * (weight / 2.2)) + (5 * height) - (6.8 * age))
    elif (gender == 1):
        BMR = (655 + (9.6 * (weight / 2.2)) + (1.8 * height) - (4.7 * age))
    else:
        print("Try again.")
    # End if

    # check activity level
    if (activityLevel == 1):
        TDEE = (BMR * 1.2)
    elif (activityLevel == 2):
        TDEE = (BMR * 1.375)
    elif (activityLevel == 3):
        TDEE = (BMR * 1.55)
    elif (activityLevel == 4):
        TDEE = (BMR * 1.725)
    elif (activityLevel == 5):
        TDEE = (BMR * 1.9)
    else:
        print("Try again.")
    # End if

    # Round Numbers
    BMR = round(BMR)
    TDEE = round(TDEE)

    # Return values
    return (BMR, TDEE)

def calPerDaycalculculator(TDEE, goalSpeed):
    # Declare local variables
    calPerDay = 0

    # calculate cal per day

    if (goalSpeed == 1):
        calPerDay = (TDEE - 250)
    elif (goalSpeed == 2):
        calPerDay = (TDEE - 500)
    elif (goalSpeed == 3):
        calPerDay = (TDEE + 250)
    elif (goalSpeed == 4):
        calPerDay = (TDEE + 500)
    elif (goalSpeed == 5):
        calPerDay = TDEE
    else:
        print("Try again.")
    # End If

    # Round Numbers
    calPerDay = round(calPerDay)

    # Return values
    return calPerDay

def timeTakencalculator(goalWeight, goalSpeed, weight):
    # Declare local variables
    timeTaken = 0
    weightDifference = 0

    # find Weight difference
    if (weight < goalWeight):
        weightDifference = (goalWeight - weight)
    elif (weight > goalWeight):
        weightDifference = (weight - goalWeight)
    elif (weight == goalWeight):
        weightDifference = 0
    else:
        print("Try again.")
    # End if

    # calculate timeTaken
    if (goalSpeed == 1) or (goalSpeed == 3):
        timeTaken = ((weightDifference * 3500) / 250)
    elif (goalSpeed == 2) or (goalSpeed == 4):
        timeTaken = ((weightDifference * 3500) / 500)
    elif (weightDifference == 0):
        timeTaken = 0
    else:
        print("Try again.")
    # End if

    # Return values
    return timeTaken

def macroNutrientscalculator(macroNutrients, carbohydrate, fat, protein, calPerDay):
    # Declare local variables
    carbohydrateGrams = 0
    fatGrams = 0
    proteinGrams = 0

    # calculate macronutrient profile
    if (macroNutrients == 10):
        pass
    else:
        carbohydrateGrams = ((calPerDay * (carbohydrate / 100)) / 4)
        fatGrams = ((calPerDay * (fat / 100)) / 9)
        proteinGrams = ((calPerDay * (protein / 100)) / 4)
    # End if

    # Round Numbers
    carbohydrateGrams = round(carbohydrateGrams)
    fatGrams = round(fatGrams)
    proteinGrams = round(proteinGrams)

    # Return values
    return carbohydrateGrams, fatGrams, proteinGrams


main()

''' After all information is inputted, a file will be created, which can be opened in Notepad. '''
