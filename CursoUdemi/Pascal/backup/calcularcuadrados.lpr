program calcularcuadrados;
  var lado: integer;
  var area: integer;
  var perimetro: integer;

begin
  writeln('Escribe cuanto mide el lado');
  readln(lado);
  perimetro:= lado*4;
  area:= lado*lado;
  writeln('El perimetro del cuadrado es ',perimetro);
  writeln('El area del lado es ',area);
  readln;
end.

