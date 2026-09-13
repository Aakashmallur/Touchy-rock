from tkinter import *

DuM_CoMpUtEr_ChOiCeS=["rock","paper","sizzors"]
def DuM_PlAyEr_ChOiCeS (pc):
    ClApO_TRON.config(text="player selected "+pc)
main= Tk()
main.geometry("1000x1000")
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
Touchy_rock=Button(sensiwoo,text="Rock",command=lambda:DuM_PlAyEr_ChOiCeS(DuM_CoMpUtEr_ChOiCeS[0]))
Touchy_rock.grid(row=0,column=0)
Touchy_sizzors_dady=Button(sensiwoo,text="sizzors",command=lambda:DuM_PlAyEr_ChOiCeS(DuM_CoMpUtEr_ChOiCeS[2]))
Touchy_sizzors_dady.grid(row=0,column=1)
Touchy_paper_DaDy=Button(sensiwoo,text="paper",command=lambda:DuM_PlAyEr_ChOiCeS(DuM_CoMpUtEr_ChOiCeS[1]))
Touchy_paper_DaDy.grid(row=0,column=2)
oil_up_at_five_gramps_is_here=Label(main, text="comp selected N/A" ,font=("Arial",20))
oil_up_at_five_gramps_is_here.grid(row=5,column=0,pady=10)
ClApO_TRON=Label(main, text="player selected N/A" ,font=("Arial",20))
ClApO_TRON.grid(row=6,column=0,pady=20)












main.mainloop()