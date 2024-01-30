from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import LoginDetails,Images, Uploads,Videos,YoutubeLinks,YTLinks,myuploadfile,Folder,ImgClassifierDisplay, VidClassifierDisplay,YouTubeVideo
from PIL import Image
import shutil
import subprocess
from django.conf import settings 

from .models import Images

import os
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponseServerError



#------------------------------------------User Login and Sign Up--------------------------------------------------#

def login(request):
    return render(request,'login.html')

def loginDetails(request):
    if request.method == 'POST':
        username = request.POST.get('userName')
        password = request.POST.get('password')
        print('input',username,password)

        loginData1 = LoginDetails.objects.all().values()
        print('DBdata',loginData1)

        login_table = LoginDetails.objects.filter(username=username, password=password)

        print("-------------------------",login_table)
        if login_table.exists():
            return render(request, 'user.html')
        else:
            return HttpResponse('Invalid login')
    return HttpResponse('Invalid request method')

def register(request):
    return render(request,'register.html')

def registrationDetails(request):
    print('registerdetails',request.POST['userName'])
    loginData = LoginDetails.objects.all().values()
    for i in range(len(loginData)):
        if loginData[i]['username']== request.POST['userName'] and loginData[i]['password']== request.POST['password'] and loginData[i]['email']== request.POST['email'] :
            return render(request,'register.html',{"data":'Try with another credentails'})

    data = LoginDetails(username=request.POST['userName'],password=request.POST['password'],email=request.POST['email'])
    data.save()
    return render(request,'login.html')



def user(request):
    current_user = request.user
    return render(request, 'user.html', {'username': current_user.username})


def aug(request):
    return render(request,'aug.html')






#-----------------------------------------------Image Augmentation-------------------------------------------------#









def addImage(request):
    global uploaded_image_path

    if request.method == 'POST':
        global sel_Img
        img_data = request.FILES['imageInput'] 
        print('inp',img_data)
        da = Images(image=img_data)
        da.save()                                         
        image_path = da.image.path
        uploaded_image_path = image_path
        Im = Images.objects.all()
        sel_Img = Im.count()-1

        return render(request, 'aug.html', {'IMG':Im[sel_Img]}) 
    


def rotateImage(request):
    global uploaded_image_path

    try:
        if uploaded_image_path:
            temp_dir = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/input"
            os.makedirs(temp_dir, exist_ok=True)

            temp_image_path = os.path.join(temp_dir, "uploaded_image.jpg")
            shutil.copyfile(uploaded_image_path, temp_image_path)

            cmnd = f'python3 crimsontool/data_augmentor.py --input "{temp_dir}" --output "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/output" --rotate'
            os.system(cmnd)

            shutil.rmtree(temp_dir)
        else:
            print("No uploaded image found.")
       
    except Exception as e:
        print(f"An error occurred: {e}")

    return render(request, 'aug.html')



def FlipImage(request):
    global uploaded_image_path

    try:
        if uploaded_image_path:
            temp_dir = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/input"
            os.makedirs(temp_dir, exist_ok=True)

            temp_image_path = os.path.join(temp_dir, "uploaded_image.jpg")
            shutil.copyfile(uploaded_image_path, temp_image_path)

            cmnd = f'python3 crimsontool/data_augmentor.py --input "{temp_dir}" --output "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/output" --flip'
            os.system(cmnd)

            shutil.rmtree(temp_dir)
        else:
            print("No uploaded image found.")
       
    except Exception as e:
        print(f"An error occurred: {e}")

    return render(request, 'aug.html')



def ScaleImage(request):
    global uploaded_image_path

    try:
        if uploaded_image_path:
            temp_dir = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/input"
            os.makedirs(temp_dir, exist_ok=True)

            temp_image_path = os.path.join(temp_dir, "uploaded_image.jpg")
            shutil.copyfile(uploaded_image_path, temp_image_path)

            cmnd = f'python3 crimsontool/data_augmentor.py --input "{temp_dir}" --output "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/output" --scale'
            os.system(cmnd)

            shutil.rmtree(temp_dir)
        else:
            print("No uploaded image found.")
       
    except Exception as e:
        print(f"An error occurred: {e}")

    return render(request, 'aug.html')



