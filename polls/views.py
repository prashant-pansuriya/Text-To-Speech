from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import  HttpResponse
from .models import  Song
from gtts import gTTS
import os

# Home Function
def index(request):
    # Get request
    if request.method == "GET":
        path = Song.objects.get(id=2).song_file.url
        print(path)
        return render(request, "index.html")

    else:
        if request.method == 'POST' and request.FILES['audio']:
            myfile = request.FILES['audio']

            # File Exits Then Only fetch file
            if os.path.exists(myfile.name):
                file_url = "/media/"+myfile.name

            # File Save
            else:
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                file_url = fs.url(filename)
                print(file_url)

            return render(request, 'index.html', {
                'path': file_url, "flag": 1, "name" : myfile.name
            })

def audio(request, path):
    f = open(path, "rb")
    response = HttpResponse()
    response.write(f.read())
    response['Content-Type'] = 'audio/mp3'
    response['Content-Length'] = os.path.getsize(path)
    return response

# File Counter
c = 0
# File Name Store
name = []
def text_to_speech(request):
    global c
    global name

    if request.method == 'POST' :
        # All File Remove in Present in List
        for i in name:
            os.remove(i)
        # clear List
        name = []
        mytext = request.POST.get("text")
        language = 'en'
        path = str(c)+"welcome.mp3"
        name.append(path)
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save(path)
        c = c + 1
        return render(request, 'index.html', {
              'path': "/media/"+path, "flag" :  1, "name" : path
        })







