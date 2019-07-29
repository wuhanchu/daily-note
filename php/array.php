<?php
$list = array(array("id"=>"12212","date"=>"1123213"),array("id"=>"1212","date"=>"1123213"),array("id"=>"1212","date"=>"11233213"));
print((in_array(array("id"=>"12122","date"=>"1123213"),$list)? "true": "fasle")."\r\n");
	
$list  = unique_multidim_array($list);
print(sizeof($list));

?>