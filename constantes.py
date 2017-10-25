#IMPORTACIÓN DE LIBRERIAS
import tensorflow as tf 
import os

#QUITAR LOS MENSAJES DE AVISO
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#CREAR EL MODELO
#Constantes nunca cambian su valor
constante1 = tf.constant(3.5, dtype=tf.float32, name="cte1")
constante2 = tf.constant(5.5, dtype=tf.float32, name="cte2")
#Operaciones
suma_cte = tf.add(constante1,constante2, name="suma_cte")

#INICIAR SESIÓN
with tf.Session() as sesion:
    
    #Información de las constantes
    print("Información: {}, valor {}".format(constante1, sesion.run(constante1)))
    print("Información: {}, valor {}".format(constante2, sesion.run(constante2)))

    #Ejecución operaciones
    for i in range(10):
        resultado = sesion.run(suma_cte)
        print("Suma {} de constantes: {}+{}={}".format(i,sesion.run(constante1), sesion.run(constante2), resultado))
    