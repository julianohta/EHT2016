from flask import redirect, url_for, flash

def process(request, db):
    desc = request.form['description']
    location = request.form['location']
    time = request.form['time']
    date = request.form['date']
    venue_name = request.form['venue-name']
    venue_type = request.form['venue-type']

    victims = ""
    counter = 1
    num_vics = int(request.form["victim_cnt"])
    while counter <= num_vics:
        nm_query = "victim[" + str(counter) + "]-name"
        if request.form.has_key(nm_query):
            name = request.form[nm_query]
            alias = request.form["victim[" + str(counter) + "]-alias"]
            ethnicity = request.form["victim[" + str(counter) + "]-ethnicity"]
            gender = request.form["victim[" + str(counter) + "]-gender"]
            age = request.form["victim[" + str(counter) + "]-age"]
            eyes = request.form["victim[" + str(counter) + "]-eyes"]
            hair = request.form["victim[" + str(counter) + "]-hair"]
            build = request.form["victim[" + str(counter) + "]-build"]
            inches = ((int(request.form["victim[" + str(counter) + "]-height-ft"]) * 12) +
                    int(request.form["victim[" + str(counter) + "]-height-in"]))
            mods = request.form["victim[" + str(counter) + "]-mods"]
            clothing = request.form["victim[" + str(counter) + "]-clothing"]
            comments = request.form["victim[" + str(counter) + "]-comments"]

            ins_id = db.execute('insert into persons (type, name, alias, ethnicity, gender, age,' +
                'eyes, hair, build, height, mods, clothing, comments) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                [0, name, alias, ethnicity, gender, age, eyes, hair, build, inches, mods, clothing, comments])

            db.commit()
            victims += str(ins_id.lastrowid) + ","
        counter += 1

    traffickers = ""
    counter = 1
    num_vics = int(request.form["trafficker_cnt"])
    while counter <= num_vics:
        nm_query = "trafficker[" + str(counter) + "]-name"
        if request.form.has_key(nm_query):
            name = request.form[nm_query]
            alias = request.form["trafficker[" + str(counter) + "]-alias"]
            ethnicity = request.form["trafficker[" + str(counter) + "]-ethnicity"]
            gender = request.form["trafficker[" + str(counter) + "]-gender"]
            age = request.form["trafficker[" + str(counter) + "]-age"]
            eyes = request.form["trafficker[" + str(counter) + "]-eyes"]
            hair = request.form["trafficker[" + str(counter) + "]-hair"]
            build = request.form["trafficker[" + str(counter) + "]-build"]
            inches = ((int(request.form["trafficker[" + str(counter) + "]-height-ft"]) * 12) +
                    int(request.form["trafficker[" + str(counter) + "]-height-in"]))
            mods = request.form["trafficker[" + str(counter) + "]-mods"]
            clothing = request.form["trafficker[" + str(counter) + "]-clothing"]
            comments = request.form["trafficker[" + str(counter) + "]-comments"]

            nextid = db.execute('insert into persons (type, name, alias, ethnicity, gender, age,' +
                'eyes, hair, build, height, mods, clothing, comments) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                [1, name, alias, ethnicity, gender, age, eyes, hair, build, inches, mods, clothing, comments])

            db.commit()
            traffickers += str(nextid.lastrowid) + ","
        counter += 1

    db.execute('insert into reports (description, location, time, date, venue_name,' +
                'venue_type, media, victims, suspects) values (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                [desc, location, time, date, venue_name, venue_type, "", victims, traffickers])

    db.commit()

    flash('Successfully added user')

    return redirect(url_for('login'))