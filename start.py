from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import blobstore
import base64
from models import *
import webapp2







def authentication(username,password):
    #test.response.out.write("yo")
    user  = ndb.Key("Users",username)
    
    if (user):
        if ((user.get()).password == password):
            return (user.get())
        return False 
        
    return False
#from view import *

def bcyx(f):
    auth = f.authorization[1]
    #a = base64.b64decode(auth).split(":")
    #f.response.out.write(authentication(a[0], a[1]))
    if (auth):
        username,password = (base64.b64decode(auth)).split(":")
        user = authentication(username,password)
        if user.is_active:
            
            return user
            #return True
        
        return False
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
        self.response.out.write(link.urlsafe())
        
        
        
        pass
    def put(self,*args,**kwargs):# update user data
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        # authentifizierung
        #
        password_2 = self.request.POST["password2"]
        email = self.request.POST["email"]
        user  = Users(password=password_2,id=username,email=email)#
        # Users get by id 
        #
        link = user.put()
        self.response.out.write(link.urlsafe())
    def delete(self,*args,**kwargs):# delete user data
        # user get by id an delete
        #
        #
        pass
           
       
class MainPage(webapp.RequestHandler):
    
    def post(self):
        user = bcyx(self.request)
        
        if (user):
            self.response.out.write(user)
        else : 
            self.response.out.write("nope")
        
    
    
    def get(self):
        upload_url = blobstore.create_upload_url('/hello')
        self.response.out.write('<html><body>')
        self.response.out.write('<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url )#% upload_url)
        self.response.out.write('''Upload File: <input type="file" name="file"><br> <input type="submit"
        name="submit" value="Submit"> </form></body></html>''')
        
        


class PhotoUploadFormHandler(webapp2.RequestHandler):
    def get(self):
        # [START upload_url]
        upload_url = blobstore.create_upload_url('/upload_photo')
        # [END upload_url]
        # [START upload_form]
        # The method must be "POST" and enctype must be set to "multipart/form-data".
        self.response.out.write('<html><body>')
        self.response.out.write('<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url)
        self.response.out.write('''Upload File: <input type="file" name="file"><br> <input type="submit"
            name="submit" value="Submit"> </form></body></html>''')
        # [END upload_form]

# [START upload_handler]

class User_Content(webapp2.RequestHandler):
    def get(self):
        # json serialization 
        # 
        #
        
        user = bcyx(self.request)
        
        if (user):
            content = Post.query(user=user)
            
            self.response.out.write(content.fetch())
        else : 
            self.response.out.write("nope")



#
#finished getting photos 
def getting_content(request):
    n =ndb.Key(urlsafe="agpkZXZ-YmxheGN5chELEgRQb3N0GICAgICAgMAIDA")
    #user = bcyx(request)
    
    #if(user):
    b = Post.get_by_id(5066549580791808)
    
    
    request.response.out.write(b.calls)
    

class PhotoUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    # todo : setting up google cloud storage
    # https://cloud.google.com/appengine/docs/python/blobstore/
    #
    def get(self):
        # get session link for upload 
        # make it in json 
        #
        
        
        upload_url = blobstore.create_upload_url('/upload_photo')
        self.response.out.write(upload_url)
        #self.response.out.write(upload_url)
        #self.response.out.write('<html><body>')
        #self.response.out.write('<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url)
        #self.response.out.write('''Upload File: <input type="file" name="file"><br> <input type="submit" name="submit" value="Submit"> </form></body></html>''')
    def post(self):
        user = bcyx(self.request)
        # if file is jpg else : 
        #
        #
        
        
        if (user):
            
            try:
                upload = self.get_uploads()[0]
            
                user_photo = Post(photo_url=upload.key(),calls=234,description="helloworld",user=user.key)
                s = user_photo.put()
                self.response.out.write('/view_photo/%s' % upload.key())
            #print 
           

            #self.redirect('/view_photo/%s' % upload.key())

            except:
                self.error(500)
            finally:
                pass
                # sendinf back a link of photo
            
            
        
# [END upload_handler]

# [START download_handler]
class ViewPhotoHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, photo_key):
        if not blobstore.get(photo_key):
            self.error(404)
        else:
            
            self.send_blob(str(photo_key))
            # 
            #
            #
            #
            """
            a = blobstore.get(photo_key)
            if (a):
                id =ndb.Key(urlsafe="agpkZXZ-YmxheGN5chELEgRQb3N0GICAgICAgKgJDA").get()"""
                
                
            
            #self.send_blob(photo_key)
            
  
class follow(webapp2.RequestHandler):
    
    def get(self):
        user = bcyx(self.request)
        if(user):
            #folow = 
            self.response.out.write()
            pass
        
        
        
    def post(self):
        pass

    
def testcode(request):
    post = ndb.gql("select calls from Post").fetch()
    
    request.response.out.write(post)
             
APPLICATION = webapp.WSGIApplication([(r'/',User_Handler),
                                      (r"/user",User_Content),
                               ('/upload_photo', PhotoUploadHandler),
                               ('/view_photo/([^/]+)?', ViewPhotoHandler),("/so",getting_content),("/test",testcode)], debug=True)

"""
user_content 

user_upload

post_coant 
""" 

"""
curl -X POST http://localhost:8082/ -d "username=ubuntu&email=ubuntu&password=ubuntu"
curl -X GET http://localhost:8082/upload_photo  #getted_link 
curl -X POST getted_link -u "ubuntu:ubuntu" -F "image=@image_path"





"""


def main():
    run_wsgi_app(APPLICATION)

if __name__ == "__main__":
    main()
