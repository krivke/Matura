from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
	
	email = forms.EmailField(widget=forms.TextInput(
			attrs={"class":"email-field hind","placeholder":"Unesi svoj e-mail"}
			
			),label=""
		)

	poruka = forms.CharField(
			widget=forms.Textarea(attrs={"placeholder":"Ovdje napiši svoju poruku...","class":"poruka-field hind"}),label=""
		)


	def clean_email(self):
		email = self.cleaned_data.get("email")
		
		if "@gmail.com" not in email:
			raise ValidationError("Invalid email")

		return email

	def clean_poruka(self):
		swear_words = ["fuck","nigger","dogshit","jeb"]
		poruka = self.cleaned_data.get("poruka")
	
		for word in swear_words:

			if word in poruka:
				
				raise ValidationError("Inappropriate message")

		return poruka





