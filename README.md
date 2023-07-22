# dump-iphone-backup

Dump an encrypted iPhone backup to a folder for analysis of any artifacts, organised by domain and path
of the source file.

Uses https://github.com/jsharkey13/iphone_backup_decrypt

This differs from the excellent [mvt](https://github.com/mvt-project/mvt), as this extracts the iOS device backup to a user-inspectable
filesystem, organised in such a way that we can manually look through device contents.

It is the author's intent that this only be used on devices where the device owner explicitly understands and consents to
the procedure.

## Installation

     pip install -r requirements.txt

## Usage

You may need to permit Terminal to have Full Disk Access on macOS for it to be permitted to read the `MobileSync/Backup` folder.

     ./dump-iphone-backup.py -b ~/Library/Application\ Support/MobileSync/Backup/SOME-GUID/ -o ~/output/ 
     # This will prompt interactively for the backup passphrase

     ./dump-iphone-backup.py -b ~/Library/Application\ Support/MobileSync/Backup/SOME-GUID/ -o ~/output/ -p some-passphrase
     # If comfortable, you can pass the passphrase on the command line

     # Or, set an environment variable for the passphrase:
     export DUMP_IPHONE_BACKUP_PASSPHRASE='some-passphrase'
     ./dump-iphone-backup.py -b ~/Library/Application\ Support/MobileSync/Backup/SOME-GUID/ -o ~/output/ 

## CLI Options

| -p | --passphrase | The passphrase of the backup. If not passed, the tool will look for `DUMP_IPHONE_BACKUP_PASSPHRASE` in the environment, or prompt interactively for the passphrase |
| -b | --backup-path | The path to the backup directory (~/Library/Application Support/MobileSync/EXAMPLE) |
| -o | --output-path | The path of the output directory where the flat files will be dumped. |
| -z | --no-create-parent-dirs | Do not create any parent directories required to create the output directory |
| -e | --remove-empty-domains | Remove any directories for backup domains that do not contain any files |

## Results

This repository of the backed up contents of the iOS device is useful for scanning against (for example) indicators of compromise of any future Pegasus-style spyware which may later become known. It is particularly interesting to examine the 

Regular backups and dumping of the encrypted backup using this tool may prove useful in shining the bright light of day on iOS spyware in the future. Perhaps even the existence of this script and the practice of regularly archiving forensic evidence of such spyware may present a disincentive to the deployment of such tools, as it increases the attacker's risk of detection and their methods.

If possible, regularly back up a device and archive each extracted backup for any future scanning for
indicators of compromise that later become known.
