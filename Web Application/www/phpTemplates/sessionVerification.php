<!-- PHP Session Verification - If no active session, return to login. -->
<?php
    session_start();
    if (session_status() == PHP_SESSION_ACTIVE && $_SESSION["signOnSuccessful"] == true) {
        require('phpTemplates/databaseConfig.php');
    } else {
        header("Location: login.php");
    }
?>