#######VERSION: 2.1
#
#DON'T TOUCH:
#Code needed to capture the input text everytime the page changes.

init -2 python:


    class GetText(Action):
        def __init__(self,screen_name,input_id):
            self.screen_name=screen_name
            self.input_id=input_id
        def __call__(self):
            if renpy.get_widget(self.screen_name,self.input_id):
                return str(renpy.get_widget(self.screen_name,self.input_id).content)



###################################################################################################
###################################################################################################
#
#screens
#
###################################################################################################
###################################################################################################


#screen to start a new event.
screen new_tutorial_menu:
    vbox:
        xalign 0.5
        yalign 0.5
        textbutton _("New Project: simple") action  [SetVariable("project_kind","simple"),Jump("new_project")]
        null height 50
        textbutton _("New Project: with branches") action  [SetVariable("project_kind","map"),Jump("new_project")]
        null height 50
        textbutton _("Tutorial") action  Jump("EE_tutorial")

#
#This is the main screen of the Event Editor. The one you will see all the time while editing.
#

screen event_window:
    imagemap:
        ground BG_temp
        #yanchor -config.screen_height
        #xalign 0.5


    if char_onscreen_temp0!="":
        add char_onscreen_temp0 xanchor 0.5 xpos position_temp_char0 yalign 1.0
    if char_onscreen_temp1!="":
        add char_onscreen_temp1 xanchor 0.5 xpos position_temp_char1 yalign 1.0
    if char_onscreen_temp2!="":
        add char_onscreen_temp2 xanchor 0.5 xpos position_temp_char2 yalign 1.0

    if project_kind=="map":
        textbutton _("MAP") action [GetText("event_window","input"),SetVariable('sel_act',"out")] xalign 1.0
    else:
        textbutton _("Event Menu") action [GetText("event_window","input"),ShowMenu("project_main_menu")] xalign 1.0

    vbox:
        hbox:
            textbutton _("Speaker") action Show('speaker_selection') xminimum 120
            textbutton _("Base BG") action Show('BG_base_selection')  xminimum 120
            textbutton _("BG") action Show('BG_selection') xminimum 120
            textbutton _("EV") action Show ('EV_bg_selection') xminimum 120
            textbutton _("Characters") action Show ('character_selection') xminimum 120
            textbutton _("Comments") action ShowMenu ('comments_screen') xminimum 120
        hbox:
            text _("page [page]/[minievent_temp.totalpages]") min_width 120  text_align 0.5
            textbutton _("<-1<") action If(page>1,[GetText("event_window","input"),SetVariable("pagechange",-1)]) xminimum 80
            textbutton _(">+1>") action [GetText("event_window","input"),SetVariable("pagechange",1),If(page==minievent_temp.totalpages,SetVariable('sel_act',"addpage2"))] xminimum 80
            textbutton _("<-10<") action If(page-10>0,[GetText("event_window","input"),SetVariable("pagechange",-10)]) xmaximum 80
            textbutton _(">+10>") action If(page+10<=minievent_temp.totalpages,[GetText("event_window","input"),SetVariable("pagechange",10)]) xmaximum 80
            textbutton _("AddPage") action [GetText("event_window","input"),SetVariable('sel_act',"addpage1")] xminimum 120
            textbutton _("RemovePage") action [GetText("event_window","input"),SetVariable('sel_act',"removepage")] xminimum 120

    window:
        has vbox
        python:
            try:
                ui.text(eval(speaker_temp).name,color=eval(speaker_temp).who_args["color"])
            except:
                ui.text(speaker_temp)
        input id "input" default minievent_temp.page_text[page]

screen comments_screen:
    imagemap:
        ground "images/bgs/start/code.png"

    vbox:
        yfill True
        viewport:
            ymaximum 400
            scrollbars "vertical"
            draggable True
            mousewheel True
            vbox:
                spacing 10
                for ii in range(1,minievent_temp.totalpages+1):
                    if minievent_temp.comments[ii]!='':
                        $ ui.text ("PAGE "+str(ii)+" : "+minievent_temp.comments[ii])

        hbox:
            xalign 0.5
            yalign 0.5
            textbutton _('delete comment') action If(minievent_temp.comments[page]!='',Jump('delete_comment')) xminimum 200
            textbutton _('change comment') action ui.callsinnewcontext('change_comment') xminimum 200
            null width 50
            textbutton _('return') action Return() xminimum 200

        window:
            text minievent_temp.comments[page]



###################################################################################################
###################################################################################################
#
#labels
#
###################################################################################################
###################################################################################################


#
#
#The label you need to point to  start the event editor.
#


label EE_start:
    "This is an Event Editor, have fun!"

    call screen new_tutorial_menu

    return



#
#
#When you start to write a new event:
#

