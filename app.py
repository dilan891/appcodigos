from tkinter import Tk,Entry,Label,StringVar,Button,messagebox,Toplevel

app = Tk()  #Abro loop de la aplicacion
app.geometry("650x650")
app.resizable(0,0)
app.config(bg="white")
app.title("codigos")

def mostrar_codigo():
    nombre_producto = Label(app,width=16,height=2,bg="gray",text="nomnre").grid(row=1,column=0)
    precio = Label(app,width=16,height=2,bg="gray",text="precio").grid(row=1,column=1)
    precioBS = Label(app,width=16,height=2,bg="gray",text="BS").grid(row=1,column=2)
    Codigo = Label(app,width=16,height=2,bg="gray",text="codigo ").grid(row=1,column=3)

Label(app,width=16,height=2,bg="gray",text="codigo ").grid(row=0,column=0)
Codigo = Entry(app,width=16,bg="gray").grid(row=0,column=1)
Label(app,width=16,height=2,bg="gray",text="Nombre").grid(row=0,column=2)
Nombre =  Entry(app,width=16,bg="gray").grid(row=0,column=3)
Label(app,width=16,height=2,bg="gray",text="precio dolar actual").grid(row=0,column=4)
precio = Entry(app,width=16,bg="gray").grid(row=0,column=5)

mostrar_codigo()

app.mainloop()