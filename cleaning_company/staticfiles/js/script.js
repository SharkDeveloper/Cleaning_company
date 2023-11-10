$(document).ready(function() {
    $('.services-button').click(function() {
        window.location.href = '/services/';
    });
    $('#select-1').click(function() {
        $(this).text('SELECTED!');
        $('#order-input').val(0);
        $('#select-2').text('SELECT');
        $('#select-3').text('SELECT');
        $('#plan-1').addClass('active');
        $('#plan-2').removeClass('active');
        $('#plan-3').removeClass('active');
    });
    $('#select-2').click(function() {
        $(this).text('SELECTED!');
        $('#order-input').val(1);
        $('#select-1').text('SELECT');
        $('#select-3').text('SELECT');
        $('#plan-2').addClass('active');
        $('#plan-1').removeClass('active');
        $('#plan-3').removeClass('active');
    });
    $('#select-3').click(function() {
        $(this).text('SELECTED!');
        $('#order-input').val(2);
        $('#select-2').text('SELECT');
        $('#select-1').text('SELECT');
        $('#plan-3').addClass('active');
        $('#plan-1').removeClass('active');
        $('#plan-2').removeClass('active');
    });


});