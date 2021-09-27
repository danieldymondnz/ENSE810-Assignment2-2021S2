<!DOCTYPE html>
<html lang="en">
<head>
    <title> Data Console | SDMMS Console </title>
    <?php require('phpTemplates/header.php'); ?>

    <!-- PHP Verification - If no active session, return to login. -->
    <?php
        session_start();
        if (session_status() == PHP_SESSION_ACTIVE && $_SESSION["signOnSuccessful"] == true) {
            executeQuery();
        } else {
            header("Location: login.php");
        }
    ?>

</head>
<body>
    <!-- Navigation Bar -->
    <?php require('phpTemplates/navigationBar.php'); ?>


    <section class="content">
        <h1 class="header-title">Data Console</h1>
        <div class="header-charms">
            <form>
            <span class="material-icons-outlined">filter_alt</span> Filter & Sort Data: 
                <select id="filterField">
                    <option value="none" selected>Filter data by... </option>
                    <option value="test">Test</option>
                    <option value="test2">Test2</option>
                </select>
                <input id="button resetButton" type="reset" value="Reset Filter"></input>
        </form>
        </div>
        <section id="inventory-splash-welcome" class="inventory-splash hidden">
            <img src="img/happy-person.jpg" /><br /><br />
            Start by typing a barcode or a tag/keyword into the search box to see results appear.<br /><br />
            Note: Xenix only supports full barcode and tag/keyword entries in this development stage.
        </section>
        <section id="inventory-splash-noitems" class="inventory-splash hidden">
            <img src="img/no-items.jpg" /><br /><br />
            Sorry, there's nothing to show. Try searching for something else.
        </section>
        <section class="inventory-results-head">
            "name" returned 12 results
        </section>
        <br />
        <section class="inventory-results">

            <?php

                function executeQuery() {

                    $servername = "localhost";
                    $database = "week8DatabaseTest";

                    // Create connection
                    $username = $_SESSION["username"];
                    $password = $_SESSION["password"];
                    $conn = new mysqli($servername, $username, $password, $database);

                    // Check connection
                    if ($conn->connect_error) {
                        die("Connection failed: " . $conn->connect_error);
                    }

                    $sql = "SELECT * FROM initalTesting";
                    $result = $conn->query($sql);

                    if ($result->num_rows > 0) {
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
                        $stringToDisplay .="</table>";
                        echo $stringToDisplay;
                    } else {
                        echo "0 results";
                    }
                    
                    

                    $conn->close();

                }
                
            ?>

        </section>

        <section id="loading-animation" class="loading-animation hidden">
            <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
        </section>
    </section>
</body>
</html>