init -200 python:
    # here you can config Event Editor to your game
    # default images config
    addBGs('images/bgs')
    addEVs('images/events')
    addChs('images/characters')

    # example of adding character(EE speaker):
    somebody = Character("Somebody")
    speakers["somebody"] = somebody

    # enable/disable DSE(Dating Sim Engine) support in Event Editor
    # this is alpha don't work now do set to True
    EE__DSEmodule_active = False
