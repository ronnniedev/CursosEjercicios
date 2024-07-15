program adivinador3_0;

uses math;

var inicial: integer;
var final: integer;
var intentos: integer;
var numeroPosible: integer;
var i: integer;
var opcion: char;
var adivino: boolean;


begin
   writeln('Intentare adivinar un numero que tu elijas.');
   writeln('Cuando indique un numero tu deberas indicar:');
   writeln('= si acierto el numero que tu quieres que adivine');
   writeln('> si el numero que tu quieres que adivine es mayor que el que mostre');
   writeln('< si el numero que tu quieres que adivine es menor que el que mostre');



  writeln('Escribeme el numero inicial');
  readln(inicial);
  writeln('Escribeme el numero final');
  readln(final);
  intentos:= round(log2(final-inicial)+1);

  if inicial < final then begin
    writeln('Adivinare tu numero en no mas de ',intentos,'.');
    writeln('Presiona ENTER cuando quieras empezar...');
    readln();

  adivino:= false;
    for i:= 1 to intentos do begin
      numeroPosible := ((final-inicial) div 2) + inicial;
      writeln('Es ', numeroPosible , ' tu numero?');
      readln(opcion);

      case opcion of
           '=': begin
                adivino:= true;
                break;
           end;
           '>': begin
                inicial := numeroPosible +1;
           end;
           '<': begin
                final := numeroPosible -1;
           end;
      end;

      if (inicial > final) or (final < inicial) then begin
        writeln('Estas haciendo trampa!!!');
        break;
      end;
    end;
  end;

  if adivino = true then begin
    writeln('Gane!!! Ponmelo mas dificil');
  end else if i=intentos then begin
    writeln('GANASTE!!! No pude encontrar el numero.');
  end;
  readln();

end.

