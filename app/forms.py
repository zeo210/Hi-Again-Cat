from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class CatForm(Form):
    search = StringField('Cat Number', [DataRequired()])