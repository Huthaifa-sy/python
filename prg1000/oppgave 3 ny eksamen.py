import os

slett = input('oppgi fødselsnr som skal slettes: ')

# 1. Finn alle biler som eieren har
bil = open('bil.txt', 'r')
finnes = False
bilnr = bil.readline().strip()

# lagrer bilnummer midlertidig i en tekststreng
mine_biler = ""

while bilnr != '':
    eier = bil.readline().strip()
    if slett == eier:
        finnes = True
        mine_biler = mine_biler + bilnr + '\n'
    bilnr = bil.readline().strip()

bil.close()

if not finnes:
    print('finnes ikke bil og eier')
else:
    # 2. Sjekk bompasseringer
    bompassering = open('bompassering.txt', 'r')
    funnet = False
    regnr = bompassering.readline().strip()

    while regnr != '':
        bomid = bompassering.readline().strip()
        tid = bompassering.readline().strip()
        belop = bompassering.readline().strip()

        # sjekk om regnr finnes i mine_biler
        if regnr in mine_biler:
            print('denne eieren har bompassering – kan ikke slettes')
            funnet = True

        regnr = bompassering.readline().strip()

    bompassering.close()

    # 3. Hvis ingen passeringer → slett eieren
    if not funnet:
        bileier = open('bileier.txt', 'r')
        ny = open('ny.txt', 'w')

        fød = bileier.readline().strip()

        while fød != '':
            fornavn = bileier.readline().strip()
            etternavn = bileier.readline().strip()

            if fød == slett:
                print('du slettet eieren')
            else:
                ny.write(fød + '\n')
                ny.write(fornavn + '\n')
                ny.write(etternavn + '\n')

            fød = bileier.readline().strip()

        bileier.close()
        ny.close()

        os.remove('bileier.txt')
        os.rename('ny.txt', 'bileier.txt')
