# -*- coding: utf-8 -*-
import scrapy
import functools
import hashlib
import six
import pdb

try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

from PIL import Image

from string import maketrans

from scrapy.utils.misc import md5sum
from scrapy.utils.python import to_bytes
from scrapy.http import Request
from scrapy.settings import Settings
from scrapy.exceptions import DropItem
#TODO: from scrapy.pipelines.media import MediaPipeline
from scrapy.pipelines.files import FileException, FilesPipeline
from scrapy.pipelines.images import ImagesPipeline

class T66YImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x,meta={'folder': item.get('t_title')}) for x in item.get(self.images_urls_field, [])]

    def file_path(self, request, response=None, info=None):
        ## start of deprecation warning block (can be removed in the future)
        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('ImagesPipeline.image_key(url) and file_key(url) methods are deprecated, '
                          'please use file_path(request, response=None, info=None) instead',
                          category=ScrapyDeprecationWarning, stacklevel=1)

        # check if called from image_key or file_key with url as first argument
        if not isinstance(request, Request):
            _warn()
            url = request
        else:
            url = request.url

        # detect if file_key() or image_key() methods have been overridden
        if not hasattr(self.file_key, '_base'):
            _warn()
            return self.file_key(url)
        elif not hasattr(self.image_key, '_base'):
            _warn()
            return self.image_key(url)
        ## end of deprecation warning block

        image_guid = hashlib.sha1(to_bytes(url)).hexdigest()  # change to request.url after deprecation
        folder = request.meta['folder']
        if len(folder):
            folder = folder[0]
            #pdb.set_trace()
            table = dict((ord(char), None) for char in "|\\?*<\":>+[]/'")
            folder = folder.translate(table)
        else:
            folder = u'未知'
        #pdb.set_trace()
        return '%s/%s.jpg' % (folder,image_guid)
