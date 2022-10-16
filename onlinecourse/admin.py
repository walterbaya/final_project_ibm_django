from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Choice, Question

# <HINT> Register QuestionInline and ChoiceInline classes here

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class QuestionInline(admin.ModelAdmin):
    model = Question

class ChoiceInline(admin.ModelAdmin):
    model = Choice


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionInline(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('grade', 'text')
    list_filter = ['text']
    search_fields = ['text', 'grade']


class ChoiceInline(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('choice', 'correct')
    list_filter = ['choice']
    search_fields = ['choice', 'correct']


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question)
admin.site.register(Choice)
