from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
import logging

import re
from django.core.cache import cache
from django.conf import settings

from apps.page_generator.models import *
from django.dispatch import receiver
from django.db.models.signals import post_save

logger = logging.getLogger('product')


class CacheMixin:
    @method_decorator(cache_page(60 * 15))
    def dispatch(self, *args, **kwargs):
        logger.debug(f"Вызван метод {self.request.method} для {self.__class__.__name__}")
        return super().dispatch(*args, **kwargs)


def delete_cache_pattern(pattern: str):
    cache_keys = cache._cache.keys()
    regex = re.compile(pattern)
    keys_to_delete = [key for key in cache_keys if regex.match(key)]

    for key in keys_to_delete:
        cache.delete(key)


def delete_cache(key_prefix: str):
    keys_pattern = f"views.decorators.cache.cache_.*.{key_prefix}.*.{settings.LANGUAGE_CODE}.{settings.TIME_ZONE}"
    delete_cache_pattern(keys_pattern)


@receiver(post_save, sender=NavLinks)
def delete_caches_service(sender, instance, created, **kwargs):
    print(f"Delete cash in {instance.CACHE_KEY_PREFIX}")
    if created:
        delete_cache(instance.CACHE_KEY_PREFIX)


@receiver(post_save, sender=NAVImages)
def delete_caches(sender, instance, created, **kwargs):
    print(f"Delete cash in {instance.CACHE_KEY_PREFIX}")
    if created:
        delete_cache(instance.CACHE_KEY_PREFIX)


@receiver(post_save, sender=TextContent)
def delete_caches(sender, instance, created, **kwargs):
    print(f"Delete cash in {instance.CACHE_KEY_PREFIX}")
    if created:
        delete_cache(instance.CACHE_KEY_PREFIX)


@receiver(post_save, sender=Images)
def delete_caches(sender, instance, created, **kwargs):
    print(f"Delete cash in {instance.CACHE_KEY_PREFIX}")
    if created:
        delete_cache(instance.CACHE_KEY_PREFIX)


@receiver(post_save, sender=Veteran)
def delete_caches(sender, instance, created, **kwargs):
    print(f"Delete cash in {instance.CACHE_KEY_PREFIX}")
    if created:
        delete_cache(instance.CACHE_KEY_PREFIX)


@receiver(post_save, sender=VeteransImages)
def delete_caches(sender, instance, created, **kwargs):
    print(f"Delete cash in {instance.CACHE_KEY_PREFIX}")
    if created:
        delete_cache(instance.CACHE_KEY_PREFIX)


@receiver(post_save, sender=Partners)
def delete_caches(sender, instance, created, **kwargs):
    print(f"Delete cash in {instance.CACHE_KEY_PREFIX}")
    if created:
        delete_cache(instance.CACHE_KEY_PREFIX)


@receiver(post_save, sender=PartnersImages)
def delete_caches(sender, instance, created, **kwargs):
    print(f"Delete cash in {instance.CACHE_KEY_PREFIX}")
    if created:
        delete_cache(instance.CACHE_KEY_PREFIX)


@receiver(post_save, sender=News)
def delete_caches(sender, instance, created, **kwargs):
    print(f"Delete cash in {instance.CACHE_KEY_PREFIX}")
    if created:
        delete_cache(instance.CACHE_KEY_PREFIX)


@receiver(post_save, sender=NewsImages)
def delete_caches(sender, instance, created, **kwargs):
    print(f"Delete cash in {instance.CACHE_KEY_PREFIX}")
    if created:
        delete_cache(instance.CACHE_KEY_PREFIX)