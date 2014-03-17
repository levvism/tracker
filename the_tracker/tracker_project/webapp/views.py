from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from forms import UserForm, UserProfileForm, TaskForm, new_project_form
from models import Project, Task, UserProfile

def index(request):
	context = RequestContext(request)
	
	user_projects = []
	context_dict = {}	
	
	if request.user.is_authenticated():
		projects = Project.objects.filter(collaborators = request.user)	
		context_dict["projects"] = projects
		
	
	return render_to_response('webapp/index.html', context_dict, context)
    
@login_required   
def about(request):
	context = RequestContext(request)
	
	context_dict = {}
	
	return render_to_response('webapp/about.html', context_dict, context)
	
	
# taken from leifos - https://github.com/leifos/tango_with_django/blob/master/tango_with_django_project/rango/views.py	
def register(request):
    # Request the context.
    context = RequestContext(request)

    context_dict = {}

    # Boolean telling us whether registration was successful or not.
    # Initially False; presume it was a failure until proven otherwise!
    registered = False

    # If HTTP POST, we wish to process form data and create an account.
    if request.method == 'POST':
        # Grab raw form data - making use of both FormModels.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # Two valid forms?
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data. That one is easy.
            user = user_form.save()

            # Now a user account exists, we hash the password with the set_password() method.
            # Then we can update the account with .save().
            user.set_password(user.password)
            user.save()

            # Now we can sort out the UserProfile instance.
            # We'll be setting values for the instance ourselves, so commit=False prevents Django from saving the instance automatically.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Profile picture supplied? If so, we put it in the new UserProfile.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the model instance!
            profile.save()

            # We can say registration was successful.
            registered = True

        # Invalid form(s) - just print errors to the terminal.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render the two ModelForms to allow a user to input their data.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict['user_form'] = user_form
    context_dict['profile_form']= profile_form
    context_dict['registered'] = registered

    # Render and return!
    return render_to_response(
        'webapp/register.html',
        context_dict,
        context)


# taken from leifos - https://github.com/leifos/tango_with_django/blob/master/tango_with_django_project/rango/views.py	
def user_login(request):
    # Obtain our request's context.
    context = RequestContext(request)

    context_dict = {}

    # If HTTP POST, pull out form data and process it.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Attempt to log the user in with the supplied credentials.
        # A User object is returned if correct - None if not.
        user = authenticate(username=username, password=password)

        # A valid user logged in?
        if user is not None:
            # Check if the account is active (can be used).
            # If so, log the user in and redirect them to the homepage.
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            # The account is inactive; tell by adding variable to the template context.
            else:
                context_dict['disabled_account'] = True
                return render_to_response('webapp/login.html', context_dict, context)
        # Invalid login details supplied!
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            context_dict['bad_details'] = True
            return render_to_response('webapp/login.html', context_dict, context)

    # Not a HTTP POST - most likely a HTTP GET. In this case, we render the login form for the user.
    else:
        return render_to_response('webapp/login.html', context_dict, context)
        
        
        
# Only allow logged in users to logout - add the @login_required decorator!
@login_required
def user_logout(request):
    # As we can assume the user is logged in, we can just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')
   
def new_project(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        form = new_project_form(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = new_project_form()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('webapp/create_project.html', {'form': form}, context)
   
def project(request):
    context = RequestContext(request)
    return render_to_response('webapp/project_home_page.html', {}, context)

def task(request):
	context = RequestContext(request)	
	taskid = int(request.GET.get('taskid', '0'));
	
	project_names = []
	titles = []
	classifications = []
	priorities = []
	descriptions = []
	context_dict = {}
	if(taskid !=0):
		TaskObjects = Task.objects.all();
		for t in TaskObjects:
			if(t.id == taskid):
				project_names.append(t.project.name)
				titles.append(t.title)
				descriptions.append(t.description)
				classifications.append(t.classification)
				priorities.append(t.priority)
				
	context_dict["project_names"] = project_names
	context_dict["titles"] = titles
	context_dict["descriptions"] = descriptions
	context_dict["priorities"] = priorities
	context_dict["classifications"] = classifications
	context_dict["taskid"] = taskid
	
	return render_to_response('webapp/task.html', context_dict, context)
	
def view_tasks(request):
	context = RequestContext(request)	
	projectid = int(request.GET.get('projectid', '0'));
	
	tasks = []
	context_dict = {}
	if (projectid != 0):
		TaskObjects = Task.objects.all();
		for t in TaskObjects:
			if (t.project.id == projectid):
				tasks.append(t)		
		
	context_dict["tasks"] = tasks
	context_dict["projectid"] = projectid
	
	return render_to_response('webapp/view_tasks.html', context_dict, context)

def add_task(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = TaskForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return task(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = TaskForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('webapp/add_requirement.html', {'form': form}, context)
