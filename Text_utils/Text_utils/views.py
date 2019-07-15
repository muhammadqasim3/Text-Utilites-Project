# I have Created this File - Qasim Aslam
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    # Get the text
    text = request.GET.get('text', 'default')
    #Default checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    allcaps = request.GET.get('allcaps', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
    spaceremove = request.GET.get('spaceremove', 'off')
    charcount = request.GET.get('charcount', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
    # Parameters pass variable to html For changing html
        parameters = {'purpose':'removed Punctuations', 'analyzed_text': analyzed}
        return render(request, "analyze.html", parameters)
    elif allcaps == "on":
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        parameters = {'purpose':'To Upper Case', 'analyzed_text': analyzed}
        return render(request, "analyze.html", parameters)
    elif newlineremove == "on":
        analyzed = ""
        for char in text:
            if not char == "\n" and char != "\r":
                analyzed = analyzed + char
        parameters = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        return render(request, "analyze.html", parameters)
    elif spaceremove == "on":
        analyzed = ""
        for index, char in enumerate(text):
            if not (text[index] == " " and text[index + 1] == " "):
                analyzed = analyzed + char
        parameters = {'purpose': 'Remove Extra spaces', 'analyzed_text': analyzed}
        return render(request, "analyze.html", parameters)
    elif charcount == "on":
        analyzed = len(text)
        parameters = {'purpose': 'Remove Extra spaces', 'analyzed_text': analyzed}
        return render(request, "analyze.html", parameters)
    else:
        return HttpResponse("Please click the checkbox first.")
