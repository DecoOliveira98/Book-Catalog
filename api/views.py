from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


class HealthView(APIView):
    """
    Book API View
    """
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "Status": "ok",
            
            }
        )

health_view = HealthView.as_view()

# Book Resource
# /api/books/
# 

class BookView(APIView):
    """
    Book API View
    """
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "Hello": "Django",
            
            }
        )

book_view = BookView.as_view()
# Book ViewSet


