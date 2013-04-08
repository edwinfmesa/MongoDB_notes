<html>
<title>Bootle with Forms</title>
<body>
Formulario de saludo de nombre
<form action="/my_name" method="POST">
	<input type="text" name="name" />
	<input type="submit" value="Enviar Nombre" />
</form>

%if message:
<h2>Mensaje {{message}}</h2>
%end

%if name:
<h2>Tu nombre es: {{name}}</h2>
%end
</body>
</html>