from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from .forms import RegisterForm, ProfileForm
from .models import UserProfile
# Create your views here.
 
class SignUpView(CreateView):
    
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileView(DetailView):
    model = UserProfile
    template_name = 'profile.html'
    context_object_name = 'profile'

def profile_redirect_view(request):
    user = request.user
    if hasattr(user, 'profile'):
        return redirect('profile-page', user.profile.id)
    else:
        return redirect('create_profile') 
      
def create_profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_all')
            
    user = request.user
    form = ProfileForm(initial={'user': user})
    
    context = {'form': form}
    return render(request, 'create_profile.html', context)
    