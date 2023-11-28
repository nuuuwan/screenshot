from workflows.configs import (_misc, cbsl, ceb, globalpetrolprices, nuuuwan,
                               owid, te, ventusky)


def get_config_list():
    modules = [
        _misc,
        cbsl,
        ceb,
        globalpetrolprices,
        nuuuwan,
        owid,
        te,
        ventusky,
    ]
    config_list = []
    for module in modules:
        config_list.extend(module.get_config_list())
