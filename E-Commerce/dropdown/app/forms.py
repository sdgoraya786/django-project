from dataclasses import fields
from django import forms
from .models import Product, ParentCategory, ChildCategory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # super(Product, self).__init__()
        super().__init__(*args, **kwargs)

        # when there is instance key, select the default value
        # Provinsi always loaded for initial data, because Provinsi is on the first level 
        try:
            self.initial['app_parent_category'] = kwargs['instance'].app_parent_category.id
        except:
            pass
        parent_category_list = [('', '---------')] + [(i.id, i.parent_cat) for i in ParentCategory.objects.all()]

        # Kabupaten, Kecamatan, and Kelurahan is on the child level, it will be loaded when user click the parent level
        try:
            self.initial['app_child_category'] = kwargs['instance'].app_child_category.id
            child_category_init_form = [(i.id, i.child_cat) for i in ChildCategory.objects.filter(parent_category=kwargs['instance'].app_parent_category)]
        except:
            child_category_init_form = [('', '---------')]

        # try:
        #     self.initial['kecamatan'] = kwargs['instance'].kecamatan.id
        #     kecamatan_init_form = [(i.id, i.name) for i in Kecamatan.objects.filter(
        #         kabupaten=kwargs['instance'].kabupaten
        #     )]
        # except:
        #     kecamatan_init_form = [('', '---------')]

        # try:
        #     self.initial['kelurahan'] = kwargs['instance'].kelurahan.id
        #     kelurahan_init_form = [(i.id, i.name) for i in Kelurahan.objects.filter(
        #         kecamatan=kwargs['instance'].kecamatan
        #     )]
        # except:
        #     kelurahan_init_form = [('', '---------')]

        # Override the form, add onchange attribute to call the ajax function
        self.fields['parent_category'].widget = forms.Select(
            attrs={
                'id': 'id_parent_category',
                'onchange': 'getchildcat(this.value)',
                'style': 'width:200px'
            },
            choices=parent_category_list,
        )
        self.fields['child_category'].widget = forms.Select(
            attrs={
                'id': 'id_child_category',
                'style': 'width:200px'
            },
            choices=child_category_init_form
        )