from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# from rest_framework.permissions import IsAuthenticated



class GetServerDetails(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self,request):
       # qs = ServerInventory.objects.all()
        qs = ServerInventory.objects.all()
        ser = ServerDetails(qs,many=True)

        return Response(ser.data)


# def update_inventory(request, ip_address):
#     user = request.user.id
#     payload = json.loads(request.body)
#     try:
#         updated = ip_address.objects.filter(added_by=user, id=ip_address)
        
#         ServerInventory.update(**payload)
#         ip = ip.objects.get(id=ip)
#         serializer = ipSerializer(ip)
#         return JsonResponse({'ip': serializer.data}, safe=False, status=status.HTTP_200_OK)
#     except ObjectDoesNotExist as e:
#         return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
#     except Exception:
#         return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        