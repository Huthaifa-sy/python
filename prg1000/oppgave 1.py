reg = input('legg inn bruker id: ')

finnes = False

# Først: sjekk om brukeren finnes
with open('bruker.txt', 'r', encoding='utf-8') as bruker:
    brukid = bruker.readline().strip()
    while brukid != '':
        fornavn = bruker.readline().strip()
        etternavn = bruker.readline().strip()
        epost = bruker.readline().strip()

        if brukid == reg:
            print('du er registrert fra før')
            finnes = True

        brukid = bruker.readline().strip()

# Hvis ikke finnes → registrer ny bruker
if not finnes:
    forn = input('legg inn fornavn: ')
    ettern = input('legg inn etternavn: ')
    eposten = input('legg inn epost: ')

    with open('bruker.txt', 'a', encoding='utf-8') as bruker:
        bruker.write(reg + '\n')
        bruker.write(forn + '\n')
        bruker.write(ettern + '\n')
        bruker.write(eposten + '\n')

    print('du er registrert som ny')
    print('hello world from python')
    print('this is Huthaifa')
