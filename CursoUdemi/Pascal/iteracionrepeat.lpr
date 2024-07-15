program iteracionrepeat;

var numero: byte;

begin


  writeln('While');
  readln(numero);

  writeln('Repeat');
  repeat
  readln(numero);
  until numero = 10;


end.

