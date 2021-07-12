import os
from datetime import datetime


def file_name_profile(instance, pic_name):
    name = os.path.basename(pic_name)
    pre, ext = os.path.splitext(name)
    return "{}-{}{}".format(instance.username,
                            str(datetime.now()), ext)


def file_name(instance, pic_name):
    name = os.path.basename(pic_name)
    pre, ext = os.path.splitext(name)
    return "{}-{}{}".format(instance.user.username,
                            str(datetime.now()), ext)


def rename_profile(instance, pic_name):
    name = file_name_profile(instance, pic_name)
    return "{}/profiles/{}".format(instance.username, name)


def rename_file(instance, pic_name):
    name = file_name(instance, pic_name)
    return "{}/post_files/{}".format(instance.user.username, name)
