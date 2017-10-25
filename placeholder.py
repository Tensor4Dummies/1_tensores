#IMPORTACIÓN DE LIBRERIAS
import tensorflow as tf 
import os

#QUITAR LOS MENSAJES DE AVISO
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#CREAR EL MODELO
#Placeholder se asignan en cada computación
ph1 = tf.placeholder(tf.float32, shape=(None), name="ph1")
ph2 = tf.placeholder(tf.float32, shape=(None), name="ph2")
#Operaciones
suma_ph =tf.add(ph1,ph2,name="suma_ph")

#INICIAR SESIÓN
with tf.Session() as sesion:

    #Ejecución operaciones
    resultado = sesion.run(suma_ph, feed_dict={ph1:3.5, ph2:5.5})
    print("Suma de placeholders: 3.5+5.5={}".format(resultado))

    lista1 = [1, 2, 10]
    lista2 = [4, 2, 10]

    for i in range(10):
        resultado2 = sesion.run(suma_ph, feed_dict={ph1: lista1, ph2:lista2})
        print("Suma {} de placeholders: {}+{}={}".format(i,lista1,lista2,resultado2))