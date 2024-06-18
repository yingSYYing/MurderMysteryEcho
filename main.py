import tkinter as tk
import time

#MURDER MYSTERY 

CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 720
root = tk.Tk()
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
canvas.pack()

BOX_HEIGHT = 120
BOX_WIDTH = 950

textc = "grey"
textf = "Times New Roman"
font = 15

MAIN_INDENT = 100
INDENT_X = 40
MAIN_MID_Y = (CANVAS_HEIGHT - 2 * MAIN_INDENT) / 2 - font / 2

mainx1 = MAIN_INDENT
mainx2 = CANVAS_WIDTH - MAIN_INDENT
mainy1 = 1.5*MAIN_INDENT
mainy2= CANVAS_HEIGHT - mainy1
StartBoxX = CANVAS_WIDTH / 2 - 1.5*mainx1
StartBoxY = mainy2 - MAIN_INDENT
StartBoxX2 = CANVAS_WIDTH / 2 + 1.5*mainx1
StartBoxY2 = mainy2 - MAIN_INDENT/2


choice_box_width = 240
norm_indent = 20
choice_box_height = 80

coords3X = norm_indent + norm_indent + choice_box_width 
coords4X = coords3X + 240 + 2*(norm_indent)

caraDavid1 = False
firaEvie1 = False
Jasper1 = False
Rupert1 = False
Group5 = False
Annabeth1 = False
Butler1 = False
Body1 = False

knife1 = False
head1 = False
pillar1 = False
pedestal1 = False
vase1 = False
wound1 = False
chest1 = False
weapon1 = False
kitchen1 = False

Evie2 = False
Jasper2 = False
Group2 = False
caraDavid2 = False
Annabeth2 = False

scene1_1_ = False
scene1_2_ = False
scene1_3_ = False
Conclusion1 = False
scene2_1_ = False
scene2_2_ = False
scene2_3_ = False
scene2_4_ = False
Conclusion2 = False
scene3_1_ = False
scene3_2_ = False
Conclusion3 = False
scene4_1_ = False
scene4_2_ = False
scene4_3_ = False
scene4_4_ = False
scene4_5_ = False
scene4_6_ = False
scene4_7_ = False
scene4_8_ = False
scene4_9_ = False
Conclusion4 = False
scene5_1_ = False
scene5_2_ = False
Conclusion5 = False


custom_colors = {
    "light_blue": "#ADD8E6",
    "light_yellow": "#FFFFE0",
    "light_green": "#90EE90",
    "light_pink": "#FFB6C1",
    "light_gray": "#D3D3D3",
    "light_red": "#f0847d",
}

scene_colors = {
    "main_menu": "white",  # Example color for main menu
    "scene1": custom_colors["light_blue"],  # Example color for scene 1
    "scene1_stove_on": custom_colors["light_green"],  # Example color for scene 1 after "stove on" dialogue
    "scene3": custom_colors["light_pink"],
    "retry": custom_colors["light_red"],
}

def set_background_color(scene, color=None):
    if color:
        canvas.config(bg=color)
    else:
        canvas.config(bg=scene_colors.get(scene, "white"))

# def set_background_color(scene, color):
#     canvas.configure(bg=color)

def box(x1, y1, x2, y2, fill="white"):
    return canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline="black")

def text(x1, y1, content, font_size, width):
    return canvas.create_text(x1, y1, text=content, font=(textf, font_size), anchor="nw", width=width)

def Straightline(x1, y, x2):
    return canvas.create_line(x1, y, x2, y, fill="black", width=5)

def DialogueBox():
    nameBox = box(3, CANVAS_HEIGHT - 280, CANVAS_WIDTH, CANVAS_HEIGHT)
    sepLine = Straightline(3, CANVAS_HEIGHT-3*(280/4), CANVAS_WIDTH)

def NPCText(name, dialogue):
    NPC = canvas.create_text(CANVAS_WIDTH - MAIN_INDENT + 50, CANVAS_HEIGHT - 270, text=name, font=(textf, 32, "bold"), anchor="ne", tags = "dialogue_text")
    NPCTalk = canvas.create_text(20, CANVAS_HEIGHT - 180, text=dialogue, font=("Century", 20), anchor="nw", width=CANVAS_WIDTH - 40, tags = "dialogue_text")

def PlayerText(name, dialogue):
    Player = canvas.create_text(MAIN_INDENT, CANVAS_HEIGHT - 270, text=name, font=(textf, 32, "bold"), anchor="nw", tags = "dialogue_text")
    PlayerTalk = canvas.create_text(20, CANVAS_HEIGHT - 180, text=dialogue, font=("Century", 20), anchor="nw", width=CANVAS_WIDTH - 40, tags = "dialogue_text")

def transition(x, y, x2, y2, action, item2):
    def on_click(event):
        click_x, click_y = event.x, event.y
        if x <= click_x <= x2 and y <= click_y <= y2:
            # canvas.itemconfig(item, fill="light grey")
            canvas.itemconfig(item2, fill="light grey")
            canvas.update()

            # Delay for a short period to indicate click feedback
            time.sleep(0.2)

            # Reset button color to its original color
            # canvas.itemconfig(item, fill="black")
            canvas.itemconfig(item2, fill="white")
            canvas.update()

            canvas.delete("all")
            time.sleep(0.4)
            action()
    return on_click

def mainmenu():
    set_background_color("main_menu")

    global mainx1, mainx2, mainy1, mainy2, StartBoxX, StartBoxY, StartBoxX2, StartBoxY2

    mainx1 = MAIN_INDENT
    mainx2 = CANVAS_WIDTH - MAIN_INDENT
    mainy1 = 1.5*MAIN_INDENT
    mainy2= CANVAS_HEIGHT - mainy1
    StartBoxX = CANVAS_WIDTH / 2 - 1.5*mainx1
    StartBoxY = mainy2 - MAIN_INDENT
    StartBoxX2 = CANVAS_WIDTH / 2 + 1.5*mainx1
    StartBoxY2 = mainy2 - MAIN_INDENT/2

    mainbox = box(mainx1, mainy1, mainx2, mainy2)
    font = 36

    maintext = canvas.create_text(
        mainx1 + mainx1 / 4, 
        mainy1 + MAIN_INDENT / 2, 
        text="WELCOME TO:", 
        font=("Bookman Old Style", 28, "italic"), 
        width=840, 
        anchor="nw"
    )

    maintext2 = canvas.create_text(
        mainx1 + mainx1 / 4, 
        mainy1 + MAIN_INDENT + 80, 
        text="ECHO: A VOICE UNHEARD", 
        font=("Algerian", 50, "bold underline"), 
        fill="darkred", 
        width=840, 
        anchor="nw"
    )

    # Create the author text
    maintext3 = canvas.create_text(
        mainx1 + mainx1 / 4,  
        mainy1 + 2 * MAIN_INDENT + 150, 
        text="By Siew Yue Ying for CIP2024", 
        font=("Bookman Old Style", 24, "bold italic"), 
        width=840, 
        anchor="nw"
    )
    maintext = text(mainx1 + mainx1/4, mainy1 + MAIN_INDENT/2, "CODE IN PLACE FINAL PROJECT", font, 840)
    maintext = text(mainx1 + mainx1/4, mainy1 + MAIN_INDENT + font, "BY SIEW YUE YING", font, 840)
    startbox = box(StartBoxX, StartBoxY, StartBoxX2, StartBoxY2)
    starttext = text((mainx2 - mainx1)/2.5 + mainx1 -17, (mainy2 - mainy1)/2 + 1.8*mainy1, "CLICK TO START", 20, 800)
    

    # button = tk.Button(root, text="Click To Start", command=next_scene, font=(textf, 20))
    # button_window = canvas.create_window(CANVAS_WIDTH / 2, mainy2 - MAIN_INDENT / 2, window=button)
 
    canvas.update()
    canvas.bind("<Button-1>", transition(StartBoxX, StartBoxY, StartBoxX2, StartBoxY2, FirstScene, startbox))

def display_dialogue(dialogues, next_scene_callback): #pure dialogue only
    dialogue_index = 0

    def next_dialogue(event=None):
        nonlocal dialogue_index
        if dialogue_index < len(dialogues):
            speaker, text_content = dialogues[dialogue_index]

            canvas.delete("dialogue_text")

            if speaker == "You":
                PlayerText(speaker, text_content)
            else:
                NPCText(speaker, text_content)

            dialogue_index += 1

            if dialogue_index == len(dialogues):
                continueX = CANVAS_WIDTH - 1.8*MAIN_INDENT 
                continueY = MAIN_INDENT + 270
                continueX2 = CANVAS_WIDTH - 0.2*MAIN_INDENT
                continueY2 = MAIN_INDENT + 330
                continue_box = box(CANVAS_WIDTH - 1.8*MAIN_INDENT , MAIN_INDENT + 270, CANVAS_WIDTH - 0.2*MAIN_INDENT, MAIN_INDENT + 330, fill="white")
                continue_text = canvas.create_text(
                    CANVAS_WIDTH - MAIN_INDENT, MAIN_INDENT + 300, text="CONTINUE", font=(textf, 20), fill="black", tags="continue_button"
                )
                print(continueX)
                print(continueY)
                print(continueX2)
                print(continueY2)
                # canvas.tag_bind("continue_button", "<Button-1>", lambda event: next_scene_callback())
                canvas.bind("<Button-1>", transition(continueX, continueY, continueX2, continueY2, next_scene_callback, continue_box))

    next_dialogue()
    canvas.bind("<Button-1>", next_dialogue)
    canvas.bind("<KeyPress-space>", next_dialogue)  
    canvas.focus_set()
    canvas.update()

def transition2(event, action):

    item_id = event.widget.find_closest(event.x, event.y)[0]
    canvas.itemconfig(item_id, fill="light grey")
    canvas.update()

    # Delay for a short period to indicate click feedback
    time.sleep(0.2)

    # Reset button color to its original color
    canvas.itemconfig(item_id, fill="white")
    canvas.update()

    # Perform the action associated with the choice
    canvas.delete("all")
    time.sleep(0.4)
    action()

def display_choice(dialogues, choices): #dialogues, coords, next_scene_callback, choice
    dialogue_index = 0

    def next_dialogue(event=None):
        nonlocal dialogue_index
        if dialogue_index < len(dialogues):
            speaker, text_content = dialogues[dialogue_index]

            canvas.delete("dialogue_text")

            if speaker == "You":
                PlayerText(speaker, text_content)
            else:
                NPCText(speaker, text_content)

            dialogue_index += 1

            if dialogue_index == len(dialogues):
                time.sleep(0.1)
                for choice in choices:
                    
                    coords, choice_text, next_scene_callback = choice
                    x1, y1, x2, y2 = coords
                    choice_box = box(x1, y1, x2, y2, fill="white")
                    choice_text_id = canvas.create_text(
                        (x1 + x2) // 2, (y1 + y2) // 2, text=choice_text, font=("Bookman Old Style", 16), fill="black", tags="choice_button", width=220, anchor = 'center'
                    )
                    canvas.tag_bind(choice_text_id, "<Button-1>", lambda event, cb=next_scene_callback: cb())
                    # canvas.bind("<Button-1>", transition(x1, y1, x2, y2, next_scene_callback, choice_box))
                    canvas.tag_bind(choice_box, "<Button-1>", lambda event, action=next_scene_callback: transition2(event, action))
                    

    next_dialogue()
    canvas.bind("<Button-1>", next_dialogue)
    canvas.bind("<KeyPress-space>", next_dialogue)  
    canvas.focus_set()  
    canvas.update()



def FirstScene():
    set_background_color("scene1", custom_colors["light_blue"])
    dialogues = [
        ("", "Whitmore manor... every month, on the full moon, the heiress of the Whitmore Family would throw a soiree, inviting guests of all social classes over. It would be the talk of town for days, everyone wants to get an invite."),
        ("", "There were always notable figures in such a soiree. The Whitmore heiress, of course, then there was the lovely newly-engaged couple of the Blackwood heir and the Sinclair heiress. A contrast to them was the fierce couple only known for their arguments, of the Winston Lord and Montgomery's second daughter."),
        ("", "There was even an extremely skilled artist, sponsored by the Whitmore family themselves. Can't forget the second daughter of Beaumont, goodness knows the reputation she has. "),
        ("", "There would be scandals every time after a soiree, mostly due to a certain Beaumont daughter with her own scandal accompanying her."),
        ("You", "Looks like the one who causes the scandals, is the scandal this time."),
        ("", "A murder has been reported, and as the detective with the highest success rate in the MPS, you were sent to investigate."),

        ]

    canvas.delete("all")
    DialogueBox()

    display_dialogue(dialogues, SecondScene)
    
def SecondScene():
    
    global choice_box_height, choice_box_width, norm_indent, coords3X, coords4X
    
    dialogues = [
        ("You", "Let's take note of the situation. The victim is Gwendolyn Beaumont, 5 minutes before the end of the soiree, the butler Rupert Davies found the body, the heiress Annabeth Whitmore put the manor under lockdown."),
        ("You", "Five minutes before the end, however? Must have been a close call, either the Whitmore family is involved, someone close to them, or someone looking to put the Whitmore family in a hard place."),
        ("", "After all, if not reported, the Whitmore Family would have to sweep it under the rugs to prevent further disgrace from news getting out."),
        ("You", "Luckily or not, the body was found before any of the guests left."),
        ("", "Heiress of Whitmore and hostess of all the soirees, Annabeth Whitmore. The family butler, Rupert Davies. The artist with rumours circling about him being the hostess' half-brother, Jasper Winters."),
        ("", "Cara Montgomery and David Winston. Famous for their couple tiffs, even before they were officially engaged, I wonder what their parents were thinking, pairing those two together..."),
        ("", "The exact opposite of those two, Freyr Blackwood and Evelyn Sinclair, newly-engaged, sweet as sugar. Rumour has it that the victim was born from Sinclair's father with someone outside of Lady Sinclair."),
        ("", "(There are a good number of parties to question, as these 6 used to be close with Beaumont before they became distant. I need to have a talk with the one who found the body first)"),
    ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()
    
    choice_box_width = 240
    norm_indent = 20
    choice_box_height = 80

    # mid_indent = (CANVAS_WIDTH - 2 *(norm_indent) - 4*(choice_box_width))/4
    coords3X = norm_indent + norm_indent + choice_box_width 
    coords4X = coords3X + 240 + 2*(norm_indent)
    #width minus the two side indents, 2 box widths on the sides, divide by 4 for one indent between left and middle, middle and middle have 2 idents
    

    coords3 = [coords3X, 290, coords3X + choice_box_width, 290+choice_box_height]
    coords6 = [coords4X, 150, coords4X + choice_box_width, 150+choice_box_height]
    coords1 = [coords3X, 20, coords3X + choice_box_width , 20 + choice_box_height]
    coords2 = [coords4X, 20, coords4X + choice_box_width, 20 + choice_box_height]
    coords5 = [coords3X, 150, coords3X + choice_box_width , 150+choice_box_height]
    coords4 = [coords4X, 290, coords4X + choice_box_width , 290+choice_box_height]
    # coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]

    if(not(Rupert1)):
        next_action2 = next_action3  = next_action4 = next_action5 = next_action6 = Wait

    next_action = Butler_

    text1 = "QUESTION THE BUTLER"
    text2 = "QUESTION HOSTESS"
    text3 = "QUESTION THE ARTIST"
    text4 = "QUESTION WHISPERING GUESTS"
    text5 = "QUESTION COUPLE GLARING AT EACH OTHER"
    text6 = "QUESTION SILENT COUPLE"

    choices = [
        (coords1, text1, next_action),
        (coords2, text2, next_action2),
        (coords3, text3, next_action3),
        (coords4, text4, next_action4),
        (coords5, text5, next_action5),
        (coords6, text6, next_action6),
        # (coords7, text7, next_action7)
    ]

    display_choice(dialogues, choices)

def Wait():
    global caraDavid1, firaEvie1, Jasper1, Rupert1, Group5, Annabeth1
    dialogues = [
        ("",""),
        ("", "I need to talk with the butler first.")
    ]
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    coords1 = [coords3X, 20, coords3X + choice_box_width , 20 + choice_box_height]
    coords2 = [coords4X, 20, coords4X + choice_box_width, 20 + choice_box_height]
    coords3 = [coords3X, 290, coords3X + choice_box_width, 290+choice_box_height]
    coords4 = [coords4X, 290, coords4X + choice_box_width , 290+choice_box_height]
    coords5 = [coords3X, 150, coords3X + choice_box_width , 150+choice_box_height]
    coords6 = [coords4X, 150, coords4X + choice_box_width, 150+choice_box_height]

    # coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]

    if(not(Rupert1)):
        next_action2 = next_action3  = next_action4 = next_action5 = next_action6 = Wait

    next_action = Butler_

    text1 = "QUESTION THE BUTLER"
    text2 = "QUESTION HOSTESS"
    text3 = "QUESTION THE ARTIST"
    text4 = "QUESTION WHISPERING GUESTS"
    text5 = "QUESTION COUPLE GLARING AT EACH OTHER"
    text6 = "QUESTION SILENT COUPLE"

    choices = [
        (coords1, text1, next_action),
        (coords2, text2, next_action2),
        (coords3, text3, next_action3),
        (coords4, text4, next_action4),
        (coords5, text5, next_action5),
        (coords6, text6, next_action6),
        # (coords7, text7, next_action7)
    ]
        
    display_choice(dialogues, choices)

def Butler_():
    global caraDavid1, firaEvie1, Jasper1, Rupert1, Group5, Annabeth1, Butler1
    

    dialogues =[
            ("",""),
            ("Butler?", "You must be the detective sent by the MPS. A pleasure to have you here, I must apologize that it isn't under better circumstances."),
            ("You", "Perfectly alright, sir. Could I assume you to be Mr. Rupert Davies? Long time butler of the Whitmore family?"),
            ("Mr. Davies", "Yes, you would be correct. Long time... indeed, I even watched the Young Lady Annabeth grow up, I had entered their service when her mother was still an adolescent."),
            ("You", "An impressive amount of time! You are also the one to find the body of Miss Beaumont? Could you tell me where?"),
            ("Mr. Davies", "Indeed. It was truly a shock, I was merely patrolling the hallways as the night was coming to a close, ensuring that no one is left or lost in the manor. Her body was sprawled right outside a lavatory."),
            ("You", "A lavatory, you say? Why was it discovered so late if it was outside a lavatory?"),
            ("Mr. Davies", "In the manor, there is a lavatory that is seldomly used, at the end of a hallway. It is out of the way, thus no one venturing there to use it. It is a rather popular spot for scandals of the personal type."),
            ("You", "Do elaborate. What sort of scandals, aside from the obvious, has happened?"),
            ("Mr. Davies", "Oh, couple arguments, physical fights that must not be seen in public, emotional breakdowns, a little hide away for a few minutes."),
            ("You", "(I see...) Point me the direction, I'll find my way. And protocol must, but I do need to investigate other rooms as well."),
            ("Mr. Davies", "But of course, detective. Only the ground floor is accessible to guests. The young miss keeps the stairways gated and locked during soirees."),
            ("You", "Is that so? Have they been unlocked at any point this night?"),
            ("Mr. Davies", "None, as I am the one who holds the keys. If it was opened at any point in the night, it would make a loud creaking sound, so if you do not trust my words, feel free to ask the guests."),
            ("You", "And when was she killed? Do you have an estimate of her last seen?"),
            ("Mr. Davies", "Why, I believe she was last seen at dinner. After dinner and before the dancing commenced, everyone went off their separate ways throughout the ground floor of the manor. She would have showed up for the dance, she loves causing a fuss, but she didn't."),
            ("You", "I see. Thank you for your assistance, Mr. Davies."),
            ("", "(Interesting. Much was spoken, but not much was revealed. Only the estimated time of murder, and the location, a popular one, I wonder if any of the suspects were there? I can question him again later.)"),
    ]

    
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    coords1 = [norm_indent, 290, norm_indent + choice_box_width, 290+choice_box_height]
    coords2 = [norm_indent, 150, norm_indent + choice_box_width, 150+choice_box_height]
    coords3 = [coords3X, 20, coords3X + choice_box_width , 20 + choice_box_height]
    coords4 = [coords4X, 20, coords4X + choice_box_width, 20 + choice_box_height]
    coords5 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 150, CANVAS_WIDTH - norm_indent , 150+choice_box_height]
    coords6 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 290, CANVAS_WIDTH - norm_indent , 290+choice_box_height]
    coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]    # coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]

    text1 = "TALK TO MR. DAVIES"
    next_action = Butler_1

    if(Annabeth1):
        text2 = "TALK TO ANNABETH WHITMORE"
        next_action2 = Annabeth_1
    else: 
        text2 = "QUESTION HOSTESS"
        next_action2 = Annabeth_1

    if(Jasper1):
        text3 = "TALK TO JASPER WINTERS"
        next_action3 = Jasper_1
    else:
        text3 = "QUESTION THE ARTIST"
        next_action3 = Jasper_1

    if(caraDavid1):
        text5 = "TALK TO CARA MONTGOMERY AND DAVID WINSTON"
        next_action5 = caraDavid_1
    else:
        text5 = "QUESTION COUPLE GLARING AT EACH OTHER"
        next_action5 = caraDavid_1

    if(firaEvie1):
        text6 = "TALK TO FREYR BLACKWOOD AND EVELYN SINCLAIR"
        next_action6 = firaEvie_1
    else:
        text6 = "QUESTION THE ARTIST"
        next_action6 = firaEvie_1

    if(Group5):
        text4 = "TALK TO WHISPERING GUESTS"
        next_action4 = Group_1
    else:
        text4 = "QUESTION WHISPERING GUESTS"
        next_action4 = Group_1

    next_action7 = Wait2

    text1 = "TALK TO THE BUTLER"
    text2 = "QUESTION HOSTESS"
    text3 = "QUESTION THE ARTIST"
    text4 = "QUESTION WHISPERING GUESTS"
    text5 = "QUESTION COUPLE GLARING AT EACH OTHER"
    text6 = "QUESTION SILENT COUPLE"
    text7 = "INVESTIGATE THE BODY"

    choices = [
        (coords1, text1, next_action),
        (coords2, text2, next_action2),
        (coords3, text3, next_action3),
        (coords4, text4, next_action4),
        (coords5, text5, next_action5),
        (coords6, text6, next_action6),
        (coords7, text7, next_action7)
    ]
        
    display_choice(dialogues, choices)
    Rupert1 = True

