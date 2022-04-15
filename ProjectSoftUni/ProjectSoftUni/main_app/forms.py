from django import forms

from ProjectSoftUni.main_app.models import Recipe, Product, Course


class CreateRecipeForm(forms.ModelForm):
    def __init__(self, author, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.author = author

        self.fields['image'].required = True
        # self.fields['title'].label = ''
        self.fields['servings'].widget.attrs['min'] = 1
        self.fields['servings'].widget.attrs['max'] = 21

    def save(self, commit=True):
        recipe = super().save(commit=False)

        recipe.author = self.author
        if commit:
            recipe.save()
        return recipe

    class Meta:
        model = Recipe

        fields = ('title', 'image', 'category', 'servings', 'description')


class EditRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].label = ''
        self.fields['servings'].widget.attrs['min'] = 1
        self.fields['servings'].widget.attrs['max'] = 21

    class Meta:
        model = Recipe
        fields = ('title', 'image', 'category', 'servings', 'description')

        widgets = {
            'image': forms.FileInput(),
        }


class AddProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image'].required = True

    class Meta:
        model = Product
        fields = ('name', 'image', 'info', 'price')
        widgets = {
            'image': forms.FileInput(),
        }


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'image', 'info', 'price')
        widgets = {
            'image': forms.FileInput(),
        }


class AddCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image'].required = True

    class Meta:
        model = Course
        fields = ('name', 'image', 'link')
        widgets = {
            'image': forms.FileInput(),
        }


class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'image', 'link')
        widgets = {
            'image': forms.FileInput(),
        }
