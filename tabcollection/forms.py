from django.forms import ModelForm, Textarea
from models import Song

class SongForm(ModelForm):
	class Meta:
		model = Song
		exclude = ('pub_date')
		widgets = {
            'body': Textarea(attrs={'cols': 80, 'rows': 20}),
        }