<!DOCTYPE html>
<html lang="en">
<head>
    <title> Fleet Health | SDMMS Console </title>
    <?php require('phpTemplates/header.php'); ?>
    <?php require('phpTemplates/sessionVerification.php'); ?>

</head>
<body>
    <!-- Navigation Bar -->
    <?php require('phpTemplates/navigationBar.php'); ?>

    <section class="content">
        <h1 class="header-title">Fleet Health</h1>
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
                <span class="heartbeatVehicleStatusLabel back-orange">
                    TEMP WARN
                </span>
                <span class="heartbeatVehicleStatusLabel back-green">
                    SYNCED
                </span>
            </span>
            
        </div>

        <div class="heartbeatVehicle">
            <span class="heartbeatVehicleRegistration">
                BNK611
            </span>
            <span class="heartbeatVehicleInfo">
                No Trip Data Available
            </span>
            <span class="heartbeatVehicleLink material-icons-outlined">
                read_more
            </span>
            <span class="heartbeatVehicleStatus">
                <span class="heartbeatVehicleStatusLabel back-red">
                    HEARTBEAT MISSED
                </span>
            </span>
            
        </div>
            <!-- SELECT REGISTRATION FROM `VEHICLES` -->
    </section>
</body>
</html>