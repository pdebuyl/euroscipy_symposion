from django import forms
from django.db.models import Q

from symposion.proposals.models import SupportingDocument, SupportingURL
# from markitup.widgets import MarkItUpWidget


# @@@ generic proposal form


class AddSpeakerForm(forms.Form):
    
    email = forms.EmailField(
        label="Email address of new speaker (use their email address, not yours)"
    )
    
    def __init__(self, *args, **kwargs):
        self.proposal = kwargs.pop("proposal")
        super(AddSpeakerForm, self).__init__(*args, **kwargs)
    
    def clean_email(self):
        value = self.cleaned_data["email"]
        exists = self.proposal.additional_speakers.filter(
            Q(user=None, invite_email=value) |
            Q(user__email=value)
        ).exists()
        if exists:
            raise forms.ValidationError(
                "This email address has already been invited to your talk proposal"
            )
        return value


class SupportingDocumentCreateForm(forms.ModelForm):
    
    class Meta:
        model = SupportingDocument
        fields = [
            "file",
            "description",
            "is_public",
        ]

class SupportingURLCreateForm(forms.ModelForm):

    class Meta:
        model = SupportingURL
        fields = [
            "url",
            "description",
        ]
