from django import forms
from redacao.models import Reporter, Article


class ArtigoForm(forms.ModelForm):
	class Meta:
		model= Article
