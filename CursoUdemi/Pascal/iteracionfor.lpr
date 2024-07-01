program iteracionfor;

var intentos: byte;
var numeroSecreto: byte;
var numeroUsuario: byte;


begin

  numeroSecreto:= 5;

  for intentos:= 1 to 3 do begin
    write('Adivina el numero: ');
    readln(numeroUsuario);

    if numeroUsuario=numeroSecreto then begin

       writeln('GANASTE');
       break;
    end;
  end;

  readln;
end.

