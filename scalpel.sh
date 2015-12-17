#!/usr/bin/env bash

mkdir 9gag_scalpel && mkdir amazon_scalpel && mkdir soundcloud_scalpel && mkdir twitter_scalpel && mkdir youtube_scalpel
mkdir session_expires_scalpel && mkdir system_reboot_scalepl

scalpel 9gag.dump -c ../scalpel_conf/scalpel.conf -o 9gag_scalpel/
scalpel amazon.dump -c ../scalpel_conf/scalpel.conf -o amazon_scalpel/
scalpel soundcloud.dump -c ../scalpel_conf/scalpel.conf -o soundcloud_scalpel/
scalpel twitter.dump -c ../scalpel_conf/scalpel.conf -o twitter_scalpel/
scalpel youtube.dump -c ../scalpel_conf/scalpel.conf -o youtube_scalpel/
scalpel session_expires -c ../scalpel_conf/scalpel.conf -o session_expires_scalpel
scalpel system_reboot -c ../scalpel_conf/scalpel.conf -o system_reboot_scalepl
#---------------------------------#
