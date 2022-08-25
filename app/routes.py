import json
from app import app, render_template, request, db, redirect
from app.models.profile import Profile

@app.route("/add", methods=["GET","POST"])
def add_profile():
    if request.method == "GET":
        return render_template("add_profile.html")
        pass
    elif request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        age = request.form.get("age")

        if first_name != '' and last_name != '' and age is not None:
            payload = Profile(first_name=first_name, last_name=last_name, age=age)
            db.session.add(payload)
            db.session.commit()
        return redirect('/')
        pass

@app.route("/", methods=["GET"])
def show_profile():
    if request.method == "GET":
        profiles = Profile.query.all()
        return render_template("show_profile.html", profiles=profiles)
        pass

@app.route('/delete/<int:id>')
def delete_profile(id):
    # Deletes the data on the basis of unique id and
    # redirects to home page
    data = Profile.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')