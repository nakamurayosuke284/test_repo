#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.shortcuts import render
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    # return HttpResponse(output)
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

    # return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You are looking at the results of question %s." % question_id)


def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)
