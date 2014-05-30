function responsivize() {
  $('.responsive')
    .css({
      height: $(window).height()-50 + 'px',
      width:  $(window).width() + 'px'
    });
}

$(document).ready(function() {
  
  $('#tiles li').wookmark({
		autoResize: true, // This will auto-update the layout when the browser window is resized.
		container: $('#tiles'), // Optional, used for some extra CSS styling
		offset: 3, // Optional, the distance between grid items
		itemWidth: 300 // Optional, the width of a grid item
	});
  
  $('.featured-image').imgLiquid();
  responsivize();
  $(window).on('resize', responsivize);
  
});