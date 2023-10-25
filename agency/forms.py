from django import forms


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )


class ArticleSearchForm(forms.Form):
    title = forms.CharField(
        max_length=127,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"}),
    )
