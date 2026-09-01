def reg_bilde():
    reg = input('legge inn bilde id: ')

    with open('bilder.txt', 'r', encoding='utf-8') as bilder:
        with open('bruker.txt', 'r', encoding='utf-8') as bruker:

            finnes = False
            fotograf_funnet = False

            # sjekk om bildet finnes fra før
            bildeid = bilder.readline().strip()
            while bildeid != '':
                beskrivelse = bilder.readline().strip()
                opplastdato = bilder.readline().strip()
                fotograf = bilder.readline().strip()

                if reg == bildeid:
                    print('den bilde har registrert fra før')
                    finnes = True

                bildeid = bilder.readline().strip()   # ← تصحيح مهم

            # sjekk om fotograf finnes
            brukerid = bruker.readline().strip()
            while brukerid != '':
                fornavn = bruker.readline().strip()
                etternavn = bruker.readline().strip()
                epost = bruker.readline().strip()

                if brukerid == fotograf:
                    print('fotograf er funnet')
                    fotograf_funnet = True

                brukerid = bruker.readline().strip()   # ← تصحيح مهم

    # nå sjekker vi الشرطين معاً
    if not finnes and fotograf_funnet:
        besk = input('legge inn beskrivelse: ')
        dato = input('legge inn opplast dato: ')
        foto = input('legge inn fotograf: ')

        with open('bilder.txt', 'a', encoding='utf-8') as bilder:
            bilder.write(reg + '\n')
            bilder.write(besk + '\n')
            bilder.write(dato + '\n')
            bilder.write(foto + '\n')

        print('bilde registrert som ny')

    elif not fotograf_funnet:
        print('fotograf finnes ikke – kan ikke registrere bilde')
