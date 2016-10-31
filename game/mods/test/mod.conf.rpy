# this is example config mod to develop with Ren'Py Event Editor
init -20 python:
    sylvie = Character("Sylvie", color = "#e65fc8")
    speakers["sylv"] = sylvie

    you =  Character("You")
    speakers["you"] = you

    test_mod = "test"
    test_mp = "mods/"+ test_mod
    addBGs(test_mp + '/imgs/bgs', "test bg")
    #addEVs(test_mp + '/imgs/events', "test env")
    addChs(test_mp + '/imgs/sprites')

    mods[test_mod] = "test_start"

label test_start:
    developer "This is just example of mod develop with Ren'Py Event Editor"
    menu:
        "0 Choices story":
            jump EEout_test_zero
        "2 Choices stroy":
            jump EEout_test_two

    return
