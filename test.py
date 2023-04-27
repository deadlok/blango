class TagViewSet(viewsets.ModelViewSet):
    # exiting methods omitted

    @method_decorator(cache_page(300))
    def list(self, *args, **kwargs):
        return super(TagViewSet, self).list(*args, **kwargs)

    @method_decorator(cache_page(300))
    def retrieve(self, request, *args, **kwargs):
        return super(TagViewSet, self).retrieve(*args, **kwargs)