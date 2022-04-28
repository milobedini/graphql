""" 
Schema is a description of what data to include, all the queries and mutations, and the db relationships.
Initially, everything is in this one file for GraphQL. Big difference to DRF.
 """
import graphene
from graphene_django import DjangoObjectType

from .models import Category, Product, ProductImage

# Graph is connected data in a space that we can then query. DjangoObjectType is data object within the graph.


class ProductImageType(DjangoObjectType):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        # Just need to include related name below to show relationship.
        fields = ("id", "title", "description", "regular_price", "slug", "product_image")


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "product")


# Can still run a query from the FE and only select relevant fields.


# Now need a query:


class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    # below is for individuals
    all_products_by_name = graphene.Field(ProductType, slug=graphene.String(required=True))
    # categories:
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    # how do we want to resolve our query from above. With Graph, start very general.
    def resolve_all_products(root, info):
        return Product.objects.all()

    def resolve_all_products_by_name(root, info, slug):
        try:
            return Product.objects.get(slug=slug)

        except Product.DoesNotExist:
            return None

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


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
