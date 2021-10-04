<!DOCTYPE html>
<html lang="en"><html>
<head>
    <title> Login | SDMMS Console </title>
    <?php require('phpTemplates/header.php'); ?>
</head>
<body class="sessionBody">

    <section class="floatingSessionContainer">
        <h1 class="header-title header-title-login">Kia ora</h1>
        <p>Welcome back to SDMMS</p>
        <p id="submissionOutcome">Please enter your username and password</p>
        <br></br>
        <form method="post" action="login.php">
            <input id= "username" name="username" type="text" placeholder="Username" autocomplete="off" arial-label="Inventory Search Box" />
            <br></br>
            <input id= "password" name="password" type="password" placeholder="Password" autocomplete="off" arial-label="Inventory Search Box" />
            <br></br>
            <br></br>
            <input class="englargedButton" type="submit" value="Log In"/>
            <input class="englargedButton" id="button" type="button" value="Cancel" onclick="location.href = '/';"></input>
        </form>

        <!-- Floating Session Logo Template -->
        <?php require('phpTemplates/floatingSessionLogo.php'); ?>
    
    </section>

</body>

<!-- PHP Login Script -->
<?php

    # If a POST Request is recieved, attempt to sign in
    if(isset($_POST['username']) && isset($_POST['password'])) {

        // Create connection
        $servername = "localhost";
        $username = $_POST["username"];
        $password = "l0ck3dR3alT!GHT:D";
        $database = "sdmms_db";

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
        $_SESSION['servername'] = $servername;
        $_SESSION['database'] = $database;
        $_SESSION["username"] = $username;
        $_SESSION["password"] = $password;
        $_SESSION["signOnSuccessful"] = true;
        
        $_SESSION["startIndex"] = 0;

        // Redirect to console
        header("Location: home.php");

    }

?>

</html>