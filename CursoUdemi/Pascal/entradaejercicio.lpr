program entradaejercicio;

var nombre: string;
    nombreDos: string;
    edad: byte;
    edadDos: byte;
begin
  write('Escribe tu nombre: ');
  readln(nombre);
  write(nombre + ' Escribe tu edad: ');
  readln(edad);
  write('Usuario 2 escribe el nombre de tu pariente: ');
  readln(nombreDos);
  write(nombreDos + ' Escribe tu edad: ');
  readln(edadDos);
  write('Tu nombre es ' + nombre +' y tu edad ',edad,' el nombre de tu pariente es '+ nombreDos + ' y su edad ',edadDos);
  readln;
end.

