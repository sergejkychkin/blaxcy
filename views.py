from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import users
from django.core.serializers import serialize
from ace.models import *

from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
import base64

def authentication(username,password):
    if(ndb.Key("Users",username).get().password == password):
        return ndb.Key("Users",username)



def bcx(f):
    def g(request,*args,**kwargs):

        if request.META.get("HTTP_AUTHORIZATION",False):
            authtype , auth = request.META["HTTP_AUTHORIZATION"].split()
            auth = base64.b64decode(auth)
            username,password = auth.split(":")
            auths = authentication(username=username,password=password)
            if(auths):

                if auths.get().is_active:
                    kwargs["user"] = auths
                    print kwargs


                    return f(request,*args,**kwargs)
                else :
                    r = HttpResponse(str(args),status = 401)

                    r["WWW-Authenticate"] = "Basic realm='bats'"
                    return r
        r = HttpResponse(str("hello"),status = 401)
        r["WWW-Authenticate"] = "Basic realm='batx'"
        return r
    return g






class User_View(View):


    def get(self,request,*args,**kwargs):
        return HttpResponse(self.kwargs["user"])

class Post_View(blobstore_handlers.BlobstoreUploadHandler,View):

    def create_post(self,calls,user,description,pictures=None):

        post = Post(user=user,calls=calls,description=description,photo_url=ndb.B(pictures))

        return post.put()


    def get(self,request,*args,**kwargs):
        #query = query.fetch()
        calls = int(request.GET["calls"])
        description = request.GET["description"]
        post = self.create_post(user=self.kwargs["user"],calls=calls,description=description)





        return HttpResponse(post.get())
    #def delete(self,request,*args,**kwargs):
    def post(self,request,*args,**kwargs):
        upload_url = blobstore.create_upload_url("/photos")
        #calls = int(request.POST["calls"])
        #description = request.POST["description"]
        photo = request.FILES["photo"]
        #post = self.create_post(user=self.kwargs["user"],calls=calls,description=description,pictures=photo)

        return HttpResponse(photo.key())







        #return HttpResponse(self.create_post(calls=int(calls),description=description,user=self.kwargs["user"].key))




@csrf_exempt
def registration(request,*args,**kwargs):
    user_key = ndb.Key(Users,request.GET["id"])
    user  = Users(email = request.GET["email"],password=request.GET["password"])
    user.key = user_key
    user.put()

    #user = User(email=request.GET["email"],password=request.GET["password"])
    #user.key = user_key
    #user = user.put()



    return HttpResponse()
def get(request,*args,**kwargs):

    return HttpResponse(a)
