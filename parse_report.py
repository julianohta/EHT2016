def process(request):
	counter = 1
	num_vics = int(request.form["victim_cnt"])
	while counter <= num_vics:
		query = "victim[" + str(counter) + "]-name"
		if request.form.has_key(query):
			print("Name: " + request.form[query])

		counter += 1

	# var time print("Victim count: " + request.form["victim_cnt"])