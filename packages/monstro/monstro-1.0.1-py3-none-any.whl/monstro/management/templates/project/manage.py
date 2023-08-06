#!/usr/bin/env python
# coding=utf-8

import os

import monstro.management
from monstro.core.constants import SETTINGS_ENVIRONMENT_VARIABLE


if __name__ == '__main__':
    os.environ.setdefault(
        SETTINGS_ENVIRONMENT_VARIABLE, 'settings.development.Settings'
    )

    monstro.management.manage()
