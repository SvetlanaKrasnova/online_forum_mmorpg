from django.forms import ModelForm, TextInput, CharField, Textarea, Select
from .models import Post, Reply
from django_summernote.widgets import SummernoteWidget


class PostForm(ModelForm):
    title = CharField(
        label='Наименовние',
        widget=TextInput(
            attrs={'type': 'text',
                   # 'class': "form-control form_field_post",
                   # 'placeholder': "Наименование объявления",
                   },
        ),
    )
    description = CharField(
        label='Описание',
        widget=SummernoteWidget(),
    )

    category = CharField(
        initial="Не выбрано",
        label="Категория",
        widget=Select(
            choices=Post.CATEGORIES,
            attrs={"class": "form-select", "name": "category"},
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
    class Meta:
        model = Reply
        fields = [
            'text',
        ]
