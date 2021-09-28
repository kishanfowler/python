print("vind je chocola lekker?")
choice = input()
if choice == 'ja':
    print("Welke chocola vind je het lekkerst?")
    type = input()
    if type == "puur":
        print('Dat is mijn favoriet!')
    elif type == "wit":
        print('Die is lekker')
    elif type == "melk":
        print("Die is ook lekker")
elif choice == 'nee':
    print("jij bent raar")
else:
    print(choice, " wasn't a valid choice")