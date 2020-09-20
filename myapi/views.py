from django.shortcuts import render, redirect

from .forms import NoteForm
from .models import Note

def index(request):
  if request.method == "POST":
    form = NoteForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')

  notes = Note.objects.order_by("-modified")
  return render(request,'myapi/index.html', {"form":NoteForm(), "notes":notes})


def delete(request, note_id):
  Note.objects.get(id=note_id).delete()
  return redirect('index')
