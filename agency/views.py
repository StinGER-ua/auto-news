from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from agency.models import Redactor, Article, Topic


@login_required
def index(request):
    num_redactors = Redactor.objects.count()
    num_articles = Article.objects.count()
    num_topics = Topic.objects.count()

    contex = {
        "num_redactors": num_redactors,
        "num_articles": num_articles,
        "num_topics": num_topics,
    }

    return render(request, "agency/index.html", context=contex)
