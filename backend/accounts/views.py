import jwt, datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from accounts.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
# Create your views here.


class Register(APIView):

	def post(self, request):
		serializer = UserSerializer(data = request.data)
		if serializer.is_valid():
			user = serializer.save()
			if user:
				token = Token.objects.create(user=user)
				json = serializer.data
				json['token'] = token.key
				print(json)
				return Response(json, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
	def post(self, request):
		email = request.data['email']
		password = request.data['password']
		user = User.objects.filter(email=email).first()
		if user is None:
			raise AuthenticationFailed("User not found!!!")

		if not user.check_password(password):
			raise AuthenticationFailed("Incorrect found!!!")

		payload = {
			"id": user.id,
			"user": user.name,
			"email": user.email,
			"exp": datetime.datetime.utcnow() + datetime.timedelta(days=30),
			"iat": datetime.datetime.utcnow()
		}
		token = jwt.encode(payload, "secret", algorithm="HS256")
		# token = jwt.encode(payload,'secret', algorithm='HS256')
		response = Response()
		response.set_cookie(key='jwt', value=token, httponly=True)
		response.data = {
			"jwt": token
		}
		return response


class UserView(APIView):
	def get(self, request):
		token = request.COOKIES.get("jwt")
		if not token:
			raise AuthenticationFailed("Unauthorisation token!!!")
		try:
			payload = jwt.decode(token, "secret", algorithms=["HS256"])
		except jwt.ExpiredSignatureError:
			raise AuthenticationFailed("Login Required token!!!")
		user = User.objects.filter(id = payload['id']).first()
		serializer = UserSerializer(user)
		return Response(serializer.data)



class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
