
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

// ------------------------ OLD VV

function inventoryShowSplashNoItems() {
    $('#inventory-splash-noitems').removeClass('hidden');
    $('#inventory-splash-welcome').addClass('hidden');
    $('#loading-animation').addClass('hidden');
}

function inventoryShowSplashWelcome() {
    $('#inventory-splash-noitems').addClass('hidden');
    $('#inventory-splash-welcome').removeClass('hidden');
    $('#loading-animation').addClass('hidden');
}

function inventoryShowLoadingAnimation() {
    $('#inventory-splash-noitems').addClass('hidden');
    $('#inventory-splash-welcome').addClass('hidden');
    $('#loading-animation').removeClass('hidden');
}

function inventoryShowSearchResults() {
    $('#inventory-splash-noitems').addClass('hidden');
    $('#inventory-splash-welcome').addClass('hidden');
    $('#loading-animation').addClass('hidden');
}

function constructor(id, name, inOut, isMissing, isRetired, location) {
    var construct = "<div class='inventory-result-entry'><div class='inventory-result-entry-id'>";
    construct += id;
    construct += "</div><div class='inventory-result-entry-name'>";
    construct += name;
    construct += "</div><div class='inventory-result-entry-location ";
    if (isMissing == true) {
        construct += "back-red'> MISSING - LAST SEEN: ";
    } else if (inOut == 'in') {
        construct += "back-green'> IN - ";
    } else if (inOut == 'out') {
        construct += "back-orange'> OUT - ";
    }
    construct += location;
    construct += "</div></div>";
    $('.inventory-results').append(construct);
}

function inventorySearchL() {
    var searchQuery = $('#searchField').val();
    var searchQueryStripped;
    var searchResults = [];
    clearTimeout(searchTimeOut);
    searchTimeOut = setTimeout(function () {

        // Show loading animation, check to see if more than 3 characters have been entered
        $('.inventory-results').empty();
        inventoryShowLoadingAnimation();
        if (searchQuery.length < 3) {
            inventoryShowSplashWelcome();
        } else {


          

            // If the query could be an ID
            if (searchQuery.length == 20 && searchQuery.includes(" ") !== true) {
                inventoryStore.doc(searchQuery).get().then(function (doc) {
                    if (doc.exists) {
                        searchResults.push(doc.id);
                        console.log("HIT " + doc.id);
                        constructor(doc.id, doc.data().itemName, doc.data().itemInOut, doc.data().itemIsMissing, doc.data().itemIsRetired, doc.data().itemLocation);
                    } else {
                        // doc.data() will be undefined in this case
                        console.log("No such document!");
                    }
                }).catch(function (error) {
                    console.log("Error getting document:", error);
                }).then(function () {
                    // Wait Here for Promise
                    if (searchResults.length <= 0) {
                        inventoryShowSplashNoItems();
                    } else {
                        inventoryShowSearchResults();
                    }
                });

            }

            // Or else, run query based on Tags
            else {
                inventoryShowSplashNoItems();
            }

        }
    }, 500);
}

function inventorySearch() {

    var searchQuery = $('#searchField').val();
    var searchQueryStripped = searchQuery.split(' ');
    var searchResults = [];
    console.log(searchQueryStripped);
    clearTimeout(searchTimeOut);
    searchTimeOut = setTimeout(function () {

        // Show loading animation, check to see if more than 3 characters have been entered
        $('.inventory-results').empty();
        inventoryShowLoadingAnimation();
        if (searchQuery.length < 3) {
            inventoryShowSplashWelcome();
        } else if (true) {

            // GO through each db item
            inventoryStore.orderBy("itemName").get().then(function (querySnapshot) {
                querySnapshot.forEach(function (doc) {

                    var match = false;

                    if (doc.id == searchQuery) {
                        constructor(doc.id, doc.data().itemName, doc.data().itemInOut, doc.data().itemIsMissing, doc.data().itemIsRetired, doc.data().itemLocation);
                        match = true;
                        inventoryShowSearchResults();
                    } else {
                        
                        var i = 0;

                        while (match !== true && i < searchQueryStripped.length) {
                            console.log(searchQueryStripped[i]);
                            console.log(doc.data().itemTags.length);

                            var j = 0;
                            while (match !== true && j < doc.data().itemTags.length) {
                                console.log(doc.data().itemTags[j]);
                                if (searchQueryStripped[i].toLowerCase() == doc.data().itemTags[j].toLowerCase()) {
                                    constructor(doc.id, doc.data().itemName, doc.data().itemInOut, doc.data().itemIsMissing, doc.data().itemIsRetired, doc.data().itemLocation);
                                    match = true;
                                }
                                j++;
                            }
                            i++;
                        }

                        if (match) {
                            inventoryShowSearchResults();
                        } else {
                            inventoryShowSplashNoItems();
                        }
                    }
                });
            });

        } else {
            inventoryShowSplashNoItems();
        }

    }, 500);
    

}



function testPush() {
    inventoryStore.add({

        itemName: "Test Item Name 1",
        itemDescription: "This is a description",
        itemInOut: "out",
        itemLocation: 6,
        itemLastLogDate: "16/03/2008",
        itemIsMissing: true,
        itemIsRetired: false,
        itemLog: null,
        itemLinks: null,
        itemTags: [
            "Test",
            "Item",
            "Name",
            "1"
        ]

    })
        .then(function (docRef) {
            console.log("Document written with ID: ", docRef.id);

        })
        .catch(function (error) {
            console.error("Error adding document: ", error);
        });

}