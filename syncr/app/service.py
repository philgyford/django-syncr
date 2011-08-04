from taggit.models import Tag

class ServiceSyncr(object):
    """
    The base class for all syncr classes.
    Any *Syncr classes for future services should inherit this class.
    """

    def __init__(self, *args, **kwargs):
        pass


    def syncTags(self, remote_slugnames, obj):
        """
        Sync the remote tags on an item with its local Django object.
        The local object might have just been created, or might be an existing
        one that we're updating and syncing.

        Works for services that have standard tags that are nothing more than a
        name and slug (which may be the same). Services which have more complicated 
        tags, and use a 'through' model in taggit (like Flickr), should use a
        custom method.

        Required arguments
            remote_slugnames: A dictionary of slug:name on the remote item.
                        eg, 'Nye Bevan': 'nye-bevan'
            obj: The Django object we're syncing. Should have been created/saved already.
        """
        local_tags = obj.tags.all() 
        local_slugs = set([tag.slug for tag in local_tags])
        remote_slugs = set(remote_slugnames.keys())

        # Are there any new slugs to add to the local object?
        slugs_to_add = remote_slugs.difference(local_slugs)
        if len(slugs_to_add):
            tags_to_add = []
            for slug, name in remote_slugnames.items():
                if slug in slugs_to_add:
                    tag_obj, tag_created = Tag.objects.get_or_create(
                            slug=slug, defaults={'name':name}
                    )
                    tags_to_add.append(tag_obj)
            obj.tags.add(*tags_to_add)

        # Are there any slugs held locally that have been removed on the remote 
        # photo?
        slugs_to_remove = local_slugs.difference(remote_slugs)
        if len(slugs_to_remove):
            tags_to_remove = []
            for tag in local_tags:
                if tag.slug in slugs_to_remove:
                    tags_to_remove.append(tag)
            obj.tags.remove(*tags_to_remove)


