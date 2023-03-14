from django.shortcuts import render


def index(request):
    text = '<p>Не очікували, а я тут!</p>'
    data = {
        'text': text,
    }

    return render(request, 'heart_one/index.html', context=data)


def about(request):
    return render(request, 'heart_one/about.html')


def my_skills(request):
    return render(request, 'heart_one/skills')


def my_experience(request):
    return render(request, 'heart_one/experience.html')

