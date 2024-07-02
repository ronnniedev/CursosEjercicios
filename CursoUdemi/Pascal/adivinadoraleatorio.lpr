program adivinadoraleatorio;

const MAX_INTENTOS= 10;
var numeroSecreto: byte;
var numeroUsuario: byte;
var i: byte;
var adivino : boolean;


begin
  randomize; // llamamos a la funcion randomize, como importar
  numeroSecreto:= random(100)+1;

  for i:= MAX_INTENTOS downto 1 do begin
    write ('Tienes ',i, ' intentos: ');
    readln(numeroUsuario);

    adivino:= numeroUsuario=numeroSecreto;

    if (numeroUsuario= numeroSecreto) then begin
      writeln('GANASTE');
      adivino:= true;
      break;
    end;
  end;

  if not adivino then begin
     writeln('Perdiste');
  end;
  readln();
end.

