<section class="nav">
    <section class="nav-logo">
        <a class="nav-link" href="home.php">
            SDMMS
        </a>
    </section>
    <section class="nav-button">
        <a class="nav-link" href="">
            <span class="material-icons material-icons-outlined">
                monitor_heart
            </span> Status - disabled
        </a>
    </section>
    <section class="nav-button">
        <a class="nav-link" href="">
            <span class="material-icons material-icons-outlined">
                policy
            </span> Fleet Inspector - disabled
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