from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    """
    The form for entering values during patient encounter. Feel free to add additional 
    fields for the remaining features in the data set (features missing in the form 
    are set to default values in `predict.py`).
    """
    
    sex = SelectField('Gender', choices=[(0, 'Male'), (1, 'Female')])
    pclass = SelectField('Ticket-class', choices=[(1, '1st'), (2, '2nd'), (3, '3rd')])
    
    embarked = SelectField('Embarked', choices=[(2, 'Southampton'), (0, 'Cherbourg'), (1, 'Queenstown')])

    title = SelectField('Title', choices=[(3, 'Mr.'), (2, 'Miss.'), (4, 'Mrs.'), (1, 'Master'), (5, 'Officer.'), (6, 'Royal.'), (0, 'Col.')])
    age = SelectField('Age-group', choices=[(0, '16 or below'), (1, '17-32'), (2, '33-48'), (3, '49-64'), (4, '65 or higher')])

    sibSp = IntegerField('# of siblings/spouses aboard', validators=[NumberRange(min=0, max=10)])
    parch = IntegerField('# of parents/children aboard', validators=[NumberRange(min=0, max=10)])
    fare = FloatField('Ticket-price')

    submit = SubmitField('Submit')