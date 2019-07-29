<?php
/*
���ӣ�����Сͼ���ֱ������������ 
$obj = new ReSizeImage(); 
$obj->setSourceFile('win.png'); 
$obj->saveFile(false); 
$obj->setWidth(250); 
$obj->setHeight(250); 
$obj->draw();
���ӣ�����Сͼ��󱣴���ͼ���ļ�Ϊ��new.png�� 
$obj = new ReSizeImage(); 
$obj->setSourceFile('win.png'); 
$obj->setDstFile('new.png'); 
$obj->setWidth(250); 
$obj->setHeight(250); 
$obj->draw();
���ӣ�����Сͼ��󱣴���ͼ���ļ�Ϊ��new.jpg������������qualityֵΪ��100�� 
$obj = new ReSizeImage(); 
$obj->setSourceFile('win.png'); 
$obj->setDstFile('new.jpg'); 
$obj->setWidth(250); 
$obj->setHeight(250); 
$obj->draw(100);
���ӣ�����׽�����е��쳣 
try { 
$obj = new ReSizeImage(); 
$obj->setSourceFile('no.png'); 
$obj->saveFile(false); 
$obj->setWidth(250); 
$obj->setHeight(250); 
$obj->draw(); 
} catch (Exception $ex) { 
echo $ex; 
}
* ��ͼ�������С��Ҳ�ɶ�png, gif, jpeg, wbmp��ʽ��ͼ�����ת�� 
* ��ҪGD���֧�ֲſ��ԣ���Ҫ����gifͼ��������ҪGD2.0.28����߰汾��֧��
* (��* gif�Ķ���ת��֮�󶯻���ɾ�������֪Ϊʲ*ô! 
* 
*/
class ResizeImage 
{
 const ResizeImageInfo = "�����ͼ�������С��Ҳ�ɶ�png, gif, jpeg, wbmp��ʽ��ͼ�����ת��";
 //����Ŀ��ͼ��Ŀ�͸� 
 private $height = 100; 
 private $width = 100;
 //Դͼ���ļ���Ŀ��ͼ���ļ�����ֻ��������������Ŀ��ͼ���ļ��ɲ����� 
 private $sourceFile = ''; 
 private $dstFile = '';
 //ͼ�����͡�image/gif��image/jpeg��image/png...�� 
 private $imgType;
 //Դͼ������Ŀ��ͼ���� 
 private $sim; 
 private $dim;
 //�Ƿ񱣴�ͼ����public void saveFlag(boolean $flag)�������� 
 private $saveFlag = true;
 //���캯������ϵͳ��֧��GD��ʱ�����쳣��Ϣ
 function __construct() 
 { 
  if (!function_exists('imagecreate')) 
  { 
   throw new Exception('���ϵͳ��֧��GD��'); 
  } 
 }
 //�����������Ϣ
 function __toString() 
 { 
  return ReSizeImage::ResizeImageInfo; 
 }
 //����Ŀ��ͼ��Ŀ� 
 public function setWidth($width) 
 { 
  if ($width <= 0) 
  { 
   throw new Exception('Ŀ��ͼ���Ȳ���С��0'); 
   return ; 
  } 
  $this->width = $width; 
 }
 //����Ŀ��ͼ��ĸ� 
 public function setHeight($height) 
 { 
  if ($height <= 0) 
  { 
   throw new Exception('Ŀ��ͼ��߶Ȳ���С��0'); 
   return ; 
  } 
  $this->height = $height; 
 }
 //����Դͼ���ļ� 
 public function setSourceFile($file) 
 { 
  if (!file_exists($file)) 
  { 
   throw new Exception('Դͼ���ļ�������'); 
   return ; 
  } 
  $this->sourceFile = $file; 
 }
 //����Ŀ��ͼ���ļ� 
 public function setDstFile($file) 
 { 
  $this->dstFile = $file; 
 }
 //�����Ƿ��������ļ� 
 public function saveFile($flag) 
 { 
  $this->saveFlag = (boolean)$flag; 
 }
 //ִ�л�ͼ������$quality������ʾ����ͼ���Ч��������Խ�ߣ�Ч��Խ�ã�����������jpeg���͵�ͼ�� 
 public function draw($quality = 95) 
 { 
  $sourceImgInfo = getimagesize($this->sourceFile); 
  if (!is_array($sourceImgInfo)) 
  { 
   throw new Exception('Դͼ���ļ�������'); 
   return ; 
  } 
  switch($sourceImgInfo[2])
  { 
   case 1: 
    $this->imgType="image/gif"; 
    $this->sim = imagecreatefromgif($this->sourceFile); 
    break; 
   case 2: 
    $this->imgType="image/jpeg"; 
    $this->sim = imagecreatefromjpeg($this->sourceFile); 
    break; 
   case 3: 
    $this->imgType="image/png"; 
    $this->sim = imagecreatefrompng($this->sourceFile); 
    break; 
   case 15: 
    $this->imgType="image/wbmp"; 
    $this->sim = imagecreatefromwbmp($this->sourceFile); 
    break; 
   default: 
    return '��֧�ֵ�ͼ���ʽ'; 
   break; 
  }
  //����Ŀ��ͼ���ʵ�ʿ�͸� 
  $dstWidth = $sourceWidth = $sourceImgInfo[0]; 
  $dstHeight = $sourceHeight = $sourceImgInfo[1];
  if ($sourceHeight > $this->height && $sourceWidth > $this->width) 
  { 
   if ($sourceHeight > $sourceWidth) 
   { 
    $zoom = $this->height / $sourceHeight; 
    $dstHeight = $this->height; 
    $dstWidth = $sourceWidth * $zoom; 
   } 
   else 
   { 
    $zoom = $this->width / $sourceWidth; 
    $dstWidth = $this->width; 
    $dstHeight = $sourceHeight * $zoom; 
   } 
  }
  //����Ŀ��ͼ��ľ�� 
  $this->dim = @imagecreatetruecolor($dstWidth, $dstHeight) or imagecreate($dstWidth, $dstHeight);
  //�����ɫͼ��ת��Ϊ��ɫ��ͼ�� 
  imagetruecolortopalette($this->sim, false, 256);
  //����Դͼ����ɫ���������������䵽Ŀ��ͼ���� 
  $palsize = ImageColorsTotal($this->sim); 
  for ($i = 0; $i<$palsize; $i++) 
  { 
   $colors = ImageColorsForIndex($this->sim, $i); 
   ImageColorAllocate($this->dim, $colors['red'], $colors['green'], $colors['blue']); 
  }
  //����ͼ������� 
  imagecopyresampled($this->dim, $this->sim, 0, 0, 0, 0, $dstWidth, $dstHeight, $sourceWidth, $sourceHeight);
  //�����µ�Ŀ��ͼ�� 
  if ($this->saveFlag) 
  { 
   $imgExt = substr($this->dstFile, strrpos($this->dstFile, '.') + 1); 
   switch(strtolower($imgExt))
   { 
   case 'gif': 
    if (!function_exists('imagegif')) 
    { 
     throw new Exception('���GD�ⲻ֧��gifͼ������'); 
     return ; 
    } 
    imagegif($this->dim, $this->dstFile); 
    break; 
   case 'jpeg': 
   case 'jpg': 
    imagejpeg($this->dim, $this->dstFile, $quality); 
    break; 
   case 'png': 
    imagepng($this->dim, $this->dstFile); 
    break; 
   case 'wbmp': 
    imagewbmp($this->dim, $this->dstFile); 
    break; 
   default: 
    return 'Ŀ��ͼ���ļ�Ϊ�ջ��߸�ʽ���ԣ��޷����б���'; 
    break; 
   } 
  }
  //ֱ�����Ŀ��ͼ��������� 
  else 
  { 
   header ("Content-type: " . $this->imgType); 
   switch($sourceImgInfo[2])
   { 
    case 1: 
     imagegif($this->dim); 
     break; 
    case 2: 
     imagejpeg($this->dim, '', $quality); 
     break; 
    case 3: 
     imagepng($this->dim); 
     break; 
    case 15: 
     imagewbmp($this->dim); 
     break; 
    default: 
     return '��֧�ֵ�ͼ���ʽ'; 
     break; 
   } 
  } 
  return ; 
 }
 function __destruct() 
 { 
  @ImageDestroy($this->sim); 
  @ImageDestroy($this->dim); 
 } 
} 
?>