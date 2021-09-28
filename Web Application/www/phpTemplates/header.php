<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="xenixStyle.css" />
<script src="js/jquery-3.3.1.min.js"></script>
<script src="js/xenixScript.js"></script>
<link rel="apple-touch-icon" sizes="180x180" href="/img/favicon/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="/img/favicon/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/img/favicon/favicon-16x16.png">
<link rel="manifest" href="/img/favicon/site.webmanifest">

<div id="buildHeader" style="position: fixed; bottom: 4px; left: 4px;">
    SDMMS dev build - <span id="buildHeaderDateTime"></span>

    <script>
        var dt = new Date().toDateString();
        document.getElementById('buildHeaderDateTime').innerHTML=dt;
    </script>
</div>