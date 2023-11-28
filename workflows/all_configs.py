from workflows import configs


def get_config_list():
    modules = [
        configs._misc,
        configs.cbsl,
        configs.ceb,
        configs.globalpetrolprices,
        configs.nuuuwan,
        configs.owid,
        configs.te,
        configs.ventusky,
    ]
    config_list = []
    for module in modules:
        config_list.extend(module.get_config_list())
    return config_list