label new_project:
    $ project_name=renpy.input("Write a name for the event","test")
    if project_name=="":
        "You must write a name for the event"
        jump new_project
    elif project_kind=="map":
        jump EE_map
    else:
        $ minievent_list[project_name]=minievent(project_name,project_name,False)
        $ minievent_temp=minievent_list[project_name]
        $ page=1
        $ pagechange = 0
        $ sel_act=""
        $ BG_temp = "black"
        $ speaker_temp='narrator'
        $ c_position="0"
        $ char_expressions=[""]
        $ char_onscreen_temp0=""
        $ char_onscreen_temp1=""
        $ char_onscreen_temp2=""
        $ char_nu_temp = 0
        $ position_temp_char0= 0
        $ position_temp_char1= 0
        $ position_temp_char2= 0
        jump event_editor
    return




label insert_pos_manually:
    if char_nu_temp == 0:
        $ position_temp_char0 = float(renpy.input("Write the xpos (remember it must be a float number):",allow=",.0123456789"))
    if char_nu_temp == 1:
        $ position_temp_char1 = float(renpy.input("Write the xpos (remember it must be a float number):",allow=",.0123456789"))
    if char_nu_temp == 2:
        $ position_temp_char2 = float(renpy.input("Write the xpos (remember it must be a float number):",allow=",.0123456789"))
    return


label insert_speaker_manually:
    $ speaker_temp = "\""+renpy.input("Write who is speaking:")+"\""
    return

label change_comment:
    $ minievent_temp.comments[page] = renpy.input("Change the comment:",default=minievent_temp.comments[page])
    return

label delete_comment:
    $ minievent_temp.comments[page] = ''
    return

label change_project_name:
    $ project_name=renpy.input("Write a name for the event",default=project_name)
    if project_name=="":
        "You must write a name for the event"
        jump change_project_name
    return

#
#This code is looped every time you change page while editing. It is needed to save all the variable modified and to update them for the new page.
#

label event_editor:


    label event_editor_repeat:
    $ minievent_temp.page_text[page]=renpy.call_screen("event_window")
    if sel_act=="addpage1":
        $ sel_act=""
        $ minievent_temp.totalpages +=1
        $ minievent_temp.page_text.insert(page,"")
        $ minievent_temp.speaker.insert(page,'narrator')
        $ minievent_temp.char_onscreen.insert(page,["","",""])
        $ minievent_temp.char_position.insert(page,[0,0,0])
        $ BG_temp=minievent_temp.BG[page]
        $ minievent_temp.BG.insert(page,"black")
        $ minievent_temp.comments.insert(page,"")
    elif sel_act=="addpage2":
        $ sel_act=""
        $ minievent_temp.totalpages +=1
        $ minievent_temp.page_text.append("")
        $ minievent_temp.speaker.append('narrator')
        $ minievent_temp.BG.append(BG_temp)
        $ minievent_temp.char_onscreen.append([char_onscreen_temp0,char_onscreen_temp1,char_onscreen_temp2])
        $ minievent_temp.char_position.append([position_temp_char0,position_temp_char1,position_temp_char2])
        $ minievent_temp.comments.append("")
    elif sel_act=="removepage":
        menu:
            "Are you sure you want to delete this page?"

            "YES":
                $ sel_act=""
                $ minievent_temp.totalpages -=1
                $ minievent_temp.page_text.pop(page)
                $ minievent_temp.speaker.pop(page)
                $ minievent_temp.BG.pop(page)
                $ minievent_temp.char_onscreen.pop(page)
                $ minievent_temp.char_position.pop(page)
                $ minievent_temp.comments.pop(page)
                if page>minievent_temp.totalpages:
                    $ page -= 1
                $ BG_temp=minievent_temp.BG[page]
                $ speaker_temp=minievent_temp.speaker[page]
                $ [char_onscreen_temp0,char_onscreen_temp1,char_onscreen_temp2] = minievent_temp.char_onscreen[page]
                $ [position_temp_char0,position_temp_char1,position_temp_char2] = minievent_temp.char_position[page]
            "NO":
                $ sel_act=""
    $ minievent_temp.char_onscreen[page]=[char_onscreen_temp0,char_onscreen_temp1,char_onscreen_temp2]
    $ minievent_temp.char_position[page]=[position_temp_char0,position_temp_char1,position_temp_char2]
    $ minievent_temp.BG[page]=BG_temp
    $ minievent_temp.speaker[page]=speaker_temp
    $ page += pagechange
    $ BG_temp=minievent_temp.BG[page]
    $ speaker_temp=minievent_temp.speaker[page]
    $ [char_onscreen_temp0,char_onscreen_temp1,char_onscreen_temp2] = minievent_temp.char_onscreen[page]
    $ [position_temp_char0,position_temp_char1,position_temp_char2] = minievent_temp.char_position[page]
    $ pagechange = 0
    if sel_act=='out':
        $ sel_act=""
        scene
        hide screen sc
        hide screen event_main_menu
        if project_kind=="map":
            jump EE_map_repeat

    jump event_editor_repeat

#
#
#The code that runs to export the event and create the output file. It should be created in the same folder as the .exe
#

