<!DOCTYPE html>
<html lang="en">
<head>
    <title> Fleet Inspector | SDMMS Console </title>
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
        <h1 class="header-title">Data Console</h1>
        <div class="header-charms">
            <form>
            <span class="material-icons-outlined">filter_alt</span> Filter & Sort Data: 
                <select id="filterTypeField">
                    <option value="none" selected>Filter data by... </option>
                    <?php getColumnNamesForSelectInput() ?>
                </select>
                <select id="filterOrderField">
                    <option value="asc" selected>Ascending</option>
                    <option value="desc">Descending</option>
                </select>
                <input id="button resetButton" type="reset" value="Reset Filter"></input>
                <input id="button resetButton" type="submit" value="Apply Filter"></input>
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
        <?php executeQuery() ?>
        <section id="loading-animation" class="loading-animation hidden">
            <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
        </section>
    </section>
</body>
</html>