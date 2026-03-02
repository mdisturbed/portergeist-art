#!/bin/bash
# Download images from Instagram CDN URLs already extracted
DIR=~/clawd/portergeist-art/images
# We'll collect URLs by clicking through posts via browser
# For now just track what we have
ls -la "$DIR"/portfolio-*.jpg 2>/dev/null | wc -l
