from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al usuario al inicio de sesión después de registrarse
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})
