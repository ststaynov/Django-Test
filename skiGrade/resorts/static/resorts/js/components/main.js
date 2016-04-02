/**
 * Created by ststa on 3/24/2016.
 */


$('.c-grades').on('click', function () {
    $(this).css('background-color','red');
});

// open menu
$('.e-menu-title').on('click', function () {
    if($(this).hasClass('is-active')) {
        $(this).removeClass('is-active');
        $('.c-menu-overlay').removeClass('is-active');
    } else{
        $(this).addClass('is-active');
        $('.c-menu-overlay').addClass('is-active');
    }
});

// close menu when overlay is clicked
$('.c-menu-overlay').on('click', function () {
    $(this).removeClass('is-active');
    $('.e-menu-title').removeClass('is-active');
});
