from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from agency.forms import TopicSearchForm, RedactorSearchForm
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
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(TopicListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        contex["search_form"] = TopicSearchForm(initial={"name": name})
        return contex

    def get_queryset(self):
        queryset = Topic.objects.all().order_by("id")
        form = TopicSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "agency/redactor_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(RedactorListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        contex["search_form"] = (
            RedactorSearchForm(initial={"username": username})
        )
        return contex

    def get_queryset(self):
        queryset = Redactor.objects.all().order_by("id")
        form = RedactorSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset
