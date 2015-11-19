'''
Created on Oct 3, 2015

@author: bcy-3
'''
from google.appengine.ext import webapp
import base64
from google.appengine.ext.webapp import blobstore_handlers
from models import *
"""
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
"""

def authentication(username,password):
    return True
    #pass# authernticate user


def bcyx(f):
    auth = f.request.authorization.get[1]
    if auth:
        auth = base64.b64decode(auth)
        username,password = auth.split(":")
        auth = authentication(username, password)
        if (auth):
            return True
        else : 
            return False
    else:
        return False
    
    




        
class User_Handler(webapp.RequestHandler):
    def get(self,*args,**kwargs):#get user data 
        self.response.out.write("hello you")
    def post(self,*args,**kwargs):#create user data
        # todo : try 
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        email = self.request.POST["email"]
        user  = Users(password=password,id=username,email=email)
        link = user.put()
        self.response.out.write(link)
        
        
        
        pass
    def put(self,*args,**kwargs):# update user data
        pass
    def delete(self,*args,**kwargs):# delete user data
        
        
        
        