program ejerciciocase;

var opcion: byte;

begin
  readln(opcion);

  case opcion of
  1: begin
    writeln('Es muy pequeño');
    end;
  5: begin
    writeln('Es mediano');
    end;
  6,7,8: begin
    writeln('Me gusta ese valor');
    end;
  50: begin
    writeln('ES ENORME');
    end;
  else begin
    writeln('No me gusta ese valor');
  end;
  end;
  readln;
end.

