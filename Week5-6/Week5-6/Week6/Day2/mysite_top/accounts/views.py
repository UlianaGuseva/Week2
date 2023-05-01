from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.urls import reverse_lazy
from .forms import ProfileForm
# Create your views here.
class ProfileView(DetailView):
    model = UserProfile
    template_name = 'profile.html'
    context_object_name = 'profile'
    
class SignUpView(CreateView):
    
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
 
def profile_redirect_view(request):
    user = request.user
    if hasattr(user, 'profile'):
        return redirect('posts-all')
    else:
        return redirect('create_profile') 
      
def create_profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts-all')
            
    user = request.user
    form = ProfileForm(initial={'user': user})
    
    context = {'form': form}
    return render(request, 'create_profile.html', context)
    