def Butler_1():
    global caraDavid1, firaEvie1, Jasper1, Rupert1, Group5, Annabeth1, Butler1, coords3X, coords4X

    dialogues =[
        ("", ""),
        ("Mr. Davies", "Ah, young detective."),
        ("You", "Hello again, Mr. Davies. I need to ask some questions and get your statement."),
        ("Mr. Davies", "But of course!"),
        ("You", "Thank you. First off, what is your relationship with the victim? Is there anyone here that knew her?"),
        ("Mr. Davies", "Ah.... Gwendolyn Beaumont was once a good friend of young lady Annabeth. However, they grew distant when Miss Beaumont found a love for spreading rumours and eavesdropping."),
        ("You", "Eavesdropping? (Could this lead to a motive?)"),
        ("Mr. Davies", "As distasteful as it is, yes... Everyone here knows and fears Gwendolyn Beaumont, she has information that could ruin one's life."),
        ("You", "You are speaking of blackmail? Has she acted on it before?"),
        ("Mr. Davies", "Indeed I am, and yes she has. Why, I'm sure you're familiar with Lord and Lady Winston's tiffs with each other? The reason it's spread so far is because of Miss Beaumont."),
        ("You", "(Cara Montgomery and David Winston...) I remember rumours that she has a half-sister?"),
        ("Mr. Davies", "Ah, Lady Evelyn Sinclair, yes. A timid, soft-spoken, but firm young woman, why, I have never liked the way Miss Beaumont interacts with her. You are not familiar?"),
        ("You", "I have heard much. But do go on, I need to cross-check."),
        ("Mr. Davies", "Not in public, but in private, she would physically harm young Evelyn. And I do not know what she has over young Evelyn's head, that caused her to not say a single word."),
        ("Mr. Davies", "We found out when her fiance, Mr. Freyr Blackwood came to us for medical help a few years prior..."),
        ("You", "It has been going on for years?!"),
        ("Mr. Davies", "Ever since the Sinclair took her in."),
        ("You", "How awful! So you would say you knew her for long, then?"),
        ("Mr. Davies", "Yes. I was always a simple butler to her. The others knew her, my young Lady Annabeth, Lord and Lady Winston, Lady Sinclair and the Heir of Blackwood, as well as Mr. Winters."),
        ("You", "Thank you. During the period after dinner and before the dance, what were you doing and where?"),
        ("Mr. Davies", "Ah, I was busy making and serving refreshments to the guests here. I'm afraid that before my patrol near the end of the soiree, I was always here in the foyer and ballroom."),
        ("You", "You were very helpful, thank you Mr. Davies."),
        ("", "Possible motive of murder could be information. Affected before confirmed to include Cara and David and Evelyn. Medical help... goodness, what a horrible woman."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    if not(Rupert1) or not(Annabeth1) or not(Jasper1) or not(firaEvie1) or not(caraDavid1) or not(Group5):
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        if not(Annabeth1 and Jasper1 and Rupert1 and caraDavid1 and firaEvie1 and Group5):
            next_action7 = Wait2
        
        text7 = "INVESTIGATE THE BODY"

        coords1 = [norm_indent, 290, norm_indent + choice_box_width, 290+choice_box_height]
        coords2 = [norm_indent, 150, norm_indent + choice_box_width, 150+choice_box_height]
        coords3 = [coords3X, 20, coords3X + choice_box_width , 20 + choice_box_height]
        coords4 = [coords4X, 20, coords4X + choice_box_width, 20 + choice_box_height]
        coords5 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 150, CANVAS_WIDTH - norm_indent , 150+choice_box_height]
        coords6 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 290, CANVAS_WIDTH - norm_indent , 290+choice_box_height]
        coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]    # coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]
        
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7)
        ]
    elif(Annabeth1 and Jasper1 and caraDavid1 and Rupert1 and firaEvie1 and Group5): #unlock profile
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
        coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
        coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
        coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
        coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
        coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
        coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
        coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        next_action7 = Body_1
        text7 = "INVESTIGATE THE BODY"
        text8 = "PROFILES"
        next_action8 = View_Info
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
        ]

    display_choice(dialogues, choices)

def Annabeth_1():
    global caraDavid1, firaEvie1, Jasper1, Rupert1, Group5, Annabeth1, Butler1, coords3X, coords4X
    Annabeth1 = True
    dialogues =[
        ("", ""),
        ("Annabeth", "You must be Detective Dubois. I offer my apologies, I wish you could have come on better circumstances."),
        ("You", "Quite alright, heiress Whitmore. It was a shocking night for all of you, I'm sure."),
        ("Annabeth", "Indeed, I must admit, I do not feel saddened at all. You are here for my statement, are you not?"),
        ("You", "(Doesn't care much about the victim, it seems) Yes, what is your relationship to the victim? And what were you doing after dinner and before the dance?"),
        ("Annabeth", "I despise Gwendolyn. We used to be close, but she changed into a witch whose magic was her mouth. However, I never barred her from my soirees. I was planning to bar her from next one onwards."),
        ("You", "Why now?"),
        ("Annabeth", "The Beaumont family would have thrown a fit if I barred their precious daughter. But tonight, she crossed a line, I'm sure others will talk about it. Jasper Winters, she spread rumours that he is my half-brother, and yes, those rumours have already been circling, but she took it a step further."),
        ("Annabeth", "She implied that Jasper's mother was nothing but a temporary fix for his father, as a way to... make my mother jealous? I was blinded with rage to hear the rest of it. After dinner when the guests were free to roam, I indulged myself in some light wine."),
        ("You", "Did you get drunk?"),
        ("Annabeth", "Do I look or sound drunk? No, of course not, it was a mere 2 glasses. Light enough to not feel the affects, but enough to keep my mind off of it."),
        ("Annabeth", "In any case, apart from retrieving things from guest rooms, such as napkins annd scarves for some of the guests, I stayed here the entire time. I love hosting, but Gwendolyn makes it feel like torture."),
        ("You", "I see. Thank you Heiress Whitmore."),
        ("", "(That was a lot of animosity. And yet, I don't know if she could be the killer. Being a hostess does get pretty busy, wandering too far would cause a ruckus.)"),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    if not(Rupert1) or not(Annabeth1) or not(Jasper1) or not(firaEvie1) or not(caraDavid1) or not(Group5):
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        if not(Annabeth1 and Jasper1 and Rupert1 and caraDavid1 and firaEvie1 and Group5):
            next_action7 = Wait2
        
        text7 = "INVESTIGATE THE BODY"
        coords1 = [norm_indent, 290, norm_indent + choice_box_width, 290+choice_box_height]
        coords2 = [norm_indent, 150, norm_indent + choice_box_width, 150+choice_box_height]
        coords3 = [coords3X, 20, coords3X + choice_box_width , 20 + choice_box_height]
        coords4 = [coords4X, 20, coords4X + choice_box_width, 20 + choice_box_height]
        coords5 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 150, CANVAS_WIDTH - norm_indent , 150+choice_box_height]
        coords6 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 290, CANVAS_WIDTH - norm_indent , 290+choice_box_height]
        coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]    # coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]
        
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7)
        ]
    elif(Annabeth1 and Jasper1 and caraDavid1 and Rupert1 and firaEvie1 and Group5): #unlock profile
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
        coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
        coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
        coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
        coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
        coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
        coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
        coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        next_action7 = Body_1

        text7 = "INVESTIGATE THE BODY"

        text8 = "PROFILES"
        next_action8 = View_Info

        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
        ]

    display_choice(dialogues, choices)

def Jasper_1():
    global caraDavid1, firaEvie1, Jasper1, Rupert1, Group5, Annabeth1, Butler1, coords3X, coords4X
    Jasper1 = True
    dialogues =[
        ("", ""),
        ("You", "(On different circumstances, I would have loved to get a signed copy of an artwork from Jasper Winters.)"),
        ("Jasper", "Hello there, detective."), 
        ("", "(He seems extremely down, I suppose it makes sense, since there are rumours circling about him.)"),
        ("You", "Hello Mr. Winters. As you may have already guessed, I'm here to ask some questions."),
        ("Jasper", "Ask away."),
        ("You", "What is your relationship to Miss Beaumont? Does she have anything to do with the rumours about your connection to the host family? What were you doing during the time after dinner and before the dance?"),
        ("Jasper", "Hah! Loaded question, right off the start. I'll answer the third one first, the entire time, I was hiding in the pantry, stress-eating. Reason for that is directly connected to the second question."),
        ("Jasper", "True or not, the Whitmore family has sponsored me and my art, and I have been on good terms with Annabeth ever since we were children. We knew Gwendolyn from then, of course. And my, what a large change she went through."),
        ("Jasper", "If I were to compare the two versions, I would not recognise her at all. Either way, Annabeth and her family always keeps my favourite snacks in the pantry, they know I stress-eat when I am overwhelmed or upset."),
        ("Jasper", "That awful woman decided that tonight, she wanted to ruin my life, my mother's life, and attempt to damage Annabeth and her family's name. She implied my mother was nothing but a temporary fun, and implied that Annabeth's mother was a neglectful wife."),
        ("Jasper", "Awful woman, I tell you."),
        ("You", "You seem to care a lot for the Whitmore family?"),
        ("Jasper", "Well, of course! They paid for my education, my mother is living a good life thanks to them, the rumours are truth, but that doesn't mean they despise me! They sponsored my artwork and exhibitions, they are the very reason why I am where I am now!"),
        ("You", "I see. Thank you, and I am sorry for what you went through tonight."),
        ("Jasper", "It is not you who should apologize, but thank you I suppose."),
        ("", "(What hostility and what protectiveness! His loyalty to the hostess and her family is truly awe-inspiring. Potential motive could be because of tonight, if he was lying about not going out of the pantry at all. Too soon to tell.)"),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()


    if not(Rupert1) or not(Annabeth1) or not(Jasper1) or not(firaEvie1) or not(caraDavid1) or not(Group5):
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        if not(Annabeth1 and Jasper1 and Rupert1 and caraDavid1 and firaEvie1 and Group5):
            next_action7 = Wait2
        
        text7 = "INVESTIGATE THE BODY"
        coords1 = [norm_indent, 290, norm_indent + choice_box_width, 290+choice_box_height]
        coords2 = [norm_indent, 150, norm_indent + choice_box_width, 150+choice_box_height]
        coords3 = [coords3X, 20, coords3X + choice_box_width , 20 + choice_box_height]
        coords4 = [coords4X, 20, coords4X + choice_box_width, 20 + choice_box_height]
        coords5 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 150, CANVAS_WIDTH - norm_indent , 150+choice_box_height]
        coords6 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 290, CANVAS_WIDTH - norm_indent , 290+choice_box_height]
        coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]    # coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]
        
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7)
        ]
    elif(Annabeth1 and Jasper1 and caraDavid1 and Rupert1 and firaEvie1 and Group5): #unlock profile
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
        coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
        coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
        coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
        coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
        coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
        coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
        coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        next_action7 = Body_1
        text7 = "INVESTIGATE THE BODY"
        text8 = "PROFILES"
        next_action8 = View_Info
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
        ]

    display_choice(dialogues, choices)


def Group_1():
    global caraDavid1, firaEvie1, Jasper1, Rupert1, Group5, Annabeth1, Butler1
    Group5 = True
    dialogues =[
        ("", ""),
        ("", "You go around taking statements from the guests, but nothing stood out. Everyone was present at the foyer, mingling and indulging in champagne or wine. Until you came across a group of whispering guests, who looked frantic."),
        ("", "Perhaps there was something."),
        ("You", "Hello there, Ladies and Gentlemen. My sincere apologies, but I must take your statements and your location during the time aftr dinner and before the dance."),
        ("Guest 1", "My, of course."),
        ("You", "Thank you."),
        ("", "Nothing out of the ordinary so far, it resonated with the rest of the guests except for those who knew the victim personally. Even their location was the same, foyer, ballroom, drinking, mingling."),
        ("You", "You say some of the guests were jeered and talked about out loud by Miss Beaumont? Where are they now?"),
        ("Guest 2", "Oh dearie, they've left long ago, before the dinner even began. Gwendolyn Beaumont does so love to stir up entertainment. I apologize, you must have been confused when I told you about them. They left before dinner even began."),
        ("Guest 3", "Yes, why, one of them left the grounds screaming at their spouse! What a loss of decorum!"),
        ("Guest 4", "Some had to be removed from the grounds because of truths unburied by Miss Beaumont! Oh, I do wonder where she had gotten her information. Pity there's no more to be found."),
        ("", "It truly seems like the guests here only see Gwendolyn as a source of scandalous information. I wonder if I should feel sorry for her."),
        ("You", "I see. And last thing, what were you whispering about just now? (You intentionally lean in, mimicking one of those women you see sharing scandolous news together all the time, hoping it'd make them more likely to talk.)"),
        ("", "It worked, and all it caused your pride. (My colleagues better not find out about this...)"),
        ("Guest 1", "Oh it is truly distressing! You see, my dear friend, while I was in the foyer, I had wandered a bit out to find the bathroom! But you see that hallway there?"),
        ("", "She pointed at the same hallway Mr. Davies told you the body was."),
        ("Guest 1", "I heard yelling and fighting from there! Not the physical fighting, goodness me, no! Just heaps of arguing! It was truly intense!"),
        ("Guest 2", "Oh yes, I heard that too! Something about an affair? Pity, it went silent when I tried to get near it. I ran back to the foyer, didn't want whoever was arguing to think me eavesdropping, you understand?"),
        ("", "Eavesdropping... fighting... "),
        ("Guest 3", "Dearie, I wished I could've heard it, my ears are good, you see. I arrived a bit too late. But I heard something interesting from the same direction, perhaps a bit closer."),
        ("Guest 4", "Oh yes! Tell! It truly was intriguing!"),
        ("Guest 3", "Why, I was lamenting my late arrival, but my ears could hear the tail ends of a short conversation. All I heard was someone saying, 'The knives are in there', and then a bit of a clinking sound!"),
        ("You", "Clinking?"),
        ("Guest 3", "Yes! It reminded me of keys on a hoop! Intriguing, don't you think?"),
        ("You", "Very! I must thank you all for talking to me! What a joy it was!"),
        ("Guest 1", "Of course, young one!"),
        ("", "I should explore later to see what rooms are down that hallway... now, eavesdropping on fighting, there was a couple here that always argues with each other, wasn't there?"),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    if not(Rupert1) or not(Annabeth1) or not(Jasper1) or not(firaEvie1) or not(caraDavid1) or not(Group5):
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        if not(Annabeth1 and Jasper1 and Rupert1 and caraDavid1 and firaEvie1 and Group5):
            next_action7 = Wait2
        
        text7 = "INVESTIGATE THE BODY"
        coords1 = [norm_indent, 290, norm_indent + choice_box_width, 290+choice_box_height]
        coords2 = [norm_indent, 150, norm_indent + choice_box_width, 150+choice_box_height]
        coords3 = [coords3X, 20, coords3X + choice_box_width , 20 + choice_box_height]
        coords4 = [coords4X, 20, coords4X + choice_box_width, 20 + choice_box_height]
        coords5 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 150, CANVAS_WIDTH - norm_indent , 150+choice_box_height]
        coords6 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 290, CANVAS_WIDTH - norm_indent , 290+choice_box_height]
        coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]    # coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]
        
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7)
        ]
    elif(Annabeth1 and Jasper1 and caraDavid1 and Rupert1 and firaEvie1 and Group5): #unlock profile
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
        coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
        coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
        coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
        coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
        coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
        coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
        coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        next_action7 = Body_1
        text7 = "INVESTIGATE THE BODY"
        text8 = "PROFILES"
        next_action8 = View_Info
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
        ]

    display_choice(dialogues, choices)

