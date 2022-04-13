from django import forms    
import os

class NoviNaslovForm(forms.Form):
    name = forms.CharField()

    #za svaki novi naslov napravi odgovarajuci html,css,js
    def save(self,*args,**kwargs):
        name = self.cleaned_data["name"]  
        name = name.lower().replace(" ","_")
      
        #html
        name_html = name + ".html" 
        path = os.path.join(os.getcwd(),f"hrvatski\\templates\\lekcije\\{name_html}")
        file = open(path,"w")
        file.close()
        #css
        name_css = name + ".css"
        path_css = os.path.join(os.getcwd(),f"main\\static\\css\\cro\\{name_css}")
        file = open(path_css,"w")
        file.close()
        #js
        name_js = name + ".js"
        path_js = os.path.join(os.getcwd(),f"main\\static\\js\\cro\\{name_js}")
        file = open(path_js,"w")
        file.close()
  
