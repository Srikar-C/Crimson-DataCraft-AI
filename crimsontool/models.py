from django.db import models

# Create your models here.

class Uploads:
    id : int
    title: str
    boolean: bool
    desc: str
    filetype: str
    img: bool
    video : bool
    link: bool
    folder:bool


from django.db import models
from embed_video.fields import EmbedVideoField

from jsonfield import JSONField

class YTLinks(models.Model):
    LinkName = models.CharField(max_length=255)
    video = EmbedVideoField()

class LoginDetails(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()


class Images(models.Model):
    image = models.FileField(upload_to="images/",max_length=250,null=True,default=None)

class Graph(models.Model):
    graphPath = models.CharField(max_length=255)

class rotate_Img(models.Model):
    image = models.FileField(upload_to="images/",max_length=250,null=True,default=None)
    
class flip_Img(models.Model):
    image = models.FileField(upload_to="images/",max_length=250,null=True,default=None)

class Videos(models.Model):
    videoName = models.CharField(max_length=255)
    video = models.FileField(upload_to="videos/",max_length=250,null=True,default=None)

class YoutubeLinks(models.Model):
    videoLinkName = models.CharField(max_length=255)
    videoLink = models.CharField(max_length=255)
    # videoLink = models.FileField(upload_to="videoLinks/",max_length=250,null=True,default=None)

class myuploadfile(models.Model):
    f_name = models.CharField(max_length=255)
    myfiles = models.FileField(upload_to="files/")


class Folder(models.Model):
    folder_name = models.CharField(max_length=255)
    files_info = JSONField(default=dict) 

    def __str__(self):
        return self.folder_name


class File(models.Model):
    file_name = models.CharField(max_length=255)
    uploaded_file = models.FileField(upload_to='uploads/')
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='files')

    def __str__(self):
        return self.file_name

class ImgClassifierDisplay(models.Model):
    Image = models.CharField(max_length=255)

class VidClassifierDisplay(models.Model):
    videoName = models.CharField(max_length=255)
    video = models.FileField(upload_to="videos/",max_length=250,null=True,default=None)



class YouTubeVideo(models.Model):
    video_link = models.URLField()
    video_name = models.CharField(max_length=255)
    downloaded_video_path = models.CharField(max_length=255)
    detection_output = models.TextField()

    def __str__(self):
        return self.video_name