def caraDavid_1():
    global caraDavid1, firaEvie1, Jasper1, Rupert1, Group5, Annabeth1, Butler1
    caraDavid1 = True
    dialogues =[
        ("", ""),
        ("David Winston", "Would you just suck it up and visit your cousin already? They're driving me insane, and sending more and more letters!"),
        ("Cara Montgomery", "Oh, perhaps I should ask you to visit your younger sister then?"),
        ("David", "Don't even go there. There's a difference, and perhaps you're just too cowardly to do so."),
        ("Cara", "Oh poor Lillian Winston, constantly wondering if her older brother had just forgotten her..."),
        ("David", "I would if I could! You know mother forbade me from visiting her!!"),
        ("You", "Hello there, Lord and Lady Winston. I'm sorry to interrupt your discussion but as the detective in charge, I need to take your statements."),
        ("", "They don't seem to be too worried at all about the dead body on the same floor as them."),
        ("Cara", "Oh, you, I have heard of you before, a high success rate for one so young. Go on then, take our statements."),
        ("You", "I'd like to ask you separately, if possible, Lady Winston first."),
        ("Cara", "I have no qualms about it, like I said, get on with it."),
        ("You", "What is your relationship to the victim? And where were you during the hours after dinner and before the dance?"),
        ("Cara", "Hah! That girl has quite the reputation for stirring things up, I'd wager she finally crossed the wrong person. She was on a roll tonight, did you know?"),
        ("Cara", "First Jasper, then her usual victim, little Evie, that's Evelyn to you, then she caused another guest to run away crying!"),
        ("Cara", "As if that was not enough, she seems to be set on ruining marriages tonight. Why, she had already did so to one such couple, who left the soiree screaming at each other. Annie dearest had to get her guards to escort them out."),
        ("Cara", "And what soiree isn't complete without her targeting us two. She truly was on a roll tonight, I supposed she forgot to stop and met her demise."),
        ("You", "Oh dear. That sounds like an intense night."),
        ("David", "You're right about that, what a headache that girl is."),
        ("Cara", "Oh right, you asked for my relationshp? Well, if you ask the others, they would say that she was a sweetheart before. However, I never liked her, she always had that glint in her eye, like she was hunting for something. I started to despise her after witnessing that onslaught of verbal abuse she'd treat Evie to."),
        ("You", "You seem to care a lot for Lady Sinclair?"),
        ("Cara", "Well of course! We all grew up together, including, and unfortunately, Gwendolyn. Well, we called her Gwen back then. She enjoys stirring the pot every soiree, Evie and us two are her favourite targets."),
        ("Cara", "As for what I was doing, well... we were having an argument, as usual. Me and David dearest here always argue, the day we don't would be a strange day to behold."),
        ("", "(That was a lot of information.... mostly about her hatred towards the victim. Argue hm? That location? Would serve a motive, after all, she did say Gwendolyn managed to cross the wrong person, could be today's argument...)"),
        ("You", "And you, Lord Winston?"),
        ("David", "Where do I begin... I've known Gwen the same amount of time as Cara, we met her at the same time. And depressing as it may be, us two are never far from each other so we'd have the same interactions with that woman."),
        ("David", "If ever there was someone even more insufferable than Cara Montgomery, it'd be Gwendolyn Beaumont."),
        ("Cara", "You should hold your tongue."),
        ("David", "Is speaking the truth considered criminal nowadays? What an intriguing discovery!"),
        ("Cara", "Oh, you truly are made from filth, seeing as that's all you can spill. No wonder I smell."),
        ("David", "Darling, that's all you."),
        ("You", "Okay! Please enough, just give me your statements and you can argue to your heart's content."),
        ("David", "Oh my apologies, we forgot you were there."),
        ("", "(Ouch!)"),
        ("David", "She was truly letting her filter go, tonight, every word that came out was pure venom, made to spread and ruin. Let me tell you, tonight was supposed to be Fira and Evie's, that's Freyr and Evelyn to you, special night. Freshly engaged as they are."),
        ("David", "And yet, oh heavens, Beaumont went and ruined it, her words cutting and toxic, and she was proud of it when she made dear Evie run away, crying. Positively heart-breaking, I tell you!"),
        ("David", "Evie is a sweetheart, is our circle's sweetheart. The very first time I witnessed her shed tears because of someone supposed to be her family, albeit half, I hated Gwendolyn with every fibre of my being."),
        ("Cara", "Dear detective, you'd be hard-pressed to find someone who actually liked Gwendolyn Beaumont. The guests who love gossip only use her as their source of new scandals, and if there were any surrounding her, they would turn on her with no hesitation."),
        ("David", "Indeed. As for where I was, well, like Cara said, we were arguing, as usual..."),
        ("You", "I see... that was quite a lot, thank you for your time. (I would have asked them where they were arguing, but maybe I should ask if anyone heard any arguing first. They were pretty loud just now...) "),
        ("", "If either of them was the killer, nothing showed it. They were not affected, and if one of them was the killer, the other didn't show anything. If either were the killer, them spewing hatred would not help their innocence."),
        ("", "They don't seem to be sad at all, they don't seem to care at all. They must have truly hated her. Could be a motive, but if so, why now? There must be something else, let's continue investigating."),
        ]
    if(Group5):
        dialogues += [
            ("You", "Ah just a moment!"),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    if not(Rupert1) or not(Annabeth1) or not(Jasper1) or not(firaEvie1) or not(caraDavid1) or not(Group5):
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        if not(Annabeth1 and Jasper1 and Rupert1 and caraDavid1 and firaEvie1 and Group5):
            next_action7 = Wait2
        
        text7 = "INVESTIGATE THE BODY"
        coords1 = [norm_indent, 290, norm_indent + choice_box_width, 290+choice_box_height]
        coords2 = [norm_indent, 150, norm_indent + choice_box_width, 150+choice_box_height]
        coords3 = [coords3X, 20, coords3X + choice_box_width , 20 + choice_box_height]
        coords4 = [coords4X, 20, coords4X + choice_box_width, 20 + choice_box_height]
        coords5 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 150, CANVAS_WIDTH - norm_indent , 150+choice_box_height]
        coords6 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 290, CANVAS_WIDTH - norm_indent , 290+choice_box_height]
        coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]    # coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]
        
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7)
        ]
    elif(Annabeth1 and Jasper1 and caraDavid1 and Rupert1 and firaEvie1 and Group5): #unlock profile
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
        coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
        coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
        coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
        coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
        coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
        coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
        coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        next_action7 = Body_1
        text7 = "INVESTIGATE THE BODY"
        text8 = "PROFILES"
        next_action8 = View_Info
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
        ]

    display_choice(dialogues, choices)

def caraDavid_2():
    global caraDavid1, firaEvie1, Jasper1, Rupert1, Group5, Annabeth1, Butler1
    if(Group5):
        dialogues=[
            ("", ""),
            ("You", "Lord and Lady Winston, I have further questions I need to ask"),
        ]
    else:
        dialogues = [
            ("", ""),
            ("You", "They seem to be in the heat of arguing again. Nevermind, let's question the others and then we can review the information."),
        ]
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    if not(Rupert1) or not(Annabeth1) or not(Jasper1) or not(firaEvie1) or not(caraDavid1) or not(Group5):
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        if not(Annabeth1 and Jasper1 and Rupert1 and caraDavid1 and firaEvie1 and Group5):
            next_action7 = Wait2
        
        text7 = "INVESTIGATE THE BODY"
        coords1 = [norm_indent, 290, norm_indent + choice_box_width, 290+choice_box_height]
        coords2 = [norm_indent, 150, norm_indent + choice_box_width, 150+choice_box_height]
        coords3 = [coords3X, 20, coords3X + choice_box_width , 20 + choice_box_height]
        coords4 = [coords4X, 20, coords4X + choice_box_width, 20 + choice_box_height]
        coords5 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 150, CANVAS_WIDTH - norm_indent , 150+choice_box_height]
        coords6 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 290, CANVAS_WIDTH - norm_indent , 290+choice_box_height]
        coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]    # coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]
        
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7)
        ]
    elif(Annabeth1 and Jasper1 and caraDavid1 and Rupert1 and firaEvie1 and Group5): #unlock profile
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
        coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
        coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
        coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
        coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
        coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
        coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
        coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        next_action7 = Body_1
        text7 = "INVESTIGATE THE BODY"
        text8 = "PROFILES"
        next_action8 = View_Info
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
        ]

    display_choice(dialogues, choices)

def firaEvie_1():
    global caraDavid1, firaEvie1, Jasper1, Rupert1, Group5, Annabeth1, Butler1
    firaEvie1 = True
    dialogues =[
        ("", ""),
        ("You", "(Freyr Blackwood and Evelyn Sinclair)"),
        ("You", "Lady Sinclair, Lord Blackwood, congratulations on the engagement. I am truly sorry that this happened to you. I understand she was your half-sister, Lady Sinclair."),
        ("Evelyn", "Ah.... she was..."),
        ("You", "(her voice is much softer than I would have expected! She seems as timid as a mouse... how much damage was caused by her half-sister)"),
        ("Freyr", "Apologies, detective. You should understand that it may be conflicting for my love."),
        ("", "Heavens am I glad to see an actual functioning couple in this soiree..."),
        ("You", "I understand, and I am sorry for your loss. To get to the bottom of this, I do need to take statements from both of you about your relationshp with the victim, and where you were during the period after dinner and before the dance."),
        ("Freyr", "If you would allow me-"),
        ("Evelyn", "Fira, it's okay. I'll go first."),
        ("Freyr", "My darling, are you sure? If you need a moment, I could talk first."),
        ("Evelyn", "You worry too much, dear Fira. I am fine, I will be fine. Now then, detective, where should I start..."),
        ("Evelyn", "As you must already know, she and I were... half-sisters. Father found out about her when we were children, due to the fuss kicked up by the Beaumont family, she joined us back then."),
        ("Evelyn", "She never liked me, presumably because she felt threatened by my position as true heiress to the Sinclair Family? Even though she had no claim to it."),
        ("", "(She stayed silent a bit, leaning into her fiance Freyr who wrapped an arm around her shoulders in comfort. This must be hard for her, especially if what Mr. Davies said was correct)"),
        ("You", "Take your time, Lady Sinclair."),
        ("Evelyn", "Ah... you have a good heart, detective, thank you but it is alright. Bad memories, you understand. Her treatment of me went... physical when no one was around..."),
        ("Evelyn", "I think... I truly think that she was trying to, for the lack of better words, remove me from my position."),
        ("", "Timid though she may be, she is still the heiress of the Sinclair family and that shows."),
        ("Evelyn", "I am not one for confrontations... so I do my best to avoid being alone with her. When me and Fira were in our courting period, it truly was a great freedom, as she has her own room in my home."),
        ("You", "Has she ever broken in to your room or your items?"),
        ("Evelyn", "The first few times, yes, she would break them intentionally, mess up my room. I've learnt to lock it soon enough, and any objects that is obviously mine are hidden."),
        ("You", "Your family, do they truly not know?"),
        ("Evelyn", "Well... I only have my father and the servants, I do not want to burden my father anymore than he already is. The servants are aware, and they help keep my things away from her, but they can't do much."),
        ("Evelyn", "Mr. Davies gave me medical attention one night when it got particularly bad... from then on, the servants of my house armed themselves with medical knowledge as well... father knows nothing, and I wish to keep it that way."),
        ("Evelyn", "Though not as powerful, the Beaumont Family can be a thorn in one's side."),
        ("Evelyn", "Well! You have an idea of our relationship now, as where my whereabouts... I ran away, ashamed to say I was crying, from dinner. I ran down a hallway and hid behind a pillar, crying until Fira found me. It was rather funny, actually."),
        ("Fira", "It made you laugh, but I am once again sorry for soaking your cloak in champagne..."),
        ("You", "Oh? What happened? (Seems like they were separated for awhlie before reuniting.)"),
        ("Fira", "I went to find my love, and I very literally stumbled upon her behind a pillar. She wore a cloak here, you see, and she had the hood pulled up, which scared me for a moment."),
        ("Evelyn", "Oh it's nothing to be embarrassed about! (she chuckled, at least she was no longer feeling so distressed)"),
        ("Fira", "Well it was! I startled and my champagne spilled all over her cloak. Annie was kind enough to scrounge for a cloak for Evie, as it brings her comfort, but there was none. So after that, I stuck to her as close as I could."),
        ("Fira", "Oh, and you asked about my relationship with her? Same as Evie, I resented her for always hurting Evie, though. When we were out, I always made sure that Evie was the furthest away from Gwen she could be."),
        ("Fira", "My number one priority will always be Evie, that will not change."),
        ("", "(This is sweet, both are potential motives, however. I notice they didn't give a concrete location... maybe finding some evidence will get more out of them.)"),
        ("You", "Thank you for your cooperation and time. Once again, my condolences to you, Lady Sinclair."),
        ("", "You walk away, but you could've sworn you heard a soft 'none needed'."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    if not(Rupert1) or not(Annabeth1) or not(Jasper1) or not(firaEvie1) or not(caraDavid1) or not(Group5):
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        if not(Annabeth1 and Jasper1 and Rupert1 and caraDavid1 and firaEvie1 and Group5):
            next_action7 = Wait2
        
        text7 = "INVESTIGATE THE BODY"
        coords1 = [norm_indent, 290, norm_indent + choice_box_width, 290+choice_box_height]
        coords2 = [norm_indent, 150, norm_indent + choice_box_width, 150+choice_box_height]
        coords3 = [coords3X, 20, coords3X + choice_box_width , 20 + choice_box_height]
        coords4 = [coords4X, 20, coords4X + choice_box_width, 20 + choice_box_height]
        coords5 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 150, CANVAS_WIDTH - norm_indent , 150+choice_box_height]
        coords6 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 290, CANVAS_WIDTH - norm_indent , 290+choice_box_height]
        coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]    # coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]
        
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7)
        ]
    elif(Annabeth1 and Jasper1 and caraDavid1 and Rupert1 and firaEvie1 and Group5): #unlock profile
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
        coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
        coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
        coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
        coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
        coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
        coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
        coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        next_action7 = Body_1
        text7 = "INVESTIGATE THE BODY"
        text8 = "PROFILES"
        next_action8 = View_Info
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
        ]

    display_choice(dialogues, choices)

def Annabeth_2():
    global caraDavid1, firaEvie1, Jasper1, Rupert1, Group5, Annabeth1, Butler1
    if(Group5):
        dialogues=[
            ("", ""),
            ("You", "Lord and Lady Winston, I have further questions I need to ask"),
        ]
    else:
        dialogues = [
            ("", ""),
            ("You", "They seem to be in the heat of arguing again. Nevermind, let's question the others and then we can review the information."),
        ]
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    if not(Rupert1) or not(Annabeth1) or not(Jasper1) or not(firaEvie1) or not(caraDavid1) or not(Group5):
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        if not(Annabeth1 and Jasper1 and Rupert1 and caraDavid1 and firaEvie1 and Group5):
            next_action7 = Wait2
        
        text7 = "INVESTIGATE THE BODY"
        coords1 = [norm_indent, 290, norm_indent + choice_box_width, 290+choice_box_height]
        coords2 = [norm_indent, 150, norm_indent + choice_box_width, 150+choice_box_height]
        coords3 = [coords3X, 20, coords3X + choice_box_width , 20 + choice_box_height]
        coords4 = [coords4X, 20, coords4X + choice_box_width, 20 + choice_box_height]
        coords5 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 150, CANVAS_WIDTH - norm_indent , 150+choice_box_height]
        coords6 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 290, CANVAS_WIDTH - norm_indent , 290+choice_box_height]
        coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]    # coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]
        
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7)
        ]
    elif(Annabeth1 and Jasper1 and caraDavid1 and Rupert1 and firaEvie1 and Group5): #unlock profile
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
        coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
        coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
        coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
        coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
        coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
        coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
        coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        next_action7 = Body_1
        text7 = "INVESTIGATE THE BODY"
        text8 = "PROFILES"
        next_action8 = View_Info
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
        ]

    display_choice(dialogues, choices)

def Jasper_2():
    global caraDavid1, firaEvie1, Jasper1, Rupert1, Group5, Annabeth1, Butler1
    if(Group5):
        dialogues=[
            ("", ""),
            ("You", "Lord and Lady Winston, I have further questions I need to ask"),
        ]
    else:
        dialogues = [
            ("", ""),
            ("You", "They seem to be in the heat of arguing again. Nevermind, let's question the others and then we can review the information."),
        ]
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    if not(Rupert1) or not(Annabeth1) or not(Jasper1) or not(firaEvie1) or not(caraDavid1) or not(Group5):
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        if not(Annabeth1 and Jasper1 and Rupert1 and caraDavid1 and firaEvie1 and Group5):
            next_action7 = Wait2
        
        text7 = "INVESTIGATE THE BODY"
        coords1 = [norm_indent, 290, norm_indent + choice_box_width, 290+choice_box_height]
        coords2 = [norm_indent, 150, norm_indent + choice_box_width, 150+choice_box_height]
        coords3 = [coords3X, 20, coords3X + choice_box_width , 20 + choice_box_height]
        coords4 = [coords4X, 20, coords4X + choice_box_width, 20 + choice_box_height]
        coords5 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 150, CANVAS_WIDTH - norm_indent , 150+choice_box_height]
        coords6 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 290, CANVAS_WIDTH - norm_indent , 290+choice_box_height]
        coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]    # coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]
        
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7)
        ]
    elif(Annabeth1 and Jasper1 and caraDavid1 and Rupert1 and firaEvie1 and Group5): #unlock profile
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
        coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
        coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
        coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
        coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
        coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
        coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
        coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        next_action7 = Body_1
        text7 = "INVESTIGATE THE BODY"
        text8 = "PROFILES"
        next_action8 = View_Info
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
        ]

    display_choice(dialogues, choices)

def firaEvie_2():
    global caraDavid1, firaEvie1, Jasper1, Rupert1, Group5, Annabeth1, Butler1
    if(Group5):
        dialogues=[
            ("", ""),
            ("You", "Lord and Lady Winston, I have further questions I need to ask"),
        ]
    else:
        dialogues = [
            ("", ""),
            ("You", "They seem to be in the heat of arguing again. Nevermind, let's question the others and then we can review the information."),
        ]
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    if not(Rupert1) or not(Annabeth1) or not(Jasper1) or not(firaEvie1) or not(caraDavid1) or not(Group5):
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        if not(Annabeth1 and Jasper1 and Rupert1 and caraDavid1 and firaEvie1 and Group5):
            next_action7 = Wait2
        
        text7 = "INVESTIGATE THE BODY"
        coords1 = [norm_indent, 290, norm_indent + choice_box_width, 290+choice_box_height]
        coords2 = [norm_indent, 150, norm_indent + choice_box_width, 150+choice_box_height]
        coords3 = [coords3X, 20, coords3X + choice_box_width , 20 + choice_box_height]
        coords4 = [coords4X, 20, coords4X + choice_box_width, 20 + choice_box_height]
        coords5 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 150, CANVAS_WIDTH - norm_indent , 150+choice_box_height]
        coords6 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 290, CANVAS_WIDTH - norm_indent , 290+choice_box_height]
        coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]    # coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]
        
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7)
        ]
    elif(Annabeth1 and Jasper1 and caraDavid1 and Rupert1 and firaEvie1 and Group5): #unlock profile
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
        coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
        coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
        coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
        coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
        coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
        coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
        coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        next_action7 = Body_1
        text7 = "INVESTIGATE THE BODY"
        text8 = "PROFILES"
        next_action8 = View_Info
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
        ]

    display_choice(dialogues, choices)

def Group_2():
    global caraDavid1, firaEvie1, Jasper1, Rupert1, Group5, Annabeth1, Butler1
    dialogues =[
        ("", ""),
        ("You", "I've gotten all I can from them. Let's continue questioning people, then we can review the information."),
    ]
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    if not(Rupert1) or not(Annabeth1) or not(Jasper1) or not(firaEvie1) or not(caraDavid1) or not(Group5):
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        if not(Annabeth1 and Jasper1 and Rupert1 and caraDavid1 and firaEvie1 and Group5):
            next_action7 = Wait2
        
        text7 = "INVESTIGATE THE BODY"
        coords1 = [norm_indent, 290, norm_indent + choice_box_width, 290+choice_box_height]
        coords2 = [norm_indent, 150, norm_indent + choice_box_width, 150+choice_box_height]
        coords3 = [coords3X, 20, coords3X + choice_box_width , 20 + choice_box_height]
        coords4 = [coords4X, 20, coords4X + choice_box_width, 20 + choice_box_height]
        coords5 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 150, CANVAS_WIDTH - norm_indent , 150+choice_box_height]
        coords6 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 290, CANVAS_WIDTH - norm_indent , 290+choice_box_height]
        coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]    # coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]
        
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7)
        ]
    elif(Annabeth1 and Jasper1 and caraDavid1 and Rupert1 and firaEvie1 and Group5): #unlock profile
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
        coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
        coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
        coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
        coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
        coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
        coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
        coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        next_action7 = Body_1
        text7 = "INVESTIGATE THE BODY"
        text8 = "PROFILES"
        next_action8 = View_Info
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
        ]

    display_choice(dialogues, choices)

