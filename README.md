# Store-Front
ORM operations...
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
            product = Order.objects.select_related('customer')\
                        .prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]