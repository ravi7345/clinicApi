from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            doctor = serializer.save()

            # Generate JWT tokens
            refresh = RefreshToken.for_user(doctor)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return Response({'doctor': serializer.data, 'token': token}, status=201)
        return Response(serializer.errors, status=400)

class DoctorLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            doctor = Doctor.objects.get(username=username)
        except Doctor.DoesNotExist:
            return Response({'error': 'Invalid username or password'}, status=400)

        if not doctor.check_password(password):
            return Response({'error': 'Invalid username or password'}, status=400)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(doctor)
        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        serializer = DoctorSerializer(doctor)
        return Response({'doctor': serializer.data, 'token': token}, status=200)