def Wait2():
    global caraDavid1, firaEvie1, Jasper1, Rupert1, Group5, Annabeth1, Body1
    dialogues = [
        ("",""),
        ("", "Let's get everyone's statements first.")
    ]
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    if not(Rupert1) or not(Annabeth1) or not(Jasper1) or not(firaEvie1) or not(caraDavid1) or not(Group5):
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        if not(Annabeth1 and Jasper1 and Rupert1 and caraDavid1 and firaEvie1 and Group5):
            next_action7 = Wait2
        
        text7 = "INVESTIGATE THE BODY"
        coords1 = [norm_indent, 290, norm_indent + choice_box_width, 290+choice_box_height]
        coords2 = [norm_indent, 150, norm_indent + choice_box_width, 150+choice_box_height]
        coords3 = [coords3X, 20, coords3X + choice_box_width , 20 + choice_box_height]
        coords4 = [coords4X, 20, coords4X + choice_box_width, 20 + choice_box_height]
        coords5 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 150, CANVAS_WIDTH - norm_indent , 150+choice_box_height]
        coords6 = [CANVAS_WIDTH - norm_indent  - choice_box_width, 290, CANVAS_WIDTH - norm_indent , 290+choice_box_height]
        coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]    # coords7 = [(CANVAS_WIDTH - 280)/2, norm_indent + choice_box_height/2  + choice_box_height + 50, CANVAS_WIDTH - (CANVAS_WIDTH - 280)/2, norm_indent + 2*choice_box_height + 60 + 50 + choice_box_height/2 ]
        
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7)
        ]
    elif(Annabeth1 and Jasper1 and caraDavid1 and Rupert1 and firaEvie1 and Group5): #unlock profile
        if (Rupert1):
            text1 = "TALK TO MR. DAVIES"
            next_action = Butler_1

        if(Annabeth1):
            text2 = "TALK TO ANNABETH"
            next_action2 = Annabeth_2
        else: 
            text2 = "QUESTION HOSTESS"
            next_action2 = Annabeth_1

        if(Jasper1):
            text3 = "TALK TO JASPER"
            next_action3 = Jasper_2
        else:
            text3 = "QUESTION THE ARTIST"
            next_action3 = Jasper_1

        if(caraDavid1):
            text5 = "TALK TO CARA AND DAVID"
            next_action5 = caraDavid_2
        else:
            text5 = "QUESTION COUPLE ARGUING WITH EACH OTHER"
            next_action5 = caraDavid_1

        if(firaEvie1):
            text6 = "TALK TO FREYR AND EVELYN"
            next_action6 = firaEvie_2
        else:
            text6 = "QUESTION THE QUIET COUPLE"
            next_action6 = firaEvie_1

        if(Group5):
            text4 = "TALK TO WHISPERING GUESTS"
            next_action4 = Group_2
        else:
            text4 = "QUESTION WHISPERING GUESTS"
            next_action4 = Group_1

        coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
        coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
        coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
        coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
        coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
        coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
        coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
        coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        next_action7 = Body_1
        text7 = "INVESTIGATE THE BODY"
        text8 = "PROFILES"
        next_action8 = View_Info
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
        ]

        
    display_choice(dialogues, choices)

def Body_1():
    global caraDavid1, firaEvie1, Jasper1, Rupert1, Group5, Annabeth1, Butler1, Body1
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global w_indent, h_indent, width2, height2
    w_indent = 30
    h_indent = 100
    width2 = 180
    height2 = 70
    Body1 = True
    dialogues =[
        ("", ""),
        ("You", "This place really is out of the way. (You look around) A lavatory, a large window, a pillar by the corner, end of a hallway with the only way left to go is back."),
        ("", "Gwendolyn's body was lying face-up, a knife sticking out of her chest. Something was strange about it... but you could not put a finger to it."),
        ("You", "There's water all over too.... is this a shard? (You bend down and pick something off the ground near her head, careful not to cut your hand)"),
        ("You", "There's something beneath her head... and there's something spilling out from behind that pillar too..."),
        ("You", "Hmm... that pedestal over here is empty, but it has signs of worn. Something was supposed to be here."),
        ("", "(What should I investigate first?)"),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Back"  
    text2 = "Knife"
    text3 = "Back of head"
    text4 = "Behind the pillar"
    text5 = "Empty pedestal"
    coords1 = [w_indent, h_indent, w_indent + width2, h_indent+height2]
    coords2 = [2*w_indent + width2, h_indent, 2*(w_indent + width2), h_indent+height2]
    coords3 = [3*w_indent + 2*width2, h_indent, 3*(w_indent + width2), h_indent+height2]
    coords4 = [4*w_indent + 3*width2, h_indent, 4*(w_indent + width2), h_indent+height2]
    coords5 = [5*w_indent + 4*width2, h_indent, 5*(w_indent + width2), h_indent+height2]
    next_action = post_statement
    next_action2 = knife_1
    next_action3 = head_1
    next_action4 = pillar_1
    next_action5 = pedestal_1
    
    if (knife1):
        text6 = "Find, search the kitchen"
        next_action6 = kitchen_1
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]
    else:
        text6 = "Require further investigation"
        next_action6 = Wait3
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]

    if(head1):
        text7 = "Broken Vase"
        next_action7 = vase_1
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text7 = "Require further investigation"
        next_action7 = Wait3
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]

    if(head1 and vase1):
        text8 = "Head wound"
        next_action8 = wound_1
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]
    else:
        text8 = "Require further investigation"
        next_action8 = Wait3
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]

    if(wound1 and knife1 and vase1):
        text9 = "Blood on chest"
        next_action9 = chest_1
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text9 = "Require further investigation"
        next_action9 = Wait3
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]

    if(chest1 and knife1 and vase1 and wound1 and head1):
        text10 = "Murder Weapon"
        next_action10 = weapon_1
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text10 = "Require further investigation"
        next_action10 = Wait3
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    
    choices = [
        (coords1, text1, next_action),
        (coords2, text2, next_action2),
        (coords3, text3, next_action3),
        (coords4, text4, next_action4),
        (coords5, text5, next_action5),
        (coords6, text6, next_action6),
        (coords7, text7, next_action7),
        (coords8, text8, next_action8),
        (coords9, text9, next_action9),
        (coords10, text10, next_action10),
    ]

    display_choice(dialogues, choices)

def Wait3():
    global caraDavid1, firaEvie1, Jasper1, Rupert1, Group5, Annabeth1, Butler1, Body1
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global w_indent, h_indent, width2, height2
    w_indent = 30
    h_indent = 100
    width2 = 180
    height2 = 70
    Body1 = True
    dialogues =[
        ("", ""),
        ("You", "I'm missing something."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Back"  
    text2 = "Knife"
    text3 = "Back of head"
    text4 = "Behind the pillar"
    text5 = "Empty pedestal"
    coords1 = [w_indent, h_indent, w_indent + width2, h_indent+height2]
    coords2 = [2*w_indent + width2, h_indent, 2*(w_indent + width2), h_indent+height2]
    coords3 = [3*w_indent + 2*width2, h_indent, 3*(w_indent + width2), h_indent+height2]
    coords4 = [4*w_indent + 3*width2, h_indent, 4*(w_indent + width2), h_indent+height2]
    coords5 = [5*w_indent + 4*width2, h_indent, 5*(w_indent + width2), h_indent+height2]
    next_action = post_statement
    next_action2 = knife_1
    next_action3 = head_1
    next_action4 = pillar_1
    next_action5 = pedestal_1
    
    if (knife1):
        text6 = "Find, search the kitchen"
        next_action6 = kitchen_1
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]
    else:
        text6 = "Require further investigation"
        next_action6 = Wait3
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]

    if(head1):
        text7 = "Broken Vase"
        next_action7 = vase_1
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text7 = "Require further investigation"
        next_action7 = Wait3
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]

    if(head1 and vase1):
        text8 = "Head wound"
        next_action8 = wound_1
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]
    else:
        text8 = "Require further investigation"
        next_action8 = Wait3
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]


    if(wound1 and knife1 and vase1):
        text9 = "Blood on chest"
        next_action9 = chest_1
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text9 = "Require further investigation"
        next_action9 = Wait3
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]

    if(chest1 and knife1 and vase1 and wound1 and head1):
        text10 = "Murder Weapon"
        next_action10 = weapon_1
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text10 = "Require further investigation"
        next_action10 = Wait3
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    
    choices = [
        (coords1, text1, next_action),
        (coords2, text2, next_action2),
        (coords3, text3, next_action3),
        (coords4, text4, next_action4),
        (coords5, text5, next_action5),
        (coords6, text6, next_action6),
        (coords7, text7, next_action7),
        (coords8, text8, next_action8),
        (coords9, text9, next_action9),
        (coords10, text10, next_action10),
    ]

    display_choice(dialogues, choices)

def knife_1():
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global w_indent, h_indent, width2, height2
    knife1 = True
    dialogues = [
        ("", ""),
        ("You", "There's a knife sticking out of her chest, aimed for the lungs."),
    ]
    if not(kitchen1):
        dialogues += [
            ("You", "Could this have come from the kitchen?"),
        ]
    if (kitchen1):
        dialogues += [
            ("You", "It's the missing knife from the kitchen."),
        ]
    if not(chest1):
        dialogues +=[
            ("You", "Something is off about it, I'm not sure what. Further investigation is required."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Back"  
    text2 = "Knife"
    text3 = "Back of head"
    text4 = "Behind the pillar"
    text5 = "Empty pedestal"
    coords1 = [w_indent, h_indent, w_indent + width2, h_indent+height2]
    coords2 = [2*w_indent + width2, h_indent, 2*(w_indent + width2), h_indent+height2]
    coords3 = [3*w_indent + 2*width2, h_indent, 3*(w_indent + width2), h_indent+height2]
    coords4 = [4*w_indent + 3*width2, h_indent, 4*(w_indent + width2), h_indent+height2]
    coords5 = [5*w_indent + 4*width2, h_indent, 5*(w_indent + width2), h_indent+height2]
    next_action = post_statement
    next_action2 = knife_1
    next_action3 = head_1
    next_action4 = pillar_1
    next_action5 = pedestal_1
    
    if (knife1):
        text6 = "Find, search the kitchen"
        next_action6 = kitchen_1
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]
    else:
        text6 = "Require further investigation"
        next_action6 = Wait3
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]

    if(head1):
        text7 = "Broken Vase"
        next_action7 = vase_1
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text7 = "Require further investigation"
        next_action7 = Wait3
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]

    if(head1 and vase1):
        text8 = "Head wound"
        next_action8 = wound_1
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]
    else:
        text8 = "Require further investigation"
        next_action8 = Wait3
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]

    if(wound1 and knife1 and vase1):
        text9 = "Blood on chest"
        next_action9 = chest_1
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text9 = "Require further investigation"
        next_action9 = Wait3
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]

    if(chest1 and knife1 and vase1 and wound1 and head1):
        text10 = "Murder Weapon"
        next_action10 = weapon_1
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text10 = "Require further investigation"
        next_action10 = Wait3
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    
    choices = [
        (coords1, text1, next_action),
        (coords2, text2, next_action2),
        (coords3, text3, next_action3),
        (coords4, text4, next_action4),
        (coords5, text5, next_action5),
        (coords6, text6, next_action6),
        (coords7, text7, next_action7),
        (coords8, text8, next_action8),
        (coords9, text9, next_action9),
        (coords10, text10, next_action10),
    ]

    display_choice(dialogues, choices)

def head_1():
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global w_indent, h_indent, width2, height2
    head1 = True
    dialogues = [
        ("", "You lift up her head and notice that it was bloody, and lying on top of shard of stained glass, with water all over the floor."),
        ("You", "My gloves are bloodied...... But this is, it looks like someone tried cleaning it up by pushing the shards beneath the head. There's a bunch of blood here, and some shards stuck in the back of her head."),
        ("You", "Looks like a shattered vase. Must have been a nice one, and it was filled with water. Whatever plants in it must have been thrown out already."),
        
    ]
    if vase1 and not(wound1):
        dialogues += [
            ("You", "I wonder... I need to take a closer look at this wound."),
        ]
    if not(vase1 and wound1):
        dialogues += [
            ("You", "Let's take a closer look at this vase first."),
        ]      
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Back"  
    text2 = "Knife"
    text3 = "Back of head"
    text4 = "Behind the pillar"
    text5 = "Empty pedestal"
    coords1 = [w_indent, h_indent, w_indent + width2, h_indent+height2]
    coords2 = [2*w_indent + width2, h_indent, 2*(w_indent + width2), h_indent+height2]
    coords3 = [3*w_indent + 2*width2, h_indent, 3*(w_indent + width2), h_indent+height2]
    coords4 = [4*w_indent + 3*width2, h_indent, 4*(w_indent + width2), h_indent+height2]
    coords5 = [5*w_indent + 4*width2, h_indent, 5*(w_indent + width2), h_indent+height2]
    next_action = post_statement
    next_action2 = knife_1
    next_action3 = head_1
    next_action4 = pillar_1
    next_action5 = pedestal_1
    
    if (knife1):
        text6 = "Find, search the kitchen"
        next_action6 = kitchen_1
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]
    else:
        text6 = "Require further investigation"
        next_action6 = Wait3
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]

    if(head1):
        text7 = "Broken Vase"
        next_action7 = vase_1
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text7 = "Require further investigation"
        next_action7 = Wait3
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]

    if(head1 and vase1):
        text8 = "Head wound"
        next_action8 = wound_1
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]
    else:
        text8 = "Require further investigation"
        next_action8 = Wait3
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]

    if(wound1 and knife1 and vase1):
        text9 = "Blood on chest"
        next_action9 = chest_1
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text9 = "Require further investigation"
        next_action9 = Wait3
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]

    if(chest1 and knife1 and vase1 and wound1 and head1):
        text10 = "Murder Weapon"
        next_action10 = weapon_1
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text10 = "Require further investigation"
        next_action10 = Wait3
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]

    choices = [
        (coords1, text1, next_action),
        (coords2, text2, next_action2),
        (coords3, text3, next_action3),
        (coords4, text4, next_action4),
        (coords5, text5, next_action5),
        (coords6, text6, next_action6),
        (coords7, text7, next_action7),
        (coords8, text8, next_action8),
        (coords9, text9, next_action9),
        (coords10, text10, next_action10),
    ]

    display_choice(dialogues, choices)

def pillar_1():
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global w_indent, h_indent, width2, height2
    pillar1 = True
    dialogues = [
        ("", ""),
        ("You", "Hmm... some sort of liquid has been spilled behind this pillar. Someone was here, question was, before or after the murder? There's no way to find out."),
        ("", "You take a sniff, there's some sort of familiar smell coming from the liquid..."),
        ("You", "Oh! Champagne!"),
        ("You", "There's a suspect that mentioned spilling champagne, I remember."),
    ]
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Back"  
    text2 = "Knife"
    text3 = "Back of head"
    text4 = "Behind the pillar"
    text5 = "Empty pedestal"
    coords1 = [w_indent, h_indent, w_indent + width2, h_indent+height2]
    coords2 = [2*w_indent + width2, h_indent, 2*(w_indent + width2), h_indent+height2]
    coords3 = [3*w_indent + 2*width2, h_indent, 3*(w_indent + width2), h_indent+height2]
    coords4 = [4*w_indent + 3*width2, h_indent, 4*(w_indent + width2), h_indent+height2]
    coords5 = [5*w_indent + 4*width2, h_indent, 5*(w_indent + width2), h_indent+height2]
    next_action = post_statement
    next_action2 = knife_1
    next_action3 = head_1
    next_action4 = pillar_1
    next_action5 = pedestal_1
    
    if (knife1):
        text6 = "Find, search the kitchen"
        next_action6 = kitchen_1
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]
    else:
        text6 = "Require further investigation"
        next_action6 = Wait3
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]

    if(head1):
        text7 = "Broken Vase"
        next_action7 = vase_1
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text7 = "Require further investigation"
        next_action7 = Wait3
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]

    if(head1 and vase1):
        text8 = "Head wound"
        next_action8 = wound_1
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]
    else:
        text8 = "Require further investigation"
        next_action8 = Wait3
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]

    if(wound1 and knife1 and vase1):
        text9 = "Blood on chest"
        next_action9 = chest_1
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text9 = "Require further investigation"
        next_action9 = Wait3
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]

    if(chest1 and knife1 and vase1 and wound1 and head1):
        text10 = "Murder Weapon"
        next_action10 = weapon_1
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text10 = "Require further investigation"
        next_action10 = Wait3
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    
    choices = [
        (coords1, text1, next_action),
        (coords2, text2, next_action2),
        (coords3, text3, next_action3),
        (coords4, text4, next_action4),
        (coords5, text5, next_action5),
        (coords6, text6, next_action6),
        (coords7, text7, next_action7),
        (coords8, text8, next_action8),
        (coords9, text9, next_action9),
        (coords10, text10, next_action10),
    ]

    display_choice(dialogues, choices)

def pedestal_1():
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global w_indent, h_indent, width2, height2
    pedestal1 = True

    dialogues = [
        ("", ""),
    ]
    if not(vase1):
        dialogues += [
            ("You", "A pretty opulent pedestal, it's empty but it looks to be quite worn. Something was supposed to be here."),
        ]
    if (vase1):
        dialogues +=[
            ("You", "This was where that vase was supposed to stand."),
        ]
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Back"  
    text2 = "Knife"
    text3 = "Back of head"
    text4 = "Behind the pillar"
    text5 = "Empty pedestal"
    coords1 = [w_indent, h_indent, w_indent + width2, h_indent+height2]
    coords2 = [2*w_indent + width2, h_indent, 2*(w_indent + width2), h_indent+height2]
    coords3 = [3*w_indent + 2*width2, h_indent, 3*(w_indent + width2), h_indent+height2]
    coords4 = [4*w_indent + 3*width2, h_indent, 4*(w_indent + width2), h_indent+height2]
    coords5 = [5*w_indent + 4*width2, h_indent, 5*(w_indent + width2), h_indent+height2]
    next_action = post_statement
    next_action2 = knife_1
    next_action3 = head_1
    next_action4 = pillar_1
    next_action5 = pedestal_1
    
    if (knife1):
        text6 = "Find, search the kitchen"
        next_action6 = kitchen_1
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]
    else:
        text6 = "Require further investigation"
        next_action6 = Wait3
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]

    if(head1):
        text7 = "Broken Vase"
        next_action7 = vase_1
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text7 = "Require further investigation"
        next_action7 = Wait3
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]

    if(head1 and vase1):
        text8 = "Head wound"
        next_action8 = wound_1
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]
    else:
        text8 = "Require further investigation"
        next_action8 = Wait3
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]

    if(wound1 and knife1 and vase1):
        text9 = "Blood on chest"
        next_action9 = chest_1
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text9 = "Require further investigation"
        next_action9 = Wait3
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]

    if(chest1 and knife1 and vase1 and wound1 and head1):
        text10 = "Murder Weapon"
        next_action10 = weapon_1
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text10 = "Require further investigation"
        next_action10 = Wait3
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    
    choices = [
        (coords1, text1, next_action),
        (coords2, text2, next_action2),
        (coords3, text3, next_action3),
        (coords4, text4, next_action4),
        (coords5, text5, next_action5),
        (coords6, text6, next_action6),
        (coords7, text7, next_action7),
        (coords8, text8, next_action8),
        (coords9, text9, next_action9),
        (coords10, text10, next_action10),
    ]

    display_choice(dialogues, choices)

