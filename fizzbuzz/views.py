from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from fizzbuzz.models import FizzBuzz
from fizzbuzz.serializers import FizzBuzzSerializer
from django.http import Http404

class FizzBuzzView(APIView):

    def get(self, request):
        fizzbuzz = FizzBuzz.objects.all()
        serializer = FizzBuzzSerializer(fizzbuzz, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data['useragent'] = request.META.get('HTTP_USER_AGENT', '')

        serializer = FizzBuzzSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FizzBuzzDetailView(APIView):

    def get(self, request, pk ):
        try:
            fizzbuzz = FizzBuzz.objects.get(pk=pk)
        except FizzBuzz.DoesNotExist:
            raise Http404

        serializer = FizzBuzzSerializer(fizzbuzz)
        return Response(serializer.data)
