def drinkAge():

    userAge = int(input("Please enter your age:"))

    if userAge >= 21:
        print ("You are", userAge, " You are able to drink alcohol")
    else:
        print ("Your are", userAge, " You are not allowed to drink alchohol")
        print (21-userAge, "more year left")



drinkAge()