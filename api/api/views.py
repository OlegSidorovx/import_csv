import os
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
import pandas as pd

from .models import ImportedFile
from .serializers import ImportedFileSerializer, UserSerializer
from .data_utils import get_file_structure, load_data_from_file


class ImportedFileViewSet(viewsets.ModelViewSet):
    queryset = ImportedFile.objects.all()
    serializer_class = ImportedFileSerializer

    def perform_create(self, serializer):
        uploaded_file = self.request.data['file']
        file_structure = get_file_structure(uploaded_file)
        serializer.save(structure=file_structure)


    def get_filtered_and_sorted_data(data, filters, sorting):
        df = pd.DataFrame(data)
        if filters:
            for column, value in filters.items():
                df = df[df[column] == value]
        if sorting:
            df = df.sort_values(by=sorting)
        return df.to_dict(orient='records')

    @action(detail=True, methods=['delete'])
    def delete_file(self, request, pk=None):
        imported_file = self.get_object()
        file_path = imported_file.file.path
        if os.path.exists(file_path):
            os.remove(file_path)
        imported_file.delete()
        return JsonResponse({'message': 'File deleted successfully'})


class FileDataView(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        file = ImportedFile.objects.get(pk=pk)
        filters = request.query_params.get('filters')
        sorting = request.query_params.get('sorting')

        data = load_data_from_file(file.file.path)
        filtered_and_sorted_data = get_filtered_and_sorted_data(data, filters, sorting)
        return Response(filtered_and_sorted_data)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
