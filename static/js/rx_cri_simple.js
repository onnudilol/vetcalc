$(document).ready(function() {
    $('#id_cri_simple_form').submit(function(event) {
        event.preventDefault();
        var weight = $('#id_weight').val();
        var resort = false;

        $.get('/calc/cri/simple/', {weight:weight}, function(data) {
            var calc_output = $('<div />').append(data).find('#id_cri_table').html();
            $('#id_cri_table').html(calc_output);
            window.alert('HELO');

        });
    });
});