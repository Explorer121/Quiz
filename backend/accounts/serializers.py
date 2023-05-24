from rest_framework import serializers
from accounts.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
	name = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
	password = serializers.CharField(max_length=200, write_only=True)


	def create(self, validated_data):
		password = validated_data.pop("password", None)
		instance = self.Meta.model(**validated_data)
		if password is not None:
			instance.set_password(password)
		instance.save()
		return instance


	class Meta:
		model = User
		fields = ["id", "name" ,"email", "password"]
		extra_kwargs = {
			'password': {
				'write_only': True,
			}
		}
