from django import forms
class UserForm(forms.Form):
    #name=forms.CharField(label="Имя чела")
    name = forms.CharField(label="Имя клиента", max_length=15, help_text="ФИО не более 15 символов")
    age=forms.IntegerField(label="LVL чела")
    vyb = forms.NullBooleanField(label="Вас всё достало?", required=False)
    email = forms.EmailField(label="Электронный адрес")
    url_text = forms.URLField(label="Введите URL")
    file_path = forms.FilePathField(label="Выберите файл", path=r"C:\Users\Олежа\Desktop\Папка", required=False)
    file = forms.FileField(label="Файл", required=False)
    regex = forms.RegexField(label="Введите текст", regex=r'^[a-zA-Z0-9]*$', help_text="Только буквы и цифры", required=False)
    basket = forms.BooleanField(label="Вы живой?", required=False)
