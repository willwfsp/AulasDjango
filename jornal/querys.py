__author__ = 'Willian'

from redacao.models import Reporter
from redacao.models import Article
from django.utils import timezone

from django.utils import timezone

# Limpa o banco de dados
Reporter.objects.all().delete()
Article.objects.all().delete()

# Adicionar 3 reporteres.

reporter1 = Reporter()
reporter1.full_name = "Roberto Cabrini"
reporter1.save()
print("\nReporter "+str(reporter1)+" adicionado;")

reporter2 = Reporter()
reporter2.full_name = "Ricardo Boechat"
reporter2.save()
print("\nReporter "+str(reporter2)+" adicionado;")

reporter3 = Reporter()
reporter3.full_name = "Abel Neto"
reporter3.save()
print("\nReporter "+str(reporter3)+" adicionado;")

# Adicionar 4 matérias

date = timezone.now()
article1 = Article()
article1.pub_date = date
article1.headline = "Dolar vai a R$ 3,95, 2a maior cotacao da historia do real"
article1.content = "No ano, moeda ja subiu 48,8%. Casas de cambio vendem por ate R$ 4,40"
article1.reporter = reporter1
article1.save()

article2 = Article()
article2.pub_date = date
article2.headline = "A Brabus 'fura' Mercedes-Benz e lanca GLE de R$ 4,2 milhoes no Brasil"
article2.content = "Crossover de 850 cv eh um dos modelos mais caros a venda por aqui. Montadora ainda nao lancou oficialmente modelo no pais"
article2.reporter = reporter1
article2.save()

article3 = Article()
article3.pub_date = date
article3.headline = "Um de bike, um de skate: os Lucas do Geracao Selfie no role da ciclovia"
article3.content = "Quadro no SPTV foi parar na nova ciclovia da Avenida Paulista. Lucas Farias levou seu skate, e Lucas Dantas foi de bicicleta."
article3.reporter = reporter2
article3.save()

article4 = Article()
article4.pub_date = date
article4.headline = "Eduardo Baptista diz que R10 foi solicito e acredita em briga pelo G-4"
article4.content = "Na apresentacao como novo treinador do Flu, ex-Sport explica motivos pelos quais deixou o Leao e afirma que nao viu grupo tricolor rachado: \"Uma equipe equilibrada\""
article4.reporter = reporter3
article4.save()

# Querys
# 1 - Todos os artigos do reporter 1
q = Article.objects.filter(reporter=reporter1)
print("\nArtigo do reporter 1:")
for article in q:
    print("\n\t" + str(article))

q = Article.objects.filter(headline__startswith="A")
print("\nArtigo comecando com 'A': \n\t" + str(q))
