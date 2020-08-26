from tkinter import Tk,Entry,Label,StringVar,Button,messagebox,Toplevel,Frame

app = Tk()  #Abro loop de la aplicacion
app.geometry("900x400")
app.resizable(0,0)
app.config(bg="white")
app.title("codigos")

codigo = StringVar()
nombre = StringVar()
Precio_actual = StringVar() 


contenedor = Frame(app,width=60,height=20).grid(row=1,column=0,pady=100,padx=0)

def mostrar_codigo():
    nombre_producto = Label(contenedor,width=16,height=2,bg="gray",text="Nomnbre").grid(row=1,column=0,padx=40)
    precio = Label(contenedor,width=16,height=2,bg="gray",text="precio").grid(row=1,column=1,padx=40)
    precioBS = Label(contenedor,width=16,height=2,bg="gray",text="BS").grid(row=1,column=2,padx=40)
    Codigo2 = Label(contenedor,width=16,height=2,bg="gray",text="codigo ").grid(row=1,column=3,padx=40)

def destruir():
    pass

Label(app,width=16,height=2,bg="gray",text="codigo ").grid(row=0,column=0)
Entry(app,width=16,bg="gray",textvariable=codigo).grid(row=0,column=1)
Label(app,width=16,height=2,bg="gray",text="Nombre").grid(row=0,column=2)
Entry(app,width=16,bg="gray",textvariable=nombre).grid(row=0,column=3)
Label(app,width=16,height=2,bg="gray",text="precio dolar actual").grid(row=4,column=0)
Entry(app,width=16,bg="gray",textvariable=Precio_actual).grid(row=4,column=1,padx=10,pady=40)

Button(app,bg="gray",text="Buscar",command=mostrar_codigo).grid(row=3,column=2)



app.mainloop()