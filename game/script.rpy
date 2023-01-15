# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define nem = Character("Nemmy")

default Name = "Isaac"

default Pron = None

#I like people. A lot.

default SubjectPron = None
default ObjectPron = None
default PossessiveAdj = None
default PossessivePron = None
default ReflexsivePron = None
default SVerbAgree = None
default ESVerbAgree = None
default IESVerbAgree = None
default ISARE = None
default DODOES = None
default GOGOES = None
default HASHAVE = None

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    menu:
        "He / Him":
            jump PHim
        "She / Her":
            jump PHer
        "They / Them":
            jump PThem

    label PHim:
    $ Pron = "Him"
    $ SubjectPron = "he"
    $ ObjectPron = "him"
    $ PossessiveAdj = "his"
    $ PossessivePron = "his"
    $ ReflexsivePron = "himself"
    $ SVerbAgree = "s"
    $ ESVerbAgree = "es"
    $ IESVerbAgree = "ies"
    $ ISARE = "is"
    $ DODOES = "does"
    $ GOGOES = "goes"
    $ HASHAVE = "has"
    jump PDone

    label PHer:
    $ Pron = "Her"
    $ SubjectPron = "she"
    $ ObjectPron = "her"
    $ PossessiveAdj = "her"
    $ PossessivePron = "hers"
    $ ReflexsivePron = "herself"
    $ SVerbAgree = "s"
    $ ESVerbAgree = "es"
    $ IESVerbAgree = "ies"
    $ ISARE = "is"
    $ DODOES = "does"
    $ GOGOES = "goes"
    $ HASHAVE = "has"
    jump PDone

    label PThem:
    $ Pron = "Them"
    $ SubjectPron = "they"
    $ ObjectPron = "them"
    $ PossessiveAdj = "their"
    $ PossessivePron = "theirs"
    $ ReflexsivePron = "themselves"
    $ SVerbAgree = ""
    $ ESVerbAgree = ""
    $ IESVerbAgree = ""
    $ ISARE = "are"
    $ DODOES = "do"
    $ GOGOES = "go"
    $ HASHAVE = "have"
    jump PDone

    label PDone:

    show nem angry work at center
    nem "We're {i}best{/i} friends is what we are! Or, we were, until [SubjectPron] left because of [PossessiveAdj]..."
    show mc sad at right
    show nem sad work at center
    nem "...'Complications'..."
    show nem happy work at center
    nem "...Honestly, I never thought I'd hear from [Name] again, and yet here [SubjectPron] [ISARE]! It's like a miracle!"

    label ch4_08_done:

    return
