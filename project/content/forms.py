from django import forms
from .models import Content
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class ContentForm(forms.ModelForm):

    text = SummernoteInplaceWidget()

    def __init__(self, *args, **kwargs):
        super(ContentForm, self).__init__(*args, **kwargs)
        self.current_user = None


    class Meta:
        model = Content
        fields = ['image', "title", "text", 'status', "categories"]
