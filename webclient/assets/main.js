function updateViews(data) {
    console.log('Starting updateViews.');
    console.log(data);
    console.log('Finishing updateViews.');

}

function sendNextQuery() {
    console.log('Starting sendNextQuery.');

    var request = $.ajax({
        method: "POST",
        url: "http://localhost/tpmj",
        data: JSON.stringify({Action: 'RandomObserve'}),
        dataType: "json",
        timeout: 1000,
    });

    request.done(function(data, textStatus, jqXHR) {
        onGameData(data);
    });

    request.fail(function(jqXHR, textStatus, errorThrown) {
        console.log('Request failed.');
        console.log(jqXHR);
        console.log(textStatus);
        console.log(errorThrown);
        onGameData({});
    });

    console.log('Finishing sendNextQuery.');
}

function onGameData(data) {
    console.log('Starting onGameData.');
    updateViews(data);
    sendNextQuery();
    console.log('Finishing sendNextQuery.');
}

$(document).ready(sendNextQuery);
