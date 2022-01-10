"""
Views for api app
"""
# REST imports
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
# local imports
from api.models import Content, Tag
from api.serializers import (
                            TagSerializer,
                            ContentSerializer,
                            OverviewSerializer,
                            )



class ContentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Content API's

    create          : Create content
    list            : List contents
    retrieve        : Retrieve content
    update          : Update content
    partial_update  : Patch contents
    destroy         : Delete content
    overview        : Lists count with hyperlink
    """
    queryset            = Content.objects.all().order_by('title')
    serializer_class    = ContentSerializer
    permission_classes  = (IsAuthenticated, )

    @action(detail=False)
    def overview(self, request):
        '''
        Lists total number of snippets and all
        available snippets with a hyperlink to
        respective detail APIs.

        Parameters:
            pk (int) : Primark key.

        Returns:
            dict: Returns count and snippets.
        '''
        queryset            = self.filter_queryset(self.get_queryset())
        output_serializer   = OverviewSerializer(
                                    queryset,
                                    many=True,
                                    context={'request': request},
                                    )

        content = {
                    'count'     : queryset.count(),
                    'snippets'  : output_serializer.data[:],
                    }
        return Response(content)



class TagViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Tag API's

    create          : Create tag
    list            : List tags
    retrieve        : Lists snippets linked
    update          : Update tag
    partial_update  : Patch tags
    destroy         : Delete tag
    """
    queryset            = Tag.objects.all().order_by('title')
    serializer_class    = TagSerializer
    permission_classes  = (IsAuthenticated, )

    def retrieve(self, request, pk=None):
        '''
        Finds snippets linked to the selected tag.

        Parameters:
            pk (int) : Primark key.

        Returns:
            list : list of contents
        '''
        # Get the contents related to the tag id
        content = Content.objects.filter(tag__id=pk).values()
        return Response(content)
