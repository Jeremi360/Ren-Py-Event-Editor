label EEout_test_two:
    scene test bg uni
    show  sylvie normal at Position(xanchor=0.5,xpos=0.000000)
    "You see girl run to you."

    show  sylvie smile at Position(xanchor=0.5,xpos=0.500000)
    girl "Hi! I'm Sylvie. I want to make Visual Novels."

    menu:
        "How do you know that I like vn?":
            scene test bg uni
            show  sylvie surprised at Position(xanchor=0.5,xpos=0.500000)
            sylvie "Do you realy want to know?"

            "You" "Yes."

            sylvie "Okey, go with me."

            scene test bg club
            "After few seconds you stand before some door. You can swear that you never before see them on your campus."

            sylvie "You will know everything when you step out throught this door."

            hide  sylvie surprised
            "Sylvie will go after you."

            "You reach handle."

            scene tango Red
            "But suddenlly you fell pain in you head."

            scene Black
            "Blackout."

            scene test bg meadow
            "You weake up on some meadow near you study camp."

            scene Black
            "You never see Sylvie again."

            "The End"

        "I like visual novels too.":
            scene test bg uni
            show  sylvie giggle at Position(xanchor=0.5,xpos=0.500000)
            sylvie "Do you want do to some visual novel with me?"

            "You" "Yes."

            sylvie "Ok, but it depends from wath vns are for you."

            menu:
                "Internet and vn are for ...":
                    scene test bg uni
                    show  sylvie surprised at Position(xanchor=0.5,xpos=0.500000)
                    "You" "... Hentai."

                    show  sylvie surprised at Position(xanchor=0.5,xpos=1.000000)
                    sylvie "What?!"
                    "She run a way"

                    scene Black
                    hide  sylvie surprised
                    "THE END."

                "beautiful and funny stories":
                    scene test bg uni
                    show  sylvie smile at Position(xanchor=0.5,xpos=0.500000)
                    sylvie         "Ok, wait for a moment."

                    show  sylvie smile at Position(xanchor=0.5,xpos=1.000000)
                    "She run some where."

                    hide  sylvie smile
                    "You wait, ..."

                    " ... wait ..."

                    "... and wait."

                    show  sylvie green smile at Position(xanchor=0.5,xpos=0.500000)
                    "Finally she cameback."

                    "You" "Why you change your dress?"

                    sylvie "What?"

                    developer "I just borow this sprites for 'The Question' that came with Ren'Py. "

                    "You" "Nevermind. What is this notebook for?"

                    sylvie "I write here some ideas for vns."

                    sylvie "Let pick to together idea for our first vn!"

                    scene Black
                    hide  sylvie green smile
                    "You both lived happliy ever after creating vns together."

                    "THE END"

    return
