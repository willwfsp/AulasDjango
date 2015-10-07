from django.shortcuts import render_to_response
from django.template import RequestContext
from redacao.forms import ArtigoForm

# Create your views here.
def homepage(request):
	return render_to_response('index.html')


def edicao(request):
	if request.method == 'POST':
		return gravar(request)
	else:
		return novo(request)

def novo(request):
	form = ArtigoForm()
	context = RequestContext(request, {'form': form})
	return render_to_response('novoArtigo.html', context)
