<?php
/**
 * 用户验证码文件
 * @Author:wangsl
 * @version : 1.0
 * @creatdate: 2008-12-24
 */
header("Cache-Control: no-cache, must-revalidate");
header("Pragma: no-cache");
require_once("Caption.php");
$rsi = "";
$code = "";
$rsi = new Utils_Caption();
$rsi->TFontSize=array(15,17);
$rsi->Width=50;
$rsi->Height=25;
$code = $rsi->RandRSI();
session_start();
$_SESSION["CHECKCODE"] = $code;
$rsi->Draw();
exit;
?>