# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import os
import six

from .functional import lazy_once


expand_path = lambda value: os.path.expanduser(os.path.expandvars(value))
expand_path_lazy = lambda value: lazy_once(expand_path, value)


def parse_response(response):
    """
    Decodes the JSON response, simply ignoring syntax errors. Therefore it should be used for filtering visible output
    only.

    :param response: Server response as a JSON string.
    :type response: unicode | str
    :return: Decoded object from the JSON string. Returns an empty dictionary if input was invalid.
    :rtype: dict
    """
    if isinstance(response, six.binary_type):
        response = response.decode('utf-8')
    try:
        obj = json.loads(response)
    except ValueError:
        return {}
    return obj


def is_repo_image(image):
    """
    Checks whether the given image has a name, i.e. is a repository image. This does not imply that it is
    assigned to an external repository.

    :param image: Image structure from the Docker Remote API.
    :type image: dict
    :return: ``False`` if the only image name and tag is <none>, ``True`` otherwise.
    :rtype: bool
    """
    return image['RepoTags'][0] != '<none>:<none>'


def tag_check_function(tags):
    """
    Generates a function that checks whether the given image has any of the listed tags.

    :param tags: Tags to check for.
    :type tags: list[unicode | str] | set[unicode | str]
    :return: Function that returns ``True`` if any of the given tags apply to the image, ``False`` otherwise.
    :rtype: (unicode | str) -> bool
    """
    suffixes = [':{0}'.format(t) for t in tags]

    def _check_image(image):
        return any(r_tag.endswith(s) for s in suffixes for r_tag in image['RepoTags'])

    return _check_image
