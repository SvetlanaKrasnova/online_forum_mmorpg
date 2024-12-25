from django.forms import ModelForm, TextInput, CharField, Select
from .models import Post, Reply, CATEGORIES
from django_summernote.widgets import SummernoteWidget


class PostForm(ModelForm):
    title = CharField(
        label='Наименовние',
        widget=TextInput(
            attrs={'type': 'text',
                   },
        ),
    )
    description = CharField(
        label='Описание',
        widget=SummernoteWidget(),
    )

    category = CharField(
        initial='Не выбрано',
        label='Категория',
        widget=Select(
            choices=CATEGORIES,
            attrs={'class': 'form-select', 'name': 'category'},
        ),
    )

    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'category',
        ]


class ReplyForm(ModelForm):
    """
    Для записи нового отклика на странице с откликами
    """
    class Meta:
        model = Reply
        fields = [
            'text',
        ]
