<?php
$servername = "classnote.cctd6tsztsfn.us-west-1.rds.amazonaws.com";
$username = "classnote";
$password = "macklineli";
$dbname = "ClassNoteDB";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM users WHERE nickname='elig'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo json_encode(['nickname'=>$row["nickname"],'name'=>$row["name"],'id'=>$row["id"]]);
    }
} else {
    echo json_encode(['result'=>'none']);
}
$conn->close();
?>
