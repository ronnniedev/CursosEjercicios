program desglosadordepalabras;

var letraUno: char;
var letraDos: char;
var letraTres: char;
var letraCuatro: char;

begin

  write('Ingresa una palabra de 4 letras: ');

  read(letraUno,letraDos,letraTres,letraCuatro);


  readln;
  writeln(letraUno+#13#10+letraDos+#13#10+letraTres+#13#10+letraCuatro);

  readln;

end.

