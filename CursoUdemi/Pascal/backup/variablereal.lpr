program CalculoTriangulos;

 var area: integer;
 var base: integer;
 var altura: integer;

begin
  write('Ingresa la base: ');
  readln(base);

  write('Ingresa la altura: ');
  readln(altura);

  area:= base * altura/2;

  writeln('Area: ',area:4:2);
  //el primer :numero es para los numeros antes de la coma y el segundo : para
  // los decimales
  readln();

end.

