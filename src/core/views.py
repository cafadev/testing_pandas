import pandas as pd
import io
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from rest_framework import status

from src.core.models import Data
from src.core.serializers import DataSerializer


class DataModelViewSet(viewsets.ModelViewSet):

    queryset = Data.objects.all()
    serializer_class = DataSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    # permission_classes = (IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)

    def __load_data_to_model(self, df):
        df = df.loc[:, ['TIMESTAMP', 'RECORD', 'WS_10m_Avg', 'WS_10m_Max']]
        row_iter = df.iterrows()

        objs = [
            Data(
                timestamp = row['TIMESTAMP'],
                record  = row['RECORD'],
                ws_10m_avg  = row['WS_10m_Avg'],
                ws_10m_max  = row['WS_10m_Max']
            )
            for index, row in row_iter
        ]

        Data.objects.bulk_create(objs, batch_size=200)
        

    def create(self, request):
        file_obj = request.data['file']
        df = pd.read_csv(io.StringIO(file_obj.read().decode('utf-8')), delimiter=',')

        self.__load_data_to_model(df)
        return Response('ok', status=status.HTTP_202_ACCEPTED)
