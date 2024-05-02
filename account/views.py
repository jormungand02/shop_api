from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

from .serializers import RegisterSerializer

User = get_user_model()

class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response('Вы успешно зарегистрировались!')
    
class ActivateView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code)
        if not user:
            return Response('Пользователь не найден!')
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Активировано')