<?php
// ini_set('display_errors', 1);
// ini_set('display_startup_errors', 1);
// error_reporting(E_ALL);
include 'main.php';

if(isset($_POST)){
	if('save' == $_POST['save']){
		$info = array(name => $_POST['name'], surname => $_POST['surname']);
		print_r($info);
		$physical = array(gender => $_POST['gender'], age => $_POST['age'],weight => $_POST['weight']);
		print_r($physical);

		createCSV('physical',$physical);
		die(predictPatient('physical_prediction'));

		$factors = array(sport => $_POST['sport'], tobacco => $_POST['tobacco'],alcohol => $_POST['alcohol'], familyHistory => $_POST['familyHistory']);
		print_r($factors);
		connectDB();
		die('savee');
	}
	else if('getUsers' == $_POST['getUsers']){

	}
}
else{
	die('Error!');
}