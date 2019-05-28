from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RecvDataSerializer
from .models import RecvData, Kid
from PIL import Image
import numpy as np
from django.conf import settings
import os, pickle, face_recognition
from .forms import PostForm


def train_Image(filename, img):
    path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'DataSet\dataset_faces.dat'))
    temp_dict = {}
    with open(path, 'rb') as f:
	    face_encodings = pickle.load(f)
    
    new_image = np.array(Image.open(img).convert(mode='RGB'))
    temp_dict[filename] = face_recognition.face_encodings(new_image)[0]

    face_encodings.update(temp_dict)

    with open(path, 'wb') as f:
        pickle.dump(face_encodings, f)

    print(face_encodings[filename])

    

def kid_upload_view(request):
    form = PostForm()
    if  request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            file_name = request.POST['parent_contact']
            incoming_image = request.FILES['image']
            train_Image(file_name,incoming_image)
    
    
    return render(request,'post_form.html', {'form':form})

class RecvDataRequest(APIView):

    def testFace(self,img_data):
        path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'DataSet\dataset_faces.dat'))
        
        with open(path, 'rb') as f:
	        all_face_encodings = pickle.load(f)
        
        face_encodings = np.array(list(all_face_encodings.values()))

        unknown_image = np.array(Image.open(img_data).convert(mode='RGB'))
        unknown_face = face_recognition.face_encodings(unknown_image)

        result = face_recognition.compare_faces(face_encodings, unknown_face)

        for i in result:
            if result:
                return True

        return False
    

    def get(self, request):
        usr = RecvData.objects.all()
        serializer = RecvDataSerializer(usr ,many = True)
        return Response(serializer.data)

    def post(self, request):

        serializer = RecvDataSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #Save encoding in a file when uploaded from police db
        #use the encoding for linear search for image in the files

        img_data = request.FILES['img']
        results = self.testFace(img_data)
        
        if results:
            print("Found")
        else:
            print("Not found :(")

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    