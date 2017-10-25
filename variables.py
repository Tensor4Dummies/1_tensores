#IMPORTACIÓN DE LIBRERIAS
import tensorflow as tf 
import os

#QUITAR LOS MENSAJES DE AVISO
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#CREAR EL MODELO
#Variables se computan constantemente 
v1 = tf.Variable([3.5], dtype=tf.float32, name="v1")
#Operaciones
#Restar v1-0.5 en cada ejecución
resta = tf.train.GradientDescentOptimizer(0.5).minimize(v1)

#INICIAR SESIÓN
with tf.Session() as sesion:

    #Iniciar variables
    init = tf.global_variables_initializer()
    sesion.run(init)

    #Información de las constantes
    print("Información: {}, valor {}".format(v1, sesion.run(v1)))

    #Ejecución operaciones
    for i in range(10):
        sesion.run(resta)
        #Información de las constantes actualizada
        print("Información {}: {}, valor {}".format(i, v1, sesion.run(v1)))
