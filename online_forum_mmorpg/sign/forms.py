from allauth.account.forms import SignupForm, LoginForm, PasswordField
from django.contrib.auth.models import Group
from django import forms


class BasicLoginForm(LoginForm):
    password = PasswordField(label="Пароль", autocomplete="current-password")

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)

        login_widget = forms.TextInput(attrs={'type': 'email',
                                              'placeholder': 'Введите адрес эл.почты',
                                              'autofocus': 'autofocus'})
        login_field = forms.EmailField(label="Email",
                                       widget=login_widget)

        self.fields["login"] = login_field


class BasicSignupForm(SignupForm):
    """
    Кастомизируем форму регистрации SignupForm, которую предоставляет пакет allauth.
    """
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)

        # Добавляем нового пользователя в группу рассылки объявлений
        # (По умолчанию, все пользователи подписаны на рассылку. Отписаться можно в личном кабинете)
        common_group = Group.objects.get(name='common')
        newsletter_group = Group.objects.get(name='postsletter')
        common_group.user_set.add(user)
        newsletter_group.user_set.add(user)

        return user
