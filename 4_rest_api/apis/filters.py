import django_filters

from .models import School, Classroom, Teacher, Student


class SchoolFilter(django_filters.FilterSet):
    class Meta:
        model = School
        fields = ['name']


class ClassroomFilter(django_filters.FilterSet):
    class Meta:
        model = Classroom
        fields = ['school']

class StudentFilter(django_filters.FilterSet):
    school = django_filters.NumberFilter(
        field_name='classroom__school_id'
    )

    class Meta:
        model = Student
        fields = [
            'school',
            'classroom',
            'first_name',
            'last_name',
            'gender',
        ]

class TeacherFilter(django_filters.FilterSet):
    school = django_filters.NumberFilter(
        field_name='classrooms__school_id'
    )

    classroom = django_filters.NumberFilter(
        field_name='classrooms__id'
    )

    class Meta:
        model = Teacher
        fields = [
            'school',
            'classroom',
            'first_name',
            'last_name',
            'gender',
        ]