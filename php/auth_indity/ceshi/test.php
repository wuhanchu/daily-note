<?php

include ('Valite.php');

$valite = new Valite();
$valite->setImage('getImage.png');
$valite->getHec();
$ert = $valite->run();
//$ert = "1234";
print_r($ert);
echo '<br><img src="abc.jpeg"><br>';

?>