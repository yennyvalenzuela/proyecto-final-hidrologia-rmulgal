"""---------------------------------LIBRERIAS NECESARIAS PARA ANALIZAR LOS DATOS--------------------------------------"""
import tkinter as tk  # """TK= PARA SIMPLIFICAR EL NOMBRE TKINTER"""
from tkinter import *  # """TKINTER= LIBRERIA PARA CREAR INTERFACES GRAFICAS(VENTANAS)"""
import matplotlib.pyplot as plt  # """MATPLOTLIB= LIBRERIA PARA GRAFICAR FIGURAS """
import pandas as pd  # """PANDAS= LIBRERIA PARA LEER Y ANALIZAR ARCHIVOS EXCEL,CSV,TXT"""
from fpdf import FPDF  # """ LIBRERIA PARA CREAR PDF'S"""
from sklearn.linear_model import \
    LinearRegression  # """SKLEARN= LIBRERIA PARA FACILITAR EL CALCULO DE LA REGRESION LINEAL"""
import sklearn.utils._weight_vector
"""--------------------------------------------------------------------------------------------------------------"""

"""--------------------------FUNCIONES DE CAMBIO DE COLOR DEL FONDO DE LA PANTALLA INICIAL----------------------------------------------"""
def fondo_inicial():
    mywindow['bg']='black'
def fondo_negro():
    mywindow['bg']='#213141'
def fondo_azul():
    mywindow['bg']='blue'
def fondo_rojo():
    mywindow['bg']='red'
def fondo_morado():
    mywindow['bg']='#8D34EB'
def fondo_agua():
    mywindow['bg']='#3382EB'
def fondo_celeste():
    mywindow['bg']='#0DEAFF'
"""--------------------------------------------------------------------------------------------------------------"""

