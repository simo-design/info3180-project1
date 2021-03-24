"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from app import db
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from .forms import PropertyForm
from werkzeug.utils import secure_filename
import psycopg2
import uuid
from .models import Property
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Nadrine Simms")


@app.route('/property', methods=['GET', 'POST'])
def property():

    myForm = PropertyForm()

    if request.method == 'POST':
        if myForm.validate_on_submit():
            title = myForm.title.data
            description = myForm.description.data
            no_of_rooms = myForm.no_of_rooms.data
            no_of_bathrooms = myForm.no_of_bathrooms.data
            price = myForm.price.data            
            property_type = myForm.property_type.data
            location = myForm.location.data
            photo = myForm.photo.data
            property_id = str(uuid.uuid4().fields[-1])[:8]

        if photo:    
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        prop =  Property(property_id=property_id, title=title, description=description, no_of_rooms=no_of_rooms, no_of_bathrooms=no_of_bathrooms, price=price, property_type=property_type, location=location, photo=photo.filename)
        db.session.add(prop)
        db.session.commit()

        flash('Form filled out successfully')

        flash_errors(PropertyForm)
        return redirect(url_for('properties'))
    
    return render_template('property.html')


#@app.route('/properties')
#def properties():


#@app.route('/property/<propertyid>')
#def propertyid():




###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
