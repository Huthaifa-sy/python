import os

slett = input('legge inn fødselsnr som skal slette')

# sjekke om eier finnes i bil.txt og finne bilnr
bil = open('bil.txt', 'r')
finnes = False
bilnr_til_eier = ''   # bare én variabel, ikke liste

regnr = bil.readline().strip()
while regnr != '':
    eier = bil.readline().strip()

    if eier == slett:
        finnes = True
        bilnr_til_eier = regnr   # lagrer bilnr til eieren

    regnr = bil.readline().strip()

bil.close()

# hvis eier ikke finnes
if not finnes:
    print('eier finnes ikke')
else:

    # sjekke bompasseringer
    bompassering = open('bompassering.txt', 'r')
    funnet = False

    reg = bompassering.readline().strip()
    while reg != '':
        bomid = bompassering.readline().strip()
        tid = bompassering.readline().strip()
        belop = bompassering.readline().strip()

        if reg == bilnr_til_eier:
            funnet = True

        reg = bompassering.readline().strip()

    bompassering.close()

    if funnet:
        print('kan ikke slett den eier har bompasseringer')
    else:

        # slette eier fra bileier.txt
        bileier = open('bileier.txt', 'r')
        fil = open('fil.txt', 'w')

        fød = bileier.readline().strip()
        while fød != '':
            fornavn = bileier.readline().strip()
            etternavn = bileier.readline().strip()

            if fød != slett:
                fil.write(fød + '\n')
                fil.write(fornavn + '\n')
                fil.write(etternavn + '\n')

            fød = bileier.readline().strip()

        bileier.close()
        fil.close()

        os.remove('bileier.txt')
        os.rename('fil.txt', 'bileier.txt')

        print('du er slette den eier')
