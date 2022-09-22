import tkinter

from tkinter import *

import home

root = Tk()

root.iconbitmap("logo.ico")
root.title("Algoritmos de Planificación")
root.geometry("450x300")

def aceptar():
    root_datos = Tk()
    root_datos.iconbitmap("logo.ico")
    root_datos.title("Ingreso de datos")
    root_datos.geometry("450x500")

    frame_ingreso_datos = Frame(root_datos, width="300", height="400")
    frame_ingreso_datos.pack()
    #FRAME, LABEL Y ENTRY NOMBRE PROCESO
    label_nom_proceso = Label(frame_ingreso_datos, text="Nombre del proceso", font=("Comic Sans MS", 14))
    label_nom_proceso.place(x=60, y= 30 )
    entry_nom_proceso = Entry(frame_ingreso_datos, width="50", justify=tkinter.CENTER)
    entry_nom_proceso.place(x= 30,y= 70)

    #LABEL Y ENTRY DURACION
    label_duracion_proceso = Label(frame_ingreso_datos, text="Duración del proceso", font=("Comic Sans MS", 14))
    label_duracion_proceso.place(x=65, y= 115 )
    entry_duracion_proceso = Entry(frame_ingreso_datos, width="50", justify=tkinter.CENTER)
    entry_duracion_proceso.place(x= 30,y= 150)

    # LABEL Y ENTRY PRIORIDAD
    label_duracion_prioridad = Label(frame_ingreso_datos, text="Prioridad del proceso", font=("Comic Sans MS", 14))
    label_duracion_prioridad.place(x=65, y=200)
    entry_duracion_prioridad = Entry(frame_ingreso_datos, width="50", justify=tkinter.CENTER)
    entry_duracion_prioridad.place(x=30, y=250)

    #BOTONES ACEPTAR Y CERRAR


    root.mainloop()

def btn_cerrar():
    exit(1)


#frame proceso
frame_proceso = Frame(root, width="300", height="350")
frame_proceso.pack()
#Label texto numero procesos
label_num_proceso = Label(frame_proceso, text="Número de procesos ",font=("Comic Sans MS", 15))
label_num_proceso.place(x= 50,y= 40)
#Entry de numero procesos
text_num_procesos = Entry(frame_proceso, width="30", justify=tkinter.CENTER)
text_num_procesos.place(x= 55, y = 100)
#Label de texto quantum
label_num_quantum = Label(frame_proceso, text="Quantum ",font=("Comic Sans MS", 15))
label_num_quantum.place(x= 90,y= 150)
#Entry de quantum
text_quantum = Entry(frame_proceso, width="30", justify=tkinter.CENTER)
text_quantum.place(x= 55 ,y=200)

#Boton aceptar
btn_aceptar = tkinter.Button(text="Aceptar", command=aceptar)
btn_aceptar.place(x=140,y=250)
#Boton cancelar
btn_cancelar = tkinter.Button(text="Cancelar", command=btn_cerrar)
btn_cancelar.place(x=230,y=250)




#Metodo para que la ventana este en ejecucion
root.mainloop()