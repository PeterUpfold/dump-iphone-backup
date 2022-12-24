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

parser = argparse.ArgumentParser(description='Command line client to dump iPhone encrypted backup to flat folder of items.')
parser.add_argument('-p', '--passphrase', type=str, default=None, required=False, help='The passphrase of the backup. If not passed, the tool will prompt interactively for the passphrase')
parser.add_argument('-b', '--backup-path', type=str, default=None, required=True, help='The path to the backup directory (~/Library/Application Support/MobileSync/EXAMPLE)')
parser.add_argument('-o', '--output-path', type=str, default=None, required=True, help='The path of the output directory where the flat files will be dumped.')

args = parser.parse_args()

if args.passphrase is None:
    passphrase = getpass.getpass(prompt='Provide the backup passphrase: ')
else:
    passphrase = args.passphrase


if not os.path.isdir(args.backup_path):
    raise TypeError('The provided backup path does not exist or is not a directory.')

if not os.path.isdir(args.output_path):
    raise TypeError('The provided output path does not exist or is not a directory.')

backup=EncryptedBackup(backup_directory=args.backup_path, passphrase=passphrase)

backup.extract_files(relative_paths_like='%', output_folder=args.output_path)