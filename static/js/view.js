$(document).ready(function() {
	$('.inspect').click(function(e) {

	});

	$('.chip').click(function(e) {
		$('.chip.active').removeClass("active");
		$(this).addClass("active");
	});
});