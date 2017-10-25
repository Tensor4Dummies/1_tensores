#TENSORES
Los tensores son los datos de Tensorflow, todos tienen tres características principales. Y además los podemos dividir en tipos.

## Características

### Rango (Rank) 
Es la dimensión del tensor, a partir de ella podemos hablar de:
 1. Escalares son tensores 0 dimensionales 
 2. Vectores o listas [] son tensores 1 dimensionales 
 3. Matrices [ [],[] ] son tensores 2 dimensionales 
 4. Matrices n dimensionales son tensores n dimensionales
###	Forma (shape) 
Es el número de elementos en cada dimensión
###	Tipo de datos (Data type) 
Es el tipo de datos de cada elemento del tensor

### Ejemplo
En la siguiente tabla se pueden ver como varían las características según el rango
<table>
	<tr>
		<th>Tensor</th>
		<th>Rango</th>
		<th>Forma</th>
		<th>Tipo de dato</th>
	</tr>
	<tr>
		<td>4</td>
		<td>0</td>
		<td>[]</td>
		<td>Int</td>
	</tr>
	<tr>
		<td>[1, 2, 3]</td>
		<td>1</td>
		<td>[3]</td>
		<td>Int</td>
	</tr>
	<tr>
		<td>[[1, 2, 3], [3, 4, 5]]</td>
		<td>2</td>
		<td>[3,2]</td>
		<td>Int</td>
	</tr>
	<tr>
		<td>[[[1], [2]], [[3], [4]]]</td>
		<td>3</td>
		<td>[2, 2, 1]</td>
		<td>Int</td>
	</tr>
</table>

##Tipos de tensores
### Constantes
Se caracterizan porque nunca cambian su valor en distintas ejecuciones.
Para crear una variable:
*constante1 = tf.constant(3.5, dtype=tf.float32, name="cte1")*
donde *3.5* es el valor que le queremos dar, *dtype* el tipo y *name* el nombre que queremos que tenga para la representación en el grafo.
Tras ejecutar el archivo constantes.py obtenemos:

  *Información: Tensor("cte1:0", shape=(), dtype=float32), valor 3.5*
   *Información: Tensor("cte2:0", shape=(), dtype=float32), valor 5.5*
   *Suma 0 de constantes: 3.5+5.5=9.0*
   *Suma 1 de constantes: 3.5+5.5=9.0*
   *Suma 2 de constantes: 3.5+5.5=9.0*
   *Suma 3 de constantes: 3.5+5.5=9.0*
   *Suma 4 de constantes: 3.5+5.5=9.0*
   *Suma 5 de constantes: 3.5+5.5=9.0*
   *Suma 6 de constantes: 3.5+5.5=9.0*
   *Suma 7 de constantes: 3.5+5.5=9.0*
   *Suma 8 de constantes: 3.5+5.5=9.0*
   *Suma 9 de constantes: 3.5+5.5=9.0*

Por lo que vemos que por muchas veces que ejecutemos una constante, su valor no cambia ni se tiene que asignar.

### Placeholders
Se caracterizan porque se les asigna un valor en cada ejecución.
Para crear un placeholder:
*ph1 = tf.placeholder(tf.float32, shape=(None), name="ph1")*
donde *tf.float32* es el tipo, *shape* el tamaño que queremos que tenga y *name* el nombre que queremos que tenga para la representación en el grafo.
Tras ejecutar el archivo placeholder.py obtenemos:

*Suma de placeholders: 3.5+5.5=9.0
*Suma 0 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]*
*Suma 1 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]*
*Suma 2 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]*
*Suma 3 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]*
*Suma 4 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]*
*Suma 5 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]*
*Suma 6 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]*
*Suma 7 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]*
*Suma 8 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]*
*Suma 9 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]*

Podemos ver que los datos no varían ya que estamos introduciendo en todas las ejecuciones los mismos datos.

### Variables
Se caracterizan porque se les reasigna un valor en cada ejecución.
Para crear un placeholder:
*v1 = tf.Variable([3.5], dtype=tf.float32, name="v1")*
donde *3.5* es el valor que le queremos dar, *dtype* el tipo y *name* el nombre que queremos que tenga para la representación en el grafo.
Tras ejecutar el archivo variables.py obtenemos:

*Información: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [ 3.5]*
*Información 0: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [ 3.]*
*Información 1: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [ 2.5]*
*Información 2: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [ 2.]*
*Información 3: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [ 1.5]*
*Información 4: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [ 1.]*
*Información 5: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [ 0.5]*
*Información 6: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [ 0.]*
*Información 7: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [-0.5]*
*Información 8: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [-1.]*
*Información 9: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [-1.5]*

En este caso vemos que su valor disminuye 0.5 en cada ejecución, ya que estamos utilizando el descenso de gradiente para esa variable.