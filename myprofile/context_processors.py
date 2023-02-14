# LIBRARIES
from myprofile.models import SocialMediaLinks, SocialMediaButtonClick
# CUSTOM FUNCTION
from custom_functions.visitors_ip_address import get_ip
from custom_functions.visitors_user_agent import get_user_agent

# CONTEXT PROCESSORS
def social_media_link_processor(request):
    """A context processor function that makes all social media links accessible in the entire web page"""
    # Creating a query set from all of the social media link data objects
    all_social_media_link_objs = SocialMediaLinks.objects.all()

    # Returning all of the social media link objects in a dictionary.
    return {'all_social_media_link_objs': all_social_media_link_objs}

def cookie_notice_processor(request):
    """A context processor function that makes the variables required for the cookie notice function, accessible in the entire web application"""
    # Creating a variable called cookie_notice_answer
    cookie_notice_answer = request.session.get('cookie_notice_answer', 0)

    # Checking if the request method is post and if the user used the iGotIt button to send the request
    if request.method == "POST" and 'iGotIt' in request.POST:

        # Checking if the cookie notice answer is less than or equal to 1
        if cookie_notice_answer <= 1:
            # Changing the cookie_notice_answer variable's value.
            cookie_notice_answer = request.session.get('cookie_notice_answer', 1)
            # Changing the cookie_notice_answer variable's value in the active session.
            request.session['cookie_notice_answer'] = cookie_notice_answer + 1
        # Checking if the cookie notice answer is greater than or equal to 2
        elif cookie_notice_answer >= 2:
            # Changing the cookie_notice_answer variable's value in the active session.
            request.session['cookie_notice_answer'] = cookie_notice_answer

    # Creating a dictionary called context
    context = {
        'cookie_notice_answer': cookie_notice_answer,
    }

    # Returning the context dictionary.
    return context

def social_media_click_processor(request):
    """A context processor function which creates a SocialMediaButtonClick data object in the database from the post requests send by users"""
    # Getting the visitor's ip address.
    ip = get_ip(request)

    # Getting the visitor's user agent.
    user_agent = get_user_agent(request)

    # Checking if the post requests id is equal to smbcp.
    if request.POST.get("id") == "smbcp":
        # Creating an object in the database using the SocialMediaButtonClick data model.
        SocialMediaButtonClick.objects.create(ipAddr=ip, user_agent=user_agent, platformChoice=request.POST.get("socialMediaChoice"))

    # Returning an empty dictionary. Hint: If you don't return anything context will be equal to Null and page won't load.
    return {}
