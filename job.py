import tkinter as tk

def inputs(window):
    label_occupation =tk.Label(window,text="Occupation:")
    label_occupation.pack()
    entry_occupation=tk.Entry(window)
    entry_occupation.pack()

    label_Noun1 =tk.Label(window,text="First Noun:")
    label_Noun1.pack()
    entry_Noun1=tk.Entry(window)
    entry_Noun1.pack()

    label_Adjective1 =tk.Label(window,text="First Adjective:")
    label_Adjective1.pack()
    entry_Adjective1=tk.Entry(window)
    entry_Adjective1.pack()

    label_Adjective2 =tk.Label(window,text="Second Adjective:")
    label_Adjective2.pack()
    entry_Adjective2=tk.Entry(window)
    entry_Adjective2.pack()

    label_Noun2 =tk.Label(window,text="Second Noun:")
    label_Noun2.pack()
    entry_Noun2=tk.Entry(window)
    entry_Noun2.pack()


    label_Verb1 =tk.Label(window,text="First Verb:")
    label_Verb1.pack()
    entry_Verb1=tk.Entry(window)
    entry_Verb1.pack()

    label_Verb2 =tk.Label(window,text="Second Verb:")
    label_Verb2.pack()
    entry_Verb2=tk.Entry(window)
    entry_Verb2.pack()

    label_Noun3 =tk.Label(window,text="Third Noun:")
    label_Noun3.pack()
    entry_Noun3=tk.Entry(window)
    entry_Noun3.pack()

    label_Verb3 =tk.Label(window,text="Third Verb:")
    label_Verb3.pack()
    entry_Verb3=tk.Entry(window)
    entry_Verb3.pack()

    label_Noun4 =tk.Label(window,text="Fourth Noun:")
    label_Noun4.pack()
    entry_Noun4=tk.Entry(window)
    entry_Noun4.pack()

    return entry_occupation,entry_Noun1,entry_Adjective1,entry_Adjective2,entry_Noun2,entry_Verb1,entry_Verb2,entry_Noun3,entry_Verb3,entry_Noun4

def generate_story(entry_occupation,entry_Noun1,entry_Adjective1,entry_Adjective2,entry_Noun2,entry_Verb1,entry_Verb2,entry_Noun3,entry_Verb3,entry_Noun4,window):
    occupation=entry_occupation.get()
    Noun1=entry_Noun1.get()
    Adjective1=entry_Adjective1.get()
    Adjective2=entry_Adjective2.get()
    Noun2=entry_Noun2.get()
    verb1=entry_Verb1.get()
    verb2=entry_Verb2.get()
    Noun3=entry_Noun3.get()
    verb3=entry_Verb3.get()
    Noun4=entry_Noun4.get()

    # Create a label to display the generated story
    label_story = tk.Label(window, text="")
    label_story.pack()

    story=f"Today a {occupation} named {Noun1} came to our school to talk to us \
    about her job. She said the most important skill you need to know to do \
    her job is to be able to {verb1} around {Adjective1} {Noun2} (a) . She said it was easy \
    for her to learn her job because she loved to {verb2} when she was my \
    age--and that helps a lot! If you're considering her profession,\
    I hope you can be near (a) {Adjective2} {Noun3}. That's very important! \
    If you get too distracted in that situation you won't\
    be able to {verb3} next to (a) {Noun4} !"
    label_story.config(text=story)

