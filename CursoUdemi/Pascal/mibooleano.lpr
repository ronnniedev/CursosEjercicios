program mibooleano;

var condicion: boolean;
    edad: byte;

begin
  write('Edad= ');
  readln(edad);
  condicion:= (edad<=30) or (edad>=40);

  if condicion then
     writeln('Estas en una linda etapa de tu vida')
  else
      writeln('Estas en un momento complicado');

  readln;
end.

