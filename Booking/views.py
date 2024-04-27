from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import ToDoList, UnsavedItem, Item, Image,SavedItem
from .forms import CreateNewList,AddItemForm
from PIL import Image as PILImage
from io import BytesIO
import os

from django.conf import settings


@login_required
def ind(request, id):
    try:
        ls = ToDoList.objects.get(id=id)
    except ToDoList.DoesNotExist:
        return HttpResponse("ToDoList does not exist.")
    return render(request, "Booking/list.html", {"ls": ls})



@login_required
def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            return HttpResponseRedirect(f"/{t.id}")
    else:
        form = CreateNewList()
    return render(request, "create.html", {"form": form})

def handle_temporary_image_upload(image, description, folder):
    img = PILImage.open(image)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    img_io = BytesIO()
    img.save(img_io, format='JPEG')

    file_name = description.replace(" ", "_").lower()

    temp_upload_path = os.path.join(settings.MEDIA_ROOT, folder)
    os.makedirs(temp_upload_path, exist_ok=True)

    temp_image_path = os.path.join(temp_upload_path, f'{file_name}.jpg')
    with open(temp_image_path, 'wb') as file:
        file.write(img_io.getvalue())

    return os.path.relpath(temp_image_path, settings.MEDIA_ROOT)


@login_required
def list_view(request, id):
    try:
        ls = ToDoList.objects.get(id=id)
    except ToDoList.DoesNotExist:
        return HttpResponse("ToDoList does not exist.")

    unsaved_items = UnsavedItem.objects.all()
    form = AddItemForm(request.POST or None, request.FILES or None)  # Pass POST and FILES data to the form

    if request.method == 'POST':
        if 'add_item' in request.POST:
            if form.is_valid():
                # Create a new unsaved item
                unsaved_item = form.save(commit=False)
                unsaved_item.save()
                return redirect('list_view', id=id)  # Redirect after successful item addition
        elif 'save' in request.POST:
            # Handle saving unsaved items
            for unsaved_item in unsaved_items:
                saved_item = Item.objects.create(
                    lists=ls,
                    name=unsaved_item.name,
                    type=unsaved_item.type,
                    description=unsaved_item.description,
                    rental_period=unsaved_item.rental_period,  # Include rental_period field

                    image=unsaved_item.image
                )
                saved_item.save()
            unsaved_items.delete()
            return redirect('list_view', id=id)
        elif 'delete_item' in request.POST:
            item_id = request.POST.get('delete_item')
            ls.items.filter(id=item_id).delete()
            return redirect('list_view', id=id)

    saved_items = ls.items.all()

    return render(request, "Booking/list.html", {"ls": ls, "unsaved_items": unsaved_items, "saved_items": saved_items, "form": form})

def delete_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('itemId')
        try:
            item = Item.objects.get(id=item_id)
            item.delete()
            return JsonResponse({'success': True})
        except Item.DoesNotExist:
            try:
                unsaved_item = UnsavedItem.objects.get(id=item_id)
                unsaved_item.delete()
                return JsonResponse({'success': True})
            except UnsavedItem.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Item not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

def Search_Engine(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        items = Item.objects.filter(description__icontains=searched)

        return render(request, 'Search_Engine.html', {'searched': searched, 'items': items})
    else:
        return render(request, 'Search_Engine.html', {})
