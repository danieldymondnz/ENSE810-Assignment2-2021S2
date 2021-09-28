<?php

    // Globals for Configuration Information
    $GLOBALS['servername'] = "localhost";
    $GLOBALS['database'] = "week8DatabaseTest";
    $GLOBALS['table'] = "initalTesting";
    $GLOBALS['columnNames'] = getColumns();
    $GLOBALS['startIndex'] = 1;
    $GLOBALS['recordsPerPage'] = 5;

    // Get Column Names
    function getColumns(){
        
        // Open Connection
        $username = $_SESSION["username"];
        $password = $_SESSION["password"];
        $conn = new mysqli($GLOBALS['servername'], $_SESSION["username"], $_SESSION["password"], $GLOBALS['database']);

        // If connection fails, throw error
        if ($conn->connect_error)
            triggerDatabaseError($conn->connect_error);

        // Run query and aggregate results
        $sqlQuery = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = 'week8DatabaseTest' AND TABLE_NAME = 'initalTesting'";
        $result = $conn->query($sqlQuery);
        $conn->close();

        // 
        if ($result->num_rows > 0) {

            // Create new array
            $returnArray = array();
            $counter = 1;

            // Extract each item from query and place into array
            while($row = $result->fetch_assoc()) {
                $returnArray[$counter] = $row["COLUMN_NAME"];
                $counter += 1;
            }

            // Return array
            return $returnArray;

        } 
        else
            return null;

    }

    // Populate a Select Input with all Column options from the database
    function getColumnNamesForSelectInput(){

        foreach($GLOBALS['columnNames'] as $column) {
            echo '<option value="' . $column . '"';
            // If part of a GET request, check and select the appropriate option to save user inputs between page loads
            if (isset($_GET['filterTypeField']) && $column == $_GET['filterTypeField']) {
                echo " selected";
            }
            echo '>' . $column . '</option>';
        }

    }

    // Create a new query for the database to filter content by a particular filter and order
    function queryByFilter($filterName, $filterOrder)
    {
        // Craft the query
        $sqlQuery = "SELECT * FROM " . $GLOBALS['table'] . " ORDER BY `" . $GLOBALS['table'] . "`.`" . $filterName . "` " . $filterOrder;

        // Execute the query and generate the table data
        executeQueryAndTabulate($sqlQuery);
    }

    function executeDefaultQuery() 
    {
        // Craft the query
        $sqlQuery = "SELECT * FROM " . $GLOBALS['table'] . " ORDER BY `" . $GLOBALS['table'] . "`.`uid` ASC LIMIT " . $GLOBALS['startIndex'] . "," . $GLOBALS['recordsPerPage'];

        // Execute the query and generate the table data
        executeQueryAndTabulate($sqlQuery);
    }

    // Execute a SQL Query, and create HTML Table
    function executeQueryAndTabulate($SQLQuery)
    {

        // Get Session Data
        $username = $_SESSION["username"];
        $password = $_SESSION["password"];
        
        // Open Connection
        $conn = new mysqli($GLOBALS['servername'], $_SESSION["username"], $_SESSION["password"], $GLOBALS['database']);

        // If connection fails, throw error
        if ($conn->connect_error)
            triggerDatabaseError($conn->connect_error);

        $SQLPreQuery = "SELECT COUNT(*) FROM " . $GLOBALS['table'];
        $result = $conn->query($SQLPreQuery);
        $count = mysqli_fetch_array($result)[0];

        // Otherwise, run query
        $result = $conn->query($SQLQuery);

        if ($result->num_rows > 0) {

            // Display Head of Results
            echo "<section class='inventory-results-head'>Showing records " . $GLOBALS['startIndex'] . " to " . ($GLOBALS['startIndex'] + $result->num_rows - 1) . " of " . $count . " result(s)</section>";
            echo "<i class='SQLQueryText'>". $SQLQuery ."</i><br><br/>";

            // Display start of div
            echo "<section class='inventory-results'>";

            // Output header of table
            $stringToDisplay = "<table class='data-console-table'><tr>";

            foreach($GLOBALS['columnNames'] as $column) {
                $stringToDisplay.= '<th>' . $column . '</th>';
            }
            $stringToDisplay .= "</tr>";

            // output data of each row
            while($row = $result->fetch_assoc()) {

                $stringToDisplay .= "<tr><th>" . $row["uid"].
                                    "</th><th>" . $row["timestamp"].
                                    "</th><th>" . $row["aPitch"].
                                    "</th><th>" . $row["aRoll"].
                                    "</th><th>" . $row["aYaw"].
                                    "</th><th>" . $row["compass"].
                                    "</th><th>" . $row["gPitch"].
                                    "</th><th>" . $row["gRoll"].
                                    "</th><th>" . $row["gYaw"].
                                    "</th><th>" . $row["humidity"].
                                    "</th><th>" . $row["pressure"].
                                    "</th><th>" . $row["temperature"].
                                    "</th></tr>";

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

    function triggerDatabaseError($errorMessage)
    {
        die("Connection failed: " . $errorMessage);
    }
?>