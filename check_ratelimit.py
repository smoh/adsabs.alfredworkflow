#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json

RATELIMIT_FILE = os.path.expanduser("~/.ads/ratelimit")

with open(RATELIMIT_FILE, 'r') as f:
    d = json.loads(f.read())
    results = json.dumps(
            dict(
                items=[dict(
                    title='Remaining: {}'.format(d['remaining']
                        ))]
                    )
            )
    sys.stdout.write(results)
