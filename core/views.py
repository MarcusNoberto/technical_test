from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PersonSerializer
from .services import PersonService


class PersonController(APIView):
    service = PersonService()

    def get(self, request, pk=None):
        if pk is not None:
            person = self.service.process_request('get', person_id=pk)
            serializer = PersonSerializer(person)
        else:
            persons = self.service.process_request('list_all')
            serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        person = self.service.process_request('create', data=serializer.validated_data)
        return Response(PersonSerializer(person).data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        person = self.service.process_request('get', person_id=pk)

        serializer = PersonSerializer(person, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self.service.process_request('delete', person_id=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class IdealWeightController(APIView):
    service = PersonService()
    def get(self, request, pk):
        ideal_weight = self.service.process_request(
            'calculate_ideal_weight',
            person_id=pk
        )
        return Response({"ideal_weight": ideal_weight}, status=status.HTTP_200_OK)
