from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired

class AddItemForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired()])
    item_location = StringField('Item Location', validators=[DataRequired()])
    item_quantity = IntegerField('Item Quantity', validators=[DataRequired()])
    item_value = DecimalField('Item Value', validators=[DataRequired()])
    submit = SubmitField('Add Item')
    clear = SubmitField('Cancel')

class EditItemForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired()])
    item_location = StringField('Item Location', validators=[DataRequired()])
    item_quantity = IntegerField('Item Quantity', validators=[DataRequired()])
    item_value = DecimalField('Item Value', validators=[DataRequired()])
    submit = SubmitField('Update Item')
    clear = SubmitField('Cancel')