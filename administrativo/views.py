from django.shortcuts import render

# Create your views here.

from django.http import Http404, HttpResponseRedirect,HttpRequest,HttpResponse

# Create your views here.
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from .forms import *
from .serializers import EmprendimientoSerializers, EmprendedorSerializers,ServicioSerializers
from .models import Emprendimiento,Emprendedor,Servicio, Producto,Rating

################################################### INDEX ###################################################

class Index(View):

    def get(self,request:HttpRequest) -> HttpResponse:
        servicios=Servicio.objects.all()
        valor=[]
        for servicio in servicios:
            emprendimientos= Emprendimiento.objects.all().filter(servicio=servicio) 
            valor.append(emprendimientos)

        # queryset = request.GET['search']
        # if queryset:
        #     listaemprendimientos = Emprendimiento.objects.filter(
        #         Q(nombreEmprendimiento__icontains =queryset) |
        #         Q(direccion__icontains=queryset) 
        #     ).distinct() 
        #contexto = {'tabla':palabras, 'paginas':paginas, 'pagina_actual':current_page}
        return render(request, 'presentacion/index.html', {'servicios':servicios,'emprendimientos':emprendimientos,'valor':valor,} )


################################################## Reserva ##################################################

class GenerarReserva(View):
    def get(self, request,id_producto):
        productos=Producto.objects.all().filter(id=id_producto)  
        form=ReservaFormulario()
        return render(request, 'emprendimiento/reserva.html', {'form':form,'productos':productos})


    def post(self, request, *args, **kwargs):
        form = ReservaFormulario(request.POST or None)
        valor= kwargs
        if form.is_valid():
            fechaReserva= form.cleaned_data.get('fechaReserva')
            emprendimiento= form.cleaned_data.get('emprendimiento')
            cantidad=form.cleaned_data.get('cantidad')
            valor= form.cleaned_data.get('valor')
            #productos=form.cleaned_data['productos']
            reserva= Reserva(
                fechaReserva=fechaReserva,
                emprendimiento=emprendimiento,
                cantidad=cantidad,
                valor=valor
            )
            reserva.save()
            form=ReservaFormulario()

            print(form)
            return HttpResponseRedirect("index")
        else:
            return render(request,'emprendimiento/reserva.html',{'form':form})




###############################        Individual View         ################################

class ListarEmprendimientos(View):
    def get(self,request:HttpRequest, id_servicio) -> HttpResponse:
        servicios= Servicio.objects.all()
        if not id_servicio:
            id_servicio=1
        emprendimientos=Emprendimiento.objects.all().order_by('servicio').filter(servicio=id_servicio)
        return render(request, 'emprendimiento/listaEmprendimientos.html',{'emprendimientos':emprendimientos,'servicios':servicios,} )


class VerEmprendimiento(View):
    def get(self, request:HttpRequest, id_emprendimiento) -> HttpResponse:
        emprendimientos=Emprendimiento.objects.all().filter(id=id_emprendimiento)

        # for emprendimiento in emprendimientos:
        #     rating = Rating.objects.filter(emprendimiento=emprendimiento, user=request.user).first()
        #     emprendimiento.user_rating = rating.rating if rating else 0

        form=ReservasForm()
        productos= Producto.objects.filter(producto__id=id_emprendimiento)
        return render(request,'emprendimiento/emprendimiento.html',{'form':form ,'emprendimientos':emprendimientos,'productos':productos})

    
    # def rate(request: HttpRequest, emprendimiento_id: int, get: int) -> HttpResponse:
    #     emprendimientorate = Emprendimiento.objects.get(id=emprendimiento_id)
    #     Rating.objects.filter(emprendimientorate=emprendimientorate, user=request.user).delete()
    #     emprendimientorate.rating_set.create(user=request.user, get=get)
    #     return  get(request)        


#################################### Servicios para aplicaciones Moviles ############################################
class Emprendedor_APIView(APIView):
    def get(self, request,format =None, *args, **Kwargs):
        emprendedores= Emprendedor.objects.all()
        serializer= EmprendedorSerializers(emprendedores,many=True)    
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=EmprendedorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)    

class Emprendedor_APIView_Detalles(APIView):
    def get_object(self, emprendedor_id):
        try:
            return Emprendedor.objects.get(id=emprendedor_id)
        except Emprendedor.DoesNotExist:
            raise Http404

    def get(self,request,id_emprendedor,format=None):
        emprendedor = self.get_object(id_emprendedor)
        serializer= EmprendedorSerializers(emprendedor)
        return Response(serializer.data)

    def put(self,request,id_emprendedor, format=None):
        emprendedor=self.get_object(id_emprendedor)
        serializer= EmprendedorSerializers(emprendedor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Servicio_APIView(APIView):
    def get(self, request,format =None, *args, **Kwargs):
        servicio= Servicio.objects.all()
        serializer= ServicioSerializers(servicio,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=ServicioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)    

class Servicio_APIView_Detalles(APIView):

    def get_object(self, servicio_id):
        try:
            return Servicio.objects.get(id=servicio_id)
        except Servicio.DoesNotExist:
            raise Http404

    def get(self,request,id_servicio,format=None):
        servicio = self.get_object(id_servicio)
        serializer= ServicioSerializers(servicio)
        return Response(serializer.data)

    def put(self,request,id_servicio, format=None):
        servicio=self.get_object(id_servicio)
        serializer= ServicioSerializers(servicio,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Emprendimiento_APIView(APIView):

    def get(self, request,format =None, *args, **Kwargs):

        emprendimientos = Emprendimiento.objects.all()
        serializer= EmprendimientoSerializers(emprendimientos,many=True)
        
        return Response(serializer.data)

    def post(self,request,format=None):

        serializer=EmprendimientoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)    

class Emprendimiento_APIView_Detalles(APIView):
    #Obtener todos los objetos
    def get_object(self, emprendimiento_id):
        try:
            return Emprendimiento.objects.get(id=emprendimiento_id)
        except Emprendimiento.DoesNotExist:
            raise Http404



    #encontrar el objeto encontrado en el api
    def get(self,request,id_emprendimiento,format=None):
        emprendimiento = self.get_object(id_emprendimiento)
        serializer= EmprendimientoSerializers(emprendimiento)
        return Response(serializer.data)

    def put(self,request,id_emprendimineto, format=None):
        emprendimiento=self.get_object(id_emprendimineto)
        serializer= EmprendimientoSerializers(emprendimiento,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


