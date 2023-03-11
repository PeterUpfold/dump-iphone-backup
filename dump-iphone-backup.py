#!/usr/bin/env python3
#
# A simple command line client to dump an iPhone encrypted backup
# to a flat file folder of items.
#
# Uses https://github.com/jsharkey13/iphone_backup_decrypt
#
# Licensed under the MIT Licence

from iphone_backup_decrypt import EncryptedBackup, RelativePath, RelativePathsLike
import argparse
import getpass
import os
import sqlite3
from contextlib import closing

parser = argparse.ArgumentParser(description='Command line client to dump iPhone encrypted backup to flat folder of items.')
parser.add_argument('-p', '--passphrase', type=str, default=None, required=False, help='The passphrase of the backup. If not passed, the tool will prompt interactively for the passphrase')
parser.add_argument('-b', '--backup-path', type=str, default=None, required=True, help='The path to the backup directory (~/Library/Application Support/MobileSync/EXAMPLE)')
parser.add_argument('-o', '--output-path', type=str, default=None, required=True, help='The path of the output directory where the flat files will be dumped.')

args = parser.parse_args()

if args.passphrase is None:
    if os.environ.get('DUMP_IPHONE_BACKUP_PASSPHRASE') is None:
        passphrase = getpass.getpass(prompt='Provide the backup passphrase: ')
    else:
        passphrase = os.environ.get('DUMP_IPHONE_BACKUP_PASSPHRASE')
else:
    passphrase = args.passphrase


if not os.path.isdir(args.backup_path):
    raise TypeError('The provided backup path does not exist or is not a directory.')

if not os.path.isdir(args.output_path):
    raise TypeError('The provided output path does not exist or is not a directory.')

backup=EncryptedBackup(backup_directory=args.backup_path, passphrase=passphrase)

# decrypt Manifest so we can search it for domains soon
manifest_path = os.path.join(args.output_path, 'Manifest.db')
backup.save_manifest_file(output_filename=manifest_path)

# get a list of domains and create top level folders
with closing(sqlite3.connect(manifest_path)) as connection:
    cursor = connection.cursor()
    for domain_row in cursor.execute('SELECT DISTINCT domain FROM Files'):
        os.makedirs(os.path.join(args.output_path, domain_row[0]), exist_ok=True)

    # for each file in the Manifest with flags = 1, extract it
    for file_row in cursor.execute('SELECT domain, relativePath, flags FROM Files WHERE flags = 1'):
        domain = file_row[0]
        relativePath = file_row[1]
        flags = file_row[2]

        # cut the last path item from relativePath
        relative_path_without_file = os.path.split(relativePath)[:-1]

        containing_dir = os.path.join(args.output_path, domain, relative_path_without_file[0])
        os.makedirs(containing_dir, exist_ok=True)

        print(f'Extracting {relativePath} from domain {domain}')
        backup.extract_file(relative_path = relativePath, output_filename=os.path.join(args.output_path, domain, relativePath))
