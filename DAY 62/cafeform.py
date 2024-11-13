from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField, TimeField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField(
        "Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()]
    )
    open_time = TimeField("Opening time", validators=[DataRequired()])
    close_time = TimeField("Closing time", validators=[DataRequired()])
    # fmt: off
    coffee_rating = SelectField(
        "Coffee Rating",
        validators=[DataRequired()],
        choices=["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"],
    )
    wifi_rating = SelectField(
        "WiFi Strength Rating",
        validators=[DataRequired()],
        choices=["✘", "💪", "💪💪","💪💪💪","💪💪💪💪","💪💪💪💪💪"])
    power_avail = SelectField(
        "Power Socket Availability",
        validators=[DataRequired()],
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"])
    submit = SubmitField("Submit")
    # fmt: on
