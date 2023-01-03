from django.contrib import admin
from polls.models import Question

class question_view(admin.ModelAdmin):
    list_display = ("question_text", "pub_date", "id")
    search_fields = ["question_text"]

admin.site.register(Question, question_view)
