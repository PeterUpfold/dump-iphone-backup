# dump-iphone-backup

Dump an encrypted iPhone backup to a folder for analysis of any artifacts, organised by domain and path
of the source file.

Uses https://github.com/jsharkey13/iphone_backup_decrypt

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

## Results

This repository of the backed up contents of the iOS device is useful for scanning against (for example) indicators of compromise of any future Pegasus-style spyware which may later become known.

Regular backups and dumping of the encrypted backup using this tool may prove useful in shining the bright light of day on iOS spyware in the future. Perhaps even the existence of this script and the practice of regularly archiving forensic evidence of such spyware may present a disincentive to the deployment of such tools, as it increases the attacker's risk of detection and their methods.

If possible, regularly back up a device and archive each extracted backup for any future scanning for
indicators of compromise that later become known.
