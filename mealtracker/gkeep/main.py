import logging
from uuid import getnode as get_mac

import gkeepapi
import gpsoauth
from django.conf import settings

logger = logging.getLogger("gkeepapi")

keep = gkeepapi.Keep()

SHOPPING_LIST_TITLE = "Testlist"


def login():
    logger.info(
        f"Logging in Google Keep: {settings.GOOGLE_USERNAME} / {settings.GOOGLE_PASSWORD}"
    )
    # Debug Google log in
    # TODO: Check https://github.com/kiwiz/gkeepapi/issues/81#issuecomment-770389348
    res = gpsoauth.perform_master_login(
        settings.GOOGLE_USERNAME, settings.GOOGLE_PASSWORD, get_mac()
    )
    logger.info("Google response")
    logger.info(res)
    # keep.login(
    #     settings.GOOGLE_USERNAME,
    #     settings.GOOGLE_PASSWORD,
    #     sync=False,
    # )


def add_shopping_list_item():
    login()
    glists = keep.find(query=SHOPPING_LIST_TITLE)
    glist = next(glists)
    glist.add("Item 2")
    keep.sync()
