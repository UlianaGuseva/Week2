from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from .models import Profile

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'  
    
def view_profile(request):
    user = request.user
    profile = user.profile
    
    context = {'profile': profile}
    return render(request, 'profile.html', context)
    
    

def profile_redirect_view(request):

    user = request.user
    if hasattr(user, 'profile'):
        return redirect('profile')
    

def update_profile(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        filled_form = ProfileForm(request.POST, instance=profile) # instance - the instance in the database to update
        if filled_form.is_valid():
            filled_form.save()
            return redirect('profile')
        else:
            errors = filled_form.errors
            print(errors)

    form = ProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'profile_update.html', context)