reg=input('legge inn bruker id')
bruker=open('bruker.txt','r')
finnes=False
brukid=bruker.readline().strip()
while brukid!='':
    fornavn=bruker.readline().strip()
    etternavn=bruker.readline().strip()
    epost=bruker.readline().strip()
    if brukid==reg:
        print('du har registrer fra før')
        finnes=True
    else:
        brukid=bruker.readline().strip()
bruker.close()

if not finnes:
    fnavn=input('legge inn fornavn')
    enavn=input('legge inn etternavn')
    ep=input('legge inn epost')
    bruker=open('bruker.txt','a')
    bruker.write(reg+'\n')
    bruker.write(fnavn+'\n')
    bruker.write(enavn+'\n')
    bruker.write(ep+'\n')
    bruker.close()
print('du registre som ny')

