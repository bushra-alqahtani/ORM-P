from multiprocessing import context
import re
from django.shortcuts import redirect, render

from app_one.models import Movie

# Create your views here.
def  index(request):
    return render(request,"index.html")

def createMovie(request):

    #check for POST method
    if request.method == "POST":
        mtitle=request.POST["mtitle"]
        mdescription=request.POST["mdescription"]
        mrelease_date=request.POST["mrelease_date"]
        mduration=request.POST["mduration"]
        #create new object of movie to assigning 
        movie=Movie.objects.create(title=mtitle , description=mdescription , release_date=mrelease_date , duration=mduration)
       
        #session to store some info between requests 
        request.session["message"]="the form submitted successfuly"
        print(movie.id)
        print(movie.pk)
        return redirect('/create-movie') #user doesnot need to resubmitt the form 

        # to print session 
    context={
            "message":request.session.pop("message","")
        }

    return render(request,"create-movie.html",context)




def list(request):
    movies=Movie.objects.all()
    context={
        "movies":movies
    }
    return render(request,"list.html",context)

def info(request,movieid):
    movie=Movie.objects.get(id=movieid)
    context={
        "movie":movie
    }
    return render(request,"view.html",context)