from tokenize import group
from rest_framework import viewsets, status
from .models import Course, Specialization, Group, Department, User, Article
from .serializers import CourseSerializer, SpecializationSerializer, GroupSerializer, DepartmentSerializer, UserSerializer, ArticleSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    @action(detail=True, methods=['get', 'post'])
    def users(self, request, pk=None):
        # print(f'self is here {pk} ')
        if request.method == 'GET':
            users = User.objects.filter(department=pk)
            serial = UserSerializer(users, many=True)
            return Response(serial.data, status=status.HTTP_200_OK)
        else:
            request.data['department'] = pk
            serial = UserSerializer(data=request.data)
            if serial.is_valid():
                serial.save()
                return Response(serial.data, status=status.HTTP_201_CREATED)
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get', 'post'])
    def articles(self, request, pk=None):
        if request.method == 'GET':
            articles = Article.objects.filter(author=pk)
            serial = ArticleSerializer(articles, many=True)
            return Response(serial.data, status=status.HTTP_200_OK)
        else:
            request.data['author'] = pk
            serial = ArticleSerializer(data=request.data)
            if serial.is_valid():
                serial.save()
                return Response(serial.data, status=status.HTTP_201_CREATED)
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
