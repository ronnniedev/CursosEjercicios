program calculadorderectangulos;

var largo: integer;
var ancho: integer;
var perimetro: integer;
var area: integer;

begin
  writeln('Escribeme el largo: ');
  readln(largo);
  writeln('Escribeme el ancho: ');
  readln(ancho);

  while  ancho >= largo  do
   begin
      writeln('El ancho no puede ser mayor que el largo introducelo de nuevo: ');
      readln(ancho);
   end;

   perimetro:= largo*2+ ancho*2;
   area:= largo*ancho;

   writeln('El perimetro de este rectangulo es: ',perimetro);
   writeln('El area de este rectangulo es: ',area);
   readln;
end.

