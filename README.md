<h1>TENSORES</h1>
<p>Los tensores son los datos de Tensorflow, todos tienen tres caracter�sticas principales. Y adem�s los podemos dividir en tipos.</p>

<h2>Caracter�sticas</h2>
<h3>Rango (Rank)</h3> 
<p>Es la dimensi�n del tensor, a partir de ella podemos hablar de:
<ul>
	<li>Escalares son tensores 0 dimensionales </li>
	<li>Vectores o listas [] son tensores 1 dimensionales </li>
	<li>Matrices [ [],[] ] son tensores 2 dimensionales </li>
	<li>Matrices n dimensionales son tensores n dimensionales</li>
</ul></p>
<h3>Forma (shape)</h3> 
<p>Es el n�mero de elementos en cada dimensi�n</p>
<h3>Tipo de datos (Data type) </h3>
<p>Es el tipo de datos de cada elemento del tensor</p>
<h3>Ejemplo</h3>
<p>En la siguiente tabla se pueden ver como var�an las caracter�sticas seg�n el rango</p>
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

<h2>Tipos de tensores</h2>

<h3>Constantes </h3>
<p>Se caracterizan porque nunca cambian su valor en distintas ejecuciones. Para crear una variable:</p>
<p><i>constante1 = tf.constant(3.5, dtype=tf.float32, name="cte1")</i></p>
<p>donde 3.5 es el valor que le queremos dar, dtype el tipo y name el nombre que queremos que tenga para la representaci�n en el grafo.</p>
<p>Tras ejecutar el archivo constantes.py obtenemos:</p>
<p><i>Informaci�n: Tensor("cte1:0", shape=(), dtype=float32), valor 3.5</br>
Informaci�n: Tensor("cte2:0", shape=(), dtype=float32), valor 5.5</br>
Suma 0 de constantes: 3.5+5.5=9.0</br>
Suma 1 de constantes: 3.5+5.5=9.0</br>
Suma 2 de constantes: 3.5+5.5=9.0</br>
Suma 3 de constantes: 3.5+5.5=9.0</br>
Suma 4 de constantes: 3.5+5.5=9.0</br>
Suma 5 de constantes: 3.5+5.5=9.0</br>
Suma 6 de constantes: 3.5+5.5=9.0</br>
Suma 7 de constantes: 3.5+5.5=9.0</br>
Suma 8 de constantes: 3.5+5.5=9.0</br>
Suma 9 de constantes: 3.5+5.5=9.0</i></p>
<p>Por lo que vemos que por muchas veces que ejecutemos una constante, su valor no cambia ni se tiene que asignar.</p>

<h3>Placeholders</h3>
<p>Se caracterizan porque se les asigna un valor en cada ejecuci�n. Para crear un placeholder:</p>
<p><i>ph1 = tf.placeholder(tf.float32, shape=(None), name="ph1")</i></p>
<p>donde tf.float32 es el tipo, shape el tama�o que queremos que tenga y name el nombre que queremos que tenga para la representaci�n en el grafo.</p>
<p>Tras ejecutar el archivo placeholder.py obtenemos:</p>
<p><i>Suma de placeholders: 3.5+5.5=9.0
Suma 0 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]</br>
Suma 1 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]</br>
Suma 2 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]</br>
Suma 3 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]</br>
Suma 4 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]</br>
Suma 5 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]</br>
Suma 6 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]</br>
Suma 7 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]</br>
Suma 8 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]</br>
Suma 9 de placeholders: [1, 2, 10]+[4, 2, 10]=[  5.   4.  20.]</i></p>
<p>Podemos ver que los datos no var�an ya que estamos introduciendo en todas las ejecuciones los mismos datos.</p>

<h3>Variables</h3>
<p>Se caracterizan porque se les reasigna un valor en cada ejecuci�n. Para crear un placeholder:</p>
<p><i>v1 = tf.Variable([3.5], dtype=tf.float32, name="v1")</i></p>
<p>donde 3.5 es el valor que le queremos dar, dtype el tipo y name el nombre que queremos que tenga para la representaci�n en el grafo.<p>
<p>Tras ejecutar el archivo variables.py obtenemos:</p>
<p><i>Informaci�n: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [ 3.5]</br>
Informaci�n 0: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [ 3.]</br>
Informaci�n 1: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [ 2.5]</br>
Informaci�n 2: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [ 2.]</br>
Informaci�n 3: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [ 1.5]</br>
Informaci�n 4: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [ 1.]</br>
Informaci�n 5: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [ 0.5]</br>
Informaci�n 6: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [ 0.]</br>
Informaci�n 7: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [-0.5]</br>
Informaci�n 8: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [-1.]</br>
Informaci�n 9: <tf.Variable 'v1:0' shape=(1,) dtype=float32_ref>, valor [-1.5]</i></p>
<p>En este caso vemos que su valor disminuye 0.5 en cada ejecuci�n, ya que estamos utilizando el descenso de gradiente para esa variable.</p>