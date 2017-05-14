from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateUserForm(UserCreationForm): # ���� ȸ������ ���� ��ӹ޾Ƽ� Ȯ���Ѵ�.
    email = forms.EmailField(required=True) # �̸��� �ʵ� �߰�

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True): # �����ϴ� �κ� �������̵�
        user = super(CreateUserForm, self).save(commit=False) # ������ �θ� ȣ���ؼ� �����ϰڴ�.
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
