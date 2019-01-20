<?php
function connectDB(){
	$servername = 'localhost';
	$username = 'backend';
	$password = 'Toprak123123';

	$con = mysqli_connect($servername,$username,$password);
	if(!$con){
		die(mysqli_connect_error());
	}
	echo 'success';
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
	mysqli_close($con);

}