import tkinter as tk
from gui_app import Frame,barra_menu
from tabla_ventas import crear_tabla,tabla_productos

def main():
    root = tk.Tk()
    root.title('Registro de Ventas')
    root.iconbitmap('logo.ico')
    root.resizable(0,0)
    
    barra_menu(root)
    crear_tabla()
    tabla_productos()
  
    app = Frame(root = root)

   
    app.mainloop()

if __name__ == '__main__':
    main()




