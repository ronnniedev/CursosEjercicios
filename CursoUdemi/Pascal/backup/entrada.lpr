program entrada;

var nombre: string;
    edad: byte;

begin
   write('Escribe tu nombre: ');
   readln (nombre);
   write('Escribe tu edad: ');
   readln(edad);
   write('Hola '  + nombre + ',tienes ',edad,' aNos');
   write(' aNos.');
   readln;
end.

