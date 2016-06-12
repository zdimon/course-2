##File type

    import os 
    def get_upload_path(instance, filename): 
        return os.path.join( "user_%d" % instance.owner.id, "car_%s" % instance.slug, filename)

    photo = models.ImageField(upload_to=get_upload_path)
