from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def note_list(request):
    """
    Display a list of all notes.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Renders the note list template with all notes.
    """
    notes = Note.objects.all()
    return render(request, "notes/note_list.html", {"notes": notes})


def note_detail(request, pk):
    """
    Display details of a single note.

    Args:
        request (HttpRequest): The request object.
        pk (int): The primary key of the note.

    Returns:
        HttpResponse: Renders the detail template for a specific note.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    """
    Create a new note.

    Handles both displaying the form and processing the form submission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Renders the note creation/edit form.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)  # Prepare the note object
            note.save()  # Save the new note to the database
            return redirect(
                "note_detail", pk=note.pk
            )  # Redirect to the new note's detail page
    else:
        form = NoteForm()  # Instantiate a new form for GET requests
    return render(request, "notes/note_edit.html", {"form": form})


def note_edit(request, pk):
    """
    Edit an existing note.

    Args:
        request (HttpRequest): The request object.
        pk (int): The primary key of the note to edit.

    Returns:
        HttpResponse: Renders the note edit form.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)  # Update the note object
            note.save()  # Save changes to the database
            return redirect(
                "note_detail", pk=note.pk
            )  # Redirect to the updated note's detail page
    else:
        form = NoteForm(instance=note)  # Load the form with existing note data
    return render(request, "notes/note_edit.html", {"form": form})


def note_delete(request, pk):
    """
    Delete a note.

    Args:
        request (HttpRequest): The request object.
        pk (int): The primary key of the note to delete.

    Returns:
        HttpResponseRedirect: Redirects to the note list after deletion.
    """
    note = get_object_or_404(Note, pk=pk)
    note.delete()  # Delete the note from the database
    return redirect("note_list")  # Redirect to the list of notes
