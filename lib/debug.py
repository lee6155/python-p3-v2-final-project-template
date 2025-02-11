#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.user import User
from models.file import File

import ipdb

User.drop_table()
User.create_table()

File.drop_table()
File.create_table()

ipdb.set_trace()
