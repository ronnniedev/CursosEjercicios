program constantes;

const IVA = 22;  // esto es para declarar constantes
var valorSinIva: real;
var ivaCalculado: real;
var valorConIva: real;

begin
  write('Ingresa el valor sin IVA: ');
  readln(valorSinIva);

  ivaCalculado:= valorSinIva*iva/100;
  valorConIva:= valorSinIva+ivaCalculado;

  write('Precio final= ',valorConIva:4:2);
  readln;

end.

