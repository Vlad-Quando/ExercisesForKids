from django.shortcuts import render, redirect
from .forms import TextsForm, SetRunTextParameters
from .models import Texts, Modes
from .text_exercise_modes import modes


# Главное окно со списком тренажёров.
def main_window(request):
    return render(request, 'mainhost/exercises_window.html')


def text_exercise_settings(request):
    error = ''
    if request.method == 'POST':
        form = SetRunTextParameters(request.POST)
        if form.is_valid():
            text_id = request.POST.get('text')
            text = Texts.objects.get(id=text_id)

            mode_id = request.POST.get('mode')
            mode = Modes.objects.get(id=mode_id)
            text = modes[mode.mode](text.text)
            return render(request, 'mainhost/run_text.html', {'text': text})
        else:
            error = "Форма заполнена неверно!"

    form = SetRunTextParameters()
    return render(request, 'mainhost/text-exercise-settings.html', {'form': form})


def create(request):
    error = ''
    if request.method == "POST":
        form = TextsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainhost_window')
        else:
            error = "Форма заполнена неверно!"

    form = TextsForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'mainhost/create_text.html', data)


def run_text(request):
    return render(request, 'mainhost/run_text.html')
