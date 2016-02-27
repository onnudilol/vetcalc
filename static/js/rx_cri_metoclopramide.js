$(document).ready(function() {
    $('#id_cri_metoclopramide_form').submit(function(event) {
        event.preventDefault();
        var weight = $('#id_weight').val();
        var rate = $('#id_rate').val();
        var volume = $('#id_volume').val();
        var infusion = $('#id_infusion').val();
        var inc_volume = $('#id_inc_volume').val();
        var inc_infusion = $('#id_inc_infusion').val();

        $.get('/calc/cri/metoclopramide/', {weight:weight, rate:rate, volume:volume, infusion:infusion,
            inc_volume:inc_volume, inc_infusion:inc_infusion},

            function(data) {
            var calc_output = $('<div />').append(data).find('#id_cri_metoclopramide_dosages').html();
            $('#id_cri_metoclopramide_dosages').html(calc_output)
        });
    });
});