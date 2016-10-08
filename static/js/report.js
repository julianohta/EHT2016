$(document).ready(function() {
	var d = new Date();
	$('input[name="time"]').val(d.getHours() + ":" + d.getMinutes());

	$('.datepicker').pickadate({
	    selectMonths: true, // Creates a dropdown to control month
	    selectYears: 15 // Creates a dropdown of 15 years to control year
	 });

	var next = 0;
    $(".add-victim").click(function(e){
        e.preventDefault();
        // var addto = "#field" + next;
        // var addRemove = "#field" + (next);
        next += 1;

        var new_input = '<div class="card-panel white"><div class="row"><div class="input-field col s6">' +
        					'<input id="victim[' + next + ']-name" type="text" class="validate" name="victim[' + next + ']-name">' +
            				'<label for="victim[' + next + ']-name">Name</label>' +
        				'</div><div class="input-field col s6">' +
            				'<input id="victim[' + next + ']-alias" type="text" class="validate" name="victim[' + next + ']-alias">' +
            				'<label for="victim[' + next + ']-alias">Aliases</label>' +
        				'</div></div>' +
        				'<div class="row"><div class="input-field col s6">' +
        					'<select id="victim[' + next + ']-ethnicity" name="victim[' + next + ']-ethnicity">' +
      							'<option value="" disabled selected>Select</option>' +
      							'<option value="white">White</option>' +
      							'<option value="latino">Hispanic/Latino</option>' +
     							'<option value="black">Black</option>' +
     							'<option value="asian">Asian</option>' +
     							'<option value="native">Native American</option>' +
     							'<option value="other">Other</option>' +
    						'</select>' +
    						'<label>Ethnicity</label>' +
        				'</div><div class="input-field col s6">' +
        					'<select id="victim[' + next + ']-gender" name="victim[' + next + ']-gender">' +
      							'<option value="" disabled selected>Select</option>' +
      							'<option value="male">Male</option>' +
      							'<option value="female">Female</option>' +
    						'</select>' +
    						'<label>Gender</label>' +
        				'</div></div>' +
        				'<div class="row"><div class="input-field col s6">' +
        					'<input id="victim[' + next + ']-age" type="text" class="validate" name="victim[' + next + ']-age">' +
            				'<label for="victim[' + next + ']-age">Age</label>' +
        				'</div><div class="input-field col s6">' +
            				'<input id="victim[' + next + ']-eyes" type="text" class="validate" name="victim[' + next + ']-eyes">' +
            				'<label for="victim[' + next + ']-eyes">Eyes</label>' +
        				'</div></div>' +
        				'<div class="row"><div class="input-field col s6">' +
        					'<input id="victim[' + next + ']-hair" type="text" class="validate" name="victim[' + next + ']-hair">' +
            				'<label for="victim[' + next + ']-hair">Hair</label>' +
        				'</div><div class="input-field col s6">' +
            				'<input id="victim[' + next + ']-build" type="text" class="validate" name="victim[' + next + ']-build">' +
            				'<label for="victim[' + next + ']-build">Build</label>' +
        				'</div></div>' +
        				'<div class="row"><div class="input-field col s6">' +
        					'<input id="victim[' + next + ']-height" type="text" class="validate" name="victim[' + next + ']-height">' +
            				'<label for="victim[' + next + ']-height">Height</label>' +
        				'</div><div class="input-field col s6">' +
            				'<input id="victim[' + next + ']-weight" type="text" class="validate" name="victim[' + next + ']-weight">' +
            				'<label for="victim[' + next + ']-weight">Weight</label>' +
        				'</div></div>' +
        				'<div class="row"><div class="input-field col s6">' +
        					'<input id="victim[' + next + ']-mods" type="text" class="validate" name="victim[' + next + ']-mods">' +
            				'<label for="victim[' + next + ']-mods">Body Modifications</label>' +
        				'</div><div class="input-field col s6">' +
            				'<input id="victim[' + next + ']-clothing" type="text" class="validate" name="victim[' + next + ']-clothing">' +
            				'<label for="victim[' + next + ']-clothing">Clothing</label>' +
        				'</div></div>' +
        				'<div class="row"><div class="input-field col s12">' +
        					'<textarea id="victim[' + next + ']-comments" class="materialize-textarea"></textarea>' +
            				'<label for="victim[' + next + ']-comments">Other Comments</label>' +
        				'</div></div>' +
        				'<a class="remove-victim btn"><i class="material-icons right">delete</i>Remove Victim</a>' +
        				'</div>';

        $("#victims").append(new_input);

        $('select').material_select();

        $('.remove-victim').click(function(e){
        	e.preventDefault(); $(this).parent('div').remove();
    	})
        // var newIn = '<input autocomplete="off" class="input form-control" id="field' + next + '" name="field' + next + '" type="text">';
        // var newInput = $(newIn);
        // var removeBtn = '<button id="remove' + (next - 1) + '" class="btn btn-danger remove-me" >-</button></div><div id="field">';
        // var removeButton = $(removeBtn);
        // $(addto).after(newInput);
        // $(addRemove).after(removeButton);
        // // $("#field" + next).attr('data-source',$(addto).attr('data-source'));
        // $("#count").val(next);  
        
        //     $('.remove-me').click(function(e){
        //         e.preventDefault();
        //         var fieldNum = this.id.charAt(this.id.length-1);
        //         var fieldID = "#field" + fieldNum;
        //         $(this).remove();
        //         $(fieldID).remove();
        //     });
    });
});