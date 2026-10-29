from django.shortcuts import render
from .models import TeamMemberModel

def team_list(request):
    members = TeamMemberModel.objects.filter(is_active=True)

    context = {
        "members": members
    }
    return render(request, "team/team_list.html", context)