def kitchen_1():
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global w_indent, h_indent, width2, height2
    kitchen1 = True
    dialogues = [
        ("", "The kitchen is just a bit up from the hallway, in the middle of the lavatory and the entrance to the foyer."),
        ("You", "Just as I expected, the pantry is connected to the kitchen just a bit further in."),
        ("You", "Cookie crumbs in the pantry. This might be from Jasper Winters' stress-eating."),
        ("You", "Hmm.... nothing seems admist in the pantry... The kitchen..."),
        ("You", "What did that guest say they heard again? The knives are in that drawer..."),
        ("", "You open each drawer that isn't locked, hoping that the clue wasn't in any of the locked drawers. And then you find one that has obviously been touched."),
        ("You", "A knife drawer with a place that's for a missing knife! So this was where the knife came from."),
        ("You", "Jasper Winters is the most likely person to have given out the information for the knife. I'll have to question him again later."),
    ]
    
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Back"  
    text2 = "Knife"
    text3 = "Back of head"
    text4 = "Behind the pillar"
    text5 = "Empty pedestal"
    coords1 = [w_indent, h_indent, w_indent + width2, h_indent+height2]
    coords2 = [2*w_indent + width2, h_indent, 2*(w_indent + width2), h_indent+height2]
    coords3 = [3*w_indent + 2*width2, h_indent, 3*(w_indent + width2), h_indent+height2]
    coords4 = [4*w_indent + 3*width2, h_indent, 4*(w_indent + width2), h_indent+height2]
    coords5 = [5*w_indent + 4*width2, h_indent, 5*(w_indent + width2), h_indent+height2]
    next_action = post_statement
    next_action2 = knife_1
    next_action3 = head_1
    next_action4 = pillar_1
    next_action5 = pedestal_1
    
    if (knife1):
        text6 = "Find, search the kitchen"
        next_action6 = kitchen_1
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]
    else:
        text6 = "Require further investigation"
        next_action6 = Wait3
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]

    if(head1):
        text7 = "Broken Vase"
        next_action7 = vase_1
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text7 = "Require further investigation"
        next_action7 = Wait3
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]

    if(head1 and vase1):
        text8 = "Head wound"
        next_action8 = wound_1
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]
    else:
        text8 = "Require further investigation"
        next_action8 = Wait3
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]

    if(wound1 and knife1 and vase1):
        text9 = "Blood on chest"
        next_action9 = chest_1
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text9 = "Require further investigation"
        next_action9 = Wait3
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]

    if(chest1 and knife1 and vase1 and wound1 and head1):
        text10 = "Murder Weapon"
        next_action10 = weapon_1
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text10 = "Require further investigation"
        next_action10 = Wait3
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    
    choices = [
        (coords1, text1, next_action),
        (coords2, text2, next_action2),
        (coords3, text3, next_action3),
        (coords4, text4, next_action4),
        (coords5, text5, next_action5),
        (coords6, text6, next_action6),
        (coords7, text7, next_action7),
        (coords8, text8, next_action8),
        (coords9, text9, next_action9),
        (coords10, text10, next_action10),
    ]

    display_choice(dialogues, choices)

def vase_1():
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global w_indent, h_indent, width2, height2
    vase1 = True
    dialogues = [
        ("", ""),
        ("You", "I was right, it was a shattered vase. Hmm... looks like someone used it to hit Gwendolyn from the back of her head. There's a lot of blood stuck to these pieces in her skin..."),
    ]
    if not(wound1):
        dialogues += [
            ("You", "I need to take a closer at the wound."),
        ]
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Back"  
    text2 = "Knife"
    text3 = "Back of head"
    text4 = "Behind the pillar"
    text5 = "Empty pedestal"
    coords1 = [w_indent, h_indent, w_indent + width2, h_indent+height2]
    coords2 = [2*w_indent + width2, h_indent, 2*(w_indent + width2), h_indent+height2]
    coords3 = [3*w_indent + 2*width2, h_indent, 3*(w_indent + width2), h_indent+height2]
    coords4 = [4*w_indent + 3*width2, h_indent, 4*(w_indent + width2), h_indent+height2]
    coords5 = [5*w_indent + 4*width2, h_indent, 5*(w_indent + width2), h_indent+height2]
    next_action = post_statement
    next_action2 = knife_1
    next_action3 = head_1
    next_action4 = pillar_1
    next_action5 = pedestal_1
    
    if (knife1):
        text6 = "Find, search the kitchen"
        next_action6 = kitchen_1
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]
    else:
        text6 = "Require further investigation"
        next_action6 = Wait3
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]

    if(head1):
        text7 = "Broken Vase"
        next_action7 = vase_1
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text7 = "Require further investigation"
        next_action7 = Wait3
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]

    if(head1 and vase1):
        text8 = "Head wound"
        next_action8 = wound_1
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]
    else:
        text8 = "Require further investigation"
        next_action8 = Wait3
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]

    if(wound1 and knife1 and vase1):
        text9 = "Blood on chest"
        next_action9 = chest_1
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text9 = "Require further investigation"
        next_action9 = Wait3
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]

    if(chest1 and knife1 and vase1 and wound1 and head1):
        text10 = "Murder Weapon"
        next_action10 = weapon_1
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text10 = "Require further investigation"
        next_action10 = Wait3
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    
    choices = [
        (coords1, text1, next_action),
        (coords2, text2, next_action2),
        (coords3, text3, next_action3),
        (coords4, text4, next_action4),
        (coords5, text5, next_action5),
        (coords6, text6, next_action6),
        (coords7, text7, next_action7),
        (coords8, text8, next_action8),
        (coords9, text9, next_action9),
        (coords10, text10, next_action10),
    ]

    display_choice(dialogues, choices)

def wound_1():
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global w_indent, h_indent, width2, height2
    wound1 = True
    dialogues = [
        ("", ""),
        ("You", "Head wound from the back, from the way the shards stick to the back of her head, and the scratches and bruising from the impact..."),
        ("You", "Whoever used the vase to hit her on the head was taller than her."),
    ]
    if not(weapon1):
        dialogues += [
            ("You", "With the knife, however, this doesn't add up. Unless..."),
            ("You", "I need to take a look at her stab wound again."),
        ]
    if(weapon1):
        dialogues += [
            ("You", "And now I know that it's the true murder weapon, the killer is taller than her."),
        ]
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Back"  
    text2 = "Knife"
    text3 = "Back of head"
    text4 = "Behind the pillar"
    text5 = "Empty pedestal"
    coords1 = [w_indent, h_indent, w_indent + width2, h_indent+height2]
    coords2 = [2*w_indent + width2, h_indent, 2*(w_indent + width2), h_indent+height2]
    coords3 = [3*w_indent + 2*width2, h_indent, 3*(w_indent + width2), h_indent+height2]
    coords4 = [4*w_indent + 3*width2, h_indent, 4*(w_indent + width2), h_indent+height2]
    coords5 = [5*w_indent + 4*width2, h_indent, 5*(w_indent + width2), h_indent+height2]
    next_action = post_statement
    next_action2 = knife_1
    next_action3 = head_1
    next_action4 = pillar_1
    next_action5 = pedestal_1
    
    if (knife1):
        text6 = "Find, search the kitchen"
        next_action6 = kitchen_1
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]
    else:
        text6 = "Require further investigation"
        next_action6 = Wait3
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]

    if(head1):
        text7 = "Broken Vase"
        next_action7 = vase_1
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text7 = "Require further investigation"
        next_action7 = Wait3
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]

    if(head1 and vase1):
        text8 = "Head wound"
        next_action8 = wound_1
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]
    else:
        text8 = "Require further investigation"
        next_action8 = Wait3
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]

    if(wound1 and knife1 and vase1):
        text9 = "Blood on chest"
        next_action9 = chest_1
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text9 = "Require further investigation"
        next_action9 = Wait3
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]

    if(chest1 and knife1 and vase1 and wound1 and head1):
        text10 = "Murder Weapon"
        next_action10 = weapon_1
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text10 = "Require further investigation"
        next_action10 = Wait3
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    
    choices = [
        (coords1, text1, next_action),
        (coords2, text2, next_action2),
        (coords3, text3, next_action3),
        (coords4, text4, next_action4),
        (coords5, text5, next_action5),
        (coords6, text6, next_action6),
        (coords7, text7, next_action7),
        (coords8, text8, next_action8),
        (coords9, text9, next_action9),
        (coords10, text10, next_action10),
    ]

    display_choice(dialogues, choices)

def chest_1():
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global w_indent, h_indent, width2, height2
    chest1 = True
    dialogues = [
        ("", ""),
        ("You", "There's less blood here, it's stagnant, unlike the ones on her head, cleverly absorbed by the shards."),
        ("You", "The blood here is dark and coagulated too."),
        ("You", "This could only mean one thing."),
        ("You", "She was stabbed after she had died."),
    ]
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Back"  
    text2 = "Knife"
    text3 = "Back of head"
    text4 = "Behind the pillar"
    text5 = "Empty pedestal"
    coords1 = [w_indent, h_indent, w_indent + width2, h_indent+height2]
    coords2 = [2*w_indent + width2, h_indent, 2*(w_indent + width2), h_indent+height2]
    coords3 = [3*w_indent + 2*width2, h_indent, 3*(w_indent + width2), h_indent+height2]
    coords4 = [4*w_indent + 3*width2, h_indent, 4*(w_indent + width2), h_indent+height2]
    coords5 = [5*w_indent + 4*width2, h_indent, 5*(w_indent + width2), h_indent+height2]
    next_action = post_statement
    next_action2 = knife_1
    next_action3 = head_1
    next_action4 = pillar_1
    next_action5 = pedestal_1
    
    if (knife1):
        text6 = "Find, search the kitchen"
        next_action6 = kitchen_1
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]
    else:
        text6 = "Require further investigation"
        next_action6 = Wait3
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]

    if(head1):
        text7 = "Broken Vase"
        next_action7 = vase_1
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text7 = "Require further investigation"
        next_action7 = Wait3
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]

    if(head1 and vase1):
        text8 = "Head wound"
        next_action8 = wound_1
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]
    else:
        text8 = "Require further investigation"
        next_action8 = Wait3
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]

    if(wound1 and knife1 and vase1):
        text9 = "Blood on chest"
        next_action9 = chest_1
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text9 = "Require further investigation"
        next_action9 = Wait3
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]

    if(chest1 and knife1 and vase1 and wound1 and head1):
        text10 = "Murder Weapon"
        next_action10 = weapon_1
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text10 = "Require further investigation"
        next_action10 = Wait3
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    
    choices = [
        (coords1, text1, next_action),
        (coords2, text2, next_action2),
        (coords3, text3, next_action3),
        (coords4, text4, next_action4),
        (coords5, text5, next_action5),
        (coords6, text6, next_action6),
        (coords7, text7, next_action7),
        (coords8, text8, next_action8),
        (coords9, text9, next_action9),
        (coords10, text10, next_action10),
    ]

    display_choice(dialogues, choices)

def weapon_1():
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global w_indent, h_indent, width2, height2
    weapon1 = True
    dialogues = [
        ("", ""),
        ("You", "Since the blood near her chest, where the knife was, was coagulated and minimal compared to the back of her head, most of which was absorbed by the countless amount of glass shards from the broken vase."),
        ("You", "It's obvious now, the murder weapon was not the knife, as most observers would be led to believe at first glance."),
        ("You", "It was the broken vase. That means the killer was the one who used the vase to hit her from behind the head, taller than her too, judging from the wound."),
        ("You", "But where does the knife come in? This doesn't look planned, it looks panicked, in fact."),
        ("You", "The murderer must have acted on impulse, driven by some negative emotion. And according to the guest, shortly after the yelling stopped, was when they heard someone talking about the knives."),
        ("You", "Two scenarios, either the murderer thought fast and went to get something to deflect attention from the actual weapon. Or someone was helping the murderer hide the body."),
        ("You", "Who was here? Gwen, obviously. Jasper in the pantry. Then the argument, Cara and David, and then the champagne, Evelyn, followed soon after by Freyr."),
        ("You", "Arguments.... Cara and David. Evelyn and Gwen, maybe? I need information from Jasper about who went into the kitchen."),
        ("You", "And then there's the possibiltiy of Annabeth Whitmore too..."),
        ("You", "I'm close, yet still so far."),
    ]
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Back"  
    text2 = "Knife"
    text3 = "Back of head"
    text4 = "Behind the pillar"
    text5 = "Empty pedestal"
    coords1 = [w_indent, h_indent, w_indent + width2, h_indent+height2]
    coords2 = [2*w_indent + width2, h_indent, 2*(w_indent + width2), h_indent+height2]
    coords3 = [3*w_indent + 2*width2, h_indent, 3*(w_indent + width2), h_indent+height2]
    coords4 = [4*w_indent + 3*width2, h_indent, 4*(w_indent + width2), h_indent+height2]
    coords5 = [5*w_indent + 4*width2, h_indent, 5*(w_indent + width2), h_indent+height2]
    next_action = post_statement
    next_action2 = knife_1
    next_action3 = head_1
    next_action4 = pillar_1
    next_action5 = pedestal_1
    
    if (knife1):
        text6 = "Find, Search the kitchen"
        next_action6 = kitchen_1
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]
    else:
        text6 = "Require further investigation"
        next_action6 = Wait3
        coords6 = [w_indent, 2*h_indent + height2, w_indent + width2, 2*(h_indent+height2)]

    if(head1):
        text7 = "Broken Vase"
        next_action7 = vase_1
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text7 = "Require further investigation"
        next_action7 = Wait3
        coords7 = [2*w_indent + width2, 2*h_indent + height2,  2*(w_indent + width2), 2*(h_indent+height2)]

    if(head1 and vase1):
        text8 = "Head wound"
        next_action8 = wound_1
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]
    else:
        text8 = "Require further investigation"
        next_action8 = Wait3
        coords8 = [3*w_indent + 2*width2, 2*h_indent + height2, 3*(w_indent + width2),2*(h_indent+height2)]

    if(wound1 and knife1 and vase1):
        text9 = "Blood on chest"
        next_action9 = chest_1
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text9 = "Require further investigation"
        next_action9 = Wait3
        coords9 = [4*w_indent + 3*width2, 2*h_indent + height2, 4*(w_indent + width2), 2*(h_indent+height2)]

    if(chest1 and knife1 and vase1 and wound1 and head1):
        text10 = "Murder Weapon"
        next_action10 = weapon_1
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    else:
        text10 = "Require further investigation"
        next_action10 = Wait3
        coords10 = [5*w_indent + 4*width2, 2*h_indent + height2, 5*(w_indent + width2), 2*(h_indent+height2)]
    
    choices = [
        (coords1, text1, next_action),
        (coords2, text2, next_action2),
        (coords3, text3, next_action3),
        (coords4, text4, next_action4),
        (coords5, text5, next_action5),
        (coords6, text6, next_action6),
        (coords7, text7, next_action7),
        (coords8, text8, next_action8),
        (coords9, text9, next_action9),
        (coords10, text10, next_action10),
    ]

    display_choice(dialogues, choices)

