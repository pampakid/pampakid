from django.conf import settings

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template

from .forms import PostForm, ContactForm
from .models import Post, Author

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    context = {
        'object_list': featured,
        'latest': latest,
    }
    return render(request, 'index.html', context)

def manifesto(request):
    return render(request, 'manifesto.html')

def login(request):
    return render(request, 'login.html')

def success(request):
    return render(request, 'success.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            # Email ourselves the submitted contact message
            subject = "New contact message for Pampa Kid"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [settings.DEFAULT_TO_EMAIL]

            # contact_message = "{0}, from {1} with email {2}".format(message, name, email)

            # Email the profile with the contact information
            template = get_template('contact_template.txt')

            context = {
                'name':name,
                'email':email,
                'message':message
            }
            content = template.render(context)

            send_mail(subject, content, from_email, to_email, fail_silently=True)
            # email = EmailMessage(
            #     "New contact form submission",
            #     content,
            #     "pampakid.com" + "",
            #     ["kid@pampakid.com"],
            #     headers = {"Reply-To":email}
            # )
            # email.send_mail()
            return render(request, 'success.html')

    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset' : paginated_queryset,
        'page_request_var' : page_request_var,
    }
    return render(request, 'blog.html', context)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    context = {
        'post' : post,
    }
    return render(request, 'post.html', context)

def post_create(request):
    title = 'Create'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)

    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id': form.instance.id
            }))

    context = {
        'title': title,
        'form': form
    }
    return render(request, "post_create.html", context)

def post_update(request, id):
    title = 'Update'
    post = get_object_or_404(Post, id=id)
    form = PostForm(
        request.POST or None,
        request.FILES or None,
        instance=post)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, "post_create.html", context)

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse("post-list"))
