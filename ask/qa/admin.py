from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "added_add", "rating")
    # inlines = (FieldMappingInline)
    # fields = []
    # exclude = ["type"]
    # search_fields = ['category', subCategory','suggestKeyword']
    class Meta:
        model = Question


admin.site.register(Question, QuestionAdmin)
