from tkinter import *
def søk():
    bileier=open('bileier.txt','r')
    finnes=False
    fød=bileier.readline().strip()
    while fød!='':
        fornavn=bileier.readline().strip()
        etternavn=bileier.readline().strip()
        if fød==brukid.get():
            finnes=True
            navn.set(fornavn)
            enavn.set(etternavn)
        fød=bileier.readline().strip()
    bileier.close()
    if not finnes:
        navn.set('')
        enavn.set('finnes ikke')
window=Tk()
window.title('finn bileier')
fødnr=Label(window,text='oppgi fødselsnr').grid(row=0,column=0,padx=10,pady=10)
brukid=StringVar()
e_fød=Entry(window,width=20,textvariable=brukid).grid(row=0,column=1,padx=10,pady=10)
l_navn=Label(window,text='fornavn').grid(row=1,column=0,padx=10,pady=10)
navn=StringVar()
r_navn=Entry(window,width=20,textvariable=navn,state='readonly').grid(row=1,column=1,padx=10,pady=10)
l_enavn=Label(window,text='etternavn').grid(row=2,column=0,padx=10,pady=10)
enavn=StringVar()
r_enavn=Entry(window,width=20,textvariable=enavn,state='readonly').grid(row=2,column=1,padx=10,pady=10)
finn=Button(window,text='søk',command=søk).grid(row=0,column=2,padx=10,pady=15)
slutt=Button(window,text='avslutt',command=window.destroy).grid(row=3,column=3,padx=10,pady=15)
window.mainloop()






