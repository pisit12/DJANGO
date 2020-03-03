from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class InputNumber(APIView):

    def post(self, request):
        output = {}
        _input = request.data.get('number')
        for i in range(0, 11, 1):
            if i in _input:
                output[str(i)] = _input.count(i)
            else:
                output[str(i)] = 0
        return Response(output, status=status.HTTP_200_OK)
