print("""Welcome to Fung Game
A game about surviving in hazardous science lab. Enjoy!""")
health = 10
players_name = input("To start off, answer these quetions:\nHello, what is your name? ")
age = int(input("How old are you? "))
if age >= 18:
    print("You are ready to play " + players_name)
else:
    print("You are not old enough to play. You must be at least 18 years or older.")
print("""Today is a new day and you are ready to go into the lab
Like always you have to decide whether or not to wear proper PPE.""")
wear_ppe = input("Do you want to wear PPE? (Yes or No)")
if wear_ppe == "Yes":
    print("Great! You have common knowledge of lab safety.\n*you proceed to your workstation*")
    print("Now you instructed to whether clean your materials before using.")
    clean_materials = input("Do you want to wash your materials before using them? (Yes or No) ")
    print("Now you need to mix your agar with in the petri dish")
    if clean_materials == "Yes":
        print("Everything goes smoothly\n")

    else:
        print("Game over. You caused an explosion by mixing the agar with substances used in the petri dish prior")
elif wear_ppe == "No":
    print("Game over. You were kicked out of the lab.")
