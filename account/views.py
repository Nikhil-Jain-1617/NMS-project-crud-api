from django.db import reset_queries
from account.models import User
from .serializers import UserSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.hashers import make_password

class SignupAPI(APIView):
    def post(self,request):
        print("request>>>",request.data)
        ser = UserSerializer(data= request.data)
        if (ser.is_valid()):
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        
        return Response(ser.errors, status= status.HTTP_400_BAD_REQUEST)



# class DetailApiView(APIView):
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]

#     def get_object(self, id, username):
#         '''
#         Helper method to get the object with given todo_id, and user_id
#         '''
#         try:
#             return User.objects.get(id=id, user = username)
#         except User.DoesNotExist:
#             return None

#     # 3. Retrieve
#     def get(self, request, id, *args, **kwargs):
#         '''
#         Retrieves the Todo with given todo_id
#         '''
#         instance = self.get_object(id, request.user.id)
#         if not instance:
#             return Response(
#                 {"res": "Object with todo id does not exists"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         serializer = UserSerializer(instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 4. Update
#     def put(self, request, id, *args, **kwargs):
#         '''
#         Updates the todo item with given todo_id if exists
#         '''
#         instance = self.get_object(id, request.user.id)
#         if not instance:
#             return Response(
#                 {"res": "Object with todo id does not exists"}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         data = {
#             'task': request.data.get('task'), 
#             'completed': request.data.get('completed'), 
#             'user': request.user.id
#         }
#         serializer = UserSerializer(instance = instance, data=data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # 5. Delete
#     def delete(self, request, id, *args, **kwargs):
#         '''
#         Deletes the todo item with given todo_id if exists
#         '''
#         instance = self.get_object(id, request.user.id)
#         if not instance:
#             return Response(
#                 {"res": "Object with todo id does not exists"}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         instance.delete()
#         return Response(
#             {"res": "Object deleted!"},
#             status=status.HTTP_200_OK
#         )
class ResetPassword(APIView):

    def put(self,request):
        user_name = request.POST.get('username')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        new_password = make_password(new_password)
        user = User.objects.get(username = user_name)

        if user:
            user.password = new_password
            user.save()
            resp ={
                'success': 'True',
                'message': '''Password has been successfully changed, You can login with new password''',
            }

            return Response(resp, status=status.HTTP_201_CREATED)
        resp = {
                'success': 'false',
                'message': 'Something went wrong Please try again later',
               }
        return Response(resp,status=status.HTTP_304_NOT_MODIFIED)