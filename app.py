import tkinter as tk
import base_de_datos
from tkinter import messagebox

app = tk.Tk()  #Abro loop de la aplicacion
app.geometry("800x400")
app.resizable(0,0)
app.config(bg="white")
app.title("codigos")

global c,n,Precio_actual # variables globales
c = tk.StringVar()  
n = tk.StringVar()
Precio_actual = tk.StringVar() 

def calculo(num1,num2):
    resultado = num1 * num2
    return resultado

def Resultado_busqueda(event):        # muestra el resultado de la busqueda en base de datos
    if c.get() == "" and n.get() == "":
        nombre ="Nombre"
        precio ="Precios"
        codigo ="Codigo"
        precioBS = "PrecioBs"
    else:
        if c.get() != "":
            try:
                codigo = (c.get(),)
                nombre = base_de_datos.Buscar_por_ID(codigo)[1]
                precio = base_de_datos.Buscar_por_ID(codigo)[3]
                codigo = base_de_datos.Buscar_por_ID(codigo)[0]
                precioBS = ("{:,.2f} BS").format(calculo(precio,int(Precio_actual.get())))
                c.set("")
                n.set("")
            except ValueError:
                messagebox.showwarning(title="dolar no dado",message="Valor del dolar en BS no dado")
                print("valor del dolar no dado")
            except TypeError: 
                messagebox.showerror(title="Error",message="objeto no existe")
                print("+",c.get(),"+")
        if n.get() != "":
            nombre = "juanito"
            precio = "0"
            codigo = "0"
            precioBS = "0"
            print("busqueda por nombre")
    mostrar_codigo(nombre,precio,codigo,precioBS)

contenedor_datos = tk.Frame(app,width=50,height=20,bg="yellow")
contenedor_datos.grid(row=2,column=0,padx=0,columnspan=4,pady=40)

def mostrar_codigo(nombre,precio,codigo,precioBS):
    tk.Label(contenedor_datos,width=16,height=2,bg="gray",text="nombre").grid(row=1,column=1,padx=40)
    tk.Label(contenedor_datos,width=16,height=2,bg="gray",text="Precio").grid(row=1,column=2,padx=40)
    tk.Label(contenedor_datos,width=16,height=2,bg="gray",text="PrecioBS").grid(row=1,column=3,padx=40)
    tk.Label(contenedor_datos,width=16,height=2,bg="gray",text="codigo").grid(row=1,column=0,padx=40)
    nombre_producto = tk.Label(contenedor_datos,width=16,height=2,bg="gray",text=nombre)
    nombre_producto.grid(row=2,column=1,padx=40)
    precio_label = tk.Label(contenedor_datos,width=16,height=2,bg="gray",text=str(precio) + " $")
    precio_label.grid(row=2,column=2,padx=40)
    tk.Label(contenedor_datos,width=16,height=2,bg="gray",text=precioBS).grid(row=2,column=3,padx=40)
    Codigo_label = tk.Label(contenedor_datos,width=16,height=2,bg="gray",text=codigo)
    Codigo_label.grid(row=2,column=0,padx=40)
    destruir(nombre_producto,precio_label,Codigo_label)

def destruir(num1,num2,num3):
    pass

contenedor_superior = tk.Frame(app,width=50,height=20,bg="yellow")
contenedor_superior.grid(row=0,column=0,columnspan=4,pady=10)

mostrar_codigo("","","","")

tk.Label(contenedor_superior,width=16,height=2,bg="gray",text="codigo: ").grid(row=0,column=0)
Ncodigo= tk.Entry(contenedor_superior,width=16,bg="gray",textvariable=c)
Ncodigo.grid(row=0,column=1)
tk.Label(contenedor_superior,width=16,height=2,bg="gray",text="Nombre:").grid(row=0,column=2)
tk.Entry(contenedor_superior,width=16,bg="gray",textvariable=n).grid(row=0,column=3)
tk.Label(app,width=16,height=2,bg="gray",text="precio dolar actual:").grid(row=4,column=0)
tk.Entry(app,width=16,bg="gray",textvariable=Precio_actual).grid(row=4,column=1,padx=10)

Ncodigo.bind("<Return>",Resultado_busqueda)

tk.Button(app,bg="gray",text="Buscar",command=lambda:Resultado_busqueda("enter")).grid(row=3,column=1)
app.mainloop()