def ContrastImage(request):
    global uploaded_image_path

    try:
        if uploaded_image_path:
            temp_dir = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/input"
            os.makedirs(temp_dir, exist_ok=True)

            temp_image_path = os.path.join(temp_dir, "uploaded_image.jpg")
            shutil.copyfile(uploaded_image_path, temp_image_path)

            cmnd = f'python3 crimsontool/data_augmentor.py --input "{temp_dir}" --output "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/output" --contrast'
            os.system(cmnd)

            shutil.rmtree(temp_dir)
        else:
            print("No uploaded image found.")
       
    except Exception as e:
        print(f"An error occurred: {e}")

    return render(request, 'aug.html')



def BrightnessImage(request):
    global uploaded_image_path

    try:
        if uploaded_image_path:
            temp_dir = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/input"
            os.makedirs(temp_dir, exist_ok=True)

            temp_image_path = os.path.join(temp_dir, "uploaded_image.jpg")
            shutil.copyfile(uploaded_image_path, temp_image_path)

            cmnd = f'python3 crimsontool/data_augmentor.py --input "{temp_dir}" --output "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/output" --brightness'
            os.system(cmnd)

            shutil.rmtree(temp_dir)
        else:
            print("No uploaded image found.")
       
    except Exception as e:
        print(f"An error occurred: {e}")

    return render(request, 'aug.html') 



def ShearImage(request):
    global uploaded_image_path

    try:
        if uploaded_image_path:
            temp_dir = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/input"
            os.makedirs(temp_dir, exist_ok=True)

            temp_image_path = os.path.join(temp_dir, "uploaded_image.jpg")
            shutil.copyfile(uploaded_image_path, temp_image_path)

            cmnd = f'python3 crimsontool/data_augmentor.py --input "{temp_dir}" --output "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/output" --shear'
            os.system(cmnd)

            shutil.rmtree(temp_dir)
        else:
            print("No uploaded image found.")
       
    except Exception as e:
        print(f"An error occurred: {e}")

    return render(request, 'aug.html')



def TranslateImage(request):
    global uploaded_image_path

    try:
        if uploaded_image_path:
            temp_dir = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/input"
            os.makedirs(temp_dir, exist_ok=True)

            temp_image_path = os.path.join(temp_dir, "uploaded_image.jpg")
            shutil.copyfile(uploaded_image_path, temp_image_path)

            cmnd = f'python3 crimsontool/data_augmentor.py --input "{temp_dir}" --output "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/output" --translate'
            os.system(cmnd)

            shutil.rmtree(temp_dir)
        else:
            print("No uploaded image found.")
       
    except Exception as e:
        print(f"An error occurred: {e}")

    return render(request, 'aug.html')



def GrayScaleImage(request):
    global uploaded_image_path

    try:
        if uploaded_image_path:
            temp_dir = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/input"
            os.makedirs(temp_dir, exist_ok=True)

            temp_image_path = os.path.join(temp_dir, "uploaded_image.jpg")
            shutil.copyfile(uploaded_image_path, temp_image_path)

            cmnd = f'python3 crimsontool/data_augmentor.py --input "{temp_dir}" --output "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/output" --grayscale'
            os.system(cmnd)

            shutil.rmtree(temp_dir)
        else:
            print("No uploaded image found.")
       
    except Exception as e:
        print(f"An error occurred: {e}")

    return render(request, 'aug.html')



