
from django import forms

from app.models import Bookmark


class BookmarkForm(forms.ModelForm):

    class Meta:
        model = Bookmark
        exclude = ['output_url']


