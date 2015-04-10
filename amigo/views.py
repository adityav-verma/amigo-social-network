from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from amigo.models import UserProfile, Status, Friends
from amigo.forms import UserProfileForm, StatusForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from itertools import chain
# Create your views here.


#home view for showing the status form as well as the new feed
@login_required
def home(request):
	user = request.user
	statusForm = statusUpdate(request)
	
	allStatus = Status.objects.order_by('-pubDate')[:]
	allFriends1 = Friends.objects.values_list('user2', flat = True).filter(user1 = user, active = True)
	allFriends2 = Friends.objects.values_list('user1', flat = True).filter(user2 = user, active = True)

	allFriends = list(chain(allFriends1, allFriends2))
	
	contextDict = {'form': statusForm, 'allFriends': allFriends, 'allStatus':allStatus}
	return render(request, 'amigo/home.html', contextDict)


#Showing all the users 
@login_required
def allUsers(request):
	user = request.user
	allUsers = User.objects.all()

	#all relations in which user was requeted and it accepted
	try:
		allFriends = Friends.objects.values_list('user2', flat = True).filter(user1 = user, active = True)
	except Friends.DoesNotExist:
		allFriends = None

	#all relations in which user requested for friendship and got accepted
	try:
		allFriends2 = Friends.objects.values_list('user1', flat = True).filter(user2 = user, active = True)
	except Friends.DoesNotExist:
		allFriends2 = None
	
	#all relations in which user is been requeted but has still not accepted the request
	try:
		allRequested = Friends.objects.values_list('user2', flat = True).filter(user1 = user, active = False)
	except Friends.DoesNotExist:
		allRequested = None
	
	#all relation in which user has requested for friendship but didnt got accepted yet!!
	try:
		allRequested2 = Friends.objects.values_list('user1', flat = True).filter(user2 = user, active = False)
	except Friends.DoesNotExist:
		allRequested = None

	contextDict = {'allUsers': allUsers, 'allFriends': allFriends, 'allRequested': allRequested, 'allFriends2': allFriends2, 'allRequested2': allRequested2}
	return render(request, 'amigo/allUsers.html', contextDict)

#showing friends and friend request on this page
@login_required
def friends(request):
	user = request.user
	allUsers = User.objects.all()
	#all those users who are friends
	try:
		allFriends1 = Friends.objects.values_list('user2', flat = True).filter(user1 = user, active = True)
	except User.DoesNotExist:
		allFriends1 = None

	try:
		allFriends2 = Friends.objects.values_list('user1', flat = True).filter(user2 = user, active = True)
	except User.DoesNotExist:
		allFriends2 = None

	#combining all friends together
	allFriends = list(chain(allFriends1, allFriends2))

	#all those users whome this users has requested friendship
	try:
		allRequested = Friends.objects.values_list('user1', flat = True).filter(user2 = user, active = False)
	except User.DoesNotExist:
		allRequested = None

	#all those users who have sent a request to this user
	try:
		allRequesting = Friends.objects.values_list('user2', flat = True).filter(user1 = user, active = False)
	except User.DoesNotExist:
		allRequesting = None


	return render(request, 'amigo/friends.html', {'allUsers':allUsers,'allFriends': allFriends, 'allRequesting':allRequesting, 'allRequested':allRequested})

@login_required
def sendRequest(request, uid):
	requestingUser = request.user
	relation = Friends()
	requestedUser = User.objects.get(pk = uid)
	relation.user1 = requestedUser
	relation.user2 = requestingUser
	relation.active = False
	relation.save()
	return HttpResponse("Request Sent")

def acceptRequest(request, uid):
	user = request.user
	relation = Friends.objects.get(user1 = user.pk, user2 = uid)
	relation.active = True
	relation.save()
	return HttpResponse("Friends :)")




#function ot update status!! it the request and return empty form if status is updated or form with errors
@login_required
def statusUpdate(request):
	user = request.user
	if request.method == 'POST':
		statusForm = StatusForm(request.POST)
		if statusForm.is_valid():	#if form is valid save it
			status = statusForm.save(commit = False)
			status.user = user
			if 'statusImage' in request.FILES:
				status.statusImage = request.FILES['statusImage']
			status.save()
			statusForm = StatusForm()	#make form empty and return it if it was valid
			#return the status form may be empty.. if it was valid else would be with errors
	else:
		statusForm = StatusForm()

	return statusForm








#adding the user profile details and mapping it to the 
def addProfile(request):
	#User shoudl be authenticated
	if request.user.is_authenticated():
		user = request.user
	else:
		return HttpResponseRedirect('/accounts/register')
	
	registered = False

	if request.method == 'POST':
		userForm = UserProfileForm(data = request.POST)

		if userForm.is_valid():
			userProfile = userForm.save(commit = False)
			user.first_name = userProfile.fname
			user.last_name = userProfile.lname
			userProfile.user = user

			if 'profilePic' in request.FILES:
				userProfile.profilePic = request.FILES['profilePic']

			userProfile.save()
			user.save()
			registered = True
			return HttpResponseRedirect('/amigo/home')
	else:
		userForm = UserProfileForm()

	contextDict = {'form': userForm}

	return render(request, 'amigo/addProfile.html', contextDict)

