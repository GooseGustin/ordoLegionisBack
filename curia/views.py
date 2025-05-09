from django.shortcuts import render
from rest_framework import viewsets, permissions, views, status
from rest_framework.response import Response

from .models import Announcement, Curia
from .serializers import AnnouncementSerializer, CuriaSerializer
from accounts.models import Legionary 
from api.function_vault import removeDuplicates

from rest_framework.decorators import api_view 
from .cloudinary_helpers import upload_file_to_server, delete_file_from_cloudinary

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    # permission_classes = [permissions.AllowAny]

    def list(self, request): 
        print("In list method of AnnouncementViewSet\n\n", request.GET)
        cid = request.GET.get('cid') 
        if cid: # filter by praesidium 
            # Ensure user has access to this praesidium
            announcements = self.queryset.filter(curia=cid)
            serializer = self.get_serializer(announcements, many=True)
            return Response(serializer.data)
        # work_list = WorkList.objects.all()
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data) 


@api_view(['POST'])
def announcementFormView(request):
    data = request.data.copy()
    create = data.get("create") == "true" or data.get("create") is True
    image_file = request.FILES.get("image")
    announcement = None
    image_url = None

    # Editing: fetch existing object
    if not create:
        try:
            announcement = Announcement.objects.get(id=data.get("id"))
        except Announcement.DoesNotExist:
            return Response({"error": "Announcement not found."}, status=status.HTTP_404_NOT_FOUND)

    # Upload new image if provided
    if image_file:
        print("Announcement has image file")
        if not create and announcement.image:
            print("Announcement deleting old image file")
            delete_file_from_cloudinary(announcement.image)
        image_result = upload_file_to_server(image_file, folder="announcements")
        print("Setting new image file")
        image_url = image_result["secure_url"]
        data["image"] = image_url
    else: 
        print("no image file")

    serializer = None
    if create:
        serializer = AnnouncementSerializer(data=data)
    else:
        serializer = AnnouncementSerializer(announcement, data=data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED if create else status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def delete_announcement(request):
    id = request.data.get("id")
    try:
        announcement = Announcement.objects.get(id=id)
    except Announcement.DoesNotExist:
        return Response({"error": "Announcement not found."}, status=status.HTTP_404_NOT_FOUND)

    if announcement.image:
        delete_file_from_cloudinary(announcement.image)
    else: 
        print("Announcement doesn't have an image to delete")

    announcement.delete()
    return Response({"message": "Announcement deleted."}, status=status.HTTP_204_NO_CONTENT)



class CuriaViewSet(viewsets.ModelViewSet):
    queryset = Curia.objects.all()
    serializer_class = CuriaSerializer

    def list(self, request): 
        print("In list method of CuriaViewSet\n\n", request.GET)
        uid = request.GET.get('uid')
        if uid: # filter by user membership
            # Ensure user has permission
            legionary = Legionary.objects.get(user=request.user)
            print(legionary, legionary.associated_praesidia)  # type: ignore
            curiae = [praesidium.curia for praesidium in legionary.associated_praesidia.iterator()]  # type: ignore
            curiae.extend([curia for curia in legionary.curiae_created.iterator()]) # type: ignore
            curiae = removeDuplicates(curiae)
            # print('Curia', curiae)
            serializer = self.get_serializer(curiae, many=True) 
            return Response(serializer.data) 

        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data) 