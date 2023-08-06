#! /bin/bash

# This script must be ran from inside the folder containing it
# (with "./install.sh").

# It doesn't need root privileges, since it "installs" the scripts only for the
# user running it.
# WARNING: it will close all your currently opened folders.


mkdir ~/.gnome2/nautilus-scripts/Gallery

upload=~/.gnome2/nautilus-scripts/Gallery/Upload\ to\ Gallery

if [ -h "$upload" ]
    then
        unlink "$upload"
fi


ln -s `pwd`/gallery-uploader "$upload"

killall nautilus; nautilus &

# After you ran it, just rightclick on an image and take a look under "Scripts".
