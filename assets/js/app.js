function responsivize() {
  $('.responsive')
    .css({
      height: $(window).height()-50 + 'px',
      width:  $(window).width() + 'px'
    });
}

$(document).ready(function() {
  
  $('.featured-image').imgLiquid();
  responsivize();
  $(window).on('resize', responsivize);
  
});