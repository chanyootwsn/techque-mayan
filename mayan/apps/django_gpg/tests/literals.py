from __future__ import unicode_literals

import os

from django.conf import settings

TEST_KEY_DATA = '''-----BEGIN PGP PRIVATE KEY BLOCK-----
Version: GnuPG v1

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
8aeg3z/W+YctdRt81bi5isgM+oML9LAQ
=JZ5G
-----END PGP PRIVATE KEY BLOCK-----'''

TEST_KEY_ID = '4125E9C571F378AC'
TEST_KEY_FINGERPRINT = '6A24574E0A35004CDDFD22704125E9C571F378AC'
TEST_KEY_PASSPHRASE = 'testpassphrase'

TEST_KEYSERVERS = ['pool.sks-keyservers.net']

TEST_SEARCH_UID = 'Roberto Rosario'
TEST_SEARCH_FINGERPRINT = '607138F1AECC5A5CA31CB7715F3F7F75D210724D'

TEST_SIGNED_FILE = os.path.join(
    settings.BASE_DIR, 'mayan', 'apps', 'django_gpg', 'tests', 'contrib',
    'test_files', 'test_file.txt.gpg'
)
