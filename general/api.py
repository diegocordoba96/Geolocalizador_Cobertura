
from rest_framework.decorators import api_view
from app.models import Cobertura
from Planes.models import Plan
from rest_framework.response import Response
from .serializers import CoberturaSerializer, PlanSerializer, LocalizacionSerealizer
from rest_framework import status
from django.db import connection
c = connection.cursor()
from django.contrib.auth.decorators import login_required


# get cobertura
@login_required
@api_view(['GET', 'POST'])
def get_cobertura(request):
    if request.method == 'GET':
        cobertura = Cobertura.objects.all()
        cobertura_serializer = CoberturaSerializer(cobertura, many=True)
        return Response(cobertura_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        coberturas = []
        localizacion_serealizer = LocalizacionSerealizer(data=request.data)
        if localizacion_serealizer.is_valid():
            try:
                long = str(request.data['longitud'])
                lat = str(request.data['latitud'])
                c.execute(f"""
                    	SELECT CAST( ST_Point({long},{lat}, 4326) AS geography);
                    """)
                geom = c.fetchone()
                c.execute(f"""
                    SELECT   ac.color,"Planes_plan".nombre
                    FROM app_cobertura_planes acp
                    INNER JOIN app_cobertura ac ON acp.cobertura_id = ac.id
                    INNER JOIN "Planes_plan" ON "Planes_plan".id = acp.plan_id
                    WHERE ST_Intersects(ac.location,'{geom[0]}');
                    """)
                coberturas = c.fetchall()

        
                return Response(coberturas, status=status.HTTP_200_OK)

            except Exception as e:
                print(e)
        return Response(localizacion_serealizer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({f'message': f'{request.data} no exist'}, status=status.HTTP_400_BAD_REQUEST)

# get planes
@login_required
@api_view(['GET', 'POST'])
def get_planes(request):
    if request.method == 'GET':
        planes = Plan.objects.all()
        planes_serializer = PlanSerializer(planes, many=True)
        return Response(planes_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        planes_serializer = PlanSerializer(data=request.data)
        if planes_serializer.is_valid():
            planes_serializer.save()
            data = {
                'id': planes_serializer.data['id'],
                'color': planes_serializer.data['nombre'],
            }
            return Response(planes_serializer.data, status=status.HTTP_201_CREATED)
        return Response(planes_serializer.errors)


