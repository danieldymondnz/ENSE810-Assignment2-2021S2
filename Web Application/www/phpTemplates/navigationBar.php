<section class="nav">
    <section class="nav-logo">
        <a class="nav-link" href="home.php">
            DMS
        </a>
    </section>
    <section class="nav-button">
        <a class="nav-link" href="fleetInspector.php">
            <span class="material-icons material-icons-outlined">
                policy
            </span> Fleet Inspector
        </a>
    </section>
    <section class="nav-button">
        <a class="nav-link" href="dataConsole.php">
            <span class="material-icons material-icons-outlined">
                table_chart
            </span> Data Console
        </a>
    </section>
    <section class="nav-button">
        <a class="nav-link" href="logout.php">
            <span class="material-icons material-icons-outlined">
                logout
            </span> Logout
        </a>
    </section>
    <section class="nav-user-session">
        Hello, <?php echo $_SESSION['username']; ?>
    </section>
</section>