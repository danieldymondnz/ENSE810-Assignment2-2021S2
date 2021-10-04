<?php

    // Globals for Configuration Information
    $GLOBALS['recordsPerPage'] = 10;
    $GLOBALS['vehicleData'] = "initalTesting";
    $GLOBALS['tripData'] = "TRIPS";
    $GLOBALS['columnNames'] = getColumns();
    
    // Get Column Telemetry such as names and length
    function getColumns(){
        
        // Open Connection
        $username = $_SESSION["username"];
        $password = $_SESSION["password"];
        $conn = new mysqli($_SESSION['servername'], $_SESSION["username"], $_SESSION["password"], $_SESSION['database']);

        // If connection fails, throw error
        if ($conn->connect_error)
            triggerDatabaseError($conn->connect_error);

        $SQLPreQuery = "SELECT COUNT(*) FROM `" . $GLOBALS['vehicleData'] . "`";
        $result = $conn->query($SQLPreQuery);
        $GLOBALS['numRecords'] = mysqli_fetch_array($result)[0];

        // Run query and aggregate results
        $sqlQuery = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = '" . $_SESSION['database'] . "' AND TABLE_NAME = '" . $GLOBALS['vehicleData'] . "'";
        $result = $conn->query($sqlQuery);
        $conn->close();

        // Generate array of rows
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

    // Populate a Select Input with all Filter options for data
    function getFiltersForSelectInput(){

        echo '<option value="ASC"';
        // If part of a GET request, check and select the appropriate option to save user inputs between page loads
        if (isset($_GET['filterOrderField']) && 'ASC' == $_GET['filterOrderField']) {
            echo " selected";
        }
        echo '>Ascending</option>';

        echo '<option value="DESC"';
        // If part of a GET request, check and select the appropriate option to save user inputs between page loads
        if (isset($_GET['filterOrderField']) && 'DESC' == $_GET['filterOrderField']) {
            echo " selected";
        }
        echo '>Descending</option>';

    }

    // Determine the new start index for the tabulation when the increase button is selected
    function increaseRange() {
        return min(($_SESSION["startIndex"] + $GLOBALS['recordsPerPage']), $GLOBALS['numRecords'] - 1);
    }

    // Determine the new start index for the tabulation when the decrease button is selected
    function decreaseRange() {
        return max($_SESSION["startIndex"] - $GLOBALS['recordsPerPage'], 0);
    }

    // Insert text for the current range displayed by the table
    function getCurrentRange() {
        echo $_SESSION["startIndex"] + 1 . " - " . min(($_SESSION["startIndex"] + $GLOBALS['recordsPerPage']), $GLOBALS['numRecords']) . " of " . $GLOBALS['numRecords'];
    }

    // Create a new query for the database to filter content by a particular filter and order
    function queryByFilter($filterName, $filterOrder, $startVal)
    {
        // Craft the query
        $sqlQuery = "SELECT * FROM " . $GLOBALS['vehicleData'] . " ORDER BY `" . $GLOBALS['vehicleData'] . "`.`" . $filterName . "` " . $filterOrder . " LIMIT " . $startVal . "," . $GLOBALS['recordsPerPage'];

        // Execute the query and generate the table data
        executeQueryAndTabulate($sqlQuery);
    }

    // Execute the default query when no sorting filters have been selected.
    function executeDefaultQuery() 
    {
        // Craft the query
        $sqlQuery = "SELECT * FROM " . $GLOBALS['vehicleData'] . " ORDER BY `" . $GLOBALS['vehicleData'] . "`.`uid` ASC LIMIT 0," . $GLOBALS['recordsPerPage'];

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
        $conn = new mysqli($_SESSION['servername'], $_SESSION["username"], $_SESSION["password"], $_SESSION['database']);

        // If connection fails, throw error
        if ($conn->connect_error)
            triggerDatabaseError($conn->connect_error);

        // Otherwise, run query
        $result = $conn->query($SQLQuery);

        if ($result->num_rows > 0) {

            // Display Head of Results
            echo "<section class='inventory-results-head'>Showing records " . ($_SESSION["startIndex"] + 1) . " to " . ($_SESSION["startIndex"] + $result->num_rows) . " of " . $GLOBALS['numRecords'] . " result(s)</section>";
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

                $stringToDisplay .= "<tr><td>" . $row["uid"].
                                    "</td><td>" . $row["timestamp"].
                                    "</td><td>" . $row["aPitch"].
                                    "</td><td>" . $row["aRoll"].
                                    "</td><td>" . $row["aYaw"].
                                    "</td><td>" . $row["compass"].
                                    "</td><td>" . $row["gPitch"].
                                    "</td><td>" . $row["gRoll"].
                                    "</td><td>" . $row["gYaw"].
                                    "</td><td>" . $row["humidity"].
                                    "</td><td>" . $row["pressure"].
                                    "</td><td>" . $row["temperature"].
                                    "</td></tr>";

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




    /* Fleet Inspector */

    // Execute a SQL Query, and create HTML Table
    function executeInspectorQueryAndTabulate($registration)
    {
        // Filter input to remove spaces at either end of registration
        $registration = trim($registration);
        
        // Construct SQL Query - Use registration if available, otherwise default
        $SQLQuery = "";
        if (strlen($registration) > 0) {
            $SQLQuery = "SELECT * FROM `" . $GLOBALS['tripData'] . "` WHERE `REGISTRATION` LIKE '%" . $registration . "%' ORDER BY TRIP_TIMESTAMP DESC";
        } else {
            $SQLQuery = "SELECT * FROM `" . $GLOBALS['tripData'] . "` ORDER BY TRIP_TIMESTAMP DESC";
        }

        // Open Connection
        $conn = new mysqli($_SESSION['servername'], $_SESSION["username"], $_SESSION["password"], $_SESSION['database']);

        // If connection fails, throw error
        if ($conn->connect_error)
            triggerDatabaseError($conn->connect_error);

        // Otherwise, run query
        $result = $conn->query($SQLQuery);

        if ($result->num_rows > 0) {

            // Display Head of Results
            echo "<section class='inventory-results-head'>Showing " . $result->num_rows . " result(s)";
            
            if (strlen($registration) > 0) {
                echo  " for registration containing '" . $registration . "'";
            }
            
            echo ".<br>";
            echo "<i class='SQLQueryText'>". $SQLQuery ."</i><br><br/>";

            $output = "";

            // Output each matching result
            while($row = $result->fetch_assoc()) 
            {
                // Generate Div
                $output .= '<div class="heartbeatVehicle">';

                // Place registration
                $output .= '<span class="heartbeatVehicleRegistration">' . $row["REGISTRATION"] . "</span>";

                // Place Info
                $output .= '<span class="heartbeatVehicleInfo">Trip ' . $row["TRIP_ID"] . " - " . $row["TIMESTAMP"] . "</span>";

                // Place Status Container
                $output .= '<span class="heartbeatVehicleStatus">';

                // Determine labels
                // Enviromental Warnings
                if ($row['TEMP_WARN'] == 1 && $row['HUMIDITY_WARN'] == 1) {
                    $output .= '<span class="heartbeatVehicleStatusLabel back-orange">ENVIRO WARN</span>';
                } else if ($row['TEMP_WARN'] == 1) {
                    $output .= '<span class="heartbeatVehicleStatusLabel back-orange">TEMP WARN</span>';
                } else if ($row['HUMIDITY_WARN'] == 1) {
                    $output .= '<span class="heartbeatVehicleStatusLabel back-orange">HUMIDITY WARN</span>';
                }

                // Driving Warnings
                if ($row['SPEED_WARN'] == 1 && $row['ACCEL_WARN'] == 1) {
                    $output .= '<span class="heartbeatVehicleStatusLabel back-orange">DRIVING WARN</span>';
                } else if ($row['SPEED_WARN'] == 1) {
                    $output .= '<span class="heartbeatVehicleStatusLabel back-orange">SPEED WARN</span>';
                } else if ($row['ACCEL_WARN'] == 1) {
                    $output .= '<span class="heartbeatVehicleStatusLabel back-orange">ACCEL WARN</span>';
                }

                // Display Sync Status
                if ($row['IS_SYNCED'] == 1) {
                    $output .= '<span class="heartbeatVehicleStatusLabel back-green">SYNCED</span>';
                } else {
                    $output .= '<span class="heartbeatVehicleStatusLabel back-red">PARTIAL SYNC</span>';
                }
                
                // Close off
                $output .= '</span></div>';

            }
            echo $output;
        } else {
            echo "0 results";
        }
        
        $conn->close();
        
    }

    // Trigger a critical execution error
    function triggerDatabaseError($errorMessage)
    {
        echo 'alert("A Critical execution error has occured. Please try to login again, by selecting \"Logout\". Error code: " . $errorMessage)';
    }
?>