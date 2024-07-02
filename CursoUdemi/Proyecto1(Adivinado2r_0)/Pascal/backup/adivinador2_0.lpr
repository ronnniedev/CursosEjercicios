program adivinador2_0;

const MAX_INTENTOS= 10;
var numeroSecreto: byte;
var numeroUsuario: byte;
var i: byte;
var adivino : boolean;


begin
  randomize; // llamamos a la funcion randomize, como importar
  numeroSecreto:= random(100)+1;

  writeln('Adivinador 2.0 - Dispones de ' ,MAX_INTENTOS, ' intentos para adivinar');

  for i:= 1 to MAX_INTENTOS do begin
    write ('Intento ',i,':');
    readln(numeroUsuario);

    adivino:= numeroUsuario=numeroSecreto;

    if (numeroUsuario= numeroSecreto) then begin // si acertamos escribimos ganaste
      writeln('GANASTE');
      adivino:= true;
      break;
    end;

    if (numeroUsuario < numeroSecreto) and (i < MAX_INTENTOS) then //asi hacemos que no salga en el ultimo intento este mensaje
    begin
      writeln('El numero a adivinar es mayor');
    end
    else if i < MAX_INTENTOS then
    begin
      writeln('El numero a adivinar es menor');
    end;
  end;

  if not adivino then begin
     writeln('Perdiste');
  end;

  readln();

end.

