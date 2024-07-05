from tests import TestCase
from tests import TestCase, Client
from tests import reverse
from .models import Note
from .forms import NoteForm


class NoteViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.note = Note.objects.create(
            title="Test Note", content="This is a test note."
        )

    def test_note_list_view(self):
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_list.html")
        self.assertIn("notes", response.context)

    def test_note_detail_view(self):
        response = self.client.get(reverse("note_detail", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_detail.html")
        self.assertEqual(response.context["note"], self.note)

    def test_note_new_view_get(self):
        response = self.client.get(reverse("note_new"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_edit.html")
        self.assertIsInstance(response.context["form"], NoteForm)

    def test_note_new_view_post_valid(self):
        response = self.client.post(
            reverse("note_new"),
            {"title": "New Note", "content": "Content for new note."},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title="New Note").exists())

    def test_note_new_view_post_invalid(self):
        response = self.client.post(
            reverse("note_new"),
            {
                "title": "",  # Invalid data (empty title)
                "content": "Content with empty title.",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_edit.html")
        self.assertFalse(
            Note.objects.filter(content="Content with empty title.").exists()
        )

    def test_note_edit_view_get(self):
        response = self.client.get(reverse("note_edit", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_edit.html")
        self.assertIsInstance(response.context["form"], NoteForm)

    def test_note_edit_view_post_valid(self):
        response = self.client.post(
            reverse("note_edit", args=[self.note.pk]),
            {"title": "Updated Title", "content": "Updated content."},
        )
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Title")

    def test_note_delete_view(self):
        response = self.client.post(reverse("note_delete", args=[self.note.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
