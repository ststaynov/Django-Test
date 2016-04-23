/**
 * Created by ststa on 3/24/2016.
 */

var dataFeed;
var refreshIntervalId;

function consoleLog(l) {
    console.log(l);
}

$('.c-grades').on('click', function () {
    $(this).css('background-color','red');
});

// open menu
$header = $('.e-menu-title');

$header.on('click', function () {
    if($(this).hasClass('is-active')) {
        $('.e-menu-item').removeClass('is-active');
        $('.c-menu-overlay').removeClass('is-active');
    } else{
        $('.e-menu-item').addClass('is-active');
        $('.c-menu-overlay').addClass('is-active');
    }
});

// close menu when overlay is clicked
$('.c-menu-overlay').on('click', function () {
    $(this).removeClass('is-active');
    $('.e-menu-item').removeClass('is-active');
});

// if span width is more than parent width, span {display:block;}


$(window).scroll(function() {

    var scroll = $(window).scrollTop();

    if (scroll > 20) {
        $header.addClass('animated').removeClass('fix');
    } else {
        $header.removeClass('animated').addClass('fix');
    }

});

// instagram
get_instagram_feed();

function get_instagram_feed() {
$.ajax({
  url: '/api/instagram/',
  error: function () {
    consoleLog('error');
  },
  success: function (data) {
    if (dataFeed != data) {
      consoleLog('update');
      $('.c-instagram').html(data);
      clearInterval(refreshIntervalId);
      //use_instagram_feed();
    }
    dataFeed = data;
  },
  type: 'GET'
});
}


//function use_instagram_feed(){
//var $divs = $('div#media');
//var count = 1;
//
//$divs.eq(0).addClass('is-shown');
//console.log('use_instagram_feed');
//refreshIntervalId = setInterval(function() {
//  console.log('In Interval');
//  $divs.eq(count - 1).removeClass('is-shown');
//  if (count == 10) {
//    $divs.eq(9).addClass('is-shown');
//    count = 0;
//  }
//  if (count == 0) {
//    $divs.eq(9).removeClass('is-shown');
//    $divs.eq(count).addClass('is-shown');
//  } else {
//    $divs.eq(count - 1).removeClass('is-shown');
//    $divs.eq(count).addClass('is-shown');
//  }
//  count++;
//}, 4000)}


/* Submit Registration Form Start */
$('span[contenteditable]').keyup(function () {
    console.log('Shit');
    $('input#id_' + $(this).attr('id')).val($(this).text());
}).trigger('keyup');

//$('#submit').on('click tap', function (e) {
//    e.preventDefault();
//});
/* Submit Registration Form End */
