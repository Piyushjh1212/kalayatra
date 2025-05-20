from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def home(request):
    return JsonResponse({"message": "Welcome to KalaYatra API"})

@api_view(['POST'])
def contact_submit(request):
    name = request.data.get('name')
    email = request.data.get('email')
    message = request.data.get('message')

    if name and email and message:
        # yahan aap database me save kar sakte hain
        return Response({"message": "Form submitted successfully!"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)
