from rest_framework import serializers
from .models import Student

# Validator function
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should start with R')

class StudentSerializer(serializers.ModelSerializer):
    # Apply the custom validator to the 'name' field
    name = serializers.CharField(validators=[start_with_r])
    
    class Meta:
        model = Student  # 'model' should be lowercase
        fields = ['name', 'roll', 'city']  # Ensure this is on a new line
    
    # Field Level Validation for 'roll'
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    # Object Level Validation for multiple fields
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'nancy' and ct.lower() != 'china':
            raise serializers.ValidationError('City must be China')
        return data









    
    