from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, DepartmentViewSet,GroupViewSet,ArticleViewSet,SpecializationViewSet, UserViewSet
router=DefaultRouter()
router.register('users',UserViewSet,basename='users')
router.register('departments',DepartmentViewSet, basename='departments')
router.register('courses',CourseViewSet,basename='courses')
router.register('groups',GroupViewSet,basename='groups')
router.register('articles',ArticleViewSet, basename='articles')
router.register('specializations',SpecializationViewSet,basename='specializations')

urlpatterns=[]

urlpatterns+=router.urls
