program ejercicioif;

var opcion: char;
var largo: real;
var ancho: real;


begin
  writeln('Selecciona una opcion: ');
  writeln;
  writeln('1) Calcular perimetro');
  writeln('2) Calcular area');
  writeln('0) Salir');
  writeln;
  write('Opcion: ');
  readln(opcion);

  if opcion = '1' then begin
    write('Ingresa el largo = ');
    readln(largo);
    write('Ingresa el ancho = ');
    readln(ancho);

    write('El perimetro del rectangulo es ',largo*2+ancho*2:4:2);

  end else if opcion = '2' then begin
    write('Ingresa el largo = ');
    readln(largo);
    write('Ingresa el ancho = ');
    readln(ancho);
    write('El area del rectangulo es ',ancho*largo:4:2);

  end else if opcion = '0' then begin
      writeln('Gracias por participar');
  end else begin
      writeln('ERROR: La opcion que el usuario ingreso no es valida');
  end;

  writeln('Presiona ENTER para salir...');
  readln;
end.

