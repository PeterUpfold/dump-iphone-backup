# dump-iphone-backup

Dump an encrypted iPhone backup to a (very messy, structure-less) folder for analysis of any artifacts.

Uses https://github.com/jsharkey13/iphone_backup_decrypt

## Installation

     pip install -r requirements.txt

## Usage

You may need to permit Terminal to have Full Disk Access on macOS for it to be permitted to read the `MobileSync/Backup` folder.

     ./dump-iphone-backup.py -b ~/LibraryApplication\ Support/MobileSync/Backup/SOME-GUID/ -o ~/output/ 
     # This will prompt interactively for the backup passphrase

     ./dump-iphone-backup.py -b ~/LibraryApplication\ Support/MobileSync/Backup/SOME-GUID/ -o ~/output/ -p some-passphrase
     # If comfortable, you can pass the passphrase on the command line

## Results

This will give you a flat-file, very messy directory with every file that was backed up.

While lacking structure, this repository of the backed up contents of the iOS device is useful for scanning against (for example) indicators of compromise of any future Pegasus-style spyware which may later become known.

Regular backups and dumping of the encrypted backup using this tool may prove useful in shining the bright light of day on iOS spyware in the future. Perhaps even the existence of this script and the practice of regularly archiving forensic evidence of such spyware may present a disincentive to the deployment of such tools, as it increases the attacker's risk of detection and their methods.

