program numerospares;

var a,b,c,d,e,i,j,aux: byte;

begin

  writeln('Ingresa 5 valores enteros');
  readln(a,b,c,d,e);


  for i:= 1 to 5 do begin
      case i of
        1:
        aux:=a;

        2:
        aux:=b;

        3:
        aux:=c;

        4:
        aux:=d;

        5:
        aux:=e;

    else
        writeln('ERROR');
    end;
      writeln('---',aux,'---');
      for j:= 1 to aux do  begin

          if (j mod 2) = 0 then begin
            writeln(j);
          end;

      end;
  end;
   readln();
end.

