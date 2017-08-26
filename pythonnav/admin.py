from django.contrib import admin

# Register your models here.
from .models import QuestionCategory,Question, ReplyQuestion, StudyrRecoder, Userphoto


admin.site.register(QuestionCategory)
admin.site.register(Question)
admin.site.register(ReplyQuestion)
admin.site.register(Userphoto)
admin.site.register(StudyrRecoder)