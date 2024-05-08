from rest_framework import serializers
from .models import User,ExpenseCategory,Expense
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ['email','username','password','password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        
        if password != password2:
            raise serializers.ValidationError('Password and confirmpassword does not match')
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']

class ExpenseCategorySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',read_only=True)
    class Meta:
        model = ExpenseCategory
        fields = ['id', 'name', 'description', 'user']

    def validate_name(self, value):
        # Add validation logic for name field
        if len(value) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return value
    
class ExpenseSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    class Meta:
        model = Expense
        fields = ['id', 'title', 'date', 'amount', 'category']
        
