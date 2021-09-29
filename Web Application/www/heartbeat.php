<!DOCTYPE html>
<html lang="en">
<head>
    <title> Heartbeat | SDMMS Console </title>
    <?php require('phpTemplates/header.php'); ?>

    <!-- PHP Verification - If no active session, return to login. -->
    <?php
        session_start();
        if (session_status() == PHP_SESSION_ACTIVE && $_SESSION["signOnSuccessful"] == true) {
            require('phpTemplates/databaseConfig.php');
        } else {
            header("Location: logout.php");
        }
    ?>

</head>
<body>
    <!-- Navigation Bar -->
    <?php require('phpTemplates/navigationBar.php'); ?>

    <section class="content">
        <h1 class="header-title">Heartbeat</h1>
        <div class="header-charms">

            <!-- Search for Heartbeat -->
            <form method="get" action="heartbeat.php">
                <input id="registration" type="text" placeholder="Search for Registration..."></input>
                <input id="button" type="submit" value="Search"></input>
            </form>

        </div>
        <section id="inventory-splash-noitems" class="inventory-splash hidden">
            <img src="img/no-items.jpg" /><br /><br />
            Sorry, there's nothing to show. Try searching for something else.
        </section>

        <div class="heartbeatVehicle">
            <span class="heartbeatVehicleRegistration">
                UF0R1A
            </span>
            <span class="heartbeatVehicleInfo">
                Trip 1 - 29-09-2021 20:07:00
            </span>
            <span class="heartbeatVehicleLink material-icons-outlined">
                read_more
            </span>
            <span class="heartbeatVehicleStatus">
                <span class="heartbeatVehicleStatusLabel back-red">
                    TEMP WARN
                </span>
                <span class="heartbeatVehicleStatusLabel back-green">
                    SYNCED
                </span>
            </span>
            
        </div>

        <section id="loading-animation" class="loading-animation hidden">
            <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
        </section>
    </section>
</body>
</html>