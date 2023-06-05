from django.shortcuts import render
from store.models import Customer, Order, Product,OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q , F,Value,Func,Count
from django.db.models.functions import Concat
from django.db.models.aggregates import Min,Max,Sum,Avg,StdDev

# Create your views here.
def balu():
    a=45
    return a
def hello(request):
    
    x = balu()
    y = 30
    try:
            # product = Product.objects.filter(pk=0).first()#none
            # query_set = Product.objects.filter(unit_price__gte=20)
            # offers = Product.objects.filter(inventory__lt=10,unit_price__lt=20)
            # offers = Product.objects.filter(Q(inventory__gt=10) & ~Q(unit_price__lt=20))
            # offers = Product.objects.filter(inventory=F('collection_id'))#compares the two fields
            #sorting..
            # offers = Product.objects.filter(inventory=F('collection_id')).order_by('-title','inventory').reverse()#sorting...
            # offers = Product.objects.filter(collection_id=3).order_by('-unit_price')[0]
            # offers = Product.objects.all()[:5]
            #selecting fields to query...
            # offers = Product.objects.values('id','title','collection__title')#related field
            # offers = Product.objects.values_list('id','title','collection__title')#related field
            # offers = Product.objects.values_list().order_by('title')
            #select the products that have been ordered and sort them by title
            # orders = OrderItem.objects.values_list('product_id','product__title').distinct()
            #method -2
            # product = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
            #deferring fields...
            # product = Product.objects.only('unit_price','title')
            # product = Product.objects.defer('unit_price')
            #select_related...to avoid multiple queries...
            # product = Product.objects.select_related('collection').all()
            #pre_fecth_realted
            # product = Product.objects.prefetch_related('promotion').all()
            #combine prefetch_related..
            # product = Product.objects.prefetch_related('promotion').select_related('collection').all()
            
            #get the last 5 orders with their customer and items(include product)
            # product = Order.objects.select_related('customer')\
            #             .prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
                        
        # Aggrigations....
        result = Product.objects.aggregate(sum=Sum('unit_price'),min_price=Min('unit_price'),max_price = Max('unit_price'))
        result = Product.objects.filter(collection__id=3).aggregate(total=Sum('unit_price'))
        
        queryset = Product.objects.annotate(is_new=Value(True))
        queryset = Product.objects.annotate(new_id=F('id')+1)
        queryset = Customer.objects.annotate(
            #concat
            Full_name = Func(F('first_name'),Value(' '),F('last_name'),function='CONCAT')
        )
        queryset = Customer.objects.annotate(
                #concat
                Full_name = Concat('first_name',Value(' '),'last_name')
            )
        
        #grouping DAta...
        queryset = Customer.objects.annotate(
            orders_count =Count('order')
        )

        #expression wrappers...
        queryset = ''
        
        
    except ObjectDoesNotExist:
        pass
    return render(request,'hello.html',{'name':'bala','age':24,'result':queryset})