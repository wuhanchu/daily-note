<?php

$json = '{"foo": {"a":12345}}';
$obj = json_decode($json,true);
print $obj["foo"]["a"];