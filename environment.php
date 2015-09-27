<?php
		$output = array();
$handle = fopen("./DB/environment.csv", "r");
if ($handle) {
    while (($line = fgets($handle)) !== false) {
        $array = explode(',', $line);
        $output.push($array);
    }
    $output = array_splice($output, 0, 1);
    fclose($handle);
} else {
	echo "failed";
    // error opening the file.
} 
print_r(json_encode($output));
}
?>