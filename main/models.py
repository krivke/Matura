from django.db import models
from django.db.models.fields import related
from django.urls import reverse

from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save


class AbstractModel(models.Model):
	name = models.CharField(max_length=300)

	class Meta:
		abstract = True
	def __str__(self):
		return self.name
	
	@property
	def get_name(self):
		return str(self.name)

class Predmet(AbstractModel):

	class Meta:
		verbose_name_plural = "Predmeti"
		ordering = ["id"]

	


class Razred(models.Model):
	id = models.AutoField(primary_key=True)
	predmet = models.ForeignKey(Predmet,related_name="razredi",on_delete=models.CASCADE,null=True)
	RAZRED_CHOICES = (
		("Prvi Razred","prvi"),
		("Drugi Razred","drugi"),
		("Treci Razred","treci"),
		("Cetvrti Razred","cetvrti")
	)
	name = models.CharField(max_length=50,choices=RAZRED_CHOICES)

	class Meta:
		verbose_name_plural = "Razredi"
	
		ordering = ["id"]

	def __str__(self):
		return f"{self.name} - {self.predmet}"
	def get_all_N(self):
		return Naslov.objects.filter(razred=self.id)
	@property
	def get_name(self):
		return str(self.name)

class Naslov(AbstractModel):
	predmet = models.ForeignKey(Predmet,related_name="predmetni_naslov",on_delete=models.CASCADE,null=True)
	razred = models.ForeignKey(Razred,related_name="razredni_naslov",on_delete=models.CASCADE,null=True)


	class Meta:
		verbose_name_plural = "Naslovi"
		ordering = ["id"]

	
		
"""
class Podnaslov(AbstractModel):
	predmet = models.ForeignKey(Predmet,related_name="podnaslov_predmet",on_delete=models.CASCADE,null=True)
	razred = models.ForeignKey(Razred,on_delete=models.CASCADE,null=True,related_name="podnaslov_razred")
	naslov = models.ForeignKey(Naslov,on_delete=models.CASCADE,null=True,related_name="podnaslov_naslov")
	
	slug = models.SlugField(unique=True,null=True,blank=True)


	class Meta:
		verbose_name_plural = "Podnaslovi"
		ordering = ["id"]





def create_slug(instance,new_slug=None):
	slug = slugify(instance.name)

	if new_slug is not None:
		slug = new_slug
	qs = Podnaslov.objects.filter(slug=slug)
	exists = qs.exists()
	
		
	if exists:
		new_slug = "%s-%s" %(slug,qs.first().id)
		return create_slug(instance,new_slug=new_slug)
	return slug




@receiver(pre_save,sender=Podnaslov)
def slug_field(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

"""