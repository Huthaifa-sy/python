def reg_bilde():
    reg=input('legge inn bilde id')

    # --- Sjekk om bildet finnes fra før ---
    bilder=open('bilder.txt','r')
    finnes=False
    bildeid=bilder.readline().strip()

    while bildeid!='':
        beskrivelse=bilder.readline().strip()
        opplastdato=bilder.readline().strip()
        fotograf=bilder.readline().strip()

        if bildeid==reg:
            print('den bilde er registrert fra før')
            finnes=True

        bildeid=bilder.readline().strip()

    bilder.close()

    # --- Sjekk om fotograf/bruker finnes ---
    bruker=open('bruker.txt','r')
    funnet=False
    brukerid=bruker.readline().strip()

    while brukerid!='':
        fornavn=bruker.readline().strip()
        etternavn=bruker.readline().strip()
        epost=bruker.readline().strip()

        if brukerid==fotograf:
            print('fotograf er funnet')
            funnet=True

        brukerid=bruker.readline().strip()

    bruker.close()

    # --- Registrer nytt bilde ---
    if not finnes and funnet:
        besk=input('skriv beskrivelse')
        dato=input('legge inn opplastdato')
        foto=input('legge inn fotograf')

        bilder=open('bilder.txt','a')
        bilder.write(reg + '\n')
        bilder.write(besk + '\n')
        bilder.write(dato + '\n')
        bilder.write(foto + '\n')
        bilder.close()

        print('du registrerer bilde som ny')

    elif not funnet:
        print('fotograf finnes ikke, kan ikke registrere')

    elif finnes:
        print('bildet finnes fra før')
