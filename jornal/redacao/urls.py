from django.conf.urls import patterns, include, url

urlpatterns = patterns('redacao.views',
	url(r'^$', 'edicao', name='edicao'),
	url(r'^(\d+)/sucesso/$', 'success', name='success'),
)
