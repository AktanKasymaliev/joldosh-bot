from django.contrib import admin
from .models import Problem, ProblemImage

class ImageInline(admin.TabularInline):
    model = ProblemImage
    fields = ('image',)

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    inlines = [ImageInline,]
