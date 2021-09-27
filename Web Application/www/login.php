<!DOCTYPE html>
<html>
<head>
    <title> Login | SDMMS Console </title>
    <!-- Header Template -->
    <?php require('phpTemplates/header.php'); ?>
</head>
<body class="sessionBody">

    <section class="floatingSessionContainer">
        <h1 class="header-title header-title-login">Kia Ora</h1>
        <p>Welcome back to the SDMMS Console</p>
        <p id="submissionOutcome">Please enter your username and password to access the database</p>
        <br></br>
        <form method="post" action="login.php">
            <input id= "username" name="username" type="text" placeholder="Username" autocomplete="off" arial-label="Inventory Search Box" />
            <br></br>
            <input id= "password" name="password" type="password" placeholder="Password" autocomplete="off" arial-label="Inventory Search Box" />
            <br></br>
            <br></br>
            <input type="submit" value="Log In"/>
        </form>
    </section>

    <!-- Floating Session Logo Template -->
    <?php require('phpTemplates/floatingSessionLogo.php'); ?>
    

</body>

<!-- PHP Login Script -->
<?php

    # If a POST Request is recieved, attempt to sign in
    if(isset($_POST['username']) && isset($_POST['password'])) {

        // Create connection
        $servername = "localhost";
        $username = $_POST["username"];
        $password = "l0ck3dR3alT!GHT:D";
        $database = "week8DatabaseTest";

        $conn = new mysqli($servername, $username, $password, $database);

        // Check connection
        if ($conn->connect_error) {
            echo '<script type="text/JavaScript">displayLoginFail();</script>';
            die();
        }
        
        // If successful, update controls to indicate this
        echo '<script type="text/JavaScript">displayLoginSuccess();</script>';

        // Create new container for session
        session_start();
        $_SESSION["username"] = $username;
        $_SESSION["password"] = $password;
        $_SESSION["signOnSuccessful"] = true;

        // Redirect to console
        header("Location: dataConsole.php");

    }

?>

</html>