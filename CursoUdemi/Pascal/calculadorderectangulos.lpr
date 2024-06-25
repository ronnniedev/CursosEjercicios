(* Este programa calcula el area y perimetro de un rectangulo, mostrandolos
al final *)

program calculadorderectangulos;

{Aqui declaro las variables a usar.}

var largo: real;
var ancho: real;
var perimetro: real;
var area: real;

begin
  writeln('Escribeme el largo: ');  //Calculo del largo
  readln(largo);
  writeln('Escribeme el ancho: ');
  readln(ancho);

  while  ancho >= largo  do
   begin
      writeln('El ancho no puede ser mayor que el largo introducelo de nuevo: ');
      readln(ancho);
   end;

   // Se realizan los calculos
   perimetro:= largo*2+ ancho*2;
   area:= largo*ancho;

   writeln('El perimetro de este rectangulo es: ',perimetro:4:2);
   writeln('El area de este rectangulo es: ',area:4:2);
   readln;
end.

