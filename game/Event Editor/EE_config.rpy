init -10 python:
    # here you can config Event Editor to your game
    # default images config
    addBGs('images/bgs')
    addEVs('images/events')
    addChs('images/characters')

    # example of adding character(EE speaker):
    somebody = Character("Somebody")
    speakers["Somebody"] = somebody

    #change this if you want add EE as mod to your game
    EE_as_mod = False
    EE_edit_main_plot = True


    # enable/disable DSE(Dating Sim Engine) support in Event Editor
    # this is alpha don't work now do set to True
    EE__DSEmodule_active = True
    
    #DSE config example
    EE__DES_possible_conditions_list = [
                                        possible_condition('Lucky','lucky','number'),
                                        possible_condition('Cash', 'cash', 'number')
                                        ]

    EE__DSE_group_list = [
                        'cafeteria','class','library'
                        ]

    if EE_as_mod:
        persistent.mod_trigger__EE = True
        mod_list.insert(0,('Event Editor','Editor','2.6.3','??','stable','persistent.mod_trigger__EE'))

        persistent.mod_custom_new_game = "EE__newgameStart"

label EE__newgameStart:
    menu:
        "Enter the event editor":
            jump EE__start
        "See the event you created with the Event Editor":
            jump EE__watch_event_list
        "Start a new game":
            jump new_game
