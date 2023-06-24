import tkinter as tk

def generate_story():
    noun = entry_noun.get()
    verb = entry_verb.get()
    adjective = entry_adjective.get()
    adverb = entry_adverb.get()
    
    story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}."
    label_story.config(text=story)

# Create the main window
window = tk.Tk()
window.title("Mad Libs!")

# Create input fields
label_noun = tk.Label(window, text="Noun:")
label_noun.pack()
entry_noun = tk.Entry(window)
entry_noun.pack()

label_verb = tk.Label(window, text="Verb:")
label_verb.pack()
entry_verb = tk.Entry(window)
entry_verb.pack()

label_adjective = tk.Label(window, text="Adjective:")
label_adjective.pack()
entry_adjective = tk.Entry(window)
entry_adjective.pack()

label_adverb = tk.Label(window, text="Adverb:")
label_adverb.pack()
entry_adverb = tk.Entry(window)
entry_adverb.pack()

# Create a label to display the generated story
label_story = tk.Label(window, text="")
label_story.pack()

# Create a button to generate the story
button_generate = tk.Button(window, text="Generate Story", command=generate_story)
button_generate.pack()


# Start the main event loop
window.mainloop()
