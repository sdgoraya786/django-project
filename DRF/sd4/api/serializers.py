from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student

#  iii Validators - Priority(1)
def start_with_s(value):
    if value[0].lower() != 's':
        raise serializers.ValidationError('Name should be start with S')


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_s])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        # print(instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # i Field-level validation - Priority(2)
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    # ii Object-level validation - Priority(3)
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'shahzad' and ct.lower() != 'lahore':
            raise serializers.ValidationError('City must be lahore')
        return data