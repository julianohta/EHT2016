$(document).ready(function() {
	$('.inspect').click(function(e) {
		if($(this).html() == '<i class="material-icons">zoom_in</i>') {
			$(this).parent('div').children('.expand').show(350);
			$(this).html('<i class="material-icons">zoom_out</i>');
		} else {
			$(this).parent('div').children('.expand').hide(350);
			$(this).html('<i class="material-icons">zoom_in</i>');
		}
	});

	$('.chip').click(function(e) {
		$('.chip.active').removeClass("active");
		$(this).addClass("active");
	});
});