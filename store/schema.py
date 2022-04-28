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


# Can still run a query from the FE and only select relevant fields.


# Now need a query:


class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)

    # how do we want to resolve our query from above. With Graph, start very general.
    def resolve_all_products(root, info):
        return Product.objects.all()


schema = graphene.Schema(query=Query)

""" 
Example of how query is made in GraphiQL:

query {
  allProducts{
    id
    title
    regularPrice
  }
}
 """
