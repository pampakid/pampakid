from django import forms
from tinymce import TinyMCE
from .models import Post


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'timestamp', 'content', 'featured')

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Your name"
        self.fields['email'].label = "Your email"
        self.fields['message'].label = "Our next collaboration..."
