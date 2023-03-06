from django.shortcuts import render
import googletrans
# Create your views here.
def index(request):
    bf = request.GET.get("bf", "")
    to = request.GET.get("to", "")
    context = {
        "ndict" : googletrans.LANGUAGES,
        "to" : to,
    }
    if bf:
        trans = googletrans.Translator()
        after = trans.translate(bf, dest=to)
        context.update({
            "bf" : bf,
            "af" : after.text,
            "fr" : after.src
        })

    return render(request, "trans/index.html", context)