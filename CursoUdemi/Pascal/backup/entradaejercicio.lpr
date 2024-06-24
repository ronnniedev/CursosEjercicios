program entradaejercicio;

var nombre: string;
    edad: byte;
    nombreDos: string;
    edadDos: byte;
begin
  write('Escribe tu nombre: ');
  readln(nombre);
  write('Escribe tu edad: ');
  readln(edad);
  write('Escribe el nombre de tu pariente: ');
  readln(nombreDos);
  write('Escribe la edad de tu pariente: ');
  readln(edadDos);
  write('Tu nombre es ' + nombre +' y tu edad ',edad,' el nombre de tu pariente es '+ nombreDos + ' y su edad ',edadDos);
  readln;
end.

