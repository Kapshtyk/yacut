from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp


class CutForm(FlaskForm):
    original_link = URLField("Ссылка", validators=[DataRequired(), Length(max=2048)])
    custom_id = StringField(
        "Короткая ссылка",
        validators=[Optional(), Length(max=16), Regexp(r"^[a-zA-Z0-9]+$")],
    )
    submit = SubmitField("Обрезать")
