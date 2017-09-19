# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.models import Person
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from myapp.serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    "Person API"
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
