from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import exceptions
from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializers import LoginSerializer, RegisterSerializer


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return response

        except exceptions.AuthenticationFailed:
            return Response({
                'error': True,
                'message': 'Invalid Username or Password',
            }, status=status.HTTP_401_UNAUTHORIZED)


class Register(APIView):
    permission_classes = []

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)