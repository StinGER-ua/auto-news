from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

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


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "agency/topic_list.html"
    queryset = Topic.objects.all()

