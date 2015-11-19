#from django.db import models

# Create your models here.
from google.appengine.ext import ndb



class HashTag(ndb.Model):

    date = ndb.DateProperty(auto_now_add=True)

class Users(ndb.Model):
    password  = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    date = ndb.DateProperty(auto_now_add=True)
    is_active = ndb.BooleanProperty(default=True)



    #following_user = ndb.StructuredProperty(kind="Users",name="following_user") # following other User
    following_user = ndb.KeyProperty(kind="Users",repeated=True)
    following_tag = ndb.KeyProperty(kind=HashTag,repeated=True) # following hashtags
# Create your models here.





"""



#following user
class Following_User(ndb.Model):

    user_id = ndb.KeyProperty(Users,name="user")
    user_follow  = ndb.KeyProperty(User,"follow")# repeat true : cuz one to many relationships







#following hashtags class
class Following_Tag(ndb.Model):
    user_id = ndb.StructuredProperty(User)
    user_follow_hashtag = ndb.StructuredProperty(HashTag) # repeat true : cuz one to many relationships
    user_follow_hashtag = ndb.KeyProperty(HashTag)



"""




class Post(ndb.Model):
    #date
    # Hashtag : later
    # photo
    # calls + delete
    # user
    # description
    date = ndb.DateTimeProperty(auto_now_add=True)
    calls = ndb.IntegerProperty(required=True)
    user = ndb.KeyProperty(kind=Users,required=True)
    description = ndb.StringProperty()
    photo_url = ndb.BlobKeyProperty(required=True)
    #som = ndb.ComputedProperty(lambda self : Post.minus(self))
    def minus(self):
        try:
            self.calls -= 1
        except:
            print "not good"
        finally: 
            self.put()
            if (self.calls <= 0):
                #
                #make deleting 
                
                try:
                    self.delete()
                except:
                    print "not good 2"
                finally: 
                    self.put()
                    pass
            else : 
                return self.calls
        
                
            
    
    def __unicode__(self) :
        return str(self.key.id())
        
    #hashtags = ndb.StructuredProperty(Hashtag,repeat=True)
    # photo_url = ndb.StringProperty()



"""
#hastags of a postclass
class Hashtag(ndb.Model):
    post_id = models.ForeignKey(Post)
    hashtag = models.ForeignKey(hash_tagg)

"""


#taggin a user who have should recive this post
"""
class tag_user(ndb.Model):
    post_id = ndb.StructuredProperty(Post)
    attag = ndb.StructuredProperty(User)
"""
