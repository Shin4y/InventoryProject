from django import forms
from crispy_forms.helper import FormHelper

class BatchForm(forms.Form): #a form used to swap name 1 and name 2 machines. names refer to the name field of said machines
	name1 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name 1'}))
	name2 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name 2'}))
	owner1 = forms.CharField(max_length=50, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'New Owner 1'}))
	owner2 = forms.CharField(max_length=50, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'New Owner 2'}))

	extra_field_count = forms.CharField(widget=forms.HiddenInput())

	def __init__(self, *args, **kwargs):
		extra_fields = kwargs.pop('extra', 0)
		super(BatchForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'swapForm'
		self.helper.form_method = 'post'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-1'
		self.helper.field_class = 'col-md-3'
		self.helper.form_show_labels = False
		self.helper.render_hidden_fields = True
		self.fields['extra_field_count'].initial = extra_fields

		self.helper.layout = Layout(
		    Field('name1', placeholder = 'Name 1'),
		    Field('name2', placeholder = 'Name 2')
		)

		for index in range(int(extra_fields)):
			# generate extra fields in the number specified via extra_fields
			self.fields['extra_field_{index}'.format(index=index)] = \
				forms.CharField()
			self.fields['extra_owner_{index}'.format(index=index)] = forms.CharField()

class EditForm(forms.Form):
