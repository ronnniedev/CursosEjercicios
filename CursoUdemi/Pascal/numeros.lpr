program numeros;

var numero1:real;
var numero2:real;
var suma:real;
var promedio:real;
var resta:real;
var multiplicacion:real;
var division: real;

begin
  write('Ingresa un valor: ');
  readln(numero1);
  write('Ingresa otro valor: ');
  readln(numero2);

  suma := numero1+numero2;
  resta := numero1 - numero2;
  multiplicacion := numero1*numero2;
  division := numero1 / numero2;
  promedio := (numero1 + numero2)/2;

  write('Suma= ',suma:4:2);
  write('Resta= ',resta:4:2);
  write('Multiplicacion= ',multiplicacion:4:2);
  write('Division= ',division:4:2);
  write('Promedio= ',promedio:4:2);
  readln();

end.

