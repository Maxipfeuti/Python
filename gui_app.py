import tkinter as tk
from tkinter import ttk
from tabla_ventas import Tabla, Guardar,listar,combo_box

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)
    
    barra_menu.add_cascade(label = 'SALIR', command = root.destroy)


class Frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root,width=1200, height=900)
        self.root = root
        self.pack()
        self.registrar()
        self.setear_campos()
        self.tabla_ventas()

    def registrar(self):
        #labels(etiquetas)
        self.label_producto = tk.Label(self, text= 'Producto:')
        self.label_producto.config(font=('Arial',12,'bold'))
        self.label_producto.grid(row=0, column=0, padx=1, pady=5)
        
        self.label_cantidad = tk.Label(self, text= 'Cantidad:')
        self.label_cantidad.config(font=('Arial',12,'bold'))
        self.label_cantidad.grid(row=1, column=0, padx=1, pady=5)

        self.label_precio= tk.Label(self, text= 'Precio:')                         
        self.label_precio.config(font=('Arial',12,'bold'))
        self.label_precio.grid(row=2, column=0, padx=1, pady=5)
       
        #entrada de datos
        self.slist = combo_box()
        values = [row[0] for row in self.slist]
        self.producto= ttk.Combobox(self,state = "readonly")
        self.producto.grid(row=0,column=1,padx=0, pady=5)
        self.producto.config(width=20,values = values)
        
        self.cantidad=tk.StringVar()
        self.entry_cantidad= tk.Entry(self, textvariable=self.cantidad)
        self.entry_cantidad.config(width= 2,font=('Arial',12))
        self.entry_cantidad.grid(row=1,column=1,padx=0, pady=5)

        self.precio=tk.StringVar()
        self.entry_precio = tk.Entry(self,textvariable=self.precio)
        self.entry_precio.config(width= 6,font=('Arial',12))
        self.entry_precio.grid(row=2,column=1,padx=0, pady=5)
       
        #botones
        self.boton_cargar = tk.Button(self,text='Registrar Venta', command=self.guardar_datos)
        self.boton_cargar.config(width=20,font=('Arial',12,'bold'),fg='white',bg='green')
        self.boton_cargar.grid(row=3,column=0,padx=10,pady=10)

        self.boton_cancelar = tk.Button(self,text='CANCELAR', command=self.setear_campos)
        self.boton_cancelar.config(width=20,font=('Arial',12,'bold'),fg='white',bg='blue')
        self.boton_cancelar.grid(row=3,column=1,padx=10,pady=10)

    def setear_campos(self):
        self.cantidad.set('')
        self.precio.set('')
    
    def tabla_ventas(self):
        self.lista_ventas = listar()
        self.lista_ventas.reverse()
        self.tabla = ttk.Treeview(self, 
        column = ('N° venta','Producto','Cantidad','Precio P/U'))
        self.tabla.grid(row=4, column=0, columnspan=4)

        self.tabla.heading('#0', text='N° venta')
        self.tabla.heading('#1', text='Producto')
        self.tabla.heading('#2', text='Cantidad')
        self.tabla.heading('#3', text='Precio P/U')

        #iterar la lista de peliculas
        for p in self.lista_ventas:
            self.tabla.insert('',0,text=p[0],values=(p[1],p[2],p[3]))

        
    def guardar_datos(self):
       tabla = Tabla(
        self.producto.get(),
        self.cantidad.get(),
        self.precio.get(),
       )

       Guardar(tabla)
       self.tabla_ventas()
   


       



 



        


        

        






