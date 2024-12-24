from django_filters import FilterSet, CharFilter, DateFilter
from django.forms import TextInput, DateInput
from news.models import News


class NewsFilter(FilterSet):
    """
    Фильтр для поиска Новостей
    """
    author = CharFilter(
        field_name='user__last_name',
        label='Автор',
        lookup_expr='icontains',
        widget=TextInput(
            attrs={'type': 'text',
                   'class': 'form-control',
                   'placeholder': 'Введите поисковый запрос...',
                   'aria-label': 'Введите поисковый запрос...',
                   'aria-describedby': 'button-search',
                   },
        ),
    )

    create_date__gt = DateFilter(
        field_name='create_date',
        label='От даты',
        lookup_expr='gt',
        widget=DateInput(
            attrs={'type': 'date',
                   'class': 'form-control',
                   },
        ),
    )

    class Meta:
        model = News
        fields = ['title',
                  'author',
                  'create_date__gt',
                  'text',
                  ]
