from django.shortcuts import render


def available_challenges(request):
    return render(request, 'challenges/available_challenges.html')

def view_accepted_challenges(request):
    return render(request, 'challenges/accepted_challenges_list.html')