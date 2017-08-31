from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from collection.models import Post

        
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
        help_texts = {
            'gratitudeStmt': _('One sentence statement. (I am thankful for/because...)'),
        }
