$(document).ready(function() {

    selectors = [];

    var hyphenatorSettings = {
       selectorfunction: function () {
            return $(selectors.join(',')).get();
       }
    };  

    $.get(PORTAL_URL + '/@@hyphenator-configuration').success(function(data) {
        data = $.parseJSON(data);
        selectors = data['selectors'];
        hyphenatorSettings['minwordlength'] = data['minwordlength'];
        hyphenatorSettings['useCSS3hyphenation'] = data['useCSS3hyphenation'];
        /*hyphenatorSettings['hyphenchar'] = data['hyphenchar'];*/
        Hyphenator.config(hyphenatorSettings);
        Hyphenator.run();
    });
});
