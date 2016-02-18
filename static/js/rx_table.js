$(document).ready(function() {
    $('#id_rx_form').submit(function(event) {
        event.preventDefault();
        var weight = $('#id_weight').val();
        var resort = false;

        $.get('/calc/injection/', {weight:weight}, function(data) {
            var calc_output = $('<div />').append(data).find('#id_rx_table').html();
            var errors = $('<div />').append(data).find('#id_rx_errors').html();
            $('#id_rx_table').html(calc_output).trigger('updateAll', [resort]);
            $('#id_rx_errors').html(errors);
        });
    });
});