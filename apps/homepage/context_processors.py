# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Make the settings `INCLUDE_WEBTRENDS` available to all templates so it can
be used in the base.html template.
"""
from django.conf import settings



def webtrends(request):
    return {'include_webtrends': settings.INCLUDE_WEBTRENDS}