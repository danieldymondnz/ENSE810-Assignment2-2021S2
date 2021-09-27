<!DOCTYPE html>
<html>
<head>
    <title> SDMMS Console </title>
    <!-- Header Template -->
    <?php require('phpTemplates/header.php'); ?>
</head>
<script>
    function updateView() {
        replaceConnectionAddress();
    }
</script>
<body class="sessionBody" onLoad="updateView()">

   <section class="floatingSessionContainer">
        <h1 class="header-title header-title-login">Kia Ora</h1>
        <p>To access information on this system, you will need to login</p>
        <p id="connectionAddress" style="font-style: italic;"><i>localhost</i></p>
        <br></br>
        <form method="post" action="login.php">
            <input type="submit" value="Log In"/>
        </form>
    </section>

    <!-- Floating Session Logo Template -->
    <?php require('phpTemplates/floatingSessionLogo.php'); ?>

</body>