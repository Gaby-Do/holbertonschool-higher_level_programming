$(document).ready(function () {
    $.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
        $.each(data.results, function (_index, value) {
            $("#list_movies").append("<li>" + value.title + "</li>");
        });
    });
});