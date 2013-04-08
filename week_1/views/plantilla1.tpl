<html>
<title>Bootle with templates</title>
<body>
Hello {{username}}!
%for thing in things:
	<a href="#">{{thing}}</a>
%end
</body>
</html>