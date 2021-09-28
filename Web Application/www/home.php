<!DOCTYPE html>
<html lang="en">
<head>
    <title> SDMMS Console </title>
    <?php require('phpTemplates/header.php'); ?>

    <!-- PHP Verification - If no active session, return to login. -->
    <?php
        session_start();
        if (session_status() == PHP_SESSION_ACTIVE && $_SESSION["signOnSuccessful"] == true) {
            require('phpTemplates/databaseConfig.php');
        } else {
            header("Location: login.php");
        }
    ?>

</head>
<body>
    <!-- Navigation Bar -->
    <?php require('phpTemplates/navigationBar.php'); ?>

    <section class="content">
        <img src="img/splash.png" alt="splash" draggable="false" onContextMenu="return false;">    
    </section>

</body>
</html>