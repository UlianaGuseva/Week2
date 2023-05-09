from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm, ImageForm
from .models import Profile, Image
from django.contrib.auth.mixins import LoginRequiredMixin

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

class ListImagesView(ListView):
    template_name = 'images.html'
    model = Image
    context_object_name = 'images'
    
class AddImageView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = ImageForm
    model = Image
    success_url = reverse_lazy('images_list')
    template_name = 'add_image.html'
    def get_initial(self):
        user = self.request.user
        profile = user.profile
        initial_data = {'user_uploader': profile}
        return initial_data
    
# class MyImagesView(ListView):
#     template_name = 'images.html'
#     model = Image
#     context_object_name = 'images'
    
#     def get_context_data(self, **kwargs): 
#         context = super().get_context_data(**kwargs)
#         context['user_uploader'] = date.today()
#         return context
    
def my_images(request):
    current_user = request.user
    images = Image.objects.filter(user_uploader=current_user)
    context = {'images': images}
    return render(request, 'images.html', context)    