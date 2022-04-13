from django.test import TestCase
from .models import Predmet,Razred,Naslov
from django.test import Client
from .forms import ContactForm
# Create your tests here.


class Testing(TestCase):

	def setUp(self):
		client = Client()
		self.client = client

		predmet = Predmet.objects.create(name="Matematika")
		razred = Razred.objects.create(name="Prvi razred",predmet=predmet)
		naslov = Naslov.objects.create(name="Trigonometrijske funkcije",predmet=predmet,razred=razred)
		
		self.predmet = predmet
		self.razred = razred
		self.naslov = naslov




	def test_home_page(self):

		home_page = "/"
		response = self.client.get(home_page)
		

		contact = self.client.post(
			home_page,
			data={"email":"dkrivic22@gmail.com","poruka":"ovo je test"}
			)
		

	
		
		self.assertEqual(contact.status_code,302)
		self.assertEqual(response.status_code,200)
		

	def test_predmet_page(self):
		predmet_page = "/" + str(self.predmet.name) + "/"
		response_2 = self.client.get(predmet_page)

		self.assertEqual(response_2.status_code,200)


	def test_unittest_bad_words_should_fail(self):
		form = ContactForm(data={"email":"dkrivic22@gmail.com",
								"poruka":"niggers jebemti mater"})

		self.assertEqual(form.errors["poruka"],["Inappropriate message"])
	

