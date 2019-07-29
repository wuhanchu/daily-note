<?php
	$test =  array("a","b","b");
	$test = array_unique($test);
	
	foreach ($test as $item) {
		print $item;
	}
?>