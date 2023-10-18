<?php
echo "<h1 style='text-transform: uppercase;font-family:monospace;'>hello welcome to mca</h1>";
echo "<h1 style='text-transform: uppercase;font-family:monospace;'>Lets learn PHP</h1>";

$college = "KJSIM";
echo "<br>" . $college;
echo "<br>" . $college;
echo ("<br>");
echo ("this is from echo function");
echo "<br>PHP is case insensitive language";
print("<br>Output from print function");




echo "<br> college = $college"; //illiteral - replace 
echo '<br> college = $college'; //literal - shown as whole string

//embeding comment inside syntax or code

echo "<br> comment ignored : " . /* ignore by php interpreter */$college;

// $num = 123;
// $var = "karan";
// $char = 'k';
// $float = 2.5;

// echo "<br> var is " .var_dump($num);
// echo "<br> var is " .var_dump($var);
// echo "<br> var is " .var_dump($char);
// echo "<br> var is " .var_dump($float);

// echo "<br> var is " .is_int($num);
// echo "<br> var is " .is_int($var);

// echo "<br> var is " .gettype($num);

class Test
{
}
$var = new Test();


echo "<br> var is " . var_dump($var);
echo "<br> var is " . is_int($var);
echo "<br> var is " . gettype($var);

// int double float object bool resource array string

$var = tmpfile();
echo "<hr><br> var is " . var_dump($var);
echo "<br> var is " . is_resource($var);
echo "<br> var is " . gettype($var);

$var = null;
echo "<hr><br> var is " . var_dump($var);
echo "<br> var is " . is_null($var);
echo "<br> var is " . gettype($var);
?>