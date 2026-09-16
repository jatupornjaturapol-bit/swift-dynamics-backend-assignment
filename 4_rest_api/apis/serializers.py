from rest_framework import serializers

from .models import School, Classroom, Teacher, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class SchoolDetailSerializer(serializers.ModelSerializer):
    classroom_count = serializers.SerializerMethodField()
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = [
            'id',
            'name',
            'abbreviation',
            'address',
            'classroom_count',
            'teacher_count',
            'student_count',
        ]

    def get_classroom_count(self, obj):
        return obj.classrooms.count()

    def get_teacher_count(self, obj):
        return Teacher.objects.filter(
            classrooms__school=obj
        ).distinct().count()

    def get_student_count(self, obj):
        return Student.objects.filter(
            classroom__school=obj
        ).count()


class TeacherBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender']


class StudentBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender']


class ClassroomDetailSerializer(serializers.ModelSerializer):
    teachers = TeacherBriefSerializer(many=True, read_only=True)
    students = StudentBriefSerializer(many=True, read_only=True)

    class Meta:
        model = Classroom
        fields = [
            'id',
            'school',
            'grade',
            'room',
            'teachers',
            'students',
        ]

class ClassroomBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'school', 'grade', 'room']


class TeacherDetailSerializer(serializers.ModelSerializer):
    classrooms = ClassroomBriefSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Teacher
        fields = [
            'id',
            'first_name',
            'last_name',
            'gender',
            'classrooms',
        ]

class StudentDetailSerializer(serializers.ModelSerializer):
    classroom = ClassroomBriefSerializer(read_only=True)

    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'last_name',
            'gender',
            'classroom',
        ]