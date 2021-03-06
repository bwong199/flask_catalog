from flask_wtf import Form
from wtforms import validators,StringField, TextAreaField
from author.form import RegisterForm
from catalog.models import Category
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class SetupForm(RegisterForm):
	title = StringField('Catalog name', [
		validators.Required(),
		validators.Length(max=80)
	])

def categories():
	return Category.query

class ItemForm(Form):
	title = StringField('Title', [
		validators.Required(), 
		validators.Length(max=80)
	])
	description = TextAreaField('Description', validators=[validators.Required()])
	category = QuerySelectField('Category', query_factory=categories, allow_blank=True)
	new_category = StringField('New Category')