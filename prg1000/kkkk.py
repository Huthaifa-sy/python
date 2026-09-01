from tkinter import *

def beregn():
    a=int(ran.get())*int(g.get()):
    
        resultat.set(a)
    else:
        resultat.set('مبروك الخازوق')

window = Tk()
window.title('خوازيق احمد')

# العناوين
kh = Label(window, text='الخوازيق')
kh.grid(row=0, column=0, padx=100, pady=15)

g = Label(window, text='خوازيق')
g.grid(row=1, column=0, padx=100, pady=15)

re = Label(window, text='عدد الخوازيق')
re.grid(row=3, column=0, padx=100, pady=15)

# حقول الإدخال
khasoq = StringVar()
en_kh = Entry(window, width=9, textvariable=khasoq) 
en_kh.grid(row=0, column=1, padx=100, pady=15)

gol = StringVar()
en_g = Entry(window, width=9, textvariable=gol)
en_g.grid(row=1, column=1, padx=100, pady=15)

# زر الحساب
res = Button(window, text='احسب', command=beregn)
res.grid(row=2, column=1, padx=100, pady=15)

# حقل الإخراج
resultat = StringVar()
en_res = Entry(window, width=20, state='readonly', textvariable=resultat)
en_res.grid(row=3, column=1, padx=100, pady=15)

# زر الإغلاق
D = Button(window, text='done', command=window.destroy)
D.grid(row=5, column=0, padx=100, pady=15)

window.mainloop()
