program calculoCirculos;
 var radio: real;

begin
  write('Ingresa el radio: ');
  readln(radio);

  writeln('Perimetro: ',3.14*radio*2:4:2, 'Area: ', 3.14*radio*radio:4:2);
  //el primer :numero es para los numeros antes de la coma y el segundo : para
  // los decimales
  readln();

end.

