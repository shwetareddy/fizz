from rest_framework import serializers
from fizzbuzz.models import FizzBuzz

class FizzBuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = FizzBuzz
        fields = ('fizzbuzz_id', 'useragent', 'creation_date', 'message')

    def create(self, validated_data):
        fizzbuzz = FizzBuzz(
            useragent=validated_data['useragent'],
        )
        fizzbuzz.save()
        return fizzbuzz

class FizzBuzzPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FizzBuzz
        fields = ['message']