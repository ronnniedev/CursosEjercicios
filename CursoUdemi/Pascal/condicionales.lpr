program condicionales;

var edad: byte;

begin
     write('Ingresa tu edad: ');
     readln(edad);

     if edad <40 then begin
        writeln('Eres muy joven');
        writeln('Todavia tienes mucho que hacer');
     end else begin
          writeln('Eres veterano');
        writeln('Todavia tienes mucho que hacer');
     end;

     readln;
end.

