from conexion_db import ConexionDb
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDb()
    sql = '''CREATE TABLE ventas(
            n_ventas INTEGER,
            producto TEXT,
            cantidad INTEGER,
            precio REAL,
            PRIMARY KEY(n_ventas AUTOINCREMENT)
        )'''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        pass

def tabla_productos():
        conexion = ConexionDb()
        sql1 = '''CREATE TABLE productos(
                descripcion TEXT
            )'''
        sql2 = '''INSERT INTO productos(descripcion) VALUES ('Televisor 4K QLED')'''
        sql3 = '''INSERT INTO productos(descripcion) VALUES ('Lavarropas Dream Auto')'''
        sql4 = '''INSERT INTO productos(descripcion) VALUES ('Horno Elect Everest')'''
        sql5 = '''INSERT INTO productos(descripcion) VALUES ('Aire Acondicionado Philco')'''
        sql6 = '''INSERT INTO productos(descripcion) VALUES ('Procesadora Lilian')'''
        sql7 = '''INSERT INTO productos(descripcion) VALUES ('Ventilador Philips')'''
        
        try:
            conexion.cursor.execute(sql1)
            conexion.cursor.execute(sql2)
            conexion.cursor.execute(sql3)
            conexion.cursor.execute(sql4)
            conexion.cursor.execute(sql5)
            conexion.cursor.execute(sql6)
            conexion.cursor.execute(sql7)
            conexion.cerrar()
        except:
            pass

class Tabla:
    def __init__(self,producto,cantidad,precio):
        self.n_ventas = None
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f'Tabla[{self.producto}, {self.cantidad}, {self.precio}]'

def Guardar(tabla):
    conexion = ConexionDb()
        
    sql = f""" INSERT INTO ventas (producto,cantidad,precio)
    VALUES('{tabla.producto}','{tabla.cantidad}','{tabla.precio}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla Ventas no esta creada en la base de datos'
        messagebox.showerror(titulo,mensaje)

def listar():
    conexion = ConexionDb()

    lista_ventas = []
    
    sql = 'SELECT * FROM ventas'

    try:
        conexion.cursor.execute(sql)
        lista_ventas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Crea la tabla en la Base de Datos'
        messagebox.showwarning(titulo,mensaje)
    return lista_ventas

def combo_box():
    conexion = ConexionDb()
    lista = []
    sql = 'SELECT descripcion FROM productos'
    conexion.cursor.execute(sql)
    lista = conexion.cursor.fetchall()
    conexion.cerrar()
    return lista


