program ejercicioifdos;

const PI = 3.1415;
var opcion:char;
var largo: real;
var ancho: real;
var radio: real;
var base: real;
var lado: real;
var altura: real;



begin
  writeln('1) Calcular perimetro de rectangulo');
  writeln('2) Calcular area de rectangulo');
  writeln('3) Calcular perimetro de circunferencia');
  writeln('4) Calcular area de circunferencia');
  writeln('5) Calcular perimetro de triangulo');
  writeln('6) Calcular area de triangulo');
  writeln('0) Salir');
  writeln;
  write('Opcion: ');
  readln(opcion);

  if opcion = '1' then begin
     write('Escribeme el largo del rectangulo: ');
     readln(largo);
     write('Escribeme el ancho del rectangulo: ');
     readln(ancho);

     writeln('Perimetro =',largo*2+ancho*2:4:2);

  end else if opcion = '2' then begin
     write('Escribeme el largo del rectangulo: ');
     readln(largo);
     write('Escribeme el ancho del rectangulo: ');
     readln(ancho);

     writeln('Area =',largo*ancho:4:2);

  end else if opcion = '3' then begin
      write('Escribeme el radio de la circunferencia: ');
      readln(radio);

      writeln('Perimetro =',(radio*2)*PI:4:2);
  end else if opcion = '4' then begin
      write('Escribeme el area de la circunferencia: ');
      readln(radio);

      writeln('Area =',(radio*radio)*PI:4:2);
  end else if opcion = '5' then begin
      write('Escribeme la base del triangulo: ');
      readln(base);
      write('Escribeme el lado del triangulo: ');
      readln(lado);

      writeln('Perimetro =',lado*2+base:4:2);
  end else if opcion = '6' then begin
      write('Escribeme la base del triangulo: ');
      readln(base);
      write('Escribeme la altura del triangulo: ');
      readln(altura);

      writeln('Area =',(base*altura)/2:4:2);
  end else if opcion = '0' then begin
     writeln('Saliendo...');
  end else begin
     writeln('ERROR: Opcion introducida no valida');
  end;

  writeln('Te quiero puedes darle a enter para salir...');
  readln;
end.

