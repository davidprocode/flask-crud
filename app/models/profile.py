from app import db

class Profile(db.Model):
    # Id : Field which stores unique id for every row in database table.
    id = db.Column(db.Integer, primary_key=True)
    # first_name: Used to store the first name if the user
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    # last_name: Used to store last name of the user
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    # Age: Used to store the age of the user
    age = db.Column(db.Integer, nullable=False)
 
    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"