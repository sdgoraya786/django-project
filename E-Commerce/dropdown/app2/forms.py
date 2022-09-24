from email.policy import default
from django import forms
from .models import Product, ParentCategory, ChildCategory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        

# child 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['child_category'].queryset = ChildCategory.objects.none()

        if 'parent_category' in self.data:
            try:
                parent_category_id = int(self.data.get('parent_category'))
                self.fields['child_category'].queryset = ChildCategory.objects.filter(
                    parent_category_id=parent_category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.parent_category:
            self.fields['child_category'].queryset = self.instance.parent_category.child_category_set.order_by(
                'name')


CHILD_CATEGORY_STATUE_CHOICE = (
    ('1','Active')
)
class AdminForm(forms.ModelForm):
    is_active = forms.ChoiceField(choices=CHILD_CATEGORY_STATUE_CHOICE, widget=forms.CheckboxInput)
    class Meta:
        model = ChildCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_active'].widget = forms.CheckboxInput(
            attrs={
                'id': 'id_is_active',
                'style': 'width:200px',
                'checked': 'False'
            }
        )