"""--------------------------FUNCION PARA EXPORTAR EL RESULTADO A PDF----------------------------------------------"""
def send_data():
    data = pd.read_excel(r"C:\Program Files\RMULGAL\RegresionLinealDatos.xlsx")
    print(data)
    nEstprincipal = data['EstacionPrincipal'].values.reshape(-1, 1)
    nEstfaltante = data['EstacionFaltante'].values.reshape(-1, 1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(nEstprincipal, nEstfaltante)
    nEstfaltante_pred = linear_regressor.predict(nEstprincipal)
    # y= mx+c
    m = linear_regressor.coef_[0][0]
    c = linear_regressor.intercept_[0]
    label = r'$nEstFaltante = %0.4f*EstPrincipal %+0.4f$' % (m, c)
    print(label)
    fig = plt.figure(figsize=(14, 14))
    plt.scatter(data['EstacionPrincipal'], data['EstacionFaltante'], label="Datos Iniciales")
    plt.plot(nEstprincipal, nEstfaltante_pred, color='red', label=label)
    plt.xlabel("Estacion Principal")
    plt.ylabel("Estacion Faltante")
    plt.legend()
    plt.grid()
    plt.savefig('RegrLine.png')
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('arial', 'B', 11)
    pdf.cell(60)
    pdf.cell(75, 10, 'GRÁFICA DE REGRESIÓN LINEAL ', 0, 2, 'C')
    pdf.cell(75, 12, 'Hecho por: Grupo Mulga   DOCENTE: Fernando Paz   CURSO: Hidrología', 0, 2, 'C')
    pdf.cell(90, 10, '', 0, 2, 'C')
    pdf.cell(-55)
    pdf.image("RegrLine.png", 0, 30, 205)
    pdf.output('RESULTADORMULGA.pdf', 'F')
"""--------------------------------------------------------------------------------------------------------------"""

"""--------------------------FUNCION QUE CREA UNA VENTANA Y MUESTRA LA ECUACION LINEAL----------------------------------------------"""
def ecuacion():
    ewindow= Tk()
    ewindow.geometry("500x100")
    ewindow.resizable(False, False)
    ewindow.config(background="black")
    ewindow.title("ECUACIÓN DE LA RECTA DE REGRESIÓN LINEAL")
    data = pd.read_excel(r"C:\Program Files\RMULGAL\RegresionLinealDatos.xlsx")
    nEstprincipal = data['EstacionPrincipal'].values.reshape(-1, 1)
    nEstfaltante = data['EstacionFaltante'].values.reshape(-1, 1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(nEstprincipal, nEstfaltante)
    # y= mx+c
    m = linear_regressor.coef_[0][0]
    c = linear_regressor.intercept_[0]
    label = r'$nEstFaltante = %0.4f*EstPrincipal %+0.4f$' % (m, c)
    a_label = Label(ewindow, text="RESULTADO", fg="white", bg="blue", height="2",
                    width="45", font=("Cambria", 14, 'bold'))
    a_label.place(x=0, y=0)
    B_label = Label(ewindow, text=label, fg="white", bg="black", height="1",
                    width="50", font=("Cambria", 14, 'bold'))
    B_label.place(x=0, y=60)
"""--------------------------------------------------------------------------------------------------------------"""

"""--------------------------FUNCION QUE CREA UNA VENTANA Y MUESTRA EL CODIGO----------------------------------------------"""
def codigo():
    vwindow = Tk()
    vwindow.state('zoomed')
    vwindow.title("CODIGO  FUENTE  PYHTHON")
    vwindow.resizable(False, False)
    vwindow.config(background="black")
    a_label = Label(vwindow,text="CÓDIGO PRINCIPAL PARA EL ANALISIS DE DATOS", fg="white", bg="green", height="1",width="125", font=("Cambria", 14,'bold'))
    a_label.place(x=0, y=0)
    b_label = Label(vwindow,text="import pandas as pd", fg="white", bg="black", height="1", font=("Cambria", 14))
    b_label.place(x=20, y=30)
    c_label = Label(vwindow, text="import matplotlib.pyplot as plt", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    c_label.place(x=20, y=60)
    d_label = Label(vwindow, text="from sklearn.linear_model import LinearRegression", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    d_label.place(x=20, y=100)
    e_label = Label(vwindow, text="from tkinter import *", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    e_label.place(x=20, y=140)
    f_label = Label(vwindow, text="import tkinter as tk", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    f_label.place(x=20, y=180)
    g_label = Label(vwindow, text="data = pd.read_excel('RegresionLinealDatos.xlsx')", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    g_label.place(x=20, y=220)
    h_label = Label(vwindow, text="nEstprincipal = data['EstacionPrincipal'].values.reshape(-1, 1)", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    h_label.place(x=20, y=260)
    i_label = Label(vwindow, text="nEstfaltante = data['EstacionFaltante'].values.reshape(-1, 1)", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    i_label.place(x=20, y=300)
    j_label = Label(vwindow, text="linear_regressor = LinearRegression()", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    j_label.place(x=20, y=340)
    k_label = Label(vwindow, text="linear_regressor.fit(nEstprincipal, nEstfaltante)", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    k_label.place(x=20, y=380)
    l_label = Label(vwindow, text="nEstfaltante_pred = linear_regressor.predict(nEstprincipal)", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    l_label.place(x=20, y=420)
    m_label = Label(vwindow, text="# y= mx+c", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    m_label.place(x=20, y=460)
    n_label = Label(vwindow, text="m = linear_regressor.coef_[0][0]", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    n_label.place(x=20, y=500)
    o_label = Label(vwindow, text="c = linear_regressor.intercept_[0]", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    o_label.place(x=20, y=540)
    p_label = Label(vwindow, text="label = r'$nEstFaltante = %0.4f*EstPrincipal %+0.4f$' % (m, c)", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    p_label.place(x=20, y=580)
    q_label = Label(vwindow, text="fig = plt.figure(figsize=(14, 14))", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    q_label.place(x=20, y=620)
    r_label = Label(vwindow, text="plt.scatter(data['EstacionPrincipal'], data['EstacionFaltante'], label='Datos Iniciales')", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    r_label.place(x=20, y=660)
    s_label = Label(vwindow, text="plt.plot(nEstprincipal, nEstfaltante_pred, color='red', label=label)", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    s_label.place(x=20, y=700)
    t_label = Label(vwindow, text="plt.xlabel('Estacion Principal')", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    t_label.place(x=800, y=30)
    u_label = Label(vwindow, text="plt.ylabel('Estacion Faltante')", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    u_label.place(x=800, y=60)
    v_label = Label(vwindow, text="plt.legend()", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    v_label.place(x=800, y=100)
    x_label = Label(vwindow, text="plt.grid()", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    x_label.place(x=800, y=140)
    y_label = Label(vwindow, text="plt.show()", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    y_label.place(x=800, y=180)
    z_label = Label(vwindow, text="import pandas as pd", fg="white", bg="black", height="1",
                           font=("Cambria", 14))
    z_label.place(x=800, y=220)
"""--------------------------------------------------------------------------------------------------------------"""

"""--------------------------FUNCION(BOTON GRAFICAR) PARA CREAR MOSTRAR LA GRAFICA----------------------------------------------"""
def calculo():
    data = pd.read_excel(r"C:\Program Files\RMULGAL\RegresionLinealDatos.xlsx")
    print(data)
    nEstprincipal = data['EstacionPrincipal'].values.reshape(-1, 1)
    nEstfaltante = data['EstacionFaltante'].values.reshape(-1, 1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(nEstprincipal, nEstfaltante)
    nEstfaltante_pred = linear_regressor.predict(nEstprincipal)
    # y= mx+c
    m = linear_regressor.coef_[0][0]
    c = linear_regressor.intercept_[0]
    label = r'$nEstFaltante = %0.4f*EstPrincipal %+0.4f$' % (m, c)
    print(label)
    fig = plt.figure(figsize=(14, 14))
    plt.scatter(data['EstacionPrincipal'], data['EstacionFaltante'], label="Datos Iniciales")
    plt.plot(nEstprincipal, nEstfaltante_pred, color='red', label=label)
    plt.xlabel("Estacion Principal")
    plt.ylabel("Estacion Faltante")
    plt.legend()
    plt.grid()
    plt.show()
"""--------------------------------------------------------------------------------------------------------------"""

"""--------------------------FUNCION PARA CERRAR EL PROGRAMA----------------------------------------------"""
def close():
    mywindow.destroy()


"""--------------------------------------------------------------------------------------------------------------"""
"""--------------------------CREACION DE VENTANA PRINCIPAL interfaz grafica O INICIAL----------------------------------------------"""
mywindow = Tk()
mywindow.geometry("650x490")
mywindow.title("RMULGAL")
mywindow.resizable(False, False)
mywindow.config(background="black") ##213141 color azulado
"""--------------------------------------------------------------------------------------------------------------"""

"""--------------------------CREACION DE BARRA SUPERIOR  DESPLEGABLE----------------------------------------------"""
mi_menu= tk.Menu(mywindow)
mi_menu.add_command(label="Inicio",command=fondo_inicial)
mi_doc_menu= tk.Menu(mi_menu)
mi_doc_menu.add_command(label="FERNANDO PAZ ZAGACETA")
mi_menu.add_cascade(label="Docente",menu=mi_doc_menu)
mi_dropdown_menu= tk.Menu(mi_menu)
mi_dropdown_menu.add_command(label="SUSAN MELIZA SUPO ZAPANA",command=fondo_negro)
mi_dropdown_menu.add_command(label="KELVIN ELVIO SURCO PAUCCAR",command=fondo_azul)
mi_dropdown_menu.add_command(label="JUAN CARLOS TAMO TACUSI",command=fondo_rojo)
mi_dropdown_menu.add_command(label="YENNY LIZBET VALENZUELA AZURIN",command=fondo_morado)
mi_dropdown_menu.add_command(label="AHIRTHON YURDE VARGAS CURSE",command=fondo_agua)
mi_dropdown_menu.add_command(label="JHAIR GONZALO VENERO LOVATON",command=fondo_celeste,)
mi_menu.add_cascade(label="Integrantes",menu=mi_dropdown_menu)
mywindow.config(menu=mi_menu)
main_title = Label(text="Regresión  |  LINEAL   ", font=("Cambria", 14,"bold"), bg="#D7DBD7", fg="black", width="500",
                   height="2")
main_title.pack()
"""--------------------------------------------------------------------------------------------------------------"""

"""-------------------------- TEXTO DE PRESENTACIÓN INICIAL----------------------------------------------"""
username_label = Label(text="RMULGAL", fg= "white",bg="black", height="1",font=("Courier",20))
username_label.place(x=260, y=90)
password_label = Label(text="REMULGAL es un programa que nos ayuda a generar\n re"
                            "gresiones lineales para el calculo de valores inexistentes\n"
                            "entre dos estaciones, a través del método de los minimos cuadrados\n de una recta de regresion"
                            " lineal del tipo\n\n"
                            " y=a+bx ", fg= "white",bg="black",font=("Verdana",10,'italic'))
password_label.place(x=100, y=130)
fullname_label = Label(text="FUNCIONES DE RMULGA\n"
                            "\n"
                            "| Calcula la regresion lineal de gran cantidad de datos |\n"
                            "| Genera la ecuacion de la recta de primer grado |\n"
                            "| Grafica los resultados para una mejor interpretación de resultados |\n"
                            "| Exporta los resultados a un pdf para su uso |", fg= "white",bg="black",font=("Verdana",10,'italic'))
fullname_label.place(x=100, y=240)
"""--------------------------------------------------------------------------------------------------------------"""

"""----------------------------BOTONES PARA EJECUTAR EL PROGRAMA---------------------------------------"""
submit_btn = Button(mywindow, text="GRÁFICA", width="27",font=("Cambria", 10,"bold"), height="1", command=calculo, bg="yellow", fg= "#213141")
submit_btn.place(x=28, y=400)
submit_btn = Button(mywindow, text="ECUACIÓN DE LA RECTA",font=("Cambria", 10,"bold"), width="27", height="1", command=ecuacion, bg="blue", fg= "white")
submit_btn.place(x=405, y=400)
submit_btn = Button(mywindow, text="CODIGO FUENTE PYTHON",font=("Cambria", 10,"bold"), width="27", height="1", command=codigo, bg="green", fg= "white")
submit_btn.place(x=405, y=440)
submit_btn = Button(mywindow, text="EXPORTAR DATOS PDF",font=("Cambria", 10,"bold"), width="27", height="1", command=send_data, bg="#CC00BE", fg= "white")
submit_btn.place(x=28, y=440)
submit_btn = Button(mywindow, text="EXIT", width="5", height="1", command=close, bg="red",fg= "white",font=("Verdana",30,"bold"))
submit_btn.place(x=255, y=400)
"""--------------------------------------------------------------------------------------------------------------"""

"""--------------------------decoracion izquierd----------------------------------------------"""
submit_btn = Button(mywindow, text="", width="1", height="18", bg="black", fg= "#0000A0")
submit_btn.place(x=22, y=80)
submit_btn = Button(mywindow, text="", width="1", height="18", bg="#393A39", fg= "#0000A0")
submit_btn.place(x=30, y=80)
submit_btn = Button(mywindow, text="", width="1", height="18",  bg="#D7DBD7", fg= "#0000A0")
submit_btn.place(x=0, y=0)
submit_btn = Button(mywindow, text="", width="1", height="18",  bg="#393A39", fg= "#0000A0")
submit_btn.place(x=8, y=0)
submit_btn = Button(mywindow, text="", width="1", height="18", bg="black", fg= "#0000A0")
submit_btn.place(x=0, y=250)
submit_btn = Button(mywindow, text="", width="1", height="18", bg="#393A39", fg= "#0000A0")
submit_btn.place(x=8, y=250)
"""--------------------------------------------------------------------------------------------------------------"""

"""--------------------------decoracion DERECHA----------------------------------------------"""
submit_btn = Button(mywindow, text="", width="1", height="18", bg="black", fg= "#0000A0")
submit_btn.place(x=620, y=80)
submit_btn = Button(mywindow, text="", width="1", height="18", bg="#393A39", fg= "#0000A0")
submit_btn.place(x=610, y=80)
submit_btn = Button(mywindow, text="", width="1", height="18",  bg="#D7DBD7", fg= "#0000A0")
submit_btn.place(x=640, y=0)
submit_btn = Button(mywindow, text="", width="1", height="18",  bg="#393A39", fg= "#0000A0")
submit_btn.place(x=630, y=0)
submit_btn = Button(mywindow, text="", width="1", height="18",  bg="black", fg= "#0000A0")
submit_btn.place(x=640, y=250)
submit_btn = Button(mywindow, text="", width="1", height="18",  bg="#393A39", fg= "#0000A0")
submit_btn.place(x=630, y=250)
"""--------------------------------------------------------------------------------------------------------------"""

"""--------------------------decoracion INTERMEDIA----------------------------------------------"""
submit_btn = Button(mywindow, text="", width="85", height="1", bg="#D7DBD7", fg= "#DB0300")
submit_btn.place(x=25, y=55)
submit_btn = Button(mywindow, text="", width="85", height="1",  bg="#393A39", fg= "#DB0300")
submit_btn.place(x=25, y=50)
submit_btn = Button(mywindow, text="", width="85", height="1",  bg="#D7DBD7", fg= "#DB0300")
submit_btn.place(x=25, y=350)
submit_btn = Button(mywindow, text="", width="85", height="1",  bg="#393A39", fg= "#DB0300")
submit_btn.place(x=25, y=355)

mywindow.mainloop()
"""--------------------------------------------------------------------------------------------------------------"""





