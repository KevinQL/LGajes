<?php

// Asigna en número tres a la variable
$tres = 3;

// Imprime el valor de nuestra variable
echo $tres;

// Asignamos la variable pi
$pi = 3.14159265359;

// Realizamos cálculos de circunferencia (pi * diámetro)
echo $pi * 5;
echo $pi * 3;

/*
$nombre = 'Daniel';     // Legal
$Nombre = 'Daniel';     // Legal
$_nombre = 'Daniel';    // Legal
$nom_bre = 'Daniel';    // Legal
$nom_br3 = 'Daniel';    // Legal
$nom-bre = 'Daniel';    // Illegal
$1nombre = 'Daniel';    // Illegal. Numero como primer caracter de la variables
*/


$cantidadDePersonas = 2;

echo $personasMayores = 1;

echo $dedosManos = $dedosPies = 10;


/*
 * Tipos de variables:
 * integer
 * float
 * boolean
 * string
 * null
 * array
 */

// integer
$unEntero = 10;
$otroEntero = -4;

// float
$unNumeroFloat = 2.34;
$otroNumeroFloat = -80.19;

// boolean
$cosaFalsa = FALSE;
$cosaVerdadera = TRUE;
$lala = false;

// string
$nombre = 'Daniel';
$apellido = 'Romero';
print("\n");
var_dump($nombre);
var_dump($apellido);

// null
$caja = NULL;

// array
$miPrimerArray = [1, 2, 3];   ## Forma asmilada desde la version 5.x
$otroArray = array(5, 6, 7, 8);

var_dump($miPrimerArray);

// Asinación avanzada
$polos = 2;
$polos += 1;


// Muestra información de la variable
var_dump($polos);
### 

// Decrementa el valor
$polos--;
var_dump($polos);


// Decrementa el valor
--$polos;
var_dump($polos);


// Dump Antes.
var_dump($polos);

// Dump durante.
var_dump(--$polos);

// Dump después.
var_dump($polos);


// Dump Antes.
var_dump($polos);

// Dump durante.
var_dump($polos--);

// Dump después.
var_dump($polos);


// Asignar, e incrementar
$cantidadPolos = $polos++;

// Asignación
$cantidadPolos = $polos;
// Incremento
$polos = $polos + 1;