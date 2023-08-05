"""
This plugin uses django-versatileimagefield_ to do the heavy lifting.
"""

from __future__ import unicode_literals

from django import forms
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from content_editor.admin import ContentEditorInline

from versatileimagefield.fields import VersatileImageField, PPOIField


__all__ = ('Image', 'AlwaysChangedModelForm', 'ImageInline', 'render_image')


@python_2_unicode_compatible
class Image(models.Model):
    """
    Image plugin
    """
    image = VersatileImageField(
        _('image'),
        upload_to='images/%Y/%m',
        width_field='width',
        height_field='height',
        ppoi_field='ppoi',
    )
    width = models.PositiveIntegerField(
        _('image width'),
        blank=True,
        null=True,
        editable=False,
    )
    height = models.PositiveIntegerField(
        _('image height'),
        blank=True,
        null=True,
        editable=False,
    )
    ppoi = PPOIField(_('primary point of interest'))

    class Meta:
        abstract = True
        verbose_name = _('image')
        verbose_name_plural = _('images')

    def __str__(self):
        return self.image.name


class AlwaysChangedModelForm(forms.ModelForm):
    """
    This ``ModelForm``'s ``has_changed`` method always returns ``True``. This
    is a workaround for the problem where Django's inlines do not detect
    changes in ``MultiValueField`` (which is used to set the PPOI --
    primary point of interest -- in django-versatileimagefield_).

    https://github.com/respondcreate/django-versatileimagefield/issues/44
    """
    def has_changed(self):
        return True


class ImageInline(ContentEditorInline):
    """
    Image inline using the ``AlwaysChangedModelForm`` to work around a bug
    where PPOI modifications were not picked up.
    """
    form = AlwaysChangedModelForm


def render_image(plugin, **kwargs):
    """
    Return a simple, unscaled version of the image
    """
    return format_html('<img src="{}" alt="">', plugin.image.url)
