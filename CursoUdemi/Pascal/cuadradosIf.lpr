program cuadradosIf;

var lado,area,perimetro: integer;

begin
  write ('Ingresa el lado del cuadrado: ');
  readln(lado);

  if lado = 0 then begin
     write('El lado no puede ser 0');
  end else if lado < 0 then begin
     write('El lado no puede ser negativo');
  end else begin
      write('Perimetro = ',lado*4,' Area = ',lado*lado);
  end;
  readln;
end.

