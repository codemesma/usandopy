from django import forms
from .models import Post, Category, Feedback, ROLE_CHOICE, Theme
from django.template.defaultfilters import slugify
# for authentication
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=ROLE_CHOICE, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password', 'is_active')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if self.instance.id:
            if User.objects.filter(email=email, username=username).exclude(id=self.instance.id).count():
                raise forms.ValidationError(u'Email addresses must be unique.')
        else:
            if User.objects.filter(email=email).exclude(username=username).count():
                raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        for field in iter(self.fields):
            if max(enumerate(iter(self.fields)))[0] != field:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    "placeholder": "Please enter your " + field.capitalize()
                })

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user


class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Incorrect Login Details")

        return self.cleaned_data


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('slug', 'user', 'tags')

    def __init__(self, *args, **kwargs):
        self.user_role = kwargs.pop('user_role', None)
        super(BlogPostForm, self).__init__(*args, **kwargs)

        if self.user_role == 'Author':
            del self.fields['status']

        self.fields['category'].queryset = Category.objects.filter(
            is_active=True)

    def clean_status(self):
        if self.user_role == "Author":
            raise forms.ValidationError(
                "Admin and Publisher can change status only.")
        return self.cleaned_data.get("status")


class BlogCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('slug',)

    def clean_name(self):
        if not self.instance.id:
            if Category.objects.filter(slug=slugify(self.cleaned_data['name'])).exists():
                raise forms.ValidationError(
                    'Category with this Name already exists.')
        else:
            if Category.objects.filter(name__icontains=self.cleaned_data['name']).exclude(id=self.instance.id):
                raise forms.ValidationError(
                    'Category with this Name already exists.')

        return self.cleaned_data['name']

    def __init__(self, *args, **kwargs):
        super(BlogCategoryForm, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            if max(enumerate(iter(self.fields)))[0] != field:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control', "placeholder": "Please enter your Category " + field.capitalize()
                })


class UserRoleForm(forms.Form):
    role = forms.CharField(max_length=10)


class BlogThemeForm(forms.ModelForm):

    class Meta:
        model = Theme
        exclude = ('slug',)
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(BlogThemeForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                "placeholder": "Please enter your Theme " + field.capitalize()
            })


class ChangePasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!!!")
        return confirm_password


class CustomBlogSlugInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super(CustomBlogSlugInlineFormSet, self).clean()
        if any(self.errors):
            return
        active_slugs = 0
        for form in self.forms:
            if form.cleaned_data.get("is_active"):
                active_slugs += 1
        if active_slugs > 1:
            raise forms.ValidationError(
                "Only one slug can be active at a time.")
