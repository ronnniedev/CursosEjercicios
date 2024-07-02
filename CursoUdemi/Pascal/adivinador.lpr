program adivinador;

var i: byte;
var cantidadIntentos: byte;
var numeroAAdivinar: byte;
var numeroUsuario: byte;
var adivinado: boolean;

begin
     numeroAAdivinar:= 3;
     cantidadIntentos:= 3;
     adivinado := false;

     for i:= cantidadIntentos downto 1 do begin
       write('Te quedan',cantidadIntentos, ' intentos. Intenta adivinar: ');
       readln(numeroUsuario);

       if numeroUsuario=numeroAAdivinar then begin
         writeln('Has acertado');
         adivinado := true;
         break;
       end;

     end;

     if not adivinado then begin
       writeln('Perdiste');
     end;

     readln();
end.

