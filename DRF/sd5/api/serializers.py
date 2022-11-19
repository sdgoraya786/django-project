from rest_framework import serializers
from .models import Student


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'roll', 'city']




# class StudentSerializer(serializers.ModelSerializer):
#     # name = serializers.CharField(read_only=True)
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'roll', 'city']
#         # read_only_fields = ['name']
#         extra_kwargs = {'name': {'read_only': True}}




###### with validation ####
# iii Validators - Priority(1)
def start_with_s(value):
    if value[0].lower() != 's':
        raise serializers.ValidationError('Name should be start with S')

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(validators=[start_with_s])
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        extra_kwargs = {'name': {'validators': [start_with_s]}}

    ## i Field-level validation - Priority(2)
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    ## ii Object-level validation - Priority(3)
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'sadnan' and ct.lower() != 'lahore':
            raise serializers.ValidationError('City must be lahore')
        return data