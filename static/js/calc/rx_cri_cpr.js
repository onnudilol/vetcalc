$(document).ready(function() {
    $('#id_cri_cpr_form').submit(function(event) {
        event.preventDefault();
        var weight = $('#id_weight').val();
        var rate = $('#id_rate').val();
        var volume = $('#id_volume').val();
        var dobutamine = $('#id_dobutamine').val();
        var dopamine = $('#id_dopamine').val();
        var lidocaine = $('#id_lidocaine').val();

        $.get('/calc/cri/cpr/', {weight:weight, rate:rate, volume:volume,
            dobutamine:dobutamine, dopamine:dopamine, lidocaine:lidocaine}, function(data) {
            var calc_output = $('<div />').append(data).find('#id_cri_cpr_dosages').html();
            $('#id_cri_cpr_dosages').html(calc_output)
        });
    });
});