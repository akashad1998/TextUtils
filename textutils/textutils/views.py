from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    ok = 0
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    
    if removepunc == 'on':
        ok = 1
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed

    if fullcaps == 'on':
        ok = 1
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
    
    if newlineremove == 'on':
        ok = 1
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        djtext = analyzed

    if extraspaceremove == 'on':
        ok = 1
        n = len(djtext)
        analyzed = ""
        for index, char in enumerate(djtext):
            if index == n-1:
                if char != " ":
                    analyzed = analyzed + char
                break
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        djtext = analyzed
    
    if charcount == 'on':
        ok = 1
        analyzed = " Total Characters in Text = ";
        count = 0
        for char in djtext:
            if char != " " and char != '\n':
                count = count + 1
        params = {'purpose' : 'Total Characters', 'analyzed_text' : analyzed + str(count)}
        return render(request, 'analyze.html', params)
        
    if ok == 0:
        return HttpResponse("Error!")
    else:
        params = {'purpose' : 'Actions Performed', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)
        