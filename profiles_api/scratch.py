from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers


class HelloApiView(APIView):
    """Testing API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

        an_apiView = [
            'User http methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your API logic',
            'Is mapped manually to URL´s'
        ]

        message = 'Hello'

        return Response({'message': message, 'an_apiView': an_apiView})

    def post(self, request, pk=None):
        """Creates a hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handles updating an object"""

        message = 'PUT'
        return Response({'method': message})

    def patch(self, request, pk=None):
        """Handles partial update of an object"""

        message = 'PATCH'
        return Response({'message': message})

    def delete(self, request, pk=None):
        """Handles a deletion of an object"""

        message = 'DELETE'
        return Response({'message': message})


class ApiViewSet(viewsets.ViewSet):
    """Testing API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):

        an_viewset = [
            'Uses actions (List, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code',
        ]

        message = 'Hello'

        return Response({
            'message': message,
            'an_viewset': an_viewset
        })

    def create(self, request, pk=None):
        """Handles creation of an object"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({
                'message': message
            })

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handles getting an object"""

        message = 'GET'
        return Response({
            'http_method': message
        })

    def update(self, request, pk=None):
        """Handles updating an object"""

        message = 'PUT'
        return Response({
            'http_method': message
        })

    def partial_update(self, request, pk=None):
        """Handles partially updating an object"""

        message = 'PATCH'
        return Response({
            'http_method': message
        })

    def destroy(self, request, pk=None):
        """Handles deleting an object"""

        message = 'DELETE'
        return Response({
            'http_method': message
        })
