<?php
	date_default_timezone_set('UTC');

	$today = date("Y-m-d");  
	print($today."\r\n");
	$firstday = date('Y-m-01', strtotime($today));//本月第一天  
	print($firstday."\r\n");
	$lastday = date('Y-m-d', strtotime($firstday . " +1 month -1 day"));//本月最后一天  
	print($lastday."\r\n");

	$lastMonth = strtotime("-1 month", time());  
	print($lastMonth."\r\n");

	$lastMonthLastday = date("Y-m-t", $lastMonth);//上个月最后一天 
	print($lastMonthLastday."\r\n");
 
	$lastMonthFirstday = date('Y-m-01', $lastMonth);//上个月第一天 
	print($lastMonthFirstday."\r\n");

?>