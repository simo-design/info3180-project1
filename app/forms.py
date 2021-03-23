
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email
from werkzeug.utils import secure_filename

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    no_of_rooms = StringField('No. of Rooms', validators=[DataRequired()])
    no_of_bathrooms = StringField('No. of Bathrooms', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    property_type = SelectField(u'Property Type', choices=[('House' , 'Apartment')])
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
