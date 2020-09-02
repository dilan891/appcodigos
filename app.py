from tkinter import Tk,Entry,Label,StringVar,Button,messagebox,Toplevel,Frame
import base_de_datos

app = Tk()  #Abro loop de la aplicacion
app.geometry("800x400")
app.resizable(0,0)
app.config(bg="white")
app.title("codigos")

global c,n,Precio_actual # variables globales
c = StringVar()  
n = StringVar()
Precio_actual = StringVar() 

def calculo(num1,num2):
    resultado = num1 * num2
    return resultado

def Resultado_busqueda():        #muestra el resultado de la busqueda en base de datos
    if c.get() == "" and n.get() == "":
        nombre ="Nombre"
        precio ="Precios"
        codigo ="Codigo"
        precioBS = "PrecioBs"
    else:
        try:
            codigo = (c.get(),)
            nombre = base_de_datos.Buscar_por_ID(codigo)[1]
            precio = base_de_datos.Buscar_por_ID(codigo)[3]
            codigo = base_de_datos.Buscar_por_ID(codigo)[0]
            precioBS = ("{:,.2f} BS").format(calculo(precio,int(Precio_actual.get())))
            c.set("")
            n.set("")
        except ValueError:
            print("valor del dolar no dado")
    mostrar_codigo(nombre,precio,codigo,precioBS)

contenedor = Frame(app,width=60,height=20,bg="yellow").grid(row=2,column=0,padx=0)

def mostrar_codigo(nombre,precio,codigo,precioBS):
    Label(contenedor,width=16,height=2,bg="gray",text="nombre").grid(row=1,column=1,padx=40)
    Label(contenedor,width=16,height=2,bg="gray",text="Precio").grid(row=1,column=2,padx=40)
    Label(contenedor,width=16,height=2,bg="gray",text="PrecioBS").grid(row=1,column=3,padx=40)
    Label(contenedor,width=16,height=2,bg="gray",text="codigo").grid(row=1,column=0,padx=40)
    nombre_producto = Label(contenedor,width=16,height=2,bg="gray",text=nombre).grid(row=2,column=1,padx=40)
    precio_label = Label(contenedor,width=16,height=2,bg="gray",text=str(precio) + " $").grid(row=2,column=2,padx=40)
    precioBS_label = Label(contenedor,width=16,height=2,bg="gray",text=precioBS).grid(row=2,column=3,padx=40)
    Codigo_label = Label(contenedor,width=16,height=2,bg="gray",text=codigo).grid(row=2,column=0,padx=40)
    destruir(nombre_producto,precio_label,precioBS_label,Codigo_label)
    return

def destruir(num1,num2,num3,num4):
    pass

Label(app,width=16,height=2,bg="gray",text="codigo: ").grid(row=0,column=0,pady=50)
Entry(app,width=16,bg="gray",textvariable=c).grid(row=0,column=1)
Label(app,width=16,height=2,bg="gray",text="Nombre:").grid(row=0,column=2)
Entry(app,width=16,bg="gray",textvariable=n).grid(row=0,column=3)
Label(app,width=16,height=2,bg="gray",text="precio dolar actual:").grid(row=4,column=0)
Entry(app,width=16,bg="gray",textvariable=Precio_actual).grid(row=4,column=1,padx=10,pady=40)

Button(app,bg="gray",text="Buscar",command=Resultado_busqueda).grid(row=3,column=2,pady=20)
app.mainloop()