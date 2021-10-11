// Session Management Screen Functions

function replaceConnectionAddress() {
    var connectionAddress = window.location.href;
    let domain = (new URL(connectionAddress));
    connectionAddress = domain.hostname;
    $('#connectionAddress').empty();
    $('#connectionAddress').append(connectionAddress);
}

function displayLoginFail() {
    $('#username').addClass('back-red');
    $('#password').addClass('back-red');
    $('#submissionOutcome').empty();
    $('#submissionOutcome').append("Log In failed. Please check your credentials and try again.");
}

function displayLoginSuccess() {
    $('#username').addClass('back-green');
    $('#password').addClass('back-green');
    $('#submissionOutcome').empty();
    $('#submissionOutcome').append("Authentication Successful. Redirecting...");
}

function updateResults(stringText) {
    $('.inventory-results').empty();
    $('.inventory-results').append(stringText);
}

function constructResultsHeader() {
    $('.inventory-results').append("<table class='data-console-table'><tr><th>uid</th><th>Timestamp</th><th>Temperature</th></tr></table>");
}