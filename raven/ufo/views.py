from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

# from .models import Question
from .models import Event

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World")

def index(request):
    context = {"event": Event.objects.all()}
    return render(request, "ufo/index.html", context) 
    # events = Event.objects.all()
    # output = "<br/>".join([f"<h2>Event</h2><p>{q.description}</p>" for q in events])
    # return HttpResponse(f"<h1>All Events Page</h1>{output}")

def detail(request, description_id):
    q = get_object_or_404(Event, pk=description_id)
    return HttpResponse(f"<h1>Event</h1>{q.description}")

def event(request, description_id):
    q = get_object_or_404(Event, pk=description_id)
    return HttpResponse(f"<h1>Location</h1>{q.area}")

def date(request, description_id):
    q = get_object_or_404(Event, pk=description_id)
    return HttpResponse(f"<h1>Date</h1>{q.date}")

# def index(request):
#     questions = Question.objects.all()
#     output = "<br/>".join([f"<h1>{q.question_text}</h1>" for q in questions])
#     return HttpResponse(output)

# def detail(request, question_id):
#     q = get_object_or_404(Question, pk=question_id)
#     return HttpResponse(f"<h1>Details</h1>{q.question_text}")

# def votes(request, question_id):
#     q = get_object_or_404(Question, pk=question_id)
#     return HttpResponse(f"<h1>Votes</h1>{q.question_text}")

# def results(request, question_id):
#     q = get_object_or_404(Question, pk=question_id)
#     return HttpResponse(f"<h1>Results</h1>{q.question_text}")