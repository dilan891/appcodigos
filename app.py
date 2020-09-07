import tkinter as tk
import base_de_datos as BD
from tkinter import messagebox

app = tk.Tk()  #Abro loop de la aplicacion
app.geometry("800x400")
app.resizable(0,0)
app.config(bg="white")
app.title("codigos")

def nueva_ventana():
    add_windows = tk.Toplevel(app)
    
    tk.Label(add_windows,text="Codigo").grid(row=0,column=0) 
    tk.Label(add_windows,text="Nombre").grid(row=0,column=1)    
    tk.Label(add_windows,text="Nombre2 (opcional)").grid(row=0,column=2)    
    tk.Label(add_windows,text="Precio").grid(row=0,column=3)

    Nuevocodigo = tk.StringVar()
    Nuevonombre = tk.StringVar()
    Nuevonombre2 = tk.StringVar()
    Nuevoprecio = tk.StringVar()      

    tk.Entry(add_windows,textvariable=Nuevocodigo).grid(row=1,column=0)
    tk.Entry(add_windows,textvariable=Nuevonombre).grid(row=1,column=1)
    tk.Entry(add_windows,textvariable=Nuevonombre2).grid(row=1,column=2)
    tk.Entry(add_windows,textvariable=Nuevoprecio).grid(row=1,column=3)
    
    def add_Base():
        try:
            BD.insertar_producto(Nuevocodigo.get(),Nuevonombre.get(),Nuevonombre2.get(),Nuevoprecio.get())
            Nuevocodigo.set("")
            Nuevonombre.set("")
            Nuevonombre2.set("")
            Nuevoprecio.set("")
        except IndexError:
            messagebox.showerror(title="Error",message="Error al registrar el producto")

    tk.Button(add_windows,text="Añadir",command=lambda: add_Base()).grid(row=2,column=1,columnspan=2)

def Create_delete_windows():
    Delete_code = tk.StringVar()
    Ventana = tk.Toplevel()
    tk.Label(Ventana,text="Codigo").grid(row=0,column=0)
    tk.Entry(Ventana,textvariable=Delete_code).grid(row=1,column=0)
    tk.Button(Ventana,text="Eliminar",command=lambda:BD.eliminar_de_base(Delete_code.get())).grid(row=2,column=0)
    Delete_code.set("")

def Create_update_windows():
    update_window = tk.Toplevel()
    codigo = tk.StringVar()
    new_code = tk.StringVar()
    new_name = tk.StringVar()
    new_name2 = tk.StringVar()
    new_price = tk.StringVar()

    tk.Label(update_window,width=16,height=2,bg="gray",text="codigo: ").grid(row=0,column=0)
    tk.Entry(update_window,width=16,bg="gray",textvariable=codigo).grid(row=0,column=1)
    tk.Label(update_window,width=16,height=2,bg="gray",text="nombre").grid(row=1,column=1,padx=40)
    tk.Label(update_window,width=16,height=2,bg="gray",text="nombre2").grid(row=1,column=2,padx=40)
    tk.Label(update_window,width=16,height=2,bg="gray",text="Precio").grid(row=1,column=3,padx=40)
    tk.Label(update_window,width=16,height=2,bg="gray",text="codigo").grid(row=1,column=0,padx=40)

    tk.Entry(update_window,width=16,bg="gray",textvariable=new_code).grid(row=2,column=0)
    tk.Entry(update_window,width=16,bg="gray",textvariable=new_name).grid(row=2,column=1)
    tk.Entry(update_window,width=16,bg="gray",textvariable=new_name2).grid(row=2,column=2)
    tk.Entry(update_window,width=16,bg="gray",textvariable=new_price).grid(row=2,column=3)

    def busqueda(principal_code,code,name,name2,price):
        default = BD.Buscar_por_ID(codigo.get())
        if code == "":
            code = default[0]
        if name == "":
            name = default[1]
        if name2 == "":
            name2 = default[2]
        if price == "":
            price = default[3]
        name = name.capitalize()
        name2 = name2.capitalize()
        print(default)
        BD.update_base(principal_code,code,name,name2,price)

    tk.Button(update_window,text="actualizar",command=lambda:busqueda(codigo.get(),new_code.get(),new_name.get(),new_name2.get(),new_price.get())).grid(row=3,column=0)
    

#configuracion de la barra de menu en la parte superior
menuBar = tk.Menu(app)
app.config(menu= menuBar)

filemenu = tk.Menu(menuBar, tearoff=0)
filemenu.add_command(label="Añadir nuevo producto",command=nueva_ventana)
filemenu.add_command(label="Actualizar un producto",command=Create_update_windows)
filemenu.add_command(label="Eliminar un producto",command=Create_delete_windows)

helpmenu = tk.Menu(menuBar, tearoff=0)
helpmenu.add_command(label="Acerca de...")

menuBar.add_cascade(label="Archivo", menu=filemenu)
menuBar.add_cascade(label="Ayuda", menu=helpmenu)

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
                nombre = BD.Buscar_por_ID(codigo)[1]
                precio = BD.Buscar_por_ID(codigo)[3]
                codigo = BD.Buscar_por_ID(codigo)[0]
                precioBS = ("{:,.2f} BS").format(calculo(precio,int(Precio_actual.get())))
                c.set("")
                n.set("")
            except ValueError:
                messagebox.showwarning(title="dolar no dado",message="Valor del dolar en BS no dado")
                print("valor del dolar no dado")
            except TypeError: 
                messagebox.showerror(title="Error",message="Producto "+c.get()+" no existe")
                print("+",c.get(),"+")
        if n.get() != "":
            try:
                nombre = BD.Buscar_por_nombre(n.get())[1]
                precio = BD.Buscar_por_nombre(n.get())[3]
                codigo = BD.Buscar_por_nombre(n.get())[0]
                precioBS = ("{:,.2f} BS").format(calculo(precio,int(Precio_actual.get())))
            except ValueError:
                messagebox.showwarning(title="dolar no dado",message="Valor del dolar en BS no dado")
                print("valor del dolar no dado")
            except TypeError: 
                messagebox.showerror(title="Error",message="Producto "+n.get()+" no existe")
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