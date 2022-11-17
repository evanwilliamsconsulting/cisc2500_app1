from django.shortcuts import render
from .forms import NameForm
from .models import Survey
from django import forms

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Import Open Secrets API
from crpapi import CRP

# http://www.learningaboutelectronics.com/Articles/How-to-create-radio-buttons-in-a-Django-form.php
OVERALL_CHOICES= [
    ('horrible','Horrible'),
    ('average', 'Average'),
    ('good', 'Good'),
    ('great', 'Great'),
    ('fantastic', 'Fantastic'),
    ]    
PACE_CHOICES = [
    ('too_fast','Too Fast'),
    ('too_slow','Too Slow'),
    ('just_right','Just Right'),
    ]
LANGUAGE_CHOICES = [
    ('csharp','C#'),
    ('cplusplus','C++'),
    ('javascript','JavaScript'),
    ('php','PHP'),
    ('swift','Swift'),
    ('java','Java'),
    ('go','Go'),
    ('sql','SQL'),
    ('ruby','Ruby')
    ]

class UserForm(forms.Form):
    class_overall= forms.CharField(label='The course so far has been:', widget=forms.RadioSelect(choices=OVERALL_CHOICES))
    class_pace= forms.CharField(label='The pace of the class, recently:', widget=forms.RadioSelect(choices=PACE_CHOICES))
    language_choices = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=LANGUAGE_CHOICES,)  
    comment = forms.CharField(max_length=500)

def index(request):
    response = ""
    for i in range(1,10):
        response += str(i)
        response += " "
    return HttpResponse(response)

def learning(request):
    return HttpResponse("<!DOCTYPE html><html><head><title>Page Title</title></head><body><h1>This is a Heading</h1><p>This is a paragraph.</p></body></html>")

def fordham(request):
    context = {
           'my_name': "Evan J. Williams",
    }    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'fordham.html', context=context)    

def survey(request):
    context = {
           'my_name': "Evan J. Williams",
    }    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'fordham.html', context=context)    

def thanks(request):
    context = {
           'my_name': "Evan J. Williams",
    }    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'thanks.html', context=context)    

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            #messages.success(request, 'Form submission successful')
            surveyModel = Survey()
            data = form.cleaned_data
            class_overall = data['class_overall']
            class_pace = data['class_pace']
            language_choices = data['language_choices']
            comment = data['comment']
            surveyModel.comment_text = comment
            surveyModel.pace = class_pace
            surveyModel.langauge = language_choices
            surveyModel.overall = class_overall
            surveyModel.save()
            return render(request,'learning.html',{'context':form.cleaned_data})
            # redirect to a new URL:
            # return HttpResponseRedirect('thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'survey.html', {'form': form})

def opensecrets(request):
    crp = CRP("4039561d3f52c0c85c6c1ca0d8038827")
    cand = crp.candidates.get("N00007360")
    cand = crp.candidates.get("N00007360")
    contribs = crp.candidates.contrib('N00007360', '2022')
    first_donation = contribs[0]['@attributes']
    results = []
    for item in contribs:
        donation_name = item['@attributes']
        results.append({
            'donation_name' : donation_name
            })
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'opensecrets.html', {'results' : results})    