def ColorImage(request):
    global uploaded_image_path

    try:
        if uploaded_image_path:
            temp_dir = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/input"
            os.makedirs(temp_dir, exist_ok=True)

            temp_image_path = os.path.join(temp_dir, "uploaded_image.jpg")
            shutil.copyfile(uploaded_image_path, temp_image_path)

            cmnd = f'python3 crimsontool/data_augmentor.py --input "{temp_dir}" --output "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/output" --color'
            os.system(cmnd)

            shutil.rmtree(temp_dir)
        else:
            print("No uploaded image found.")
       
    except Exception as e:
        print(f"An error occurred: {e}")

    return render(request, 'aug.html')



def EqualizeImage(request):
    global uploaded_image_path

    try:
        if uploaded_image_path:
            temp_dir = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/input"
            os.makedirs(temp_dir, exist_ok=True)

            temp_image_path = os.path.join(temp_dir, "uploaded_image.jpg")
            shutil.copyfile(uploaded_image_path, temp_image_path)

            cmnd = f'python3 crimsontool/data_augmentor.py --input "{temp_dir}" --output "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/output" --equalize'
            os.system(cmnd)

            shutil.rmtree(temp_dir)
        else:
            print("No uploaded image found.")
       
    except Exception as e:
        print(f"An error occurred: {e}")

    return render(request, 'aug.html')



def BlurImage(request):
    global uploaded_image_path

    try:
        if uploaded_image_path:
            temp_dir = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/input"
            os.makedirs(temp_dir, exist_ok=True)

            temp_image_path = os.path.join(temp_dir, "uploaded_image.jpg")
            shutil.copyfile(uploaded_image_path, temp_image_path)

            cmnd = f'python3 crimsontool/data_augmentor.py --input "{temp_dir}" --output "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/output" --blur'
            os.system(cmnd)

            shutil.rmtree(temp_dir)
        else:
            print("No uploaded image found.")
       
    except Exception as e:
        print(f"An error occurred: {e}")

    return render(request, 'aug.html')



def NoiseImage(request):
    global uploaded_image_path

    try:
        if uploaded_image_path:
            temp_dir = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/input"
            os.makedirs(temp_dir, exist_ok=True)

            temp_image_path = os.path.join(temp_dir, "uploaded_image.jpg")
            shutil.copyfile(uploaded_image_path, temp_image_path)

            cmnd = f'python3 crimsontool/data_augmentor.py --input "{temp_dir}" --output "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/output" --noise'
            os.system(cmnd)

            shutil.rmtree(temp_dir)
        else:
            print("No uploaded image found.")
       
    except Exception as e:
        print(f"An error occurred: {e}")

    return render(request, 'aug.html')



def ErasingImage(request):
    global uploaded_image_path

    try:
        if uploaded_image_path:
            temp_dir = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/input"
            os.makedirs(temp_dir, exist_ok=True)

            temp_image_path = os.path.join(temp_dir, "uploaded_image.jpg")
            shutil.copyfile(uploaded_image_path, temp_image_path)

            cmnd = f'python3 crimsontool/data_augmentor.py --input "{temp_dir}" --output "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/output" --erasing'
            os.system(cmnd)

            shutil.rmtree(temp_dir)
        else:
            print("No uploaded image found.")
       
    except Exception as e:
        print(f"An error occurred: {e}")

    return render(request, 'aug.html')








#------------------------------------------Image and Object Classifier---------------------------------------------#








def image(request):
    return render(request,'image.html')

def object(request):
    return render(request,'object.html')



#---------------Video Upload-------------------------------------#

