from django.shortcuts import render, redirect

# Create your views here.
def blockly_index(request):

    context = {}

    return render(request, 'blockDuino_index.html', context)

def blockly_frame(request):

    context = {}

    return render(request, 'blockDuino_frame.html', context)