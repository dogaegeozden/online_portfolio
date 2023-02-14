# DJANGO LIBRARIES
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
# FORMS
from .forms import SubscriptionForm, CommentForm
# MODELS
from blog.models import MetaDescription, BlogPost, Subscription, Comment, BlogPageVisit, PostDetailPageVisit, PostLike, ShareClick
# CUSTOM FUNCTION
from custom_functions.visitors_ip_address import get_ip
from custom_functions.visitors_user_agent import get_user_agent
# PYTHON MODULES
from logging import basicConfig, DEBUG, debug, disable, CRITICAL

# Doing the basic configuration for the debugging feature
basicConfig(filename='blog_app_log.txt', level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# VIEW FUNCTIONS
def blog(request):
    """A view function which renders the blog page."""

    # Creating a query list from all MetaDescription objects
    all_meta_description_objs = MetaDescription.objects.all()

    # Creating a query set from all the BlogPost objects
    all_blog_post_objs = BlogPost.objects.all()

    # Getting the user's ip address.
    ip = get_ip(request)

    # Getting the user's user agent
    user_agent = get_user_agent(request)

    # Creating a data in the database using the BlogPageVisit data model.
    BlogPageVisit.objects.create(ip_address=ip, user_agent=user_agent)

    # Creating an empty subscription form
    subscription_form = SubscriptionForm()

    # Checking if the request method is post and, the subscribe button is used to send the post request
    if request.method == "POST" and 'subscribebtn' in request.POST:

        # Filling the subscription form with the request data
        subscription_form = SubscriptionForm(request.POST)

        # Checking if the form is valid
        if subscription_form.is_valid():

            # Printing the form data.
            print(subscription_form.cleaned_data)

            # Creating a data in the database using the Subscription data model.
            Subscription.objects.create(ip_address=ip, user_agent=user_agent, **subscription_form.cleaned_data,)

            # Cleaning the form input.
            subscription_form = SubscriptionForm()

            # Redirecting the user to the 'blog' sub domain
            return HttpResponseRedirect("/blog/")

        # Checking if the form is not valid.
        else:

            # Logging the form errors in debug mode.
            debug(subscription_form.errors)

    # Create context from the objects in the database and from the forms to be able to use them in the template.
    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_blog_post_objs': all_blog_post_objs,
    }

    # Rendering the request, html page and the context.
    return render(request, 'blog/blog.html', context=context)


def post_detail_view(request, id):
    """A view function which renders the blog detail pages"""

    # Creating an empty dictionary called context
    context = {}

    # Getting the user's ip address.
    ip = get_ip(request)

    # Getting the user's user agent.
    user_agent = get_user_agent(request)

    # Checking if post's request id is equal to post_like_request.
    if request.POST.get("requestId") == "post_like_request":
        
        # Checking if the object is already exists in the database.
        if PostLike.objects.filter(post=id, ip_address=ip).exists():
            # Telling to the server administrator what the application is trying to do.
            print("Object is already exists in the database so, modifying it.")
            # Updating the object.
            PostLike.objects.filter(post=id, ip_address=ip).update(like_status=request.POST.get("likeStatus"))

        # Checking if the object isn't exists in the database.
        else:
            # Telling to the server administrator what the application is trying to do.
            print("Object is not exists in the database so, creating a new one.")
            # Creating an object in the database using PostLike data model.
            PostLike.objects.create(post_id=id,  ip_address=ip, user_agent=user_agent, like_status=request.POST.get("likeStatus"))

    # Checking if post's request id is equal to share_on_social_media_request
    if request.POST.get("requestId") == "share_on_social_media_request":
        # Creating an object in the database using the ShareClick data model.
        ShareClick.objects.create(uuid=id, ip_address=ip, user_agent=user_agent, platform_choice=request.POST.get("platformCTShare"))

    # Creating a variable called post_detail by selecting the object in the database which's id is equal to post's id.
    post_detail = BlogPost.objects.get(id=id)

    # Creating an object in the database using the PostDetailPageVisit data model.
    PostDetailPageVisit.objects.create(ip_address=ip, user_agent=user_agent)

    # Checking if the object is already exists in the database by filtering all the PostLike objects.
    if PostLike.objects.filter(post=id, ip_address=ip).exists():
        # Creating a variable called post_like_objs by selecting the PostLike objects which's id is equal to post's id and ip address is equal to current visitor's ip address.
        post_like_objs = PostLike.objects.get(post=id, ip_address=ip)
        # Creating a key value pair in the context dictionary using post_like_objs variable.
        context['post_like_objs'] = post_like_objs

    # Creating a variable called post_like_count by counting PostLike object's which's id is equal to the post's id and like_status is equal to "l"(liked). 
    post_like_count = PostLike.objects.filter(post=id, like_status='l').count()

    # Creating an empty comment form
    comment_form = CommentForm()

    # Checking if the request method is equal to POST and the commentbtn is used to send the post request.
    if request.method == "POST" and "commentbtn" in request.POST:

        # Filling the form with the post request's data.
        comment_form = CommentForm(request.POST)

        # Checking if the form is valid.
        if comment_form.is_valid():
            # Printing the form data.
            print(comment_form.cleaned_data)

            # Creating an object in the database suing the Comment data model.
            Comment.objects.create(name=comment_form.cleaned_data['name'], text=comment_form.cleaned_data['text'], ip_address=ip, user_agent=user_agent, post_id=post_detail.id,)

        # Checking if the form is not valid.
        else:

            # Logging the form errors in debug mode.
            debug(comment_form.errors)

        # Redirecting the user to the blog detal page which's id is equal to the post's id.
        return HttpResponseRedirect(f'/blog/{id}')

    # Creating a variable called number_of_comments by counting the Comment object's which's id is equal to the post's id.
    number_of_comments = Comment.objects.filter(post=id).count()

    # Creating key value pairs in the context dictionary using the variables that are created in this view.
    context['comment_form'] = CommentForm
    context['post_detail'] = post_detail
    context['post_like_count'] = post_like_count
    context['usersIp'] = ip
    context['number_of_comments'] = number_of_comments

    # Rendering the request, html page and the context.
    return render(request, 'blog/blogpost_detail.html', context=context)
