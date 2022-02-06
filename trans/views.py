from django.shortcuts import render
import googletrans
# print(googletrans.LANGUAGES)
from googletrans import Translator

# Create your views here.
def index(request):
    
    # d = {1:"one", 2:"two", 3:"three"}
    context = {
        "ndict" : googletrans.LANGUAGES
    }

    if request.method == "POST":
        bf = request.POST.get("bf").strip()
        if bf:
            fr = request.POST.get("fr")
            to = request.POST.get("to")

            translator = Translator()
            trans1 = translator.translate(bf, src=fr, dest=to) 
    
            context.update({
                "af" : trans1.text,
                "bf" : bf,
                "fr" : fr,
                "to" : to
            })


    return render(request, 'trans/index.html', context)