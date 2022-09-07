from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp
from wtforms import ValidationError
from ..models import Asset

class AddAsset(FlaskForm):
    serial_number = StringField('serial_number', validators=[
        DataRequired(), Length(1, 12),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Serial Number must have only letters, numbers, dots or '
               'underscores')])
    device_model = StringField('device_model', validators=[
        DataRequired(), Length(1, 12),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Device Model must have only letters, numbers, dots or '
               'underscores')])
    assigned_to = StringField('assigned_to', validators=[
        DataRequired(), Length(1, 12), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Assigned To must have only letters, numbers, dots or '
               'underscores')])
    submit = SubmitField('Assign Device')

    def validate_serial_number(self, field):
        if Asset.query.filter_by(serial_number=field.data.lower()).first():
            raise ValidationError('Serial Number already exists.')

class SearchAsset(FlaskForm):
    search_criteria = StringField('serial_number', validators=[
        DataRequired(), Length(1, 12),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Serial Number must have only letters, numbers, dots or '
               'underscores')])
    submit = SubmitField('Serial Number Search')

class EditAsset(FlaskForm):
    device_model = StringField('device_model', validators=[
        DataRequired(), Length(1, 12),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Device Model must have only letters, numbers, dots or '
               'underscores')])
    assigned_to = StringField('assigned_to', validators=[
        DataRequired(), Length(1, 12), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Assigned To must have only letters, numbers, dots or '
               'underscores')])
    submit = SubmitField('Update Asset')
