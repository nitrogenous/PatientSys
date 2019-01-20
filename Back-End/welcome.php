<?php
// ini_set('display_errors', 1);
// ini_set('display_startup_errors', 1);
// error_reporting(E_ALL);
include 'main.php';
if(isset($_POST)){
	if('save' == $_POST['save']){
		
		$info = array(name => $_POST['name'],surname => $_POST['surname']);

		$physical = array(gender => injection($_POST['gender']), age => injection($_POST['age']), weight => injection($_POST['weight']));

		$physicalAvg = json_decode(predictPatient(injection('physical_prediction'),json_encode($physical)))[0];

		$factors = array(sport => injection($_POST['sport']),tobacco => injection($_POST['tobacco']),alcohol => injection($_POST['alcohol']),familyHistory => injection($_POST['familyHistory']),physicalAvg => injection($physicalAvg));

		$factorsAvg = json_decode(predictPatient(injection('factors_prediction'),json_encode($factors)))[0];

		$con = connectDB();
		$sql = 'INSERT INTO `usersDatabase`(`patientAvg`, `name`, `surname`, `gender`, `age`, `weight`, `sport`, `tobacco`, `alcohol`, `familyHistory`, `physicalAvg`) VALUES ('.injection($factorsAvg).',"'.injection($_POST['name']).'","'.injection($_POST['surname']).'",'.injection($_POST['gender']).','.injection($_POST['age']).','.injection($_POST['weight']).','.injection($_POST['sport']).','.injection($_POST['tobacco']).','.injection($_POST['alcohol']).','.injection($_POST['familyHistory']).','.injection($physicalAvg).')';
		// echo saveData($con,$sql);
		die('save');
	}
	else if('getUsers' == $_POST['getUsers']){
		$con = connectDB();
		$sql = 'SELECT * FROM `usersDatabase`';
		$data = getData($con,$sql);
		die($data);
	}
}
else{
	die('Error!');
}