from students.models import Students

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from students.serializers import SerializerStudents


class StudentsViewSet(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = SerializerStudents
    permission_classes = (IsAuthenticated, )

