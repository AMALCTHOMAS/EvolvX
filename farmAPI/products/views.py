from rest_framework.views import APIView
from . models import Products,Orders
from rest_framework import status,generics,permissions
from rest_framework.response import Response
from . serializers import ProductSerializer,OrderSerializer

class ManageProductsView(APIView):
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    def post(self,request):
        try:
            user = request.user
            if not user.is_farmer:
                return Response({"error":"User does not have necessary permissions for add product"},status=status.HTTP_403_FORBIDDEN)
            data = request.data
            pname = data['pname']
            discription = data['discription']
            price = data['price']
            price = float(price)
            quantity = data['quantity']
            quantity = float(quantity)
            unit = data['unit']
            photo = data['photo']

            farmer = user.email

            Products.objects.create(
                pname = pname,
                discription = discription,
                price = price,
                farmer = farmer,
                quantity = quantity,
                unit = unit,
                photo = photo
            )
            return Response({"success":"Product created successfully"},status=status.HTTP_201_CREATED)
        except:
            return Response({"error":"Something went wrong  while creating the product"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self,request):
        try:
            products = Products.objects.order_by('-create_time').all()
            products = ProductSerializer(products,many=True)
            return Response({'products':products.data},status=status.HTTP_200_OK)
        except:
            return Response({"error":"Something went wrong  while getting the the product"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetProductListView(APIView):
    def get(self,request):
        user = request.user
        try:
            if not user.is_farmer:
                return Response({"error":"User does not have necessary permissions for listing product data"},status=status.HTTP_403_FORBIDDEN)
            products = Products.objects.order_by('-create_time').filter(farmer=user.email)
            products = ProductSerializer(products,many=True)
            return Response({'products':products.data},status=status.HTTP_200_OK)
        except:
            return Response({"error":"Something went wrong  while getting the product list"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id=None):
        try:
            user = request.user
            data = request.data
            id = data['id']
            id = int(id)
            if not user.is_farmer:
                return Response({"error":"User does not have necessary permissions for listing product data"},status=status.HTTP_403_FORBIDDEN)
            products = Products.objects.filter(id=id,farmer = user.email)
            products.delete()
            return Response({"success":"Product deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"error":"Something went wrong  while Deleting"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ManageOrderAPIview(APIView):
    def get(self,request):
        user = request.user
        try:
            if not user.is_farmer:
                orders = orders.objects.order_by('-order_date').filter(customer = user.email)
                orders = OrderSerializer(orders,many=True)
                return Response({'orderCustomer':orders.data},status=status.HTTP_200_OK)
            
            orders = Orders.objects.order_by('-order_date').filter(farmer = user.email)
            orders = OrderSerializer(orders,many=True)
            return Response({'orderFarmer':orders.data},status=status.HTTP_200_OK)
        except:
            return Response({"error":"Something went wrong  while list orders"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self,request):
        user = request.user
        data = request.data

        try:
            pname = data['pname']
            price = data['price']
            price = float(price)
            quantity = data['quantity']
            quantity = float(quantity)
            farmer = data['farmer']
            customer = user.email
            total = data['total']
            total = float(total)

            Orders.objects.create(
                pname = pname,
                quantity = quantity,
                price = price,
                total = total,
                farmer = farmer,
                customer = customer
            )
            return Response({"success":"Order created successfully"},status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"error":"Something went wrong  taking order"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)