def videoData(request):
    OP=""
    print("...", request.method)
    global sel_Vid
    global videoClassificationUploadedVideoPath

    video_data = request.FILES.get('videoUpload')
    video_name = request.POST['videoName']
    print(video_name, video_data)

    video_upload = Videos(video=video_data, videoName=video_name)
    video_upload.save()

    vdb = Videos.objects.all().values()
    videoClassificationUploadedVideoPath = video_upload.video.path
    print('path', videoClassificationUploadedVideoPath)

    sel_Vid = Videos.objects.all().count() - 1
    print('sel', vdb[sel_Vid]['video'])

    try:
        print('try', sel_Vid)
        if videoClassificationUploadedVideoPath:

            #temp_dir = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/input"
            #DBVideoPath = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/media"
            temp_dir = os.path.join(os.getcwd(), "crimsontool", "input")
            DBVideoPath = os.path.join(settings.MEDIA_ROOT)

            os.makedirs(temp_dir, exist_ok=True)

            temp_video_path = os.path.join(temp_dir, "uploaded_video.mp4")
            DBTempVideoPath = os.path.join(DBVideoPath, vdb[sel_Vid]['video'])

            print('dbpath', vdb[sel_Vid]['video'])
            video_name = vdb[sel_Vid]['video'].split('/')
            print('IN', video_name[1])
            print('TVP', temp_video_path)
            shutil.copyfile(videoClassificationUploadedVideoPath, temp_video_path)

            print('tryif', sel_Vid)

            print('process video')
            #Vcmd = f'python3 crimsontool/yolov5/detect.py --weight yolov5s.pt --source "{DBTempVideoPath}" '
            script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "yolov5", "detect.py")
            Vcmd = f'python3 "{script_path}" --weight yolov5s.pt --source "{DBTempVideoPath}"'

            process = subprocess.Popen(Vcmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            if process.returncode != 0:
                print(f"Error executing the script:\n{stderr.decode('utf-8')}")
            else:
                print(f"Script output:\n{stdout.decode('utf-8')}")
                OP = stdout.decode('utf-8').strip()
        else:
            print("No uploaded video found.")

    except Exception as e:
        print(f"An error occurred: {e}")

    disVid = VidClassifierDisplay(video=OP)
    disVid.save()
    VidData = VidClassifierDisplay.objects.all().values()
    sel_class_Vid = VidData.count() - 1
    print('selCal', VidData[sel_class_Vid]['video'])

    return render(request, 'videoDisplay.html', {'vid': VidData[sel_class_Vid]['video'], 'Count': sel_class_Vid,'text':'SAMPLE'}) 






#------------YouTube Link Upload--------------------------------------------# 

def videoLinkInput(request):
    videoLinkName = request.POST['videoLink']
    youtube_link = request.POST["videoLinkUpload"]
    print("...", videoLinkName, youtube_link)

    try:
        if youtube_link:
            print('detect called')
            Scmd = f'python3 crimsontool/yolov5/detect.py --weight yolov5s.pt --source "{youtube_link}" '

            process = subprocess.Popen(Scmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            if process.returncode != 0:
                print(f"Error executing the script:\n{stderr.decode('utf-8')}")
            else:
                print(f"Script output:\n{stdout.decode('utf-8')}")
                output_text = stdout.decode('utf-8').strip()
        else:
            print("No downloaded video found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return render(request, 'videoDisplay.html')




#-----------Image Upload-------------------------------------#
def imageUpload(request):
    print("...",request.method)
    global sel_Img
    global imageClassificationUploadedImagePath
    img_data = request.FILES['imageInput'] 
    print(type(img_data)) 
    da = Images(image=img_data)
    da.save()
    OP=''

    Im = Images.objects.all().values()
    imageClassificationUploadedImagePath = da.image.path
    print('path',imageClassificationUploadedImagePath)
    
    sel_Img = Im.count()-1
    print('sel',Im[sel_Img]['image'])

    try:
        print('try',sel_Img)
        if imageClassificationUploadedImagePath:
            
            #temp_dir = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/input"
            temp_dir = os.path.join(os.getcwd(), "crimsontool", "input")
            #DBImgPath = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/media"
            DBImgPath = os.path.join(settings.MEDIA_ROOT)
            os.makedirs(temp_dir, exist_ok=True)

            temp_image_path = os.path.join(temp_dir, "uploaded_image.jpg")
            DBTempImagePath=os.path.join(DBImgPath, Im[sel_Img]['image'])

            print('dbpath',Im[sel_Img]['image'])
            imgName = Im[sel_Img]['image'].split('/')
            print('IN',imgName[1])
            print('TIP',temp_image_path)
            shutil.copyfile(imageClassificationUploadedImagePath, temp_image_path)

          

            print('tryif',sel_Img) 

            
            print('rotate called')
            #Scmd = f'python3 crimsontool/yolov5/detect.py --weight yolov5s.pt --source "{DBTempImagePath}" '
            script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "yolov5", "detect.py")
            print("-----------",script_path)
            #Scmd = f'python3 {script_path} --weight yolov5s.pt --source "{DBTempImagePath}"'
            Scmd = f'python3 "{script_path}" --weight yolov5s.pt --source "{DBTempImagePath}"'




            process = subprocess.Popen(Scmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            if process.returncode != 0:
                print(f"Error executing the script:\n{stderr.decode('utf-8')}")
            else:
                print(f"Script output:\n{stdout.decode('utf-8')}")
                OP = stdout.decode('utf-8').strip()
        else:
            print("No uploaded image found.")
       
    except Exception as e:
        print(f"An error occurred: {e}")


    print('OP',type(OP),str(img_data))

    # imgPath = os.path.join(OP,str(img_data))
    disImg = ImgClassifierDisplay(Image=OP)
    disImg.save()
    ImData = ImgClassifierDisplay.objects.all().values()
    sel_class_Img = ImData.count()-1
    print('selCal',ImData[sel_class_Img]['Image'])


    return render(request,'imageDisplay.html',{'IMG':ImData[sel_class_Img]['Image'],'text':"sample text"}) 




#------------Folder Upload------------------------------------------------------#

def handle_folder_upload(request):
    try:
        if request.method == 'POST':
            upload_directory = 'uploads/'
            os.makedirs(upload_directory, exist_ok=True)

            uploaded_folder_list = request.FILES.getlist('folder')
            uploaded_folder_name = request.POST.get('folder-name')
            folder_instance = Folder(folder_name=uploaded_folder_name)
            folder_instance.save()

            folder_path = os.path.join(upload_directory, uploaded_folder_name)
            os.makedirs(folder_path, exist_ok=True)

            files_info = folder_instance.files_info or []

            for uploaded_file in uploaded_folder_list:
                file_name = os.path.join(folder_path, uploaded_file.name)
                with open(file_name, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)

                files_info.append({
                    'file_name': uploaded_file.name,
                })
            folder_instance.files_info = files_info
            folder_instance.save()
            #temp_dir = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/crimsontool/input"
            temp_dir = os.path.join(os.getcwd(), "crimsontool", "input")
            #DBImgPath = "C:/Users/T VAMSI/Documents/Desktop/Crimson/newUI/CAT/uploads"
            DBImgPath = os.path.join(settings.MEDIA_ROOT)
            os.makedirs(temp_dir, exist_ok=True)

            temp_folder_path = os.path.join(temp_dir, uploaded_folder_name)
            DBTempFolderPath = os.path.join(DBImgPath, uploaded_folder_name)

            shutil.copytree(folder_path, temp_folder_path)
            script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "yolov5", "detect.py")
            #cmd = f'python3 crimsontool/yolov5/detect.py --weight yolov5s.pt --source "{DBTempFolderPath}"'
            Scmd = f'python3 "{script_path}" --weight yolov5s.pt --source "{DBTempFolderPath}"'
            process = subprocess.Popen(Scmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            if process.returncode != 0:
                print(f"Error executing the script:\n{stderr.decode('utf-8')}")
            else:
                print(f"Script output:\n{stdout.decode('utf-8')}")

        else:
            print("GET request received for folder upload.")
    except Exception as e:
        print(f"An error occurred: {e}")

    contents = Folder.objects.all()
    data = {'folders': contents}
    return render(request, 'foldersUploads.html', data)

