from django.contrib import admin
from .models import Menu,ClassGrade
from evaluate.models import ReviewResult,ReviewTest,TestQuestion
# Register your models here.
admin.site.register(Menu)
admin.site.register(ClassGrade)
admin.site.register(ReviewResult)
admin.site.register(ReviewTest)
admin.site.register(TestQuestion)