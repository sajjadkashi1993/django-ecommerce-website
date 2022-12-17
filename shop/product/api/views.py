from rest_framework import views
from rest_framework.response import Response


class productApiViews(views.APIView):

    
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        return Response({'usernames':'sajjad'})