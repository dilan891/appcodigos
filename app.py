from tkinter import Tk,Entry,Label,StringVar,Button,messagebox,Toplevel

app = Tk()
app.geometry("650x650")
app.resizable(0,0)
app.config(bg="white")
app.title("codigos")

Label(app,width=16,height=2,bg="gray",text="codigo ").grid(row=0,column=0)
Codigo = Entry(app,width=16,bg="gray").grid(row=0,column=1)

app.mainloop()