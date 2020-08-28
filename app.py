from tkinter import Tk,Entry,Label,StringVar,Button,messagebox,Toplevel,Frame

app = Tk()  #Abro loop de la aplicacion
app.geometry("900x400")
app.resizable(0,0)
app.config(bg="white")
app.title("codigos")

global c,n,Precio_actual # variables globales
c = StringVar()  
n = StringVar()
Precio_actual = StringVar() 

def Resultado_busqueda():        #muestra el resultado de la busqueda en base de datos
    if c.get() == "" and n.get() == "":
        nombre ="Nombre"
        precio ="Precios"
        codigo ="Codigo"
        precioBS = "PrecioBs"
    else:
        nombre = "Prueba"
        precio = "1"
        codigo = "9"
        precioBS = "2"
        c.set("")
        n.set("")
    mostrar_codigo(nombre,precio,codigo,precioBS)

contenedor = Frame(app,width=60,height=20).grid(row=1,column=0,pady=100,padx=0)

def mostrar_codigo(nombre,precio,codigo,precioBS):
    nombre_producto = Label(contenedor,width=16,height=2,bg="gray",text=nombre).grid(row=1,column=0,padx=40)
    precio_label = Label(contenedor,width=16,height=2,bg="gray",text=precio).grid(row=1,column=1,padx=40)
    precioBS_label = Label(contenedor,width=16,height=2,bg="gray",text=precioBS).grid(row=1,column=2,padx=40)
    Codigo_label = Label(contenedor,width=16,height=2,bg="gray",text=codigo).grid(row=1,column=3,padx=40)
    destruir(nombre_producto,precio_label,precioBS_label,Codigo_label)
    return

def destruir(num1,num2,num3,num4):
    pass

Label(app,width=16,height=2,bg="gray",text="codigo ").grid(row=0,column=0)
Entry(app,width=16,bg="gray",textvariable=c).grid(row=0,column=1)
Label(app,width=16,height=2,bg="gray",text="Nombre").grid(row=0,column=2)
Entry(app,width=16,bg="gray",textvariable=n).grid(row=0,column=3)
Label(app,width=16,height=2,bg="gray",text="precio dolar actual").grid(row=4,column=0)
Entry(app,width=16,bg="gray",textvariable=Precio_actual).grid(row=4,column=1,padx=10,pady=40)

Button(app,bg="gray",text="Buscar",command=Resultado_busqueda).grid(row=3,column=2)


app.mainloop()