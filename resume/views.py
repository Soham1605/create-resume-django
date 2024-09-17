from django.shortcuts import render
from .models import UserInfo, Experience

def resume_view(request):
    user_info = UserInfo.objects.first()  # Assuming there's only one user, adjust this as needed
    experiences = Experience.objects.all()
    
    context = {
        'user_info': user_info,
        'experiences': experiences,
    }
    
    return render(request, 'resume/resume.html', context)





