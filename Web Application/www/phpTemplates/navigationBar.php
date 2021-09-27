<section class="nav">
    <section class="nav-logo">
        SDMMS
    </section>
    <section class="nav-button">
        <a class="nav-link" href="dataConsole.php">
            <span class="material-icons material-icons-outlined">
                view_list
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