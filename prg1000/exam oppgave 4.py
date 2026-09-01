import os

svar = 'ja'
while svar == 'ja':
    utlann = open('utlann.txt', 'r', encoding='utf-8')
    lanner = open('lanner.txt', 'r', encoding='utf-8')
    nyfil = open('nyfile.txt', 'w', encoding='utf-8')

    slett = input('Hva er låner-ID? ')
    finnes = False

    # Sjekk om låneren har utlån
    inr = utlann.readline().strip()
    while inr != '':
        utlannsnr = utlann.readline().strip()
        isbn = utlann.readline().strip()
        utlannsdato = utlann.readline().strip()
        innleveringdato = utlann.readline().strip()

        if inr == slett:
            print('Kan ikke slette fordi låneren har registrerte utlån.')
            finnes = True
        inr = utlann.readline().strip()

    utlann.close()
    if not finnes:
        funnt=False

    # Hvis låneren ikke har utlån, gå gjennom lanner.txt
    inr = lanner.readline().strip()
    while inr != '':
        fornavn = lanner.readline().strip()
        etternavn = lanner.readline().strip()
        mobilnr = lanner.readline().strip()

        if inr == slett:
            # Ikke skriv denne låneren til nyfil (slettet)
            print('Du slettet låneren.')
            funnt = True
        else:
            # Skriv låneren videre til nyfil
            nyfil.write(inr + '\n')
            nyfil.write(fornavn + '\n')
            nyfil.write(etternavn + '\n')
            nyfil.write(mobilnr + '\n')

        inr = lanner.readline().strip()

    lanner.close()
    nyfil.close()

    # Oppdater filene
    os.remove('lanner.txt')
    os.rename('nyfile.txt', 'lanner.txt')

    if not funnt and not finnes:
        print('Låneren finnes ikke.')

    svar = input('Vil du kjøre på nytt (ja/nei)? ').lower()
