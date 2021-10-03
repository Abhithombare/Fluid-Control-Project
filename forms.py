import os
import pandas as pd
import numpy as np
import ipywidgets as widgets
from IPython.display import display
import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, SelectField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class DataframeForm(FlaskForm):
    dataframe_path = StringField('Dataframe Path', validators=[
        DataRequired(), Length(min=2, max=200)])
    duration = SelectField('Choose Duration', choices=[
        (1, 'Quarter 1'), (2, 'Quarter 2'), (3, 'Quarter 3'), (4, 'Quarter 4'), (5, 'Full Year')])
    cost_duration = SelectField('Choose Duration', choices=[
        (1, 'Full Year'), (2, 'Quarter 2'), (3, 'Quarter 3'), (4, 'Quarter 4')])
    buyer = SelectField('Choose Buyer')
    file1 = FileField('Upload the GRN Report ')
    file2 = FileField('Upload the PO Report ')
    supplier = SelectField('Sort suppliers by ', choices=[(
        'Item Quality', 'Item Quality'), ('In-time Delivery', 'In-time Delivery')])
    checkme = BooleanField('See supplier rankings?')
    supplier_sort = SelectField('Sort suppliers by ', choices=[(
        'Best to worst', 'Best to worst'), ('Worst to best', 'Worst to best')])
    analysis = SelectField('Choose analysis ', choices=[(
        'ABC', 'ABC'), ('XYZ', 'XYZ')])
    submit = SubmitField('Upload')