label exporting_project:
    python:
        target = renpy.loader.transfn("events/")
        target = open(target + project_name + ".rpy",'w+')
        ind=''
        n_ind=1
        ind=indentation(n_ind)
        target.write("label "+project_name+":\n")
        if project_kind=="map":
            export(minievent_list['beginning'],n_ind)
        else:
            export(minievent_list[project_name],n_ind)
        target.write("    return")
        target.close()
    return



init python:
    def export_scene(minievent_temp,ind):
        for xx in range(1,minievent_temp.totalpages+1):
            if minievent_temp.BG[xx-1]!=minievent_temp.BG[xx]:
                target.write(ind+"scene "+minievent_temp.BG[xx]+"\n")
            for yy in range(3):
                if minievent_temp.char_onscreen[xx][yy]!=minievent_temp.char_onscreen[xx-1][yy] or (minievent_temp.char_position[xx][yy]!=minievent_temp.char_position[xx-1][yy] and minievent_temp.char_onscreen[xx][yy]!=""):
                    if minievent_temp.char_onscreen[xx][yy]=="":
                        target.write(ind+"hide "+minievent_temp.char_onscreen[xx-1][yy]+"\n")
                    else:
                        target.write(ind+"show "+minievent_temp.char_onscreen[xx][yy]+" at Position(xanchor=0.5,xpos=%f) \n" % minievent_temp.char_position[xx][yy])
            if minievent_temp.speaker[xx]!='narrator':
                target.write(ind+minievent_temp.speaker[xx])
            target.write(" \""+minievent_temp.page_text[xx]+"\"\n")
            if minievent_temp.comments[xx]!='':
                target.write(ind+" # "+minievent_temp.comments[xx])
            target.write("\n")    #not sure +ind
        return


    def export(minievent_temp,n_ind):
        ind=indentation(n_ind)
        if minievent_temp.type=='normal':
            export_scene(minievent_temp,ind)
            if minievent_temp.branch!=False:
                export(minievent_list[minievent_temp.branch[0]],n_ind)
        elif minievent_temp.type=='branch':
            target.write(ind+'menu:\n')
            n_ind+=2
            for ii in range(len(minievent_temp.branch)):
                target.write('    '+ind+'"'+minievent_temp.branching_text[ii]+'":\n')
                export(minievent_list[minievent_temp.branch[ii]],n_ind)
            n_ind-=2
            if minievent_temp.branch_end!=False:
                export(minievent_list[minievent_temp.branch_end[0]],n_ind)
        return


    def indentation(n_ind):
        ind=''
        for ii in range(n_ind):
            ind+='    '
        return ind


label EE_tutorial:
    scene images/bgs/start/code.png
    'In the Event Editor each "page" correspond to "one click" in game.'
    'VERY IMPORTANT: The editor does not notice that you have modified a page until you "change page". So when you are going to EXPORT or SAVE the event, you should change page before doing so, this way you can be sure that your modifications are remembered.'
    'TEXT' 'When you start the Event Editor you will have the possibility to write the text that you want to show in this window you are reading now. You can input the text in this very same window. It can be both dialogue or narration text. There are just a a couple thing you have to remember.'
    'TEXT' 'You cannot write on a newline in the Event Editor. To do that you have to write "\\ n" (without the space in the middle) : when the event is shown in game, the text after "\\ n" will be shown on a new line. \nAlso remember that there is no need of space after the n: "Hi. \\ nHow are you?". No space between "\\ n" and "How".'
    'SPEAKER' 'Select this button in the top-left part of the screen to choose wich name will be shown as the "speaker" of dialogue line. Select "none" if you are going to write a narration text.\nAnd there is also a "WRITE NEW" option to let you use a name that is not in the premade list.'
    'CHARACTER' 'Select this to show some character on the screen. You can manage a max of three character on the screen at the same time. They will be "char1", "char2" and "char3". Use the bar or the numbered buttons to decide the character\'s horizontal position. You can also press the button under the bar, on the left, to input the position yourself (it must be a number between 0 and 1)'
    'CHARACTER' 'Under the position bar you will see some buttons with names on them. Choose wich character you want to display on the screen. On the right there will be other buttons with numbers: each number corrispond to a different face expression, body position or dress for the selected character.'
    'BACKGROUND' 'Select the BG button and you will have the list of background options.'
    'COMMENTS' 'This open a new screen. In this screen you can add a comment for the page you were working on (you can also delete it). The comment will also be present in the EXPORTED code, after a \# so that anyone can see that comment when working on the code.\nAlso from this screen you can see all the comments of the current event.Use this option to remind yourself something or to give some info to anyone that will work on the exported code.'
    'MENU' 'This button is in the top-right part of the screen. In this menu there are other option to modify your event.'
    'EXPORT EVENT' 'Very easy to use. Just push the button. Then, in the same folder as the .exe, you will find a file named <project_name>.rpy. \nThat is the code for your event.'
    'SAVE&LOAD' 'If you want to save your work, you can do so with the normal SAVE system. Just press "ESC", you will enter the game main menu and here you can save as if you were simply playing the game. To LOAD and contiue modifing your event just use the LOAD option.'
    return
