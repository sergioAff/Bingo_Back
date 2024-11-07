# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# from rest_framework import status
# from .serializers import UserSerializer
# from .models import User
# from django.shortcuts import get_object_or_404

# @api_view(['POST'])
# def login(request):
#     user=get_object_or_404(User, email=request.data['email'])
#     if not user.check_password(request.data['password']):
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#     token,created=Token.objects.get_or_create(user=user)  
#     serializer=UserSerializer(user)    

#     return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)

# @api_view(['POST'])
# def register(request):
#     serializer = CreateUserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
        
#         # Guardar la contraseña usando `set_password` para que se almacene de manera segura
#         user.set_password(request.data['password'])
#         user.save()
        
#         # Crear el token
#         token = Token.objects.create(user=user)
#         return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def logout(request):
#     try:
#         token = Token.objects.get(user=request.user)
#         token.delete()
#         return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
    
#     except Token.DoesNotExist:
#         return Response({'error': 'No active session found'}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def user_profile(request):
#     serializer = UserSerializer(request.user)
#     return Response({'user': serializer.data}, status=status.HTTP_200_OK)