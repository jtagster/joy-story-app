from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from collection.models import Post, Upload

        
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'gratitudeStmt', 'emotionTags', 'sensationTags', 'story', 'public')
        labels = {
            'gratitudeStmt': _("My Gratitude Statement:"),
            'sensationTags': _("The sensations in my body:"),
            'emotionTags': _("These are the emotions that I felt:"),
            'story': _("My appreciation story:"),
            'public':_("Share this journal publicly?")
        }
class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('gratitudeStmt', 'emotionTags', 'sensationTags', 'story', 'title', )
        labels = {
            'gratitudeStmt': _("Start with a statement about what brought you joy. \"I appreciate...\" "),
            'sensationTags': _("What did you see, hear, touch, sense? How did your body feel during the story:"),
            'emotionTags': _("Use feeling words to describe your emotions in this story:"),
            'story': _("Tell your story here (Be sure to include ways your story demonstrated how you acted like yourself):"),
            'title': _("Give your story a name - just 3-4 words, that will help you remember it's joy!"),
            'public': _("Who can see this?")
        }
class ShareForm(ModelForm):
    class Meta:
        model = Post
        fields=['public']
        labels = {
            'public': _("Who can see this?")
            }
            
            
class ImageUploadForm(ModelForm):
    class Meta: 
        model = Upload
        fields = ('image',)