$(window).on("load resize ", function() {
  var scrollWidth = $('.table-content').width() - $('.table-content table').width();
  $('.tbl-header').css({'padding-right':scrollWidth});
}).resize();
