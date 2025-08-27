# https://www.youtube.com/watch?v=DNFTUtZf1Zc



# CBV
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from Hotel.models import Hotel
import json

@method_decorator(csrf_exempt, name="dispatch")
class GetExampleView(View):
    def get(self, request, *args, **kwargs):
        name = request.GET.get("name", "Guest")
        return HttpResponse(f"Hello {name}")


@method_decorator(csrf_exempt, name="dispatch")
class PostExampleView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        return JsonResponse({"message": f"Welcome {name}"})


@method_decorator(csrf_exempt, name="dispatch")
class PutExampleView(View):
    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        return JsonResponse({"updated": data})


@method_decorator(csrf_exempt, name="dispatch")
class PatchExampleView(View):
    def patch(self, request, *args, **kwargs):
        data = json.loads(request.body)
        updated_fields = {}
        if "name" in data:
            updated_fields["name"] = data["name"]
        if "age" in data:
            updated_fields["age"] = data["age"]
        return JsonResponse({"patched": updated_fields})


@method_decorator(csrf_exempt, name="dispatch")
class DeleteExampleView(View):
    def delete(self, request, hotel_id, *args, **kwargs):
        try:
            hotel = Hotel.objects.get(id=hotel_id)
            hotel.delete()
            return JsonResponse({"deleted": hotel_id}, status=204)
        except Hotel.DoesNotExist:
            return JsonResponse({"error": "Hotel not found"}, status=404)








# FBV
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Hotel.models import Hotel
import json


def get_example(request):
    if request.method == "GET":
        name = request.GET.get("name", "Guest")
        return HttpResponse(f"Hello {name}")



@csrf_exempt
def post_example(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return JsonResponse({"message": f"Welcome {name}"})


@csrf_exempt
def put_example(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        return JsonResponse({"updated": data})


@csrf_exempt
def patch_example(request):
    if request.method == "PATCH":
        data = json.loads(request.body)
        updated_fields = {}
        if "name" in data:
            updated_fields["name"] = data["name"]
        if "age" in data:
            updated_fields["age"] = data["age"]
        return JsonResponse({"patched": updated_fields})



@csrf_exempt
def delete_example(request, hotel_id):
    if request.method == "DELETE":
        try:
            hotel = Hotel.objects.get(id=hotel_id)
            hotel.delete()
            return JsonResponse({"deleted": hotel_id}, status=204)
        except Hotel.DoesNotExist:
            return JsonResponse({"error": "Hotel not found"}, status=404)
    return JsonResponse({"error": "Invalid request method"}, status=405)
