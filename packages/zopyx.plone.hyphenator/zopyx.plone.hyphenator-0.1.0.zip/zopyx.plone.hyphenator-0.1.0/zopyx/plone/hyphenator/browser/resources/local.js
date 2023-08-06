$(document).ready(function() {

    selectors = [];

    var hyphenatorSettings = {
       selectorfunction: function () {
            return $(selectors.join(' ')).get();
       }
    };  

    $.get(PORTAL_URL + '/@@hyphenator-configuration').success(function(data) {
        console.log(data);
        data = $.parseJSON(data);
        selectors = data['selectors'];
        Hyphenator.config(hyphenatorSettings);
        Hyphenator.run();
    });
});
