from tkinter import *  
base = Tk()  
base.geometry("500x500")  
base.title("registration form")  
  
lb1= Label(base, text="Enter Name", width=10, font=("arial",12))  
lb1.place(x=20, y=120)  
en1= Entry(base)  
en1.place(x=200, y=120)  
  
lb3= Label(base, text="Enter Email", width=10, font=("arial",12))  
lb3.place(x=19, y=160)  
en3= Entry(base)  
en3.place(x=200, y=160)  
  
lb4= Label(base, text="Contact Number", width=13,font=("arial",12))  
lb4.place(x=19, y=200)  
en4= Entry(base)  
en4.place(x=200, y=200)  
  
lb5= Label(base, text="Select Gender", width=15, font=("arial",12))  
lb5.place(x=5, y=240)  
vars = IntVar()  
Radiobutton(base, text="Male", padx=5,variable=vars, value=1).place(x=180, y=240)  
Radiobutton(base, text="Female", padx =10,variable=vars, value=2).place(x=240,y=240)  
Radiobutton(base, text="others", padx=15, variable=vars, value=3).place(x=310,y=240)  
 
lb6= Label(base, text="Enter Password", width=13,font=("arial",12))  
lb6.place(x=19, y=280)  
en6= Entry(base, show='*')  
en6.place(x=200, y=280)  
  
Button(base, text="Register", width=10).place(x=200,y=400)  
base.mainloop()  
