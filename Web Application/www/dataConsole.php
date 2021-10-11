<!DOCTYPE html>
<html lang="en">
<head>
    <title> Data Console | DMS Console </title>
    <?php require('phpTemplates/header.php'); ?>
    <?php require('phpTemplates/sessionVerification.php'); ?>
    <?php
        
        if (isset($_GET['startVal'])) 
        {
            if ($_GET['startVal'] == "<")
                $_SESSION["startIndex"] = decreaseRange();
            else
                $_SESSION["startIndex"] = increaseRange();
        }

    ?>

</head>
<body>
    <!-- Navigation Bar -->
    <?php require('phpTemplates/navigationBar.php'); ?>

    <section class="content">
        <h1 class="header-title">Data Console</h1>
        <div class="header-charms">

            <!-- Filters for Data Console -->
            <form method="get" action="dataConsole.php">
                Sort by 
                <select name="filterTypeField">
                    <?php getColumnNamesForSelectInput() ?>
                </select>
                 in 
                <select name="filterOrderField">
                    <?php getFiltersForSelectInput() ?>
                </select>
                 order
                <input id="button" type="submit" value="Apply"></input>
                <input id="button" type="reset" value="Reset"></input>
                <span style="display: inline-block; width: 20px;"></span>
                <input name="startVal" type="submit" value="<"></input>
                <span id="num"><?php getCurrentRange() ?></span>
                <input name="startVal" type="submit" value=">"></input>
            </form>

        </div>
        <?php 

            if (isset($_GET['filterTypeField']) && isset($_GET['filterOrderField'])) {
                queryByFilter($_GET['filterTypeField'], $_GET['filterOrderField'], $_SESSION["startIndex"]);
            } else {
                executeDefaultQuery();
            }
        
        ?>
    </section>
</body>
</html>