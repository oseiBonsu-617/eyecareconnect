from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'role')

    
    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         username=validated_data['username'],
    #         password=validated_data['password'],
    #         role=validated_data.get('role', 'clinician'),
    #     )
    #     return user