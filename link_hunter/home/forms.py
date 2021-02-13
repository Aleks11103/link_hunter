from django import forms
from home.models import QuickContact


class QuickContactForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        label='User name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name *',
            }
        ),
    )
    email = forms.EmailField(
        label='User email',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email *'
            }
        ),
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Message *',
                'rows': 3,
            }
        )
    )

    def save(self):
        return QuickContact.objects.create(**self.cleaned_data)

    def clean(self):
        error = False
        if len(self.cleaned_data['name']) > 30:
            error = True
            self.add_error('name', ['Максимум 30 символов', 'Ещё какая-то ошибка'])
        if not self.cleaned_data['email'].endswith(".com"):
            error = True
            self.add_error('email', 'Не кашерный email')
        if 'FUCK' in self.cleaned_data['message']:
            error = True
            self.add_error('message', 'Не ругайтесь!!!')
        if error:
            raise forms.ValidationError('Не корректные данные!!!')
        print(self.cleaned_data)
        return self.cleaned_data


class QuickForm(forms.ModelForm):
    
    class Meta:
        model = QuickContact
        exclude = ('is_moderate',)
