<?php
function connectDB(){
	$servername = 'localhost';
	$username = 'backend';
	$password = 'Toprak123123';

	$con = mysqli_connect($servername,$username,$password);
	if(!$con){
		die(400,' ',mysqli_connect_error());
	}
	die(200);
}

function saveDate($con,$sql){
	if(mysqli_query($con,$sql)){
		die(200);
	}
	else{
		die(400);
	}
}

function getData($con,$sql){
	$result = mysqli_query($con,$sql);
	if (mysqli_num_rows($result) > 0){
		while ($row = mysqli_fetch_assoc($result)){
			echo $row;
		}
	}
	else{
		echo '0 result';
	}
}