def post_statement():
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global Evie2, Jasper2, caraDavid2, Group2, caraDavid3
    dialogues = [
        ("", ""),
    ]
    if(knife1 and not(weapon1)):
        dialogues +=[
            ("You", "I need to gather all evidence that I can, before I can start questioning."),
        ]
    if(pillar1 or kitchen1 or weapon1):
        dialogues +=[
            ("You", "There are some people I need to question further."),
        ]
    if(Annabeth2 and Jasper2 and caraDavid2 and Evie2 and Group2 and caraDavid3):
        dialogues += [
            ("", "There's nothing left to investigate, time to put together all the evidence I have."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "TALK TO MR. DAVIES"
    next_action = Butler_1

    text2 = "TALK TO ANNABETH"
    if(caraDavid2):
        next_action2 = Annabeth_post
    else:
        next_action2 = Annabeth_1

    text3 = "TALK TO JASPER"
    
    if(weapon1):
        next_action3 = Jasper_post
    else: 
        next_action3 = Jasper_1

    text5 = "TALK TO CARA AND DAVID"
    if not(weapon1):

        next_action5 = caraDavid_1
    if(weapon1):
        next_action5 = caraDavid_post

    text6 = "TALK TO FREYR AND EVELYN"
    
    if(Evie2):
        next_action6 = firaEvie_post
    else:
        next_action6 = firaEvie_1
    text4 = "TALK TO WHISPERING GUESTS"
    
    if(Jasper2):
        next_action4 = Group_post
    else: 
        next_action4 = Group_1
    text7 = "INVESTIGATE THE BODY"
    next_action7 = Body_1
    text8 = "PROFILES"
    next_action8 = View_Info

    coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
    coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
    coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
    coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
    coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
    coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
    coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def Jasper_post():
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global Evie2, Jasper2, caraDavid2, Group2, caraDavid3
    #kitchen knife
    Jasper2 = True
    dialogues = [
        ("", ""),
        ("", "You approach Jasper Winters, who had moved to a comfy armchair in the corner, sketching something, no longer looking as depressed."),
        ("", "Well, he had mentioned in an exclusive that art is more than a job or hobby to him. It's his form of escapism."),
        ("You", "Sorry to disturb you, Mr. Winters, but I need to ask you further questions."),
        ("", "He looked up from his work, none-too-plussed at the interruption and put away his materials."),
        ("Jasper", "Yes, of course, anything to help."),
        ("You", "Thank you. You say you were in the pantry, the entire time?"),
        ("Jasper", "Yes, you could confirm that with Mr. Davies, Annabeth or some of the guests here. I'm sure they've witnessed me go on, and only come out when the dance was about to start."),
        ("You", "Did you hear anyone walk into the kitchen?"),
        ("Jasper", "Hm... walk past, you mean? I did not really pay attention, Anna stores my favourite cookies in the pantry for me, and that grasps most of my attention."),
        ("You", "Apologies, allow me to be more specific. A guest said they overheard someone telling someone else something, coming from the kitchen. And then, presumably, the sound of keys."),
        ("You", "You had the keys to everything in the kitchen and pantry, it seems? Unless you wish to claim that someone else was there with you in either the kitchen or pantry."),
        ("Jasper", "Hmm......"),
        ("", "He stayed silent for awhile, perhaps thinking of what he was going to say, And the silence was deafening."),
        ("Jasper", "Correct, I was the only one there. And I do remember someone coming in and asking me where something was."),
        ("You", "You knew whoever that was, didn't you? Why would you throw your keys at them?"),
        ("Jasper", "Like I said, I was distracted. Maybe, maybe not. Tell me, what is it you're trying to get at?"),
        ("You", "Do you remember who it was? Any discerning traits?"),
        ("Jasper", "Hmm... no. No, I'm afriad not, my frustration truly had me distracted, you see."),
        ("", "We are getting nowhere. But I think I was right that it was someone he knew. Now who do we know was in that hallway that could have asked for 'knives'?"),
        ("", "Arguing... most likely Cara and David."),
        ("", "Was there anyone else?"),
    ]
    if(pillar1 and Evie2):
        dialogues += [
            ("", "The champagne spill, Evelyn. And most likely Freyr, he did say he spilled champagne over here when searching for her."),
        ]
    elif(pillar1 and not(Evie2)):
        dialogues += [
            ("", "Ah right, the champagne spill. It's adding up to include Evelyn and Freyr, but I must question them first."),
        ]
    
    dialogues +=[
            ("You", "Could you remember if it was a male or female voice?"),
            ("", "You see Jasper silently considering, and you knew that something was off. He doesn't seem to be one for telling lies, but there was something you were missing."),
            ("Jasper", "There is a reason you're asking for me to try and remember whoever it was. I do have one memory, however, I tell you this, and I will be absolved of any involvement, are we clear?"),
            ("You", "If it is proven that you didn't kill the victim, then of course. (It's not like I could do much anyway... like it or not, my family's agency could easily be paid off by the Whitmore family to keep mum or turn a blind eye.)"),
            ("", "It's not like you hold that much power compared to the ones with wealth in this town."),
            ("Jasper", "Good, I think you understand far more than others. It was a male voice, He barged in, ranting about this and that, sounded upset, infuriated, irritated. He wanted to know where some items were."),
            ("Jasper", "I grew weary of his demands and decided to humor him by disclosing the locations of every item he sought. After which, I carelessly tossed him the keys. I wasn't in a good mood, you probably knew this already, so it doesn't matter who it was, I wanted him out of there and to stop bothering me."),
            ("Jasper", "Well then, detective Dubois? Does that help?"),
            ("You", "Yes, it does. Thank you very much for your cooperation, I'll leave you to your drawing"),
            ("", "That was a rather stressful conversation. Hopefully I don't have to question him any further."),
            ("", "First, I must check with the guests to ensure that Jasper Winters never left the kitchen, being such a famous figure, his appearance would definitely cause waves if he came out of the kitchen early. Ah, and Mr. Davies too."),
        
        ]
    if(pillar1 and Evie2):
        dialogues += [
            ("", "Then I can narrow it down to David Winston and Freyr Blackwood."),
        ]
    if(pillar1 and not(Evie2)):
        dialogues += [
            ("", "I must question Evelyn first, to determine the likely whereabouts of Freyr Blackwood, before I can narrow it down to anyone."),
        ]
    if(Annabeth2 and Jasper2 and caraDavid2 and Evie2 and Group2):
        dialogues += [
            ("", "There's nothing left to investigate, time to put together all the evidence I have."),
        ]
    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "TALK TO MR. DAVIES"
    next_action = Butler_1

    text2 = "TALK TO ANNABETH"
    if(caraDavid2):
        next_action2 = Annabeth_post
    else:
        next_action2 = Annabeth_1

    text3 = "TALK TO JASPER"
    next_action3 = Jasper_post

    text5 = "TALK TO CARA AND DAVID"
    next_action5 = caraDavid_post

    text6 = "TALK TO FREYR AND EVELYN"
    next_action6 = firaEvie_post

    text4 = "TALK TO WHISPERING GUESTS"
    next_action4 = Group_2

    if(Jasper2):
        next_action4 = Group_post

    text7 = "INVESTIGATE THE BODY"
    next_action7 = Body_1
    text8 = "PROFILES"
    next_action8 = View_Info

    coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
    coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
    coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
    coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
    coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
    coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
    coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def caraDavid_post():
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global Evie2, Jasper2, caraDavid2, Group2, caraDavid3
    #kitchen knife
    caraDavid2 = True
    if not(Group2):
        dialogues = [
            ("", ""),
            ("You", "Lord and Lady Winston, my apologies for interrupting your... conversation, but I have some further questions to ask."),
            ("Cara", "Conversation? You may call it as it is. Do go ahead, detective, take as much time as you need, so long as it keeps his mouth shut."),
            ("David", "A pity you're too blind to see the facts, Cara."),
            ("", "Dear heavens, will there ever be a single moment where they don't descend into arguing? I'm starting to wonder if they enjoy it or something..."),
            ("You", "Guests have mentioned that down that hallway, they heard yelling and shouting. Was that where you two were arguing?"),
            ("Cara", "Perhaps, I do not recall. An argument is an argument."),
            ("You", "(The guests did not mention hearing yelling from any other places, so I'll take that as a yes, unless I find contrasting evidence which seems unlikely)"),
            ("You", "Could I ask, what was the argument about?"),
            ("David", "Hah! Some tiff that the lady refuses to let go, that is all."),
            ("Cara", "'Some' tiff?! I beg your pardon, would you look at the disgrace that you'd be dragging us into! Some tiff, he says! Some tiff!"),
            ("David", "I told you already! I was forbidden from doing anything!"),
            ("Cara", "She is your younger sister! Tensions are already rising, and you know you would soothe talk of it if you had just publicly acted normal with her!"),
            ("David", "Do you expect me to go against my own parents? I would if I could, but you know very well that I can't!"),
            ("", "They mentioned something about this when I talked to them previously. Something about Lillian Wiston?"),
            ("David", "Fine, then, detective! If you must know, as I'm sure it's probably already gotten out to some of the mouthier guests here tonight. My younger sister was involved in some unsavoury activities out of town."),
            ("Cara", "Some! Everything could have been normal, if you had a spine!"),
            ("David", "That is all and everything you need to know, if it even had any relevance. We were arguing there regarding such a matter, that is all."),
            ("", "(But it did. Mouthier guests, he might also be referring to Gwendolyn Beaumont. And she was known for her eavesdropping, it does paint a scenario.)"),
            ("", "(Such a situation does not sound good, especially if it got out. They were arguing there, at least I got that straight.)"),
            # ("You", "What exactly happened afterwards? Guests reported that it went silent after some yelling. And that you showed up in a different dress and gloves."),
            # ("Cara", "This fool spilled wine on me. So I had to get Annie to get my a change of clothes, it was the same reason for his change of gloves."),
            # ("David", "Hmph! After I had accidentally ruined her dress, I went to find Annie to request for a change of dress and gloves for us."),
            ("", "Something else happened afterwards, I'm sure of it. Perhaps I ought to ask the guests again, see if I'm missing anything."),
        ]
    if(Group2):
        caraDavid3 = True
        dialogues = [
            ("", ""),
            ("You", "Lord and Lady Winston, my apologies for interrupting your... conversation, but I have some further questions to ask."),
            ("Cara", "Conversation? You may call it as it is. Do go ahead, detective, take as much time as you need, so long as it keeps his mouth shut."),
            ("David", "A pity you're too blind to see the facts, Cara."),
            ("", "Dear heavens, will there ever be a single moment where they don't descend into arguing? I'm starting to wonder if they enjoy it or something..."),
            ("You", "Guests have mentioned that down that hallway, they heard yelling and shouting. Was that where you two were arguing?"),
            ("Cara", "Perhaps, I do not recall. An argument is an argument."),
            ("You", "(The guests did not mention hearing yelling from any other places, so I'll take that as a yes, unless I find contrasting evidence which seems unlikely)"),
            ("You", "Could I ask, what was the argument about?"),
            ("David", "Hah! Some tiff that the lady refuses to let go, that is all."),
            ("Cara", "'Some' tiff?! I beg your pardon, would you look at the disgrace that you'd be dragging us into! Some tiff, he says! Some tiff!"),
            ("David", "I told you already! I was forbidden from doing anything!"),
            ("Cara", "She is your younger sister! Tensions are already rising, and you know you would soothe talk of it if you had just publicly acted normal with her!"),
            ("David", "Do you expect me to go against my own parents? I would if I could, but you know very well that I can't!"),
            ("", "They mentioned something about this when I talked to them previously. Something about Lillian Wiston?"),
            ("David", "Fine, then, detective! If you must know, as I'm sure it's probably already gotten out to some of the mouthier guests here tonight. My younger sister was involved in some unsavoury activities out of town."),
            ("Cara", "Some! Everything could have been normal, if you had a spine!"),
            ("David", "That is all and everything you need to know, if it even had any relevance. We were arguing there regarding such a matter, that is all."),
            ("", "(But it did. Mouthier guests, he might also be referring to Gwendolyn Beaumont. And she was known for her eavesdropping, it does paint a scenario.)"),
            ("", "(Such a situation does not sound good, especially if it got out. They were arguing there, at least I got that straight.)"),
            ("You", "What exactly happened afterwards? Guests reported that it went silent after some yelling. And that you showed up in a different dress and gloves."),
            ("Cara", "This fool spilled wine on me. So I had to get Annie to get my a change of clothes, it was the same reason for his change of gloves."),
            ("David", "Hmph! After I had accidentally ruined her dress, I went to find Annie to request for a change of dress and gloves for us."),
            ("", "(That matches with what the guests said. Dear goodness, these two seem hot-tempered, I guess that's what a lifetime of constant arguing does to you.)"),
            ("", "(Hold on, that means David left for a bit, to the direction of the foyer or the guest room? Either way, it's in the same direction as the kitchen.)"),
            ("You", "Thank you for your time and cooperation, I will... leave you to it."),
            ("", "They didn't even wait for you to walk away before continuing their previous argument."),
        ]
    if(Annabeth2 and Jasper2 and caraDavid2 and Evie2 and Group2):
        dialogues += [
            ("", "There's nothing left to investigate, time to put together all the evidence I have."),
        ]


    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "TALK TO MR. DAVIES"
    next_action = Butler_1

    text2 = "TALK TO ANNABETH"
    if(caraDavid2):
        next_action2 = Annabeth_post
    else:
        next_action2 = Annabeth_1

    text3 = "TALK TO JASPER"
    next_action3 = Jasper_post

    text5 = "TALK TO CARA AND DAVID"
    next_action5 = caraDavid_post

    text6 = "TALK TO FREYR AND EVELYN"
    next_action6 = firaEvie_post

    text4 = "TALK TO WHISPERING GUESTS"
    next_action4 = Group_post

    text7 = "INVESTIGATE THE BODY"
    next_action7 = Body_1
    text8 = "PROFILES"
    next_action8 = View_Info

    coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
    coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
    coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
    coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
    coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
    coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
    coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def firaEvie_post():
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global Evie2, Jasper2, caraDavid2, Group2, Annabeth2, caraDavid3
    #champagne neara pillar, evies whereabouts
    #revealed: she was there crying, heard yelling but didnt bother, gwen saw her after some time and started jeering at her, someone confronted gwen, and then fira found her before taking her away
    #conclusion: that someone was cara, bc david had stormed off, at the time, cara then killed gwen
    Evie2 = True
    dialogues = [
        ("", ""),
        ("You", "Lady Evelyn Sinclair, are you feeling better?"),
        ("Evelyn", "Detective, good to see you again. Thank you, I am."),
        ("Freyr", "Are you close to solving it yet, detective? I apologize for the rush but my love here needs her rest. It has already been a stressful night."),
        ("You", "I would say I am close. I just need some final questions answered. On the same note, I need to ask you something."),
        ("You", "By the location of the body, I found champagne spills near the pillar. When you ran off, before being found by Lord Freyr Blackwood, that was where you were, correct?"),
        ("Evelyn", "Ah... yes, as you must already know, it is a popular spot for privacy, as contrasting as that sounds."),
        ("You", "What happened, between the moments of when you arrived there, and when you left with your fiance?"),
        ("Evelyn", "(she and Freyr exchanged unreadable looks, and once again, you get the feeling that there is something you do not know.)"),
        ("Evelyn", "As you know, I ran off after dinner. I hid myself there, and even when I heard a lot of noises around me, I didn't emerge from behind it. It was until I heard her again, she found me somehow, or she was seeking for more ammunition."),
        ("Evelyn", "Whichever was the case, the routine started again, I already knew to shut myself off when she started, she knew how to press one's buttons, I can tell you that. Someone pulled her attention off of me, and Freyr came just in time."),
        ("Evelyn", "He was running to find me, and ended up splashing the champagne on me when I turned around too quickly. After that, he took me away from there. Unfortunately, Annabeth did not have a spare cloak for me."),
        ("", "(Someone, I'll assume it to be one person. Yelling...)"),
        ("You", "Thank you, this will be over with soon enough."),
        ("", "(I'm getting tired of this myself.)"),
    ]
    if(Annabeth2 and Jasper2 and caraDavid2 and Evie2 and Group2):
        dialogues += [
            ("", "There's nothing left to investigate, time to put together all the evidence I have."),
        ]
   

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "TALK TO MR. DAVIES"
    next_action = Butler_1

    text2 = "TALK TO ANNABETH"
    if(caraDavid2):
        next_action2 = Annabeth_post
    else:
        next_action2 = Annabeth_1

    text3 = "TALK TO JASPER"
    next_action3 = Jasper_post

    text5 = "TALK TO CARA AND DAVID"
    next_action5 = caraDavid_post

    text6 = "TALK TO FREYR AND EVELYN"
    next_action6 = firaEvie_post

    text4 = "TALK TO WHISPERING GUESTS"
    next_action4 = Group_post

    text7 = "INVESTIGATE THE BODY"
    next_action7 = Body_1
    text8 = "PROFILES"
    next_action8 = View_Info

    coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
    coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
    coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
    coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
    coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
    coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
    coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def Group_post():
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global Evie2, Jasper2, caraDavid2, Group2, caraDavid3, Annabeth2
    #kitchen knife
    Group2 = True
    dialogues = [
        ("", ""),
        ("", "As expected, the group of guests that offered information were still huddled together."),
        ("You", "Ladies and gents, once again, I apologize for interrupting your conversation, it must be riveting, I'm sure."),
        ("Guest 1", "Oh my, hello again Detective. No harm done, well now, you have more questions I assume? Go ahead and ask, let's see if we've missed out anything."),
        ("You", "Oh thank you, esteemed guest. I'd like to ask, if you have noticed Mr. Winters exiting the kitchen anytime before the start of the dance?"),
        ("Guest 3", "Oh? Except for the one time where he exited to make it to the dance, no. The poor darling might as well have locked himself away in that room the entire time!"),
        ("Guest 4", "The poor dear indeed, why, I was hoping that he'd hold an exhibition for his latest works after dinner, but alas, we can't have what we want all the time."),
        ("", "And that marks Jasper Winters off."),
        ("You", "What about Mr. Davies and Lady Annabeth Whitmore? Were they here the entire time?"),
        ("Guest 2", "Why, of course. Poor Mr. Davies was stuck behind the bar, even until the dance! As more our dear hostess, she has such a talent for hosting, and the only times she would go out was to enter the guest room on this floor."),
        ("You", "Might I inquire what she did?"),
        ("Guest 1", "Why else! To acquire a change of clothing for some of her guests."),
        ("You", "(Now we're getting somewhere.) Did you notice anyone with different attire during the dance?"),
        ("Guest 2", "Oh yes, it was quite a difference! Lady Evelyn Sinclair, well, she was seen without her cloak."),
        ("", "(Matches what Freyr Blackwood and Evelyn Sinclair said about the champagne spill.)"),
        ("Guest 4", "You're missing someone! The famous couple too!"),
        ("Guest 2", "Oh my! I can't believe I had nearly forgotten them! But yes! Lord Winston was seen with a different pair of gloves from his white ones. And Lady Winston was wearing a diffeent dress!"),
        ("Guest 3", "Hostess Whitmore cleared it up, you see, something about a wine spill during the heats of an argument. Nothing peculiar about those two, honestly."),
        ("", "I'll decide that for myself."),
        ("You", "You all have been a tremendous help. I thank you very much."),
        ("Guest 1", "Oh, you can thank us by sharing some interesting information. As a detective, I'm sure you've come across your fair share!"),
        ("You", "Ah... I'll think about it."),
        ("", "(I got some useful information, surely this would help me.)"),
    ]
    if(Annabeth2 and Jasper2 and caraDavid2 and Evie2 and Group2):
        dialogues += [
            ("", "There's nothing left to investigate, time to put together all the evidence I have."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "TALK TO MR. DAVIES"
    next_action = Butler_1

    text2 = "TALK TO ANNABETH"
    if(caraDavid2):
        next_action2 = Annabeth_post
    else:
        next_action2 = Annabeth_1

    text3 = "TALK TO JASPER"
    next_action3 = Jasper_post

    text5 = "TALK TO CARA AND DAVID"
    next_action5 = caraDavid_post

    text6 = "TALK TO FREYR AND EVELYN"
    next_action6 = firaEvie_post

    text4 = "TALK TO WHISPERING GUESTS"
    next_action4 = Group_post

    text7 = "INVESTIGATE THE BODY"
    next_action7 = Body_1
    text8 = "PROFILES"
    next_action8 = View_Info

    coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
    coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
    coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
    coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
    coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
    coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
    coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def Annabeth_post():
    global knife1, head1, pillar1, pedestal1, vase1, wound1, chest1, weapon1, kitchen1
    global Evie2, Jasper2, caraDavid2, Group2, Annabeth2, caraDavid3
    #kitchen knife
    Annabeth2 = True
    dialogues = [
        ("", ""),
        ("Annabeth", "Detective, you look like you're on the verge of solving this case."),
        ("You", "I have made progress, I suppose. I have to ask you a few more, clarifying questions, Miss Whitmore."),
        ("Annabeth", "By all means, ask away. I tire of this long night, and I do so wish to retire soon. The rest of my guests surely feel the same way."),
        ("You", "I understand, hence I will be prompt with this. Did David Winston approach you regarding a change of clothes? And did you provide them with the change of attire? How about Miss Sinclair's cloak?"),
        ("Annabeth", "Evie's cloak has been soaked in champagne, I'm sure if you were to ask Evelyn and Freyr about it, they would tell you what happened. I have not another cloak in the guest room for her, however, so she showed up to the dance without one. Her cloak is still in the guest room."),
        ("", "(That matches, the guest room is the one that's between the kitchen and the murder location. It must be just for emergencies purposes)"),
        ("Annabeth", "As for Cara and David, well, they are the main reason why that room has become a room primarily for changes of attire."),
        ("", "(She's not offering any information about what she gave to them to change into.)"),
        ("You", "What did you give them?"),
        ("Annabeth", "Oh, for Cara, it was a clean dress. And for David, it was a pair of gloves. Them spilling drinks over themselves in the heat of arguments is not as uncommon as you might think. I would appreciate if this doesn't get out."),
        ("You", "Of course, such details will be kept confidential. Might I ask where you met David?"),
        ("Annabeth", "My, you're testing my memory! I'm afraid I can't give you a clear answer, the evening was busy and I do not remember."),
        ("", "(Everyone has been normal, yet something about all of them is tugging at me. Nonetheless, I don't have any more information to get out of her.)"),
        ("You", "I thank you for your cooperation, Miss Whitmore."),
    ]
    if(Annabeth2 and Jasper2 and caraDavid2 and Evie2 and Group2):
        dialogues += [
            ("", "There's nothing left to investigate, time to put together all the evidence I have."),
        ]
   

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "TALK TO MR. DAVIES"
    next_action = Butler_1

    text2 = "TALK TO ANNABETH"
    if(caraDavid2):
        next_action2 = Annabeth_post
    else:
        next_action2 = Annabeth_1

    text3 = "TALK TO JASPER"
    next_action3 = Jasper_post

    text5 = "TALK TO CARA AND DAVID"
    next_action5 = caraDavid_post

    text6 = "TALK TO FREYR AND EVELYN"
    next_action6 = firaEvie_post

    text4 = "TALK TO WHISPERING GUESTS"
    next_action4 = Group_post

    text7 = "INVESTIGATE THE BODY"
    next_action7 = Body_1
    text8 = "PROFILES"
    next_action8 = View_Info

    coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
    coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
    coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
    coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
    coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
    coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
    coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def View_Info():
    global Conclusion1, Conclusion2
    dialogues = [
        ("", ""),
        ("", "Let's review what we know"),
    ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Profile: Rupert Davies"
    next_action = Butler_prof
    text2 = "Profile: Annabeth Whitmore"
    next_action2 = Annabeth_prof
    text3 = "Profile: Jasper Winters"
    next_action3 = Jasper_prof
    text4 = "Profile: Cara and David"
    next_action4 = caraDavid_prof
    text5 = "Profile: Freyr and Evelyn"
    next_action5 = firaEvie_prof
    text6 = "Profile: Gwendolyn Beaumont"
    next_action6 = gwen_prof
    text7 = "Evidence compilation"
    next_action7 = evidences
    text8 = "Back"
    next_action8 = post_statement
    if(Conclusion1):
        next_action9 = scene2_1
    elif(Conclusion2):
        next_action9 = scene3_1
    elif(Conclusion3):
        next_action9 = scene4_1
    elif(Conclusion4):
        next_action9 = scene5_1
    elif(Conclusion5):
        next_action9 = Conclusion_5
    else:
        next_action9 = connection

    text9 = "Conclusions"
    
    text10= "Determine killer"
    next_action10 = killer

    coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
    coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
    coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
    coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
    coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
    coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
    coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
    coords9 = [norm_indent, 20 + 2*choice_box_height + 2*60, 150 + norm_indent, 20 + 3*choice_box_height + 2*60]
    coords10 = [norm_indent, (CANVAS_HEIGHT-choice_box_height)/2, norm_indent+choice_box_width, (CANVAS_HEIGHT-choice_box_height)/2 + choice_box_height]

    if(Jasper2 and Annabeth2 and Group2 and caraDavid2 and Evie2 and not(Conclusion5)):
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8),
            (coords9, text9, next_action9)
        ]
    elif(Conclusion5):
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8),
            (coords9, text9, next_action9),
            (coords10, text10, next_action10)
        ]
    else:
        choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
        ]

    display_choice(dialogues, choices)






