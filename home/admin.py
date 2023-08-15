from django.contrib import admin
from home.models import contact
from home.models import ques_ans
from home.models import cand_ans
from home.models import cand_bank

# Register your models here.

admin.site.register(contact)

admin.site.register(ques_ans)

admin.site.register(cand_ans)

admin.site.register(cand_bank)
