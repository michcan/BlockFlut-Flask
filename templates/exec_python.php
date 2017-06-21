<?php
	$code=$_POST['orderid'];
	#echo $code;
	$myfile = fopen("newfile.py", "w") or die("Unable to open file!");
	fwrite($myfile, $code);
	fclose($myfile);
	if(isset($_POST['pid']))
	{
		echo shell_exec("kill ".($_POST['pid']+1));
	}
	if(isset($code))
	{
		echo shell_exec("python launcher.py");
	}
?>