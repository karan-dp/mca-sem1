<?php
namespace FY_MCA_2023;

# constants wont require $ sign while declaring or accessing its value
# kind of global variables with fixed values
# value can not be changed once declared
# we can define constants using define() and const keyword
# one can use constant (const_name) to access constant variables
# const is not declared with $
#
define("kjsim", " KJ Somaiya Insitute of Management");
echo "<BR> kjsim means ", kjsim;
echo "<BR> kjsim means: ", constant("kjsim");
const dept = "Dept of Data science and technology";
echo "<BR> dept: ", dept;
echo "<BR> dept: ", constant("kjsim");

#magic constants gives you contextual value
echo "<br> <h2> magic constants </h2><hr>";
echo "<br> i am inside file: ", __FILE__;
echo "<br> i am inside file: ", __LINE__;

echo "<br> i am inside file: ", __DIR__;

function show()
{
    echo "<BR> hey this is function :", __FUNCTION__;
}

show();
echo "<br> we are currently inside namespace :", __NAMESPACE__;

echo "<hr>";
class MCA
{
    function show()
    {
        echo "<br> i am inside class : ", __CLASS__;
        echo "<br> i am inside method : ", __METHOD__;

    }
}
$m = new MCA;
$m->show();

$mca = "master";
$$mca = "KJSIM";
$$$mca = "KJSIM masters";

echo "<br> mca : " . $mca;
echo "<br> mca : " . $$mca;
echo "<br> mca : " . $$$mca;
echo "<br> masters : " . $masters;
echo "<br> KJSIM : " . $KSJIM;
echo "<br> mca : " . ${$mca};
echo "<br> mca : " . ${${$mca}};


echo "<BR> <h2> arrays </h2><HR><BR>";
/*
array collection of simillar types (datatype) of data items
in php we use array () to declare/define arrays

indexed
associative
multidiamentional
$rolls = array(11,22,33,44,55);
*/
$rolls = array(11, 22, 33, 44, 55);
//associative arrays - key => value pair
$subjects = array("wt" => "web technology", "DBA" => "database applications", "ds" => "data science");
echo "<BR> rolls: ", var_dump($rolls);
echo "<BR> rolls: ", print_r($rolls);
echo "<BR> rolls: ", var_dump($subjects);
echo "<BR> rolls: ", print_r($subjects);
//
// member access operator 
// => // array assignment operator
echo "<hr>";
//using for loop to access array
for ($i = 0; $i < count($rolls); $i++) {
    echo "<br> rolls[", $i, "] = ", $rolls[$i];
}
// using foreach for accessing the array
echo "<hr><br> using foreach";
foreach ($rolls as $r) {
    echo "<br> ", $r;
}
// using foreach for associative array
echo "<hr><br> using foreach using associative array";
foreach ($subjects as $key => $value) {
    echo "<br> $key => $value ";
}

// multidimensonal array
echo "<br> <h2> multidimensional array <h2>";
$students = array(
    array(101, "karan", "karan@gmail.com"),
    array(102, "kpanchal", "panchal@gmail.com"),
);

for ($i = 0; $i < count($students); $i++) {
    for ($j = 0; $j < count($students); $j++) {
        echo $students[$i][$j], "  |  ";
    }
    echo "<br>";
}

echo "<br><hr> while loop";
// while 
$a = 0;
while ($a < count($rolls)) {
    if ($rolls[$a] > 50) {
        echo "<br>code break here........";
        break;
    }
    echo "<br> ", $rolls[$a];
    $a++;
}

echo "<br><hr> do while loop";
$b = 0;
do {
    echo "<br> ", $rolls[$b];
    $b++;
} while ($b < count($rolls));

// switch
echo "<br><hr> switch";
$selectedNum = "26";

switch($selectedNum) {
  case 1:
    echo "Your selected Num is 1";
    break;
  case 29:
    echo "Your selected Num is 29";
    break;
  case 3:
    echo "Your selected Num is 3!";
    break;
  default:
    echo "Your selected Num does not exist";
}
?>
