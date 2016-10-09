function format_num(num) {
  if(num < 10)
    return "0" + num;
  else
    return num;
}

$(document).ready(function() {
  $('#report_frm').multipage({
      'generateNavigation': false
  });

	var d = new Date();
	$('input[name="time"]').val(format_num(d.getHours()) + ":" + format_num(d.getMinutes()));

	$('.datepicker').pickadate({
	    selectMonths: true, // Creates a dropdown to control month
	    selectYears: 15 // Creates a dropdown of 15 years to control year
	 });

  $('.next').click(function(e) {
    $('#report_frm').nextpage();
  });
  $('.back').click(function(e) {
    $('#report_frm').prevpage();
  });

	var next_vic = 0;
    $(".add-victim").click(function(e){
        e.preventDefault();
        next_vic += 1;

        var new_input = '<div><div class="row"><div class="input-field col offset-l2 l8 s12">' +
        					'<input type="text" class="validate" name="victim[' + next_vic + ']-name">' +
            				'<label for="victim[' + next_vic + ']-name">Name</label>' +
        				'</div></div>' +
                '<div class="row"><div class="input-field col offset-l2 l8 s12">' +
            				'<input type="text" class="validate" name="victim[' + next_vic + ']-alias">' +
            				'<label for="victim[' + next_vic + ']-alias">Aliases</label>' +
        				'</div></div>' +
        				'<div class="row"><div class="input-field col offset-l2 l4 s6">' +
        					'<select name="victim[' + next_vic + ']-ethnicity">' +
      							'<option value="unknown" selected>Select</option>' +
      							'<option value="white">White</option>' +
      							'<option value="latino">Hispanic/Latino</option>' +
     							'<option value="black">Black</option>' +
     							'<option value="asian">Asian</option>' +
     							'<option value="native">Native American</option>' +
     							'<option value="other">Other</option>' +
    						'</select>' +
    						'<label>Ethnicity</label>' +
        				'</div><div class="input-field col l4 s6">' +
        					'<select name="victim[' + next_vic + ']-gender">' +
      							'<option value="unknown" selected>Select</option>' +
      							'<option value="male">Male</option>' +
      							'<option value="female">Female</option>' +
    						'</select>' +
    						'<label>Gender</label>' +
        				'</div></div>' +
        				'<div class="row"><div class="input-field col offset-l2 l8 s12">' +
        					'<input type="text" class="validate" name="victim[' + next_vic + ']-age">' +
            				'<label for="victim[' + next_vic + ']-age">Age</label>' +
        				'</div></div>' +
                '<div class="row"><div class="input-field col offset-l2 l4 s6">' +
                  '<select name="victim[' + next_vic + ']-eyes">' +
                    '<option value="unknown" selected>Select</option>' +
                    '<option value="amber">Amber</option>' +
                    '<option value="blue">Blue</option>' +
                    '<option value="brown">Brown</option>' +
                    '<option value="green">Green</option>' +
                    '<option value="hazel">Hazel</option>' +
                  '</select>' +
                  '<label>Eye Color</label>' +
        				'</div><div class="input-field col l4 s6">' +
                  '<select name="victim[' + next_vic + ']-hair">' +
                      '<option value="unknown" selected>Select</option>' +
                      '<option value="black">Black</option>' +
                      '<option value="blond">Blond</option>' +
                      '<option value="brown">Brown</option>' +
                      '<option value="red">Red</option>' +
                      '<option value="other">Other</option>' +
                    '</select>' +
                    '<label>Hair Color</label>' +
        				'</div></div>' +
                '<div class="row"><div class="input-field col offset-l2 l8 s12">' +
            				'<input type="text" class="validate" name="victim[' + next_vic + ']-build">' +
            				'<label for="victim[' + next_vic + ']-build">Build</label>' +
        				'</div></div>' +
        				'<div class="row"><div class="input-field col offset-l2 l2 s3">' +
        					'<select name="victim[' + next_vic + ']-height-ft">' +
      							'<option value="-1" selected>Select</option>' +
      							'<option value="0">0</option><option value="1">1</option>' +
      							'<option value="2">2</option><option value="3">3</option>' +
      							'<option value="4">4</option><option value="5">5</option>' +
      							'<option value="6">6</option><option value="7">7</option>' +
    						'</select><label>Feet</label></div>' +
    						'<div class="input-field col l2 s3">' +
        					'<select name="victim[' + next_vic + ']-height-in">' +
      							'<option value="-1" selected>Select</option>' +
      							'<option value="0">0</option><option value="1">1</option>' +
      							'<option value="2">2</option><option value="3">3</option>' +
      							'<option value="4">4</option><option value="5">5</option>' +
      							'<option value="6">6</option><option value="7">7</option>' +
      							'<option value="8">8</option><option value="9">9</option>' +
      							'<option value="10">10</option><option value="11">11</option>' +
    						'</select><label>Inches</label></div>' +
        				'<div class="input-field col l4 s6">' +
            				'<input type="text" class="validate" name="victim[' + next_vic + ']-weight">' +
            				'<label for="victim[' + next_vic + ']-weight">Weight</label>' +
        				'</div></div>' +
        				'<div class="row"><div class="input-field col offset-l2 l8 s12">' +
        					'<input type="text" class="validate" name="victim[' + next_vic + ']-mods">' +
            				'<label for="victim[' + next_vic + ']-mods">Body Modifications</label>' +
        				'</div></div>' +
                '<div class="row"><div class="input-field col offset-l2 l8 s12">' +
            				'<input type="text" class="validate" name="victim[' + next_vic + ']-clothing">' +
            				'<label for="victim[' + next_vic + ']-clothing">Clothing</label>' +
        				'</div></div>' +
        				'<div class="row"><div class="input-field col offset-l2 l8 s12">' +
            				'<input type="text" class="validate" name="victim[' + next_vic + ']-comments">' +
            				'<label for="victim[' + next_vic + ']-comments">Comments</label>' +
        				'</div></div>' +
        				'<div class="row"><div class="remove-victim btn col offset-l2">Remove Victim</div></div></div>';

        $("#victims").append(new_input);
       	$('#victim_cnt').val((parseInt($('#victim_cnt').val()) + 1).toString());

        $('select').material_select();

        $('.remove-victim').click(function(e){
        	e.preventDefault(); $(this).parent('div').parent('div').remove();
    	})
    });

	var next_traf = 0;
    $(".add-trafficker").click(function(e){
        e.preventDefault();
        next_traf += 1;

        var new_input = '<div><div class="row"><div class="input-field col offset-l2 l8 s12">' +
                  '<input type="text" class="validate" name="trafficker[' + next_traf + ']-name">' +
                    '<label for="trafficker[' + next_traf + ']-name">Name</label>' +
                '</div></div>' +
                '<div class="row"><div class="input-field col offset-l2 l8 s12">' +
                    '<input type="text" class="validate" name="trafficker[' + next_traf + ']-alias">' +
                    '<label for="trafficker[' + next_traf + ']-alias">Aliases</label>' +
                '</div></div>' +
                '<div class="row"><div class="input-field col offset-l2 l4 s6">' +
                  '<select name="trafficker[' + next_traf + ']-ethnicity">' +
                    '<option value="unknown" selected>Select</option>' +
                    '<option value="white">White</option>' +
                    '<option value="latino">Hispanic/Latino</option>' +
                  '<option value="black">Black</option>' +
                  '<option value="asian">Asian</option>' +
                  '<option value="native">Native American</option>' +
                  '<option value="other">Other</option>' +
                '</select>' +
                '<label>Ethnicity</label>' +
                '</div><div class="input-field col l4 s6">' +
                  '<select name="trafficker[' + next_traf + ']-gender">' +
                    '<option value="unknown" selected>Select</option>' +
                    '<option value="male">Male</option>' +
                    '<option value="female">Female</option>' +
                '</select>' +
                '<label>Gender</label>' +
                '</div></div>' +
                '<div class="row"><div class="input-field col offset-l2 l8 s12">' +
                  '<input type="text" class="validate" name="trafficker[' + next_traf + ']-age">' +
                    '<label for="trafficker[' + next_traf + ']-age">Age</label>' +
                '</div></div>' +
                '<div class="row"><div class="input-field col offset-l2 l4 s6">' +
                  '<select name="trafficker[' + next_traf + ']-eyes">' +
                    '<option value="unknown" selected>Select</option>' +
                    '<option value="amber">Amber</option>' +
                    '<option value="blue">Blue</option>' +
                    '<option value="brown">Brown</option>' +
                    '<option value="green">Green</option>' +
                    '<option value="hazel">Hazel</option>' +
                  '</select>' +
                  '<label>Eye Color</label>' +
                '</div><div class="input-field col l4 s6">' +
                  '<select name="trafficker[' + next_traf + ']-hair">' +
                      '<option value="unknown" selected>Select</option>' +
                      '<option value="black">Black</option>' +
                      '<option value="blond">Blond</option>' +
                      '<option value="brown">Brown</option>' +
                      '<option value="red">Red</option>' +
                      '<option value="other">Other</option>' +
                    '</select>' +
                    '<label>Hair Color</label>' +
                '</div></div>' +
                '<div class="row"><div class="input-field col offset-l2 l8 s12">' +
                    '<input type="text" class="validate" name="trafficker[' + next_traf + ']-build">' +
                    '<label for="trafficker[' + next_traf + ']-build">Build</label>' +
                '</div></div>' +
                '<div class="row"><div class="input-field col offset-l2 l2 s3">' +
                  '<select name="trafficker[' + next_traf + ']-height-ft">' +
                    '<option value="-1" selected>Select</option>' +
                    '<option value="0">0</option><option value="1">1</option>' +
                    '<option value="2">2</option><option value="3">3</option>' +
                    '<option value="4">4</option><option value="5">5</option>' +
                    '<option value="6">6</option><option value="7">7</option>' +
                '</select><label>Feet</label></div>' +
                '<div class="input-field col l2 s3">' +
                  '<select name="trafficker[' + next_traf + ']-height-in">' +
                    '<option value="-1" selected>Select</option>' +
                    '<option value="0">0</option><option value="1">1</option>' +
                    '<option value="2">2</option><option value="3">3</option>' +
                    '<option value="4">4</option><option value="5">5</option>' +
                    '<option value="6">6</option><option value="7">7</option>' +
                    '<option value="8">8</option><option value="9">9</option>' +
                    '<option value="10">10</option><option value="11">11</option>' +
                '</select><label>Inches</label></div>' +
                '<div class="input-field col l4 s6">' +
                    '<input type="text" class="validate" name="trafficker[' + next_traf + ']-weight">' +
                    '<label for="trafficker[' + next_traf + ']-weight">Weight</label>' +
                '</div></div>' +
                '<div class="row"><div class="input-field col offset-l2 l8 s12">' +
                  '<input type="text" class="validate" name="trafficker[' + next_traf + ']-mods">' +
                    '<label for="trafficker[' + next_traf + ']-mods">Body Modifications</label>' +
                '</div></div>' +
                '<div class="row"><div class="input-field col offset-l2 l8 s12">' +
                    '<input type="text" class="validate" name="trafficker[' + next_traf + ']-clothing">' +
                    '<label for="trafficker[' + next_traf + ']-clothing">Clothing</label>' +
                '</div></div>' +
                '<div class="row"><div class="input-field col offset-l2 l8 s12">' +
                    '<input type="text" class="validate" name="trafficker[' + next_traf + ']-comments">' +
                    '<label for="trafficker[' + next_traf + ']-comments">Comments</label>' +
                '</div></div>' +
                '<div class="row"><div class="remove-trafficker btn col offset-l2">Remove trafficker</div></div></div>';

        $("#traffickers").append(new_input);
       	$('#trafficker_cnt').val((parseInt($('#trafficker_cnt').val()) + 1).toString());

        $('select').material_select();

        $('.remove-trafficker').click(function(e){
        	e.preventDefault(); $(this).parent('div').remove();
    	})
    });
    
    $( ".add-victim" ).trigger( "click" );
    $( ".add-trafficker" ).trigger( "click" );
});