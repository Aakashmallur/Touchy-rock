from tkinter import *



main= Tk()
main.geometry("500x500")
main.config(background="orange")
main.title("ohio")

oil_label=Label(main, text="Rock paper Scissors Shoot" ,font=("Arial",20))
oil_label.grid(row=0,column=0,padx=100)


oil_up_label=Label(main, text="start game" ,font=("Arial",20))
oil_up_label.grid(row=1,column=0,padx=100,pady=50)
oil_up_at_five=Label(main, text="player Options" ,font=("Arial",20))
oil_up_at_five.grid(row=3,column=0,padx=100,pady=50)
sensiwoo=Frame(main)
sensiwoo.grid(row=4,column=0)
Touchy_rock=Button(sensiwoo,text="Rock")
Touchy_rock.grid(row=0,column=0)
main.mainloop()