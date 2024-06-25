(*Calculo de divisiones enteras, dando como resultado el cociente y el resto*)
program divisionentera;

var cantidadManzanas: integer;
var cantidadInfantes: integer;
var cociente: integer;
var resto: integer;

begin
  write('Escribe la cantidad de manzanas: ');
  readln(cantidadManzanas);
  write('Escribe la cantidad de infantes: ');
  readln(cantidadInfantes);

  cociente:= cantidadManzanas DIV cantidadInfantes; // resultado entero de la division
  resto:= cantidadManzanas MOD cantidadInfantes; // modulo de la division

  writeLn('Cociente= ',cociente, ' Resto= ',resto);
  readln;
end.

