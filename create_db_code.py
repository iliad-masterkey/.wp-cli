#!/usr/bin/env python3
# _*_ coding: utf8 _*_

# /////////////////////////////////////////////////////////////////////////////
# //
# //          Title: create_db_code.py
# //         Author: Merkader
# //        Created: 2019-May-20
# //

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import pathlib
import getpass


PARSER = argparse.ArgumentParser(
    description="""
    Creates a sql code for new wordpress installation.
    """)

PARSER.add_argument('-dn', '--database-name', dest='db_name')
PARSER.add_argument('-du', '--database-username', dest='db_username')
PARSER.add_argument('-dp', '--database-password', dest='db_pwd')
PARSER.add_argument('-dh', '--database-host', dest='db_host', default='localhost')  # noqa
PARSER.add_argument('-o', '--output-file', dest='output', default='setup.sql')  # noqa
PARSER.add_argument('-p', '--template-dir-path', dest='template_path_dir', default='templates')  # noqa

ARGS = PARSER.parse_args()
TEMP_FILE = pathlib.Path.cwd() / ARGS.template_path_dir / ARGS.output
TEMP_FILE.parent.mkdir(parents=True, exist_ok=True)


CODE_BLOCK = """--
-- source:
--  https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql
--
CREATE DATABASE IF NOT EXISTS `{dn}`;
CREATE USER IF NOT EXISTS `{u}`@`{h}` IDENTIFIED BY '{p}';
GRANT ALL PRIVILEGES ON `{dn}`.* TO '{u}'@'{h}';
FLUSH PRIVILEGES;
--
-- FURTHER USAGE:
--      sudo su
--      mysql -u root -p < <path-to-templates>/'{o}'
--      exit

""".format(
    dn=ARGS.db_name or input("Enter Name of Database: "),
    u=ARGS.db_username or input("Enter UserName: "),
    p=ARGS.db_pwd or getpass.getpass(prompt="Enter Password: "),
    h=ARGS.db_host,
    o=ARGS.output
)


with TEMP_FILE.open(mode='w') as sink:
    print(CODE_BLOCK, file=sink, flush=True)

if __name__ == "__main__":
    pass
