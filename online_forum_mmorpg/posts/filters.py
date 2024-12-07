from django_filters import FilterSet, CharFilter, DateFilter, ChoiceFilter
from django.forms import Select, TextInput, DateInput
from posts.models import Post


class PostFilter(FilterSet):
    """
    Фильтр для поиска объявлений
    """
    author = CharFilter(
        field_name='user__last_name',
        label='Автор',
        lookup_expr='icontains',
        widget=TextInput(
            attrs={'type': 'text',
                   'class': "form-control",
                   'placeholder': "Введите поисковый запрос...",
                   'aria-label': "Введите поисковый запрос...",
                   'aria-describedby': "button-search",
                   },
        ),
    )

    type = ChoiceFilter(
        field_name='author',
        label='Поиск по типу объявления',
        choices=[
        ('my_reactions', 'Мои'),
        ('reactions', 'Пользователей'),
            ],
        widget=Select(
            attrs={"class": "form-control"},
        ),
    )
    category = ChoiceFilter(
        field_name='category',
        label='Поиск по категории объявления',
        choices=Post.CATEGORIES,
        widget=Select(
            attrs={"class": "form-control"},
        ),
    )

    title = CharFilter(
        field_name='title',
        label='Наименовние',
        lookup_expr='icontains',
        widget=TextInput(
            attrs={'type': 'text',
                   'class': "form-control",
                   'placeholder': "Введите поисковый запрос...",
                   'aria-label': "Введите поисковый запрос...",
                   'aria-describedby': "button-search",
                   },
        ),
    )

    # create_date__gt = DateFilter(
    #     field_name="create_date",
    #     label="От даты",
    #     lookup_expr='gt',
    #     widget=DateInput(
    #         attrs={'type': 'date',
    #                'class': "form-control",
    #                },
    #     ),
    # )

    class Meta:
        model = Post
        fields = ['title',
                  'author',
                  'category',
                  'type',
                  ]
