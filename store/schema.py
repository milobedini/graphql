""" 
Schema is a description of what data to include, all the queries and mutations, and the db relationships.
Initially, everything is in this one file for GraphQL. Big difference to DRF.
 """
import graphene
from graphene_django import DjangoObjectType

from .models import Product

# Graph is connected data in a space that we can then query. DjangoObjectType is data object within the graph.


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"


# Now need a query:


class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)

    # how do we want to resolve our query from above
    def resolve_all_products(root, info):
        return Product.objects.all()
