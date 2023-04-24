from rest_framework.views import APIView
from .models import Projects,Booking
from rest_framework import status,generics,permissions
from rest_framework.response import Response
from .serializers import ProjectSerializer,BookingSerializer

class ManageProjectView(APIView):
    def get(self,request,format=None):
        try:
            user = request.user
            if not user.is_farmer:
                return Response({"error":"User does not have necessary permissions for listing data"},status=status.HTTP_403_FORBIDDEN)
            slug = request.query_params.get('slug')

            if not slug:
                projects = Projects.objects.order_by('-date_created').filter(farmer = user.email)
                projects = ProjectSerializer(projects,many=True)
                return Response({'projects':projects.data},status=status.HTTP_200_OK)

        except:
            return Response({"error":"Something went wrong grt project"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def post(self,request):
        try:
            user = request.user

            if not user.is_farmer:
                return Response({"error":"User does not have the necessary permission"},status=status.HTTP_403_FORBIDDEN)
            
            data = request.data

            title = data['title']
            address = data['address']
            city = data['city']
            state = data['state']
            zipcode = data['zipcode']
            descriptions = data['descriptions']

            price = data['price']
            price = float(price)
            photo1 = data['photo1']
            photo2 = data['photo2']
            photo3 = data['photo3']

            Projects.objects.create(
                farmer=user.email,
                title=title,
                address = address,
                city = city,
                state = state,
                zipcode = zipcode,
                descriptions =descriptions,
                price = price,
                photo1 = photo1,
                photo2 = photo2,
                photo3 = photo3
            )
            return Response({"success":"Project created successfully"},status=status.HTTP_201_CREATED)
        except:
            return Response({"error":"Something went wrong create project"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ProjectDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

class ProjectListAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Projects.objects.order_by('-date_created').all()
    serializer_class = ProjectSerializer


class BookigAPIView(APIView):
        def post(self,request):
            try:
                data = request.data
                projectID = data['id']
                title = data['title']
                farmer = data['farmer']
                customer = request.user
                Booking.objects.create(
                    projectID = projectID,
                    title =title,
                    farmer = farmer,
                    customer = customer
                )
                return Response({"success":"Booking done successfully"},status=status.HTTP_201_CREATED)
            except:
                return Response({"error":"Something went wrong while Booking"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class BookingListAPIView(APIView):
    def get(self,request,format=None):
        try:
            user = request.user
            if not user.is_farmer:
                booking = Booking.objects.order_by('-book_date').filter(customer = user.email)
                booking = BookingSerializer(booking,many=True)
                return Response({'bookingsCustomer':booking.data},status=status.HTTP_200_OK)
            booking = Booking.objects.order_by('-book_date').filter(customer = user.email)
            booking = BookingSerializer(booking,many=True)
            return Response({'bookingsFarmer':booking.data},status=status.HTTP_200_OK)
        except:
            return Response({"error":"Something went wrong when booking booking list"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

