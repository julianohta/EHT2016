$(document).ready(function() {
	function sort_by(type) {
		if(type == "time") {
			var element_dates = [];
			for(var i = 0; i < $('.info-cards').length; i++) {
				var date_ms = Date.parse($('#row' + i).find(".date").text());
				if(isNaN(date_ms))
					date_ms = 0;
				var split_clock = ($('#row' + i).find(".time").text()).split(":");
				var hours_ms = parseInt(split_clock[0]) * 60 * 60 * 100;
				var mins_ms = parseInt(split_clock[1]) * 60 * 100;
				element_dates[i] = [i, date_ms + hours_ms + mins_ms];
			}	
			element_dates.sort(function(a, b){return b[1]-a[1]});

			$('.info-cards').hide(200);
			var last_elem;
			if($('.info-cards').length > 0)
				last_elem = $('#row' + element_dates[0][0]).show(200);

			for(var i = 1; i < $('.info-cards').length; i++) {
				$('#row' + element_dates[i][0]).insertAfter(last_elem);
				last_elem = $('#row' + element_dates[i][0]).show(200);
			}
		}	
	}

	$('.responsive-table').hide();

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

		if($(this).attr("data-id") == "time")
			sort_by("time");
	});
});