from rest_framework import serializers
from ..models.person import Person, PhoneNumber


class PhoneNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneNumber
        fields = (
            'phone_number',
        )


class PersonSerializer(serializers.ModelSerializer):
    phone_numbers = PhoneNumberSerializer(read_only=True, many=True)

    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'image',
            'position',
            'email',
            'phone_numbers'
        )
