<?php

    // Globals for Configuration Information
    $GLOBALS['servername'] = "localhost";
    $GLOBALS['database'] = "week8DatabaseTest";

    // Populate a Select Input for a filter by column name
    function getColumnNamesForSelectInput() {

        // Create connection and execute query
        $sqlQuery = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = 'week8DatabaseTest' AND TABLE_NAME = 'initalTesting'";
        $conn = new mysqli($GLOBALS['servername'], $_SESSION["username"], $_SESSION["password"], $GLOBALS['database']);

        // Establish Connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }
        $result = $conn->query($sqlQuery);

        // Generate HTML
        if ($result->num_rows > 0) {
            while($row = $result->fetch_assoc()) {
                echo '<option value="' . $row["COLUMN_NAME"] . '">' . $row["COLUMN_NAME"] . '</option>';
            }
        } 

    }

    // Query the Database and show all data
    function executeQuery() {
        
        // Create connection
        $username = $_SESSION["username"];
        $password = $_SESSION["password"];
        $conn = new mysqli($GLOBALS['servername'], $username, $password, $GLOBALS['database']);

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        $sql = "SELECT * FROM initalTesting";
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {

            // Display Head of Results
            echo "<section class='inventory-results-head'>Query returned " . $result->num_rows . " result(s)</section><br />";

            // Display start of div
            echo "<section class='inventory-results'>";

            // Output header of table
            $stringToDisplay = "<table class='data-console-table'>
                    <tr>
                        <th>uid</th>
                        <th>Timestamp</th>
                        <th>Temperature</th>
                    </tr>";
            // output data of each row
            while($row = $result->fetch_assoc()) {
                $stringToDisplay .= "<tr><th>" . $row["uid"]. "</th><th>" . $row["timestamp"]. "</th><th>" . $row["temperature"]. "</th></tr>";
            }

            // Output footer of table
            $stringToDisplay .="</table></section>
            ";
            echo $stringToDisplay;
        } else {
            echo "0 results";
        }
        
        $conn->close();

    
        
            
            

        
    }
?>