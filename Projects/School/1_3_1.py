import turtle as t
import textwrap

screen = t.Screen()
screen.bgpic("Github/Mohameds-Code-Library/Images/random/coverpage.png")
screen.listen()
name_writer = t.Turtle()
info_writer = t.Turtle()
story_writer = t.Turtle()
name_writer.hideturtle()
info_writer.hideturtle()
page = 0
names = []
infos = []
stories = []
#screen.bgpic("Github/Mohameds-Code-Library/Images/random/page.png")
def page_turn_left():
    global page
    page -= 1
def page_turn_right():
    global page
    page += 1
def page_turn_and_add():
    while True:
        screen.listen()
        screen.onkeypress(page_turn_left, "Left")
        screen.onkeypress(page_turn_right, "Right")
        screen.onkeypress(page_add, "r")
        pagenumber()
def pagenumber():
    global page
    newpage = page

    name_writer.teleport(0,270)
    info_writer.teleport(0,170)
    story_writer.teleport(-280 ,-200)
    if page > 0:
        screen.bgpic("Github/Mohameds-Code-Library/Images/random/page.png")
        name_writer.write(names[min(names.__len__() - 1, page - 1)],font = ["Arial", 25, "normal"])
        info_writer.write(infos[min(infos.__len__() - 1, page - 1)],font = ["Arial", 25, "normal"])
        storye = textwrap.fill(stories[min(stories.__len__() - 1, page - 1)], 30)
        story_writer.write(storye, font = ["Arial", 25, "normal"])
        if page > names.__len__() - 1:
            page = names.__len__()
    if newpage != page:
        screen.clear()
    if page <= 0:
        screen.bgpic("Github/Mohameds-Code-Library/Images/random/coverpage.png")
        page = 0
def page_info():
    

    file = open("Github/Mohameds-Code-Library/Projects/School/info.txt", "r")

    outerindex = 0

    for line in file:
        name = ""
        info = ""
        story = ""
        innerindex = 0

        while (line[innerindex] != "|"):
            name = name + line[innerindex]
            innerindex += 1

        names.append(name)
        innerindex += 1

        while (line[innerindex] != "|"):
            info = info + line[innerindex]
            innerindex += 1

        infos.append(info)
        innerindex += 1

        while (line[innerindex] != "þ"):
            story = story + line[innerindex]
            innerindex += 1

        stories.append(story)
        innerindex += 1
        outerindex += 1
def page_add():
    nameinput = t.textinput("name", "what is your name")
    infoinput = t.textinput("info", "what info do you want to be added,like your phone number for example")
    storyinput = t.textinput("story", "what story do you want to share")
    names.append(nameinput)
    infos.append(infoinput)
    stories.append(storyinput)
    file = open("Github/Mohameds-Code-Library/Projects/School/info.txt", "w")
    for index in range(len(names)):
        file.write(names[index] + "|" + str((infos[index])) + "|" + str((stories[index])) + "þ\n")
    file.close()


page_info()
page_turn_and_add()



t.mainloop()
