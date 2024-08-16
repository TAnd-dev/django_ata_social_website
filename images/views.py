from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from images.forms import ImageCreateForm
from images.models import Image


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            messages.success(request, "Image added successfully")
            return redirect(image.get_absolute_url())
    else:
        form = ImageCreateForm(request.GET)
    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})


def image_detail(request, pk, slug):
    image = get_object_or_404(Image, pk=pk, slug=slug)
    return render(request, 'images/image/detail.html', {'section': 'images', 'image': image})


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    image_only = request.GET.get('images_only')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if image_only:
            return HttpResponse('')
        images = paginator.page(paginator.num_pages)
    if image_only:
        return render(request, 'images/image/list_image.html', {'section': 'images', 'images': images})

    return render(request, 'images/image/list.html', {'section': 'images', 'images': images})