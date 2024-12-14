from django_filters import FilterSet, CharFilter, ChoiceFilter
from django.forms import Select, TextInput
from posts.models import Post, Reply


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

    class Meta:
        model = Post
        fields = ['title',
                  'author',
                  'category',
                  ]


class ReplyFilter(FilterSet):
    """
    Фильтр для поиска откликов
    """
    status = ChoiceFilter(
        field_name='status',
        label='Поиск по статусам откликов',
        choices=[
            ('approved', "Принятые"),
            ("rejected", "Отклоненные"),
            ("new", "Новые"),
        ],
        widget=Select(
            attrs={"class": "form-control"},
        ),
    )

    type = ChoiceFilter(
        field_name='author',
        label='Поиск по типу отклика',
        choices=[
            ('my_reactions', 'Оставленные мной'),
            ('reactions', 'Пользователей'),
        ],
        widget=Select(
            attrs={"class": "form-control"},
        ),
    )

    class Meta:
        model = Reply
        fields = ['post__author',
                  'text',
                  'create_date',
                  'status',
                  'type',
                  ]