def Butler_prof(): #intiial done
    dialogues = [
        ("", "Let's see... Rupert Davies"),
        ("", "Rupert Davies: head butler of the Whitmore family."),
        ("", "Involvement: Found the body while patrolling for stragglers in the manor"),
        ("", "Relationship with Gwendolyn Beaumont: Doesn't seem fond, gave medical attention to victim's most constant... well, victim."),
        ("", "Possible motivation: Beaumont's actions tonight would have harmed the Whitmore's reputation. Not strong enough, however."),
        ("", "Alibi: Serving drinks the entire time."),
        ("You", "That's the initial profile from the first round of questionings. Do I have more to go on off?"),
    ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Profile: Rupert Davies"
    next_action = Butler_prof
    text2 = "Profile: Annabeth Whitmore"
    next_action2 = Annabeth_prof
    text3 = "Profile: Jasper Winters"
    next_action3 = Jasper_prof
    text4 = "Profile: Cara and David"
    next_action4 = caraDavid_prof
    text5 = "Profile: Freyr and Evelyn"
    next_action5 = firaEvie_prof
    text6 = "Profile: Gwendolyn Beaumont"
    next_action6 = gwen_prof
    text7 = "Evidence compilation"
    next_action7 = evidences
    text8 = "Back"
    next_action8 = post_statement

    coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
    coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
    coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
    coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
    coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
    coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
    coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def Annabeth_prof():
    dialogues = [
        ("", "Let's see... Rupert Davies"),
        ("", "Rupert Davies: head butler of the Whitmore family."),
        ("", "Involvement: Found the body while patrolling for stragglers in the manor"),
        ("", "Relationship with Gwendolyn Beaumont: Doesn't seem fond, gave medical attention to victim's most constant... well, victim."),
        ("", "Possible motivation: Beaumont's actions tonight would have harmed the Whitmore's reputation. Not strong enough, however."),
        ("", "Alibi: Serving drinks the entire time."),
    ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Profile: Rupert Davies"
    next_action = Butler_prof
    text2 = "Profile: Annabeth Whitmore"
    next_action2 = Annabeth_prof
    text3 = "Profile: Jasper Winters"
    next_action3 = Jasper_prof
    text4 = "Profile: Cara and David"
    next_action4 = caraDavid_prof
    text5 = "Profile: Freyr and Evelyn"
    next_action5 = firaEvie_prof
    text6 = "Profile: Gwendolyn Beaumont"
    next_action6 = gwen_prof
    text7 = "Evidence compilation"
    next_action7 = evidences
    text8 = "Back"
    next_action8 = post_statement

    coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
    coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
    coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
    coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
    coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
    coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
    coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def Jasper_prof():
    dialogues = [
        ("", "Let's see... Rupert Davies"),
        ("", "Rupert Davies: head butler of the Whitmore family."),
        ("", "Involvement: Found the body while patrolling for stragglers in the manor"),
        ("", "Relationship with Gwendolyn Beaumont: Doesn't seem fond, gave medical attention to victim's most constant... well, victim."),
        ("", "Possible motivation: Beaumont's actions tonight would have harmed the Whitmore's reputation. Not strong enough, however."),
        ("", "Alibi: Serving drinks the entire time."),
    ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Profile: Rupert Davies"
    next_action = Butler_prof
    text2 = "Profile: Annabeth Whitmore"
    next_action2 = Annabeth_prof
    text3 = "Profile: Jasper Winters"
    next_action3 = Jasper_prof
    text4 = "Profile: Cara and David"
    next_action4 = caraDavid_prof
    text5 = "Profile: Freyr and Evelyn"
    next_action5 = firaEvie_prof
    text6 = "Profile: Gwendolyn Beaumont"
    next_action6 = gwen_prof
    text7 = "Evidence compilation"
    next_action7 = evidences
    text8 = "Back"
    next_action8 = post_statement

    coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
    coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
    coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
    coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
    coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
    coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
    coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def caraDavid_prof():
    dialogues = [
        ("", "Let's see... Rupert Davies"),
        ("", "Rupert Davies: head butler of the Whitmore family."),
        ("", "Involvement: Found the body while patrolling for stragglers in the manor"),
        ("", "Relationship with Gwendolyn Beaumont: Doesn't seem fond, gave medical attention to victim's most constant... well, victim."),
        ("", "Possible motivation: Beaumont's actions tonight would have harmed the Whitmore's reputation. Not strong enough, however."),
        ("", "Alibi: Serving drinks the entire time."),
    ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Profile: Rupert Davies"
    next_action = Butler_prof
    text2 = "Profile: Annabeth Whitmore"
    next_action2 = Annabeth_prof
    text3 = "Profile: Jasper Winters"
    next_action3 = Jasper_prof
    text4 = "Profile: Cara and David"
    next_action4 = caraDavid_prof
    text5 = "Profile: Freyr and Evelyn"
    next_action5 = firaEvie_prof
    text6 = "Profile: Gwendolyn Beaumont"
    next_action6 = gwen_prof
    text7 = "Evidence compilation"
    next_action7 = evidences
    text8 = "Back"
    next_action8 = post_statement

    coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
    coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
    coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
    coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
    coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
    coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
    coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def firaEvie_prof():
    dialogues = [
        ("", "Let's see... Rupert Davies"),
        ("", "Rupert Davies: head butler of the Whitmore family."),
        ("", "Involvement: Found the body while patrolling for stragglers in the manor"),
        ("", "Relationship with Gwendolyn Beaumont: Doesn't seem fond, gave medical attention to victim's most constant... well, victim."),
        ("", "Possible motivation: Beaumont's actions tonight would have harmed the Whitmore's reputation. Not strong enough, however."),
        ("", "Alibi: Serving drinks the entire time."),
    ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Profile: Rupert Davies"
    next_action = Butler_prof
    text2 = "Profile: Annabeth Whitmore"
    next_action2 = Annabeth_prof
    text3 = "Profile: Jasper Winters"
    next_action3 = Jasper_prof
    text4 = "Profile: Cara and David"
    next_action4 = caraDavid_prof
    text5 = "Profile: Freyr and Evelyn"
    next_action5 = firaEvie_prof
    text6 = "Profile: Gwendolyn Beaumont"
    next_action6 = gwen_prof
    text7 = "Evidence compilation"
    next_action7 = evidences
    text8 = "Back"
    next_action8 = post_statement

    coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
    coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
    coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
    coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
    coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
    coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
    coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def gwen_prof(): #initial done
    dialogues = [
        ("", "Here we go, Gwendolyn Beaumont"),
        ("", "Gwendolyn Beaumont: Second daughter of Beaumont family, half-sister to Evelyn Sinclair, who is her most constant victim."),
        ("", "Involvement: Victim. Body yet to be fully investigated."),
        ("", "Relationship with suspects: Annabeth Whitmore \nUsed to be close friends, crossed a line and would have been barred from future soirees after tonight."),
        ("", "Relationship with suspects: Rupert Davies \nA simple butler. Nothing to suggest anything more."),
        ("", "Relatinoship with suspects: Jasper Winters \nShe targeted him today, and indirectly targeted Whitmore family. Knew each other when were children, but most likely not fond of her after her change."),
        ("", "Relationship with suspects: Cara Montgomery and David Winston \nThese two might as well be their own pair... Neither of them liked Gwendolyn at all, Cara never liked her from the start. Implied that Gwendolyn was already on the hunt for entertaining scandals. They were Gwendolyn's favourite targets who are indifferent to it."),
        ("", "Relatinoship with suspects: Freyr Blackwood \nKnew her from when they were young, however he doesn't like her because of her treatment towards his fiance, Evelyn."),
        ("", "Relatinoship with suspects: Evelyn Sinclair \nGwen's favourite target, went physical on her in private to the point of having to seek medical attention. Seems to have no limits and would verbally lash her even in public. Caused her to run away crying and most likely the cause of her low self-esteem."),
        ("", "(It doesn't paint a pretty picture at all...... What else do I have to go on off?)"),
    ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Profile: Rupert Davies"
    next_action = Butler_prof
    text2 = "Profile: Annabeth Whitmore"
    next_action2 = Annabeth_prof
    text3 = "Profile: Jasper Winters"
    next_action3 = Jasper_prof
    text4 = "Profile: Cara and David"
    next_action4 = caraDavid_prof
    text5 = "Profile: Freyr and Evelyn"
    next_action5 = firaEvie_prof
    text6 = "Profile: Gwendolyn Beaumont"
    next_action6 = gwen_prof
    text7 = "Evidence compilation"
    next_action7 = evidences
    text8 = "Back"
    next_action8 = post_statement

    coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
    coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
    coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
    coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
    coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
    coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
    coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def evidences():
    dialogues = [
        ("", "Physical evidences: knife, broken vase."),
        ("", "Injury on victim's body: wound on the back of head, shards stuck in the skin, chest stab wound with minimal bleeding."),
        ("Scene: ", "Shards swept under the victim's head, water around the victim's body, champagne spill by a nearby pillar, empty pedestal where the vase was presumably taken from."),
        ("Guest testimonies:", "Heard yelling from the hallway, then silence. Heard someone telling someone else where the knives are, and sounds of keys."),
        ("Guest testimonies 2:", "Cara, David and Evelyn had different attires during the dance. Evelyn lost her cloak, presumably due to champagne spill. Cara was wearing a new dress, David wearing new gloves, presumably due to wine spill."),
        ("Guest testimonies 3: ", "Confirmed Annabeth's presence, confirmed Mr. Davies' presence. Confirmed that Jasper stayed in the kitchen the entire time."),
        ("Mr. Davies testimony:", "Found the body when patrolling the floor for stragglers in the manor. Confirmed to not have left the foyer and ballroom area during time of murder."),
        ("Annabeth testimony", "Implied that drinks staining outfits isn't an uncommon occurrence. Confirmed the attire changes and reasons align."),
        ("Jasper testimony", "Confirmed that was in pantry the entire time. Stated that it was a male that entered the kitchen for the knives."),
        ("Cara testimony:", "Confirmed had an argument with David down the hallway, to which David stormed off after spilling wine on her, claimed to be looking for Annabeth to request a change of attire. Confirmed by Annabeth."),
        ("David testimony:", "Confirmed had an argument with Cara down the hallway, after accidentally spilling his wine on her and his gloves, he went looking for Annabeth to request a change of certain attire. Confirmed by Annabeth, matches with Cara."),
        ("Evelyn testimony:", "Ran off after dinner, confirmed was by the pillar, heard yelling, presumably Cara and David. Confronted by Gwen who was stopped by someone, then taken away by Freyr who found her and accidentally spilled his champagne on her cloak. Asked Annabeth for a new cloak but to no avail."),
        ("Freyr testimony:", "Unseen the entire period, presumably looking for Evelyn after dinner ended. Found her being confronted by Gwen, accidentally spilled his champagne because he was startled by her sudden turn around to face him, before taking her away from the scene."),
        ("Motives:", "All suspects would have valid motives..."),
        ("Height:", "Victim's height is 152cm. Taller only than Jasper Winters, 151cm. Evelyn Sinclair is 153cm. Annabeth Whitmore is 157cm. Cara Montgomery and Freyr Blackwood are 160cm. David Winston is 164cm, Rupert Davies is 168cm."),
    ]
    if(Conclusion1):
        dialogues += [
            ("Conclusion 1", "Body found by butler, before party ends, at a lavatory at the end of a hallway."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Profile: Rupert Davies"
    next_action = Butler_prof
    text2 = "Profile: Annabeth Whitmore"
    next_action2 = Annabeth_prof
    text3 = "Profile: Jasper Winters"
    next_action3 = Jasper_prof
    text4 = "Profile: Cara and David"
    next_action4 = caraDavid_prof
    text5 = "Profile: Freyr and Evelyn"
    next_action5 = firaEvie_prof
    text6 = "Profile: Gwendolyn Beaumont"
    next_action6 = gwen_prof
    text7 = "Evidence compilation"
    next_action7 = evidences
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
    coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
    coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
    coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
    coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
    coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
    coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            # (coords1, text1, next_action),
            # (coords2, text2, next_action2),
            # (coords3, text3, next_action3),
            # (coords4, text4, next_action4),
            # (coords5, text5, next_action5),
            # (coords6, text6, next_action6),
            # (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)



def connection():
    global scene1_1_, scene1_2_, scene1_3_
    dialogues = [
        ("", ""),
        ("", "Let's build the scene. First, details of the body report."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text1 = "Rupert Davies"
    next_action = scene1_1
    text2 = "Guests testimonies"
    next_action2 = not_right
    text3 = "Jasper Winters"
    next_action3 = not_right
    text8 = "Back"
    next_action8 = View_Info

    # coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
    # coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
    # coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
    # coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
    # coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
    # coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
    # coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            # (coords4, text4, next_action4),
            # (coords5, text5, next_action5),
            # (coords6, text6, next_action6),
            # (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)


def scene1_1():
    global scene1_1_, scene1_2_, scene1_3_
    scene1_1_ = True
    dialogues = [
        ("", ""),
        ("", "Rupert Davies, butler of the Whitmore family discovered the body of victim, Gwendolyn Beaumont..."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Lavatory"
    next_action2 = scene1_2
    text3 = "Foyer"
    next_action3 = not_right
    text1 = "Ballroom"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    # coords1 = [norm_indent + 150 + 2*45, 20, norm_indent + 150 + choice_box_width + 2*45,20 + choice_box_height]
    # coords2 = [norm_indent + 150+choice_box_width + 3*45, 20, norm_indent + 150+2*choice_box_width + 3*45,20 + choice_box_height]
    # coords3 = [norm_indent + 150+2*choice_box_width + 4*45, 20, norm_indent + 150+3*choice_box_width + 4*45,20 + choice_box_height]
    # coords4 = [norm_indent + 150 + 2*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+choice_box_width + 2*45,20 + 3*choice_box_height + 2*60]
    # coords5 = [norm_indent + 150+choice_box_width + 3*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+2*choice_box_width + 3*45,20 + 3*choice_box_height + 2*60]
    # coords6 = [norm_indent + 150+2*choice_box_width + 4*45, 20 + 2*choice_box_height + 2*60, norm_indent + 150+3*choice_box_width + 4*45,20 + 3*choice_box_height + 2*60]
    # coords7 = [norm_indent + 150+choice_box_width + 3*45, 20 + choice_box_height + 60, norm_indent + 150+2*choice_box_width + 3*45,20 + 2*choice_box_height + 60]  
    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            # (coords4, text4, next_action4),
            # (coords5, text5, next_action5),
            # (coords6, text6, next_action6),
            # (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def scene1_2():
    global scene1_1_, scene1_2_, scene1_3_
    scene1_2_ = True
    dialogues = [
        ("", ""),
        ("", "...at a lavatory at the end of a hallway, a secluded one, that is both popular and unpopular. It was discovered..."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Right after the dance"
    next_action2 = not_right
    text3 = "Before the end"
    next_action3 = Conclusion_1
    text1 = "Before the dance"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def Conclusion_1():
    global scene1_1_, scene1_2_, scene1_3_, Conclusion1
    scene1_3_ = True
    Conclusion1 = True
    dialogues = [
        ("", ""),
        ("", "...5 minutes the end of the party, right before guests who haven't already left before dinner left."),
        ("Conclusion 1", "The butler of the Whitmore Family, Rupert Davies, was patrolling the ground floor of the manor for anyone still there, when he came across Gwendolyn Beaumont's body by the lavatory at the end of a hallway right before the end of the party."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text8 = "Back"
    next_action8 = View_Info
    text9 = "Next"
    next_action9 = scene2_1

    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
    coords9 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
        
    choices = [

            (coords8, text8, next_action8),
            (coords9, text9, next_action9)
    ]

    display_choice(dialogues, choices)

def scene2_1():
    global scene2_1_, scene2_2_
    # scene2_1_ = True
    dialogues = [
        ("", ""),
        ("", "Now about the body itself, what was obviously seen is..."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Water"
    next_action2 = not_right
    text3 = "Knife"
    next_action3 = scene2_2
    text1 = "Vase"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords2, text1, next_action),
            (coords1, text2, next_action2),
            (coords3, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def scene2_2():
    global scene2_1_, scene2_2_, Conclusion2
    scene2_1_ = True
    dialogues = [
        ("", ""),
        ("", "A knife which was sticking out of her chest, and the abnormality..."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Blood splatter"
    next_action2 = not_right
    text3 = "Chest"
    next_action3 = scene2_3
    text1 = "Vase"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords3, text2, next_action2),
            (coords2, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def scene2_3():
    global scene2_3_, scene2_2_
    scene2_2_ = True

    dialogues = [
        ("", ""),
        ("", "...there was minimal bleeding to the head. Consider additional factors..."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Champagne spill"
    next_action2 = not_right
    text3 = "Vase"
    next_action3 = scene2_4
    text1 = "Knife taken from kitchen"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords3, text2, next_action2),
            (coords2, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def scene2_4():
    global scene2_3_, scene2_2_
    scene2_3_ = True

    dialogues = [
        ("", ""),
        ("", "The broken vase and the shards swept below her head. And the most incriminating part here is..."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Champagne spill"
    next_action2 = not_right
    text3 = "Blood under head"
    next_action3 = Conclusion_2
    text1 = "Water everywhere"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords3, text1, next_action),
            (coords2, text2, next_action2),
            (coords1, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def Conclusion_2():
    global Conclusion2, scene2_4_
    scene2_4_ = True
    Conclusion2 = True
    dialogues = [
        ("", ""),
        ("", "...The blood and the head wound, aside from the shards, there was blood near the top and faint bruising."),
        ("Conclusion 2", "The actual murder weapon was the vase, which the murderer used to hit Gwen from behind her head. Her murderer is likely taller than her."),
        ("Conclusion 2", "The knife was a red herring, whether it was placed by a second party with a vested interest in hiding the murder, or by the murderer themselves is yet to be determined."),
        ("Conclusion 2", "The murderer is likely to have been splattered by some blood, from the shards of glass piercing Gwen's head. The one who swept the shards beneath her head is likely to be the same one with the knife, and likely to have bloodied their hands."), 
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text8 = "Back"
    next_action8 = View_Info
    text9 = "Next"
    next_action9 = scene3_1

    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
    coords9 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
        
    choices = [

            (coords8, text8, next_action8),
            (coords9, text9, next_action9)
    ]

    display_choice(dialogues, choices)

def scene3_1():
    global scene3_1_

    dialogues = [
        ("", ""),
        ("", "Let's take a look at what happened before the murder period. What happened first..."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Gwen and Evelyn"
    next_action2 = not_right
    text3 = "Gwen and Jasper"
    next_action3 = scene3_2
    text1 = "Gwen and Cara"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords3, text2, next_action2),
            (coords2, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def scene3_2():
    global scene3_1_
    scene3_1_ = True

    dialogues = [
        ("", ""),
        ("", "Gwen was talking about a rumour regarding Jasper, which also hurts the reputation of Annabeth and her family. After that, another important thing that happened..."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Attire change"
    next_action2 = not_right
    text3 = "Gwen and Evelyn"
    next_action3 = Conclusion_3
    text1 = "Cara and David"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords3, text1, next_action),
            (coords1, text2, next_action2),
            (coords2, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def Conclusion_3():
    global scene3_2_, Conclusion3
    scene3_2_ = True
    Conclusion3
    dialogues = [
        ("", ""),
        ("", "Gwen was targeting Evelyn again, causing her to run away in tears. After the dinner, Freyr immediately went after her."),
        ("Conclusion 3", "All of Gwen's actions from before the time of her death would have already earned her enemies, if they weren't already."),
        ("Conclusion 3", "Any of them could have a motive."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text8 = "Back"
    next_action8 = View_Info
    text9 = "Next"
    next_action9 = scene4_1

    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
    coords9 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
        
    choices = [

            (coords8, text8, next_action8),
            (coords9, text9, next_action9)
    ]

    display_choice(dialogues, choices)

def scene4_1():
    # global scene3_1_

    dialogues = [
        ("", ""),
        ("", "Now what happened? First, determine everyone's likely locations. Annabeth and Mr. Davies were here, Jasper stayed in the pantry, Freyr chased after Evelyn, who... "),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Champagne and Guest testimony"
    next_action2 = not_right
    text3 = "Champagne and Evelyn testimony"
    next_action3 = scene4_2
    text1 = "Cara and David testimony"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def scene4_2():
    global scene4_1_
    scene4_1_ = True
    dialogues = [
        ("", ""),
        ("", "...Evelyn who was by the pillar, by the lavatory, heard Cara and David's argument and ignored it."),
        ("Conclusion 4a: ", "The suspects at the scene were Cara, David and Evelyn. But that isn't enough, let's continue."),
        ("", "What was Gwen doing then?"),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Gwen and Evelyn"
    next_action2 = not_right
    text3 = "Testimonies about Gwen"
    next_action3 = scene4_3
    text1 = "Kitchen knife"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords3, text2, next_action2),
            (coords2, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def scene4_3():
    global scene4_2_
    scene4_2_ = True
    dialogues = [
        ("", ""),
        ("", "According to the testimonies, Gwen was likely eavesdropping on their argument."),
        ("", "A very bad argument, about a touchy topic, according to Cara and David's post-evidence testimony."),
        ("", "Then after the yelling, everything went silent, what likely happened first was..."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Gwen and Evelyn"
    next_action2 = not_right
    text3 = "Kitchen knife and David"
    next_action3 = scene4_4
    text1 = "Champagne Spill and Freyr"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords3, text2, next_action2),
            (coords2, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)


def scene4_4():
    global scene4_3_
    scene4_3_ = True
    dialogues = [
        ("", ""),
        ("", "...David went off to the kitchen, where he was given the location of knives by Jasper. The truth of Annabeth lending them a change of attire is irrelevant."),
        ("", "What else happened at the same time?"),
         ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Cara and Evelyn"
    next_action2 = not_right
    text3 = "Gwen and Evelyn"
    next_action3 = scene4_5
    text1 = "Evelyn and Freyr"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords3, text1, next_action),
            (coords2, text2, next_action2),
            (coords1, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def scene4_5():
    global scene4_4_
    scene4_4_ = True
    dialogues = [
        ("", ""),
        ("", "Gwen must have caught sight of Evelyn and took the chance to continue her belittling. "),
        ("", "Then..."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "David went back to Cara"
    next_action2 = not_right
    text3 = "Gwen and Evelyn, Gwen was stopped"
    next_action3 = scene4_6
    text1 = "Evelyn and Freyr"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords3, text2, next_action2),
            (coords2, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def scene4_6():
    global scene4_5_
    scene4_5_ = True
    dialogues = [
        ("", ""),
        ("", "Evelyn mentioned a singular person, and it could only be Cara who stopped Gwen. David had already left, and Cara already showed to be protective over Evelyn, and Freyr showed up to bring Evelyn away."),
        ("", "Now, what likely happened next was..."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "David went back to Cara"
    next_action2 = not_right
    text3 = "Broken vase murder weapon"
    next_action3 = scene4_7
    text1 = "Knife in chest murder weapon"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords2, text1, next_action),
            (coords3, text2, next_action2),
            (coords1, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def scene4_7():
    global scene4_6_
    scene4_6_ = True
    dialogues = [
        ("", ""),
        ("", "Cara used the vase by the pedestal, and hit Gwen over the head, she is a good amount taller than her."),
        ("", "It was enough to kill Gwen. But that's not the end yet..."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Cara finds Annabeth"
    next_action2 = not_right
    text3 = "David went back, shards under head"
    next_action3 = scene4_8
    text1 = "Knife in chest"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def scene4_8():
    global scene4_7_
    scene4_7_ = True
    dialogues = [
        ("", ""),
        ("", "David came back, saw the scene, and in an attempt to hide the murder weapon to deflect attention, he swept the shards underneath Gwen's head."),
        ("", "He and Cara may argue, but a scandal upon one is a scandal upon both. He has a vested interest in covering the truth up."),
        ("", "That's not the only thing..."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Empty pedestal"
    next_action2 = not_right
    text3 = "Knife in chest"
    next_action3 = scene4_9
    text1 = "Broken vase shards"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords3, text1, next_action),
            (coords2, text2, next_action2),
            (coords2, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def scene4_9():
    global scene4_8_
    scene4_8_ = True
    dialogues = [
        ("", ""),
        ("", "He stabbed the knife into her chest, with the broken shards under her head, it was an attempt to completely deflect attention from the actual weapon."),
        ("", "The minimal bleeding from the chest gave it away however, as it was stabbed into her after she had died."),
        ("", "And the reason I know it was Cara who did the deed was because of Evelyn mentioning a singular person. At that point, David had already left Cara alone"),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Empty pedestal"
    next_action2 = not_right
    text3 = "Knife in chest"
    next_action3 = Conclusion_4
    text1 = "Broken vase shards"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords1, text1, next_action),
            (coords3, text2, next_action2),
            (coords2, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def Conclusion_4():
    global scene4_9_, Conclusion4
    scene4_9_ = True
    Conclusion4 = True
    
    dialogues = [
        ("", ""),
        ("", "The main clincher was that Gwen eavesdropped on Cara and David's argument, over an extremely touchy subject with high repercussions if it got out. And it was obvious that Gwen eavesdropped when she decided to show her face to mock Evelyn."),
        ("Conclusion 4", "Cara killed Gwen over anger that she eavesdropped and her treatment of Evelyn in front of her. Murder weapon being the vase used to hit her over the head."),
        ("Conclusion 4", "David left to the kitchen to get a knife, likely for the same reason, must have seen Gwen when he was leaving. When he got back, having a vested interest in keeping suspicions off of them both, he attempted to hide the actual weapon."),
        ("Conclusion 4", "He did this by sweeping the shards underneath Gwen's head, before planting a knife in her chest. Evelyn was not witness to the scene as Freyr had already led her away by then."),
        ("", "What a scenario..."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text8 = "Back"
    next_action8 = View_Info
    text9 = "Next"
    next_action9 = scene5_1

    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
    coords9 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
        
    choices = [

            (coords8, text8, next_action8),
            (coords9, text9, next_action9)
    ]

    display_choice(dialogues, choices)

def scene5_1():
    
    dialogues = [
        ("", ""),
        ("", "The scene has been drawn out, but I do still require some supporting evidence..."),
        ("", "Guests testimony, starting with the more innocent one. The champagne spill was likely true. And now Cara's dress..."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Knife in chest"
    next_action2 = not_right
    text3 = "Head wound and vase"
    next_action3 = scene5_2
    text1 = "Broken vase shards"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords3, text1, next_action),
            (coords1, text2, next_action2),
            (coords2, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def scene5_2():
    global scene5_1_
    scene5_1_ = True
    dialogues = [
        ("", ""),
        ("", "Yes... when she hit Gwen over the head, enough to actually kill her and the shards embedded itself into the scalp, there was definitely some blood splatter."),
        ("", "If the wine excuse was true, the blood was also needed. However, that's another can of worms that will not help, whether Annabeth was actively helping to hide the evidence."),
        ("", "David might have only gone to the kitchen for a knife, or might have actually spilled wine... I don't recall seeing wine stains there however..."),
        ("", "Speaking of david..."),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text2 = "Cara's dress"
    next_action2 = not_right
    text3 = "Guest testimony: David's gloves"
    next_action3 = Conclusion_5
    text1 = "David's argument"
    next_action = not_right
    text8 = "Back"
    next_action8 = View_Info

    coords1 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-20 , CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-20 -choice_box_height]
    coords2 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-2*20 - choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-2*20 - 2*choice_box_height]
    coords3 = [CANVAS_WIDTH - 20, CANVAS_HEIGHT-280-3*20 - 2*choice_box_height, CANVAS_WIDTH - 20 -choice_box_width, CANVAS_HEIGHT-280-3*20 - 3*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            (coords2, text1, next_action),
            (coords1, text2, next_action2),
            (coords3, text3, next_action3),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def Conclusion_5():
    global scene5_2_, Conclusion5
    scene5_2_ = True
    Conclusion5 = True
    
    dialogues = [
        ("", ""),
        ("", "He lifted the head to sweep the shards beneath, so it would stain his gloves bloody, requiring a change of gloves."),
        ("Supporting Evidence for Conclusion 4:", "Guests testimonies about the change of clothes. Both would have stained their clothes, dress for Cara, gloves for David, bloody."),
        ("", "(I think we've properly solved it. Let's go back and determine the killer.)"),
        ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()

    text8 = "Back"
    next_action8 = View_Info


    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
   
    choices = [

            (coords8, text8, next_action8),
            
    ]

    display_choice(dialogues, choices)


def not_right():
    dialogues = [
        ("", ""),
        ("", "No that doesn't seem right..."),
    ]
    canvas.delete("all")
    set_background_color("retry")
    DialogueBox()
    
    text7 = "Retry"

    if not(scene1_1_):
        next_action7 = connection
    elif not(scene1_2_):
        next_action7 = scene1_1
    elif not(scene1_3_):
        next_action7 = scene1_2
    elif not(scene2_1_):
        next_action7 = scene2_1
    elif not(scene2_2_):
        next_action7 = scene2_2
    elif not(scene2_3_):
        next_action7 = scene2_3
    elif not(scene2_4_):
        next_action7 = scene2_4
    elif not(scene3_1_):
        next_action7 = scene3_1
    elif not(scene3_2_):
        next_action7 = scene3_2
    elif not(scene4_1_):
        next_action7 = scene4_1
    elif not(scene4_2_):
        next_action7 = scene4_2
    elif not(scene4_3_):
        next_action7 = scene4_3
    elif not(scene4_4_):
        next_action7 = scene4_4
    elif not(scene4_5_):
        next_action7 = scene4_5
    elif not(scene4_6_):
        next_action7 = scene4_6
    elif not(scene4_7_):
        next_action7 = scene4_7
    elif not(scene4_8_):
        next_action7 = scene4_8
    elif not(scene4_9_):
        next_action7 = scene4_9
    elif not(scene5_1_):
        next_action7 = scene5_1
    elif not(scene5_2_):
        next_action7 = scene5_2

    text8 = "Back"
    next_action8 = View_Info
    coords7 = [CANVAS_WIDTH - norm_indent, norm_indent, CANVAS_WIDTH - (150 + norm_indent), 50 + norm_indent]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            # (coords1, text1, next_action),
            # (coords2, text2, next_action2),
            # (coords3, text3, next_action3),
            # (coords4, text4, next_action4),
            # (coords5, text5, next_action5),
            # (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    
    
    display_choice(dialogues, choices)

def killer():
    dialogues +=[
        ("", ""),
        ("", "The killer is..."),
    ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()
    text1 = "Annabeth Whitmore"
    next_action = next_action2 = next_action3 = next_action6 = next_action7 = not_right2
    text2 = "Rupert Davies"
    text3 = "Jasper Winters"
    text4 = "Cara Montgomery"
    text5 = "David Winston"
    text6 = "Evelyn Sinclair"
    text7 = "Freyr Blackwood"
    coords1 = [24, 50 + 2*norm_indent, 24+choice_box_width, 50 +2*norm_indent + choice_box_height]
    coords2 = [2*24+choice_box_width, 50 + 2*norm_indent, 2*(24+choice_box_width), 50 +2*norm_indent + choice_box_height]
    coords3 = [3*24+2*choice_box_width, 50 + 2*norm_indent, 3*(24+choice_box_width), 50 +2*norm_indent + choice_box_height]
    coords4 = [4*24+3*choice_box_width, 50 + 2*norm_indent, 4*(24+choice_box_width), 50 +2*norm_indent + choice_box_height]
    coords5 = [24, 50 + 3*norm_indent + choice_box_height, 24+choice_box_width, 50 + 3*norm_indent + 2*choice_box_height]
    coords6 = [2*24+choice_box_width, 50 + 3*norm_indent + choice_box_height,  2*(24+choice_box_width), 50 + 3*norm_indent + 2*choice_box_height]
    coords7 = [3*24+2*choice_box_width, 50 + 3*norm_indent + choice_box_height,  3*(24+choice_box_width), 50 + 3*norm_indent + 2*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
    text8 = "Back"
    next_action8 = View_Info

    next_action4 = end
    next_action5 = close
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def close():

    dialogues +=[
        ("", ""),
        ("", "Well... it makes some sense, but there is something missing..."),
    ]

    canvas.delete("all")
    set_background_color("scene2", custom_colors["light_blue"])
    DialogueBox()
    text1 = "Annabeth Whitmore"
    next_action = next_action2 = next_action3 = next_action6 = next_action7 = not_right2
    text2 = "Rupert Davies"
    text3 = "Jasper Winters"
    text4 = "Cara Montgomery"
    text5 = "David Winston"
    text6 = "Evelyn Sinclair"
    text7 = "Freyr Blackwood"
    coords1 = [24, 50 + 2*norm_indent, 24+choice_box_width, 50 +2*norm_indent + choice_box_height]
    coords2 = [2*24+choice_box_width, 50 + 2*norm_indent, 2*(24+choice_box_width), 50 +2*norm_indent + choice_box_height]
    coords3 = [3*24+2*choice_box_width, 50 + 2*norm_indent, 3*(24+choice_box_width), 50 +2*norm_indent + choice_box_height]
    coords4 = [4*24+3*choice_box_width, 50 + 2*norm_indent, 4*(24+choice_box_width), 50 +2*norm_indent + choice_box_height]
    coords5 = [24, 50 + 3*norm_indent + choice_box_height, 24+choice_box_width, 50 + 3*norm_indent + 2*choice_box_height]
    coords6 = [2*24+choice_box_width, 50 + 3*norm_indent + choice_box_height,  2*(24+choice_box_width), 50 + 3*norm_indent + 2*choice_box_height]
    coords7 = [3*24+2*choice_box_width, 50 + 3*norm_indent + choice_box_height,  3*(24+choice_box_width), 50 + 3*norm_indent + 2*choice_box_height]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
    text8 = "Back"
    next_action8 = View_Info

    next_action4 = end
    next_action5 = close
    choices = [
            (coords1, text1, next_action),
            (coords2, text2, next_action2),
            (coords3, text3, next_action3),
            (coords4, text4, next_action4),
            (coords5, text5, next_action5),
            (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    display_choice(dialogues, choices)

def end():
    dialogues += [
        ("", "The killer is Cara Montgomery."),
        ("", "Here's what happened."),
        ("", "She and David were having an argument about something incredibly touchy and scandolous if it ever got out, and they were eavesdropped on by Gwendolyn Beaumont, the victim."),
        ("", "When David left, he had already seen her, which explains his venture to the kitchen. At the same time, Gwen caught sight of her favourite target, Evelyn Sinclair and started hurling jeers at her in front of Cara, who has already shown to be protective over Evelyn."),
        ("", "Cara found out that their argument was overheard, and witnessed another round of Gwen's cruelty in front of her, leading her to snap."),
        ("", "First, she stopped Gwen from doing any further damage, and at the same time, Freyr arrived to help Evelyn back. Then, they were alone."),
        ("", "She picked up the vase from a nearby pedestal and smashed it over Gwen's head from the back, causing her death."),
        ("", "When David came back with the knife, he attempted to hide the actual weapon, as he has a vested interest in ensuring their 'innocence'."),
        ("", "He swept the shards under Gwen's head, and stuck the knife in her chest, to make it look like that was the cause of death."),
        ("", "David Winston was a direct accomplice, it is uncertain if Jasper Winters knew what he was going to use the knife for."),
        ("", "As for Annabeth Whitmore, the wine spill was most likely a lie, which meant she was privy to the ongoings at the time. And she must have seen the blood."),
        ("", "Unfortunately, the lack of wine spill at the scene of crime could indicate that the entire dress was covered in wine and not a dropped spilt on the floor. There is no way to tell if it was a lie, and if Annabeth Whitmore was in the know."),
        ("", "The case has been solved. Cara Montgomery is the killer, and David Winston is the accomplice."),
        ("", "(And yet, something feels wrong... I don't know what...)"),
    ]
    canvas.delete("all")
    set_background_color("retry")
    DialogueBox()
    display_dialogue(dialogues, ending)

def not_right2():
    dialogues = [
        ("", ""),
        ("", "No that doesn't seem right..."),
    ]
    canvas.delete("all")
    set_background_color("retry")
    DialogueBox()
    
    text7 = "Retry"
    text8 = "Back"
    next_action7 = killer
    next_action8 = View_Info
    coords7 = [CANVAS_WIDTH - norm_indent, norm_indent, CANVAS_WIDTH - (150 + norm_indent), 50 + norm_indent]
    coords8 = [norm_indent, norm_indent, 150 + norm_indent, 50 + norm_indent]
        
    choices = [
            # (coords1, text1, next_action),
            # (coords2, text2, next_action2),
            # (coords3, text3, next_action3),
            # (coords4, text4, next_action4),
            # (coords5, text5, next_action5),
            # (coords6, text6, next_action6),
            (coords7, text7, next_action7),
            (coords8, text8, next_action8)
    ]

    
    
    display_choice(dialogues, choices)

def ending():
    canvas.delete("all")
    set_background_color("main_menu")

    mainbox = box(mainx1, mainy1, mainx2, mainy2)
    font = 36

    # maintext = canvas.create_text(mainx1 + mainx1/4, mainy1 + MAIN_INDENT/2, text = "THANK YOU FOR PLAYING:", font=("Bookman Old Style", 32, "bold"), width=840, anchor = "nw")
    # maintext2 = canvas.create_text(mainx1 + mainx1/4, mainy1 + MAIN_INDENT + font, text = "ECHO: A VOICE UNHEARD", font=("Bookman Old Style", 32, "bold"), width=840, anchor = "nw")
    # maintext3 = canvas.create_text(mainx1 + mainx1/4,  mainy1 + 2*MAIN_INDENT + 2*font, text = "By Siew Yue Ying for CIP2024", font=("Bookman Old Style", 32, "bold"), width=840, anchor = "nw")
    # startbox = box(StartBoxX, StartBoxY, StartBoxX2, StartBoxY2)
    # starttext = text((mainx2 - mainx1)/2.5 + mainx1 -17, (mainy2 - mainy1)/2 + 1.8*mainy1, "CLICK TO START", 20, 800)
    maintext = canvas.create_text(
        mainx1 + mainx1 / 4, 
        mainy1 + MAIN_INDENT / 2, 
        text="THANK YOU FOR PLAYING:", 
        font=("Bookman Old Style", 28, "italic"), 
        width=840, 
        anchor="nw"
    )

    maintext2 = canvas.create_text(
        mainx1 + mainx1 / 4, 
        mainy1 + MAIN_INDENT + 80, 
        text="ECHO: A VOICE UNHEARD", 
        font=("Algerian", 50, "bold underline"), 
        fill="darkred", 
        width=840, 
        anchor="nw"
    )

    maintext3 = canvas.create_text(
        mainx1 + mainx1 / 4,  
        mainy1 + 2 * MAIN_INDENT + 150, 
        text="By Siew Yue Ying for CIP2024", 
        font=("Bookman Old Style", 24, "bold italic"), 
        width=840, 
        anchor="nw"
    )

def main():
    # global Jasper2, Annabeth2, Evie2, caraDavid2, caraDavid3, Group2
    # Jasper2 = True
    # Annabeth2 = True
    # caraDavid2 = True
    # caraDavid3 = True
    # Evie2 = True
    # Group2 = True
    mainmenu()
    # Body_1()
    # Jasper_post()
    # View_Info()
    # ending()



    root.mainloop()

if __name__ == '__main__':
    main()
