from workflows.configs import (_misc, _misc_health, cbsl, ceb, dcs,
                               globalpetrolprices, nuuuwan, owid, te, ventusky)


def get_config_list():
    modules = [
        _misc,
        _misc_health,
        cbsl,
        ceb,
        dcs,
        globalpetrolprices,
        nuuuwan,
        owid,
        te,
        ventusky,
    ]
    config_list = []
    for module in modules:
        config_list.extend(module.get_config_list())
    return config_list
