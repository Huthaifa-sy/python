import os

slett = input('legg inn bilde id som du vil slette: ')

# Slette fra bilder.txt
with open('bilder.txt', 'r', encoding='utf-8') as f, \
     open('nybilder.txt', 'w', encoding='utf-8') as ny:

    bildeid = f.readline().strip()
    while bildeid != '':
        beskriv = f.readline().strip()
        dato = f.readline().strip()
        fotograf = f.readline().strip()

        if bildeid != slett:
            ny.write(bildeid + '\n')
            ny.write(beskriv + '\n')
            ny.write(dato + '\n')
            ny.write(fotograf + '\n')

        bildeid = f.readline().strip()

# Slette fra komentarer.txt
with open('komentarer.txt', 'r', encoding='utf-8') as f, \
     open('nykom.txt', 'w', encoding='utf-8') as ny:

    bildeid = f.readline().strip()
    while bildeid != '':
        brukerid = f.readline().strip()
        koment = f.readline().strip()

        if bildeid != slett:
            ny.write(bildeid + '\n')
            ny.write(brukerid + '\n')
            ny.write(koment + '\n')

        bildeid = f.readline().strip()

# Slette fra likes.txt
with open('likes.txt', 'r', encoding='utf-8') as f, \
     open('nylik.txt', 'w', encoding='utf-8') as ny:

    bildeid = f.readline().strip()
    while bildeid != '':
        brukerid = f.readline().strip()

        if bildeid != slett:
            ny.write(bildeid + '\n')
            ny.write(brukerid + '\n')

        bildeid = f.readline().strip()

# Bytte filer
os.remove('bilder.txt')
os.remove('komentarer.txt')
os.remove('likes.txt')

os.rename('nybilder.txt', 'bilder.txt')
os.rename('nykom.txt', 'komentarer.txt')
os.rename('nylik.txt', 'likes.txt')

print("bilde og alle kommentarer og likes er slettet")
