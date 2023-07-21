#!/bin/bash

archive_path="$1"

if [ ! -f "$archive_path" ]; then
    echo "Archive file not found."
    exit 1
fi

name=$(basename "$archive_path")
wname="${name%.*}"

releases_path="/data/web_static/releases/$wname/"
tmp_path="/tmp/$name"

mkdir -p "$releases_path"
tar -xzf "$archive_path" -C "$releases_path"
rm "$archive_path"
mv "${releases_path}web_static/"* "$releases_path"
rm -rf "${releases_path}web_static"
rm -rf /data/web_static/current
ln -s "$releases_path" /data/web_static/current
echo "New version deployed!"
