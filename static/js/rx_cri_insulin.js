$(document).ready(function() {
    $('#id_cri_insulin_form').submit(function(event) {
        event.preventDefault();
        var weight = $('#id_weight').val();
        var rate = $('#id_rate').val();
        var volume = $('#id_volume').val();
        var replacement = $('#id_replacement').val();

        $.get('/calc/cri/insulin/', {weight:weight, rate:rate, volume:volume, replacement:replacement}, function(data) {
            var calc_output = $('<div />').append(data).find('#id_cri_insulin_dosages').html();
            $('#id_cri_insulin_dosages').html(calc_output)
        });
    });
});