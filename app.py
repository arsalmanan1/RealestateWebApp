from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from db import db, Users, Details, Properties

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/realestateapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'realestateapp'

mysql = MySQL(app)


@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT p.*, d.bedroom, d.washroom
        FROM properties p
        JOIN details d ON p.dId = d.dId
    """)
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', PROPERTIES=data)



@app.route("/allproperties")
def allproperties():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT p.*, d.bedroom, d.washroom
        FROM properties p
        JOIN details d ON p.dId = d.dId
    """)
    data = cur.fetchall()
    cur.close()
    return render_template('properties.html', PROPERTIES=data)


@app.route("/adduserform")
def adduserform():
    return render_template('userform.html')
@app.route("/register_user", methods=['POST'])
def register_user():
    fname = request.form['firstname']
    lname = request.form['lastname']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']
    fullname = fname + " " + lname

    # Create a new user entry
    new_user = Users(userName=fullname, userAddress=address, userPhoneNo=phone, userEmail=email)
    db.session.add(new_user)
    db.session.commit()

    # After adding the user, redirect to the index page
    return redirect(url_for('index'))
@app.route("/formfetch")
def form():
    return render_template('formfetch.html')


@app.route('/add_property', methods=['POST'])
def add_property():
    loc = request.form['location']
    ptype = request.form['ptype']
    area = request.form['area']
    purpose = request.form['purpose']
    bedrooms = request.form['beds']
    washrooms = request.form['washrooms']
    floors = request.form['floors']
    lawn = request.form['lawn']
    price = request.form['price']

    # Create a new Details instance without specifying the primary key
    entry2 = Details(bedroom=bedrooms, washroom=washrooms, floors=floors, lawn=lawn)
    db.session.add(entry2)
    db.session.commit()

    # Use the generated primary key value for Details in the Properties entry
    entry = Properties(area=area, Ptype=ptype, Plocation=loc, purpose=purpose, price=price , dId=entry2.dId, userId=1)
    db.session.add(entry)
    db.session.commit()

    return redirect(url_for('index'))


@app.route("/updateform")
def updateform():
    property_id = request.args.get('property_id')
    return render_template('updateproperties.html', property_id=property_id)


@app.route('/updateproperties', methods=['POST'])
def updateproperties():
    if request.method == 'POST':
        property_id = request.form.get('property_id')
        loc = request.form['location']
        a = request.form['area']
        p = request.form['price']
        beds = request.form['beds']
        wash = request.form['washrooms']

        cur = mysql.connection.cursor()
        # Update properties table
        cur.execute("""
            UPDATE properties
            SET Plocation=%s, area=%s, price=%s
            WHERE propertyId=%s
        """, (loc, a, p, property_id))
        mysql.connection.commit()
        # Update details table
        cur.execute("""
            UPDATE details
            SET bedroom=%s, washroom=%s
            WHERE dId=%s
        """, (beds, wash, property_id))

        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))



@app.route("/filterform")
def filterform():
    return render_template('propertyfilters.html')
@app.route('/filterproperties', methods=['POST'])
def filterproperties():
    if request.method == 'POST':
        property_id = request.form.get('property_id')
        loc = request.form['location']
        a = request.form['area']
        p = request.form['price']

        cur = mysql.connection.cursor()
        # Update properties table
        cur.execute("""
            Select * from properties
            WHERE Plocation=%s OR area=%s OR price=%s
        """, (loc, a, p))
        data = cur.fetchall()

        cur.close()
        return render_template('properties.html', PROPERTIES=data)



@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM properties WHERE propertyId=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
