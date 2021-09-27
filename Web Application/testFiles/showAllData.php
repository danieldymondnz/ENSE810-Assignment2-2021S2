<?php
    $servername = "localhost";
    $username = "dbuser";
    $password = "l0ck3dR3alT!GHT:D";
    $database = "week8DatabaseTest";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $database);

    // Check connection
    if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
    }
    echo "Connected successfully";

    echo("<br>");

    $sql = "SELECT * FROM initalTesting";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "uid: " . $row["uid"]. " - Timestamp: " . $row["timestamp"]. " - Temperature: " . $row["temperature"]. "<br>";
    }
    } else {
        echo "0 results";
    }
    $conn->close();
?>