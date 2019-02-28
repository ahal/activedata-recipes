function handleErrors(response) {
    if (!response.ok) {
        return response.text().then(function (value) {
            throw Error(value);
        })

    }
    else return response.json();
}

function get(url, callback, error) {
    fetch(url)
        .then(handleErrors)
        .then(callback)
        .catch(error);
}

// Builds the HTML Table out of myList.
function buildHtmlTable(output, response) {
    // Header - item 0
    var header = $('<tr/>');
    var headerData = response.shift();
    headerData.forEach(function(headerCell){
        header.append($('<th/>').html(headerCell));
    });
    output.append(header);

    // Data - the rest
    response.forEach(function(rowData) {
        var row = $('<tr/>');
        rowData.forEach(function(cellData){
            row.append($('<td/>').html(cellData));
        });
        $(output).append(row);
    });
}

function runRecipe(url, params) {
    var recipe = url.substr(url.lastIndexOf('/') + 1);
    var api_url = "api/v1/" + recipe + "?" + params;
    $("#submit_button").addClass("is-loading");
    var output = $("#recipe_result").empty()
    get(api_url, function(response) {
        $("#submit_button").removeClass("is-loading");
        buildHtmlTable(output, response);

        // Update URL if there is diff
        var loc = url + '?' + params;
        if (loc !== window.location.href) {
            // console.log(loc);
            window.history.pushState("object or string", "Active Data Recipe - " + recipe, loc);
        }
    }, function(error){
        // Clear loading, show error message
        $("#error_msg").html(error.message);
        $("#submit_button").removeClass("is-loading");
    });
}

$(function(){
    var loc = window.location.href.split('?');
    var url = loc[0];
    var params = loc[1];
    if (params) {
        runRecipe(url, params);
    }

    $("#recipe_input").submit(function(event) {
        // stop form from submitting normally
        event.preventDefault();

        // get the action attribute from the <form action=""> element
        var form = $(this);
        runRecipe(url, form.serialize());
    });
});


$(function() {

    $('input[name="daterange"]').daterangepicker({
        "singleDatePicker": true,
        "showDropdowns": true,
        ranges: {
            //Relative time: https://github.com/mozilla/ActiveData/blob/dev/docs/jx_time.md
            'now': [moment()],
            'today': [moment().startOf('day')],
            'eod': [moment().endOf('day')],
            'today-week': [moment().startOf('day').subtract(7, 'days')],
            // 'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
        },
        // TODO: set as default value
        "startDate": moment().format("MM/DD/YYYY"),
        "endDate": moment().format("MM/DD/YYYY")
    }, function(start, end, label) {
        console.log('New date range selected: ' + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD') + ' (predefined range: ' + label + ')');
    });
});


