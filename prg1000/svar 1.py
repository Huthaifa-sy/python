def reg_ny():
    reg=input('legge inn fødselsnr')
    bileier=open('bileier.txt','r')
    finnes=False
    fød=bileier.readline().strip()
    while fød!='':
        fornavn=bileier.readline().strip()
        etternavn=bileier.readline().strip()
        if fød==reg:
            finnes=True
        fød=bileier.readline().strip()
    bileier.close()

    if not finnes:
        navn=input('legge inn fornavn')
        enavn=input('legge inn etternavn')
        bileier=open('bileier.txt','a')
        bileier.write(reg + '\n')
        bileier.write(navn + '\n')
        bileier.write(enavn + '\n')
        bileier.close()
        print('du har registrer som ny')
    else:
        print('du registrer fra før ')
