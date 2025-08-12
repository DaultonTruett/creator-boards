from django.contrib import admin
from .models import User, Creator, VotingPeriod, Vote, HallOfFame

# Register your models here.
admin.site.register(User)
admin.site.register(Creator)
admin.site.register(VotingPeriod)
admin.site.register(Vote)
admin.site.register(HallOfFame)
