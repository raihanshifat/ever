from rest_framework.views import APIView
from elasticsearch_dsl import Q
from .documents import UserProfileDocument
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileElasticSerializer

class SearchUser(APIView):

    def post(self,request):
        data = request.data
        query = data["query"]
        q = Q(
            'multi_match',
            query = query,
            fields = [
                'full_name',
                ],
            fuzziness = 'auto'
            )

        search = UserProfileDocument.search().query(q)
        result = search.execute()
      
        serializer_result = UserProfileElasticSerializer(result,many=True)
        
        return Response(serializer_result.data,status=status.HTTP_200_OK)