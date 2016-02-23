$(document).ready(function() {
    $('submit-id-submit').submit(function(event) {
        event.preventDefault();
        var weight = $('#id_weight').val();
        var rate = $('#id_rate').val();
        var volume = $('#id_volume').val();
        var infusion = $('#id_infusion').val();

        $.get('/calc/cri/advanced/', {weight:weight, rate:rate, volume:volume, infusion:infusion}, function(data) {
            var calc_output = $('<div />').append(data).find('#id_dosages').html();
            $('#id_dosages').html(calc_output)
        });
    });
});