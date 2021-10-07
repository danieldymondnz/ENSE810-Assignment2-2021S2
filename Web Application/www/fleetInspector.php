<!DOCTYPE html>
<html lang="en">
<head>
    <title> Fleet Inspector | DMS Console </title>
    <?php require('phpTemplates/header.php'); ?>
    <?php require('phpTemplates/sessionVerification.php'); ?>

</head>
<body>
    <!-- Navigation Bar -->
    <?php require('phpTemplates/navigationBar.php'); ?>

    <section class="content">
        <h1 class="header-title">Fleet Inspector</h1>
        <div class="header-charms">

            <!-- Search for Heartbeat -->
            <form method="get" action="fleetInspector.php">
                <input name="registration" id="registration" type="text" placeholder="Search for Registration..."></input>
                <input id="button" type="submit" value="Search"></input>
            </form>

        </div>
        <section id="inventory-splash-noitems" class="inventory-splash hidden">
            <img src="img/no-items.jpg" /><br /><br />
            Sorry, there's nothing to show. Try searching for something else.
        </section>

        
        <?php 
            if (isset($_GET['registration'])) {
               executeInspectorQueryAndTabulate($_GET['registration']);
            } else {
                executeInspectorQueryAndTabulate("");
            }
        ?>

    </section>
</body>
</html>