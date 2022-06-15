# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 16:06:35 2022

@author: Manuel
"""

import math
import tkinter as tk
#Popup windows
from tkinter.messagebox import showinfo


##Crear una instancia de Tkinter
ventana = tk.Tk()
ventana.geometry ("1050x900")

#Configurar color de fondo
ventana.config(bg="yellow")

#Configuracion de la primera fila y sus atributos
variable_1 = tk.Label(ventana, text="Distancia Focal (mm)=", bg="yellow", fg="black", font = "Arial 13")
variable_1.grid (row = 1, column = 0, pady = 20)

cuadro_1 = tk.Entry(ventana, font = "Arial 13", justify = "left")
cuadro_1.grid (row = 1, column = 1, pady = 20)

variable_2 = tk.Label(ventana, text="Ancho de imagen (pixel) =", bg="yellow", fg="black")
variable_2.grid (row = 1, column = 2, pady = 20)

cuadro_2 = tk.Entry(ventana, font = "Arial 13", justify = "left")
cuadro_2.grid (row = 1, column = 3, pady = 20)

variable_3 = tk.Label(ventana, text="Alto de Imagen (pixel) =", bg="yellow", fg="black")
variable_3.grid (row = 1, column = 4)

cuadro_3 = tk.Entry(ventana, font = "Arial 13", justify = "left")
cuadro_3.grid (row = 1, column = 5, pady = 20)

#Configuracion de segunda fila y sus atributos
variable_4 = tk.Label(ventana, text="Ancho de sensor (mm) =", bg="yellow", fg="black", font = "Arial 13")
variable_4.grid (row = 2, column = 0, pady = 20)

cuadro_4 = tk.Entry(ventana, font = "Arial 13", justify = "left")
cuadro_4.grid (row = 2, column = 1, pady = 20)

variable_5 = tk.Label(ventana, text="Alto del sensor (mm) =", bg="yellow", fg="black")
variable_5.grid (row = 2, column = 2, pady = 20)

cuadro_5 = tk.Entry(ventana, font = "Arial 13", justify = "left")
cuadro_5.grid (row = 2, column = 3, pady = 20)

variable_6 = tk.Label(ventana, text=" Velocidad de Vuelo (m/s) =", bg="yellow", fg="black")
variable_6.grid (row = 2, column = 4, pady = 20)

cuadro_6 = tk.Entry(ventana, font = "Arial 12", justify = "left")
cuadro_6.grid (row = 2, column = 5, pady = 20)

#Configuracion de la tercera fila y sus atributos
variable_7 = tk.Label(ventana, text="Altura de vuelo (m)=", bg="yellow", fg="black", font = "Arial 13")
variable_7.grid (row = 3, column = 0, pady = 20)

cuadro_7 = tk.Entry(ventana, font = "Arial 13", justify = "left")
cuadro_7.grid (row = 3, column = 1, pady = 20)

variable_8 = tk.Label(ventana, text="Solape Longitudinal (%)=", bg="yellow", fg="black")
variable_8.grid (row = 3, column = 2, pady = 20)

cuadro_8 = tk.Entry(ventana, font = "Arial 13", justify = "left")
cuadro_8.grid (row = 3, column = 3, pady = 20)

variable_9 = tk.Label(ventana, text="Solape Transversal (%) =", bg="yellow", fg="black")
variable_9.grid (row = 3, column = 4, pady = 20)

cuadro_9 = tk.Entry(ventana, font = "Arial 12", justify = "left")
cuadro_9.grid (row = 3, column = 5)

#Configuracion de la cuarta fila y sus atributos
variable_10 = tk.Label(ventana, text="Largo de parcela (m)=", bg="yellow", fg="black", font = "Arial 13")
variable_10.grid (row = 4, column = 0, pady = 20)

cuadro_10 = tk.Entry(ventana, font = "Arial 13", justify = "left")
cuadro_10.grid (row = 4, column = 1, pady = 20)

variable_11 = tk.Label(ventana, text="Ancho de parcela (m)=", bg ="yellow", fg = "black")
variable_11.grid (row = 4, column = 2, pady = 20)

cuadro_11 = tk.Entry(ventana, font = "Arial 13", justify = "left")
cuadro_11.grid (row = 4, column = 3, pady = 20)

#Muestra de resultados
textoResult = tk.Text(ventana)
textoResult.grid(row = 12, column = 0, columnspan = 12)

#Creación de una sola función para que no sea tan largo el codigo, no se crea funciones para cada calculo.
def parametros():
    textoResult.delete(1.0, tk.END)
    dist_focal = float(cuadro_1.get())
    ancho_imagen = float(cuadro_2.get())
    alto_imagen = float(cuadro_3.get())
    ancho_sensor = float(cuadro_4.get())
    alto_sensor = float(cuadro_5.get())
    RSI = ancho_sensor/ancho_imagen
    velo_vuelo = float(cuadro_6.get())
    alto_vuelo = int(cuadro_7.get())
    slp_long = float(cuadro_8.get())
    slp_trans = float(cuadro_9.get())
    largo_parcela = float(cuadro_10.get())
    ancho_parcela = float(cuadro_11.get())
    
    #Calculo del GSD
    GSD = (((alto_vuelo * 100 ) / (dist_focal)) * RSI)
    textoResult.insert(tk.END, f"GSD = {GSD} cm/pixel\n")
    
    #Calculo de la escala de vuelo
    escala_vuelo = 1/((dist_focal / 1000) / alto_vuelo)
    textoResult.insert(tk.END, f"Escala de vuelo = {escala_vuelo}\n")
    
    #Calculo del ancho de la imagen
    anch_img = (ancho_sensor*escala_vuelo)/1000
    textoResult.insert(tk.END, f"Ancho de la Imagen Sobre el Terreno = {anch_img} m\n\n")
    
    #Calculo de la altura de la imagen
    alt_img = (alto_sensor * escala_vuelo)/1000
    textoResult.insert(tk.END, f"Alto de la Imagen Sobre el Terreno = {alt_img} m\n")
    
    #Calculo de la base aérea
    base_aero = (((ancho_imagen * GSD ) / 100) * (1 - (slp_long / 100)))
    textoResult.insert(tk.END, f"Base Aérea = {base_aero}\n")
    
    #Calculo de la distancia entre vueltas
    dist_vuelt = (((alto_imagen * GSD ) / 100)) * (1- (slp_trans / 100))
    textoResult.insert(tk.END, f"Distancia entre vueltas = {dist_vuelt} m\n\n")
    
    #Calculo del tiempo entre fotos y velocidad de vuelo
    tiempo_fotos = base_aero/velo_vuelo
    vel_vuelo= base_aero/tiempo_fotos
    textoResult.insert(tk.END, f"Tiempo entre fotos = {tiempo_fotos} s\n")
    textoResult.insert(tk.END, f"Velocidad de Vuelo= {vel_vuelo} m/s\n")
    
    #Calculo del número de pasadas
    numero_pases = (ancho_parcela/dist_vuelt)
    textoResult.insert(tk.END, f"Numero de pasadas = {numero_pases}\n\n")
    
    #Calculo del número de fotos por vueltas
    numero_fotos = (largo_parcela/base_aero)+1
    textoResult.insert(tk.END, f"Numero de Fotos por vueltas = {numero_fotos}\n")
    
    #Calculo del número de fotos por pasada
    numero_vuelta = (numero_fotos)*(numero_pases)+1
    textoResult.insert(tk.END, f"Numero de Fotos por Vuelo = {numero_vuelta}\n")
    
    #Calculo de la distancia de vuelo
    dist_vuelo = (numero_pases*largo_parcela)+ancho_parcela
    textoResult.insert(tk.END, f"Distancia de Vuelo = {dist_vuelo} m\n")
    
    #Calculo de la duración del vuelo 
    dura = ((numero_vuelta * tiempo_fotos)/60)
    textoResult.insert(tk.END, f"Duracion del Vuelo = {dura} min")

    popup_showinfo()

#Aparición de una pequeña ventana
def popup_showinfo():
    title = "¡FIN!"
    message ="Ha concluido los cálculos"
    showinfo(title, message)

#Boton de cálculo de parámetros
boton_calculo = tk.Button(text = "Calcular", font= 'Arial 14', command = parametros)
boton_calculo.grid(row = 6, column = 2, columnspan = 2, pady = 20)


#Titulo de la ventana
ventana.title("Parámetros de Vuelo")
#Ejecutar el GUI
ventana.mainloop()