# -*- coding: utf-8 -*-
from rest_framework import serializers
from myapp.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')
