<?php

    $institute = "kj somaiya institute of management";
    $course = "MCA";

    function local(){
        global $course,$institute;
        $dept = "DST";
        echo "<br> local() called;";
        echo "<br> " .$dept;
        echo "<br> institute " .$institute;
        echo "<br> institute " .$course;

    }

    local(); // function call

    echo "<br> dept :", $dept; // local variable not accessible out of scope
    echo "<br> institute :", $institute;

    function globalAcess(){
        echo "<hr> global";

        //$GLOBALS["name"] is super global
        echo "<br> institute : ", $GLOBALS["institute"];
        echo "<br> course", $GLOBALS["course"];
        echo "<hr>";

        $institute = "ksjim";
        echo "<br> institute from local -".$institute;
    }

    static $count = 0;
    function countFunction(){
        global $count;
        ++$count;
        echo "<br>". $count;
    }

    function countf5(){
        global $count;
        $count += 5;
    }
    globalAcess();
    echo "<hr> count function";
    countFunction(); // 1
    countf5();
    countFunction(); // 7
    countf5();
    countFunction(); // 14
?>