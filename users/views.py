from django.shortcuts import render
import logging
from .models import User, UserProfile
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializers, UserProfileViewSerializer
from rest_framework_simplejwt.tokens import RefreshToken
import logging
logger = logging.getLogger(__name__)
# Create your views here.
print("This is from views.py")

def index(request):
    logging.info("inide index method log")
    logging.basicConfig(filename='debug.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] - %(message)s')
    print("inside index method executing ==> ")
    return render(request, 'users/index.html')
@api_view(['GET','POST'])
# drf view
def signup_user(request):
    print("Inside SignUp")
    # if request.query_params:
    #     print("Query params present")
    #     # If there are query parameters, returns a 404 response
    #     return Response('Page not found', status=status.HTTP_404_NOT_FOUND)

    # data=request.data) serializers tells drf to accept data from request body
    #print('req_data', request.data)
    serializers = UserCreateSerializers(data=request.data)

    # creating a dict of success msg and error to send at the end
    response_data = {"errors":None, "data":None}

    # validating input data
    if serializers.is_valid():
        print("Valid Data")
        # calculating request body keys and serializers keys
        extra_fields = set(request.data.keys()) - set(serializers.fields.keys())
        print(len(extra_fields), 'extra fields')

        # checking extra fields if yes throw error msg else proceed
        if extra_fields:
            print('Extra fields present')
            error_msg = f"{len(extra_fields)} Extra fields found:[{', '.join(extra_fields)}]"
            return Response({'error': error_msg}, status=status.HTTP_400_BAD_REQUEST)
        #if validation true save it
        user_data = serializers.save()
        print('Refersh token')
        # generates refresh token for given user
        refresh = RefreshToken.for_user(user_data)
        print(str(refresh),"Hi")
        # store in dict response_data and show in response
        response_data['data'] = {'refresh' : str(refresh),
                                    'accessToken' : str(refresh.access_token)}
        # fetching last name from req body and printing success msg in response
        #user_name = user_data.username
        #response_data['data'] = {f"User '{user_name}' created successfully": 'Success'}
        response_status = status.HTTP_200_OK
    else:
        print('Invalid data')
        # is validation is not succesful throw errors and Http 400 req
        response_data['errors'] = serializers.errors
        print(serializers.errors, 'errors')
        response_status = status.HTTP_400_BAD_REQUEST
    return Response(response_data, response_status)

# method to display list of users without any protection
@api_view(['GET'])
def user_list(request):
    # 1.protect this view
    # 2.Better representtion for user obj - hide sensitive data like passwd and show only required data of user

    print('Hi This is user list api getting invoked')
    # fetching all obj or rows from UserProfile into a var users
    try:
        users = UserProfile.objects.all()
        users_count = users.count()
        print('users_count',users_count)
        #for u in users:
            #print(u.bio)
    except Exception as e:
        print('error',e)
        return Response({'error: An error occured'},status=status.HTTP_400_BAD_REQUEST)

    # a new serializer UserProfileViewSerializer which is diff from above
    # 'instance' defined to send existing data back to response and 'many' is tell multiple objs in UserProfile
    serialized_data = UserProfileViewSerializer(instance=users, many=True)
    response_data = {
            'user_count' : users_count,
            'users' : serialized_data.data
    }
    logger.debug('serialized data is :',serialized_data)
    # serialized_data.data = returns response as multiple obj, dict that is converted into JSON
    return Response(response_data, status=status.HTTP_200_OK)

def login_view(request):
    print("inside login method executing ==> ")
    return render(request, 'users/login.html')



# THis snippet is for building jar in jenkins
from . import jarbuild
@api_view()
def JarBuild(request):
    if jarbuild.build():
        return Response('jar Building')
    return Response('Jar building failed')

















# def index(request):
#     user_cnt = User.objects.count()
#     # len(user_cnt)
#     # fav_color, fav_dish = request.GET.get("fav_color","").lower(), request.GET.get("fav_dish","").lower()
#     # message = 'no idea abt this color'
#     #
#     # if fav_color == 'blue' and fav_dish == 'omlett':
#     #     message = 'sky is blue'
#     # elif fav_color == 'yellow':
#     #     message = 'fire is yellow'
#
#     return render(request, 'users/index.html')
#
# def signup(request):
#
#     return render(request, 'users/signup.html')
#
# def login_view(request):