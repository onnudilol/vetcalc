$(document).ready(function() {
    $('#id_cri_advanced_form').submit(function(event) {
        event.preventDefault();
        var weight = $('#id_weight').val();
        var rate = $('#id_rate').val();
        var volume = $('#id_volume').val();
        var infusion = $('#id_infusion').val();

        $.get('/calc/cri/advanced/', {weight:weight, rate:rate, volume:volume, infusion:infusion}, function(data) {
            var calc_output = $('<div />').append(data).find('#id_cri_adv_dosages').html();
            $('#id_cri_adv_dosages').html(calc_output)
        });
    });
});