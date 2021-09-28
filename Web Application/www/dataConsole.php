﻿<!DOCTYPE html>
<html lang="en">
<head>
    <title> Data Console | SDMMS Console </title>
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
        <h1 class="header-title">Data Console</h1>
        <div class="header-charms">

            <!-- Filters for Data Console -->
            <form method="get" action="dataConsole.php">
                <span class="material-icons-outlined">filter_alt</span> Filter & Sort Data: 
                <select name="filterTypeField">
                    <?php getColumnNamesForSelectInput() ?>
                </select>
                <select name="filterOrderField">
                    <option value="ASC">Ascending</option>
                    <option value="DESC">Descending</option>
                </select>
                <input id="button" type="reset" value="Reset Filter"></input>
                <input id="button" type="submit" value="Apply Filter"></input>
            </form>

        </div>
        <section id="inventory-splash-noitems" class="inventory-splash hidden">
            <img src="img/no-items.jpg" /><br /><br />
            Sorry, there's nothing to show. Try searching for something else.
        </section>
        <?php 
        
            if (isset($_GET['filterTypeField']) && isset($_GET['filterOrderField'])) {
                queryByFilter($_GET['filterTypeField'], $_GET['filterOrderField']);
            } else {
                executeDefaultQuery();
            }
        
        ?>
        <section id="loading-animation" class="loading-animation hidden">
            <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
        </section>
    </section>
</body>
<?php

        
            

?>
</html>