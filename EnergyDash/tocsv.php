<?php

$host = '192.168.0.9';
$user = 'testUser';
$password = 'passpass';
$database = 'testDB';

$con = new mysqli($host, $user, $password, $database);

$query = "SELECT Sample_Value, Time_Of_Sample FROM 601sam100";
if (!$result = mysqli_query($con, $query)) {
    exit(mysqli_error($con));
}

$users = array();
if (mysqli_num_rows($result) > 0) {
    while ($row = mysqli_fetch_assoc($result)) {
        $users[] = $row;
    }
}

header('Content-Type: text/csv; charset=utf-8');
header('Content-Disposition: attachment; filename=csv.csv');
$output = fopen('php://output', 'w');
fputcsv($output, array('No', 'Sample Value', 'Time Of Sample'));

if (count($users) > 0) {
    foreach ($users as $row) {
        fputcsv($output, $row);
    }
}
?>
