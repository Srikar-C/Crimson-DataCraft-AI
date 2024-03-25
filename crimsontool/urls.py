from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('loginDetails', views.loginDetails, name='loginDetails'),
    path('registrationDetails', views.registrationDetails, name='registrationDetails'),
    path('user',views.user,name='user'),
    path('augmentation',views.aug,name='aug'),
    path('addImage', views.addImage, name='addImage'),
    path('rotateImage', views.rotateImage, name='rotateImage'),
    path('FlipImage', views.FlipImage, name='FlipImage'),
    path('ScaleImage', views.ScaleImage, name='ScaleImage'),
    path('ContrastImage', views.ContrastImage, name='ContrastImage'),
    path('BrightnessImage', views.BrightnessImage, name='BrightnessImage'),
    path('ShearImage', views.ShearImage, name='ShearImage'),
    path('TranslateImage', views.TranslateImage, name='TranslateImage'),
    path('GrayScaleImage', views.GrayScaleImage, name='GrayScaleImage'),
    path('ColorImage', views.ColorImage, name='ColorImage'),
    path('EqualizeImage', views.EqualizeImage, name='EqualizeImage'),
    path('BlurImage', views.BlurImage, name='BlurImage'), 
    path('NoiseImage', views.NoiseImage, name='NoiseImage'),
    path('ErasingImage', views.ErasingImage, name='ErasingImage'),
    path('image classifier',views.image,name='image'),
    path('object detector',views.object,name='object'),
    path('videoData', views.videoData, name='videoData'),
    path('videoLinkInput', views.videoLinkInput, name='videoLinkInput'),
    path('imageUpload', views.imageUpload, name='imageUpload'),
    path('handle_folder_upload', views.handle_folder_upload, name='handle_folder_upload'),
    path('uploadedImage/', views.uploadedImage, name='uploadedImage'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
    urlpatterns+=static(settings.SAMPLE_URL,document_root=settings.SAMPLE_ROOT)
