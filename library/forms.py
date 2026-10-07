from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "cover_image", "isbn", "genre", "published_date", "description"]
        widgets = {
            "published_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 6}),
            "cover_image": forms.ClearableFileInput(attrs={"accept": "image/*"}),
        }
