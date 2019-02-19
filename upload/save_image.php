<?php 
$info= pathinfo($_FILES['image']['name']);
$ext=$info['extension']; //get the extension of file
$newname='new_image.'.$ext; //new name of images

$target='images/'.$newname;
move_uploaded_file($_FILES['image']['tmp_name'], $target);
?>