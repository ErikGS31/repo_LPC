Function Funcion-P2
{
[CmdLetBinding()] param([Parameter()] [float] $num)
for ($i = 0; $i -lt 30; $i++){
Write-Host $i "por 3.14 = " ($num * $i)
}
}

Write-Host "funcion para saber los multiplos del 0 al 30 de 3.14"
Funcion-P2 -num 3.14