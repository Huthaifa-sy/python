from tkinter import *

def finn_bok():
    finnes = False
    bok = open('bok.txt', 'r', encoding='utf-8')

    isbn = bok.readline().strip()
    while isbn != '':
        tittel_read = bok.readline().strip()
        forfatter_read = bok.readline().strip()
        forlag_read = bok.readline().strip()
        utgitt_read = bok.readline().strip()

        if isbn == bokid.get():
            finnes = True
            tittel.set(tittel_read)
            forfatter.set(forfatter_read)
            forlag.set(forlag_read)
            utgitt.set(utgitt_read)
        isbn = bok.readline().strip()

    bok.close()  # lukker filen manuelt

    if not finnes:
        tittel.set('finnes ikke')
        forfatter.set('finnes ikke')
        forlag.set('finnes ikke')
        utgitt.set('finnes ikke')

# GUI
window = Tk()
window.title('Finn bok')

lbl_isbn = Label(window, text='Oppgi isbnNr: ')
lbl_isbn.grid(row=0, column=0, padx=5, pady=5)

bokid = StringVar()
ent_bokid = Entry(window, width=20, textvariable=bokid)
ent_bokid.grid(row=0, column=1, padx=5, pady=5)

lbl_tittel = Label(window, text='Tittel: ').grid(row=1, column=0, padx=5, pady=5)


tittel = StringVar()
ent_tittel = Entry(window, width=20, textvariable=tittel, state='readonly').grid(row=1, column=1, padx=5, pady=5)


lbl_forfatter = Label(window, text='Forfatter(e): ')
lbl_forfatter.grid(row=2, column=0, padx=5, pady=5)

forfatter = StringVar()
ent_forfatter = Entry(window, width=20, textvariable=forfatter, state='readonly')
ent_forfatter.grid(row=2, column=1, padx=5, pady=5)

lbl_forlag = Label(window, text='Forlag: ')
lbl_forlag.grid(row=3, column=0, padx=5, pady=5)

forlag = StringVar()
ent_forlag = Entry(window, width=20, textvariable=forlag, state='readonly')
ent_forlag.grid(row=3, column=1, padx=5, pady=5)

lbl_utgitt = Label(window, text='Utgitt år: ')
lbl_utgitt.grid(row=4, column=0, padx=5, pady=5)

utgitt = StringVar()
ent_utgitt = Entry(window, width=20, textvariable=utgitt, state='readonly')
ent_utgitt.grid(row=4, column=1, padx=5, pady=5)

btn_finn_bok = Button(window, text='Finn bok', command=finn_bok)
btn_finn_bok.grid(row=0, column=2, padx=5, pady=5)

btn_avslutt = Button(window, text='Avslutt', command=window.destroy)
btn_avslutt.grid(row=5, column=2, padx=5, pady=5)

window.mainloop()
