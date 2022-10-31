
from rest_framework import serializers
from .models import User, Department, Group, Specialization, Article, Course


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, required=False)

    class Meta:
        model= User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, required=False)

    class Meta:
        model= Group
        fields = '__all__'


class SpecializationSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, required=False)

    class Meta:
        model= Specialization
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, required=False)
    courses = CourseSerializer(many=True, required=False)
    specializations = SpecializationSerializer(many=True, required=False)

    class Meta:
        model= Department
        fields = '__all__'
