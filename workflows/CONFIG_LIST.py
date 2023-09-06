
from screenshot.config import config_utils
from workflows.CONFIG_LISTS.CBSL import CONFIG_LIST_CBSL
from workflows.CONFIG_LISTS.CEB import CONFIG_LIST_CEB
from workflows.CONFIG_LISTS.MISC import CONFIG_LIST_MISC
from workflows.CONFIG_LISTS.TE import CONFIG_LIST_TE
from workflows.CONFIG_LISTS.VENTUSKY import CONFIG_LIST_VENTUSKY

CONFIG_LIST = (
    CONFIG_LIST_VENTUSKY
    + CONFIG_LIST_TE
    + CONFIG_LIST_CBSL
    + CONFIG_LIST_CEB
    + CONFIG_LIST_MISC
)

'''
    ConfigScreenshot(
        '',
        '',
        '',
        SECONDS_IN.DAY,
        Point2D(1920- 1920, 1920- 1920),
        Size2D(1920, 1920),
    ),
'''
