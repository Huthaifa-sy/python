fortsette = "Ja"

while fortsette == "Ja":

    tall = int(input("Oppgi et partall: "))

    # Sjekk om tallet er partall
    while tall % 2 != 0:
        print("Dette er jo ikke et partall, forsøk igjen")
        tall = int(input("Oppgi et partall: "))

    print("Halveringene blir")

    # Halver tallet helt til det blir 1
    while tall > 1:
        tall = tall / 2
        print(format(tall, '.2f'))


    print("Halvering avsluttet")

    fortsette = input("Kjøre programmet en gang til (Ja/Nei)?")

print("Program avsluttet")
