#!/usr/bin/env/bash

echo "script ára saber si el numero de la variable es par o inpar"
variable=5
echo ""
echo "el valor de la variable utilizada es: " $variable
if [ $variable%2==0 ]
then
	echo ""
	echo "el numero de la variable es par"
	echo ""
else
	echo "el numero de la variables es inpar"
fi