<?php
include 'main.php';

// if(isset($POST)){
	if('save' == 'save'){//$POST['save']){
		$info = json_encode($POST['info']);
		$physical = json_encode($POST['physical']);
		$factors = json_encode($POST['factors']);
		connectDB();
		die('savee');
	}
	else if('getUsers' == $POST['getUsers']){

	}
// }
// else{
	// die('Error!');
// }