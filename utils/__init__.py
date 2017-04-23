#!/usr/bin/env python
# coding=utf-8

import os

# from utils.common import *  # noqa
from .ip2Region import Ip2Region

ip_region = Ip2Region(os.path.abspath('utils/ip2region.db'))
