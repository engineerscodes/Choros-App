from django.core.exceptions import ValidationError

def validate_number(value):
    if value<0 :  # Your conditions here
        raise ValidationError("MARKS CANNOT BE NEGATIVE")