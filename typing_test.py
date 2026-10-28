import tkinter as tk
import ctypes
from PIL import Image, ImageTk
import random


try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass



root = tk.Tk()
root.title("TypeFlow - Typing Speed Test")
root.geometry("1100x700")
root.minsize(1000, 650)


THEMES = {
    "light": {
        "bg": "#F9F8FF",
        "card": "#FFFFFF",
        "primary": "#7769D8",
        "primary_hover": "#685AC9",
        "text": "#292641",
        "secondary": "#77738C",
        "soft_purple": "#EAE7FF",
        "soft_blue": "#E8F3FF",
        "border": "#E7E4F2"
    },

    "dark": {
        "bg": "#171622",
        "card": "#211F30",
        "primary": "#9A8CF0",
        "primary_hover": "#8879E0",
        "text": "#F5F3FF",
        "secondary": "#AAA6BC",
        "soft_purple": "#302D49",
        "soft_blue": "#253044",
        "border": "#38344A"
    }
}

current_theme = "light"



main = tk.Frame(root)
main.pack(fill="both", expand=True)



def start_test():
    show_test_page()
    


def toggle_theme():

    global current_theme

    if current_theme == "light":
        current_theme = "dark"
    else:
        current_theme = "light"

    apply_theme()


def apply_theme():

    theme = THEMES[current_theme]

    root.configure(bg=theme["bg"])
    main.configure(bg=theme["bg"])

    header.configure(bg=theme["bg"])
    hero.configure(bg=theme["bg"])
    left_panel.configure(bg=theme["bg"])
    right_panel.configure(bg=theme["bg"])
    stats_frame.configure(bg=theme["bg"])
    footer.configure(bg=theme["bg"])

    logo.config(
        bg=theme["bg"],
        fg=theme["primary"]
    )

    small_heading.config(
        bg=theme["bg"],
        fg=theme["primary"]
    )

    heading.config(
        bg=theme["bg"],
        fg=theme["text"]
    )

    description.config(
        bg=theme["bg"],
        fg=theme["secondary"]
    )

    start_button.config(
        bg=theme["primary"],
        fg="white",
        activebackground=theme["primary_hover"],
        activeforeground="white"
    )

    theme_button.config(
        bg=theme["card"],
        fg=theme["text"],
        activebackground=theme["soft_purple"],
        activeforeground=theme["text"]
    )

    if current_theme == "light":
        theme_button.config(text="☾  Dark")
    else:
        theme_button.config(text="☀  Light")

    # Stats
    for number_label, text_label in stat_widgets:

        number_label.config(
            bg=theme["bg"],
            fg=theme["text"]
        )

        text_label.config(
            bg=theme["bg"],
            fg=theme["secondary"]
        )

    footer_text.config(
        bg=theme["bg"],
        fg=theme["secondary"]
    )

    


header = tk.Frame(main)
header.pack(
    fill="x",
    padx=65,
    pady=(35, 0)
)


logo = tk.Label(
    header,
    text="⌨  TypeFlow",
    font=("Segoe UI", 20, "bold")
)
logo.pack(side="left")


theme_button = tk.Button(
    header,
    text="☾  Dark",
    font=("Segoe UI", 10),
    relief="flat",
    bd=0,
    padx=18,
    pady=8,
    cursor="hand2",
    command=toggle_theme
)
theme_button.pack(side="right")



hero = tk.Frame(main)
hero.pack(
    fill="both",
    expand=True,
    padx=80,
    pady=(35, 20)
)



left_panel = tk.Frame(hero)
left_panel.pack(
    side="left",
    fill="both",
    expand=True
)


small_heading = tk.Label(
    left_panel,
    text="TYPING SPEED TEST",
    font=("Segoe UI", 12, "bold")
)
small_heading.pack(
    anchor="w",
    pady=(30, 12)
)


heading = tk.Label(
    left_panel,
    text="Improve your typing,\none word at a time.",
    font=("Segoe UI", 50, "bold"),
    justify="left"
)
heading.pack(anchor="w")


description = tk.Label(
    left_panel,
    text=(
        "A simple typing challenge designed to measure\n"
        "your speed, accuracy and typing performance."
    ),
    font=("Segoe UI", 17),
    justify="left"
)
description.pack(
    anchor="w",
    pady=(20, 30)
)


start_button = tk.Button(
    left_panel,
    text="Let's Go   →",
    font=("Segoe UI", 14, "bold"),
    relief="flat",
    bd=0,
    padx=38,
    pady=17,
    cursor="hand2",
    command=start_test
)
start_button.pack(anchor="w")


stats_frame = tk.Frame(left_panel)
stats_frame.pack(
    anchor="w",
    pady=(55, 0)
)


stats = [
    ("3", "Difficulty modes"),
    ("4", "Time options"),
    ("✓", "Instant results")
]

stat_widgets = []


for number, text in stats:

    box = tk.Frame(stats_frame)
    box.pack(
        side="left",
        padx=(0, 35)
    )

    number_label = tk.Label(
        box,
        text=number,
        font=("Segoe UI", 17, "bold")
    )
    number_label.pack(anchor="w")

    text_label = tk.Label(
        box,
        text=text,
        font=("Segoe UI", 10)
    )
    text_label.pack(anchor="w")

    stat_widgets.append(
        (number_label, text_label)
    )

    # Include box in theme updates
    stat_widgets[-1] = (
        number_label,
        text_label
    )



right_panel = tk.Frame(hero)
right_panel.pack(
    side="right",
    fill="both",
    expand=True
)

image_path = r"D:\TypingSpeedTest\Typing_Image(1).jpg"

typing_image = Image.open(image_path)
typing_image = typing_image.resize((750, 650))

typing_photo = ImageTk.PhotoImage(typing_image)

image_label = tk.Label(
    right_panel,
    image=typing_photo,
    bd=0
)

image_label.pack(expand=True)


footer = tk.Frame(main)
footer.pack(
    fill="x",
    padx=65,
    pady=(0, 25)
)


footer_text = tk.Label(
    footer,
    text="TypeFlow  •  Practice makes progress",
    font=("Segoe UI", 9)
)
footer_text.pack(side="left")



def update_frame_colors(widget):

    theme = THEMES[current_theme]

    for child in widget.winfo_children():

        if isinstance(child, tk.Frame):
            child.configure(bg=theme["bg"])
            update_frame_colors(child)


original_apply_theme = apply_theme


def apply_theme():

    original_apply_theme()

    update_frame_colors(stats_frame)

    theme = THEMES[current_theme]

    image_label.config(bg=theme["bg"])



apply_theme()


paragraphs = {
    "Easy": [
        "Practice makes us better every day. Typing is a useful skill that becomes easier with regular practice.",

        "Learning new things can be fun and exciting. Small steps every day can lead to great improvement.",

        "Technology helps people communicate and learn. Computers have become an important part of our daily lives."
    ],

    "Medium": [
        "Good typing skills can improve productivity and save valuable time. Regular practice helps develop speed, accuracy, and confidence while working on a computer.",

        "Technology continues to change the way people study, communicate, and work. Developing strong digital skills can help students become more confident and productive.",

        "Success does not always come from making huge changes. Consistent effort, patience, and regular practice can gradually produce meaningful improvements."
    ],

    "Hard": [
        "In today's rapidly evolving digital environment, efficient typing has become an essential skill. Developing accuracy, consistency, and speed requires focused practice and continuous improvement.",

        "Technological advancements have significantly transformed communication, education, and professional environments. Individuals who continuously develop their digital abilities are better prepared to adapt to emerging challenges.",

        "Productivity depends not only on completing tasks quickly but also on maintaining accuracy and concentration. Developing efficient working habits can significantly improve overall performance."
    ]
}

def show_test_page():

    for widget in main.winfo_children():
        widget.destroy()

    theme = THEMES[current_theme]

    main.configure(bg=theme["bg"])



    test_header = tk.Frame(main, bg=theme["bg"])
    test_header.pack(
        fill="x",
        padx=70,
        pady=(35, 20)
    )

    back_button = tk.Button(
        test_header,
        text="←  Back",
        font=("Segoe UI", 11),
        bg=theme["bg"],
        fg=theme["secondary"],
        activebackground=theme["bg"],
        activeforeground=theme["primary"],
        relief="flat",
        bd=0,
        cursor="hand2"
    )
    back_button.pack(side="left")

    tk.Label(
        test_header,
        text="⌨  TypeFlow",
        font=("Segoe UI", 16, "bold"),
        bg=theme["bg"],
        fg=theme["primary"]
    ).pack(side="right")



    tk.Label(
        main,
        text="Typing Challenge",
        font=("Segoe UI", 30, "bold"),
        bg=theme["bg"],
        fg=theme["text"]
    ).pack(pady=(10, 5))

    tk.Label(
        main,
        text="Choose your challenge and start typing when you're ready.",
        font=("Segoe UI", 11),
        bg=theme["bg"],
        fg=theme["secondary"]
    ).pack()



    settings_frame = tk.Frame(
        main,
        bg=theme["bg"]
    )

    settings_frame.pack(pady=25)




    mode_frame = tk.Frame(
        settings_frame,
        bg=theme["bg"]
    )

    mode_frame.pack(
        side="left",
        padx=30
    )

    tk.Label(
        mode_frame,
        text="Difficulty",
        font=("Segoe UI", 10, "bold"),
        bg=theme["bg"],
        fg=theme["text"]
    ).pack(anchor="w", pady=(0, 7))


    mode_var = tk.StringVar(value="Easy")

    mode_menu = tk.OptionMenu(
        mode_frame,
        mode_var,
        "Easy",
        "Medium",
        "Hard"
    )

    mode_menu.config(
        width=15,
        font=("Segoe UI", 10),
        bg=theme["card"],
        fg=theme["text"],
        activebackground=theme["soft_purple"],
        relief="flat",
        highlightthickness=0
    )

    mode_menu["menu"].config(
        font=("Segoe UI", 10)
    )

    mode_menu.pack()


    time_frame = tk.Frame(
        settings_frame,
        bg=theme["bg"]
    )

    time_frame.pack(
        side="left",
        padx=30
    )

    tk.Label(
        time_frame,
        text="Test Duration",
        font=("Segoe UI", 10, "bold"),
        bg=theme["bg"],
        fg=theme["text"]
    ).pack(anchor="w", pady=(0, 7))


    time_var = tk.StringVar(value="60 seconds")

    time_menu = tk.OptionMenu(
        time_frame,
        time_var,
        "30 seconds",
        "60 seconds",
        "2 minutes",
        "5 minutes"
    )

    time_menu.config(
        width=15,
        font=("Segoe UI", 10),
        bg=theme["card"],
        fg=theme["text"],
        activebackground=theme["soft_purple"],
        relief="flat",
        highlightthickness=0
    )

    time_menu["menu"].config(
        font=("Segoe UI", 10)
    )

    time_menu.pack()


    paragraph_card = tk.Frame(
        main,
        bg=theme["card"],
        highlightthickness=1,
        highlightbackground=theme["border"]
    )

    paragraph_card.pack(
        fill="x",
        padx=160,
        pady=(10, 15)
    )


    tk.Label(
        paragraph_card,
        text="TYPE THIS PARAGRAPH",
        font=("Segoe UI", 9, "bold"),
        bg=theme["card"],
        fg=theme["primary"]
    ).pack(
        anchor="w",
        padx=25,
        pady=(18, 8)
    )


    sample_paragraph = random.choice(paragraphs["Easy"])


    paragraph_label = tk.Label(
        paragraph_card,
        text=sample_paragraph,
        font=("Segoe UI", 12),
        bg=theme["card"],
        fg=theme["text"],
        wraplength=720,
        justify="left"
    )

    paragraph_label.pack(
        anchor="w",
        padx=25,
        pady=(0, 20)
    )

    def change_paragraph(*args):

        selected_mode = mode_var.get()

        new_paragraph = random.choice(
        paragraphs[selected_mode]
        )

        paragraph_label.config(text=new_paragraph)


    mode_var.trace_add(
        "write",
        change_paragraph
        )



    typing_frame = tk.Frame(
        main,
        bg=theme["bg"]
    )

    typing_frame.pack(
        fill="x",
        padx=160
    )


    tk.Label(
        typing_frame,
        text="Your typing",
        font=("Segoe UI", 10, "bold"),
        bg=theme["bg"],
        fg=theme["text"]
    ).pack(
        anchor="w",
        pady=(0, 7)
    )


    typing_box = tk.Text(
        typing_frame,
        height=5,
        font=("Segoe UI", 12),
        bg=theme["card"],
        fg=theme["text"],
        insertbackground=theme["primary"],
        relief="flat",
        bd=0,
        padx=18,
        pady=15,
        wrap="word"
    )

    typing_box.pack(fill="x")

    # User cannot type until Start is clicked
    typing_box.config(state="disabled")



    controls = tk.Frame(
        main,
        bg=theme["bg"]
    )

    controls.pack(
        fill="x",
        padx=160,
        pady=22
    )


    timer_label = tk.Label(
        controls,
        text="⏱  01:00",
        font=("Segoe UI", 16, "bold"),
        bg=theme["bg"],
        fg=theme["text"]
    )

    timer_label.pack(side="left")

    def update_timer_display(*args):

        selected_time = time_var.get()

        time_values = {
            "30 seconds": "00:30",
            "60 seconds": "01:00",
            "2 minutes": "02:00",
            "5 minutes": "05:00"
        }

        timer_label.config(
            text="⏱  " + time_values[selected_time]
        )


    time_var.trace_add(
        "write",
        update_timer_display
    )


    timer_running = False
    remaining_time = 60


    def get_selected_seconds():
        time_values = {
            "30 seconds": 30,
            "60 seconds": 60,
            "2 minutes": 120,
            "5 minutes": 300
        }

        return time_values[time_var.get()]


    def countdown():
        nonlocal remaining_time, timer_running

        if timer_running and remaining_time >= 0:

            minutes = remaining_time // 60
            seconds = remaining_time % 60

            timer_label.config(
                text=f"⏱  {minutes:02d}:{seconds:02d}"
            )

            if remaining_time == 0:
                stop_test()
                return

            remaining_time -= 1

            root.after(1000, countdown)


    def start_typing_test():
        nonlocal remaining_time, timer_running

    # Get selected test duration
        remaining_time = get_selected_seconds()
        timer_running = True

  
        typing_box.config(state="normal")
        typing_box.delete("1.0", "end")

        typing_box.focus_set()

        mode_menu.config(state="disabled")
        time_menu.config(state="disabled")

    
        start_button.config(state="disabled")

        countdown()


    def stop_test():
        nonlocal timer_running, remaining_time

        if not timer_running:
            return

        timer_running = False

    
        typed_text = typing_box.get("1.0", "end-1c")

    
        original_text = paragraph_label.cget("text")

    

        total_time = get_selected_seconds()
        time_used = total_time - remaining_time

        if time_used <= 0:
            time_used = 1


        typed_characters = len(typed_text)

        wpm = round(
            (typed_characters / 5) /
            (time_used / 60)
        )


        original_words = original_text.split()
        typed_words = typed_text.split()

        mistake_details = []
        correct_words = 0

        for i in range(len(typed_words)):

            if i < len(original_words):

                if typed_words[i] == original_words[i]:
                    correct_words += 1

                else:
                    mistake_details.append(
                        (original_words[i], typed_words[i])
                    )

            else:
                mistake_details.append(
                    ("—", typed_words[i])
                )

        mistakes = len(mistake_details)


        if len(typed_words) > 0:
            accuracy = round(
                (correct_words / len(typed_words)) * 100
            )
        else:
            accuracy = 0

        typing_box.config(state="disabled")

        show_result_page(
            wpm,
            accuracy,
            mistakes,
            time_used,
            mistake_details
        )

    stop_button = tk.Button(
        controls,
        text="Stop",
        font=("Segoe UI", 11, "bold"),
        bg=theme["card"],
        fg=theme["primary"],
            relief="flat",
        bd=0,
        padx=25,
        pady=10,
        cursor="hand2",
        command=stop_test
     )

    stop_button.pack(
        side="right",
        padx=(10, 0)
    )


    start_button = tk.Button(
        controls,
        text="Start Test",
        font=("Segoe UI", 11, "bold"),
        bg=theme["primary"],
        fg="white",
        activebackground=theme["primary_hover"],
        activeforeground="white",
        relief="flat",
        bd=0,
        padx=28,
        pady=10,
        cursor="hand2",
        command=start_typing_test
    )

    start_button.pack(side="right")

def show_result_page(wpm, accuracy, mistakes, time_used, mistake_details):

    # Remove Page 2
    for widget in main.winfo_children():
        widget.destroy()

    theme = THEMES[current_theme]
    main.configure(bg=theme["bg"])

    header = tk.Frame(
        main,
        bg=theme["bg"]
    )
    header.pack(
        fill="x",
        padx=70,
        pady=(20, 10)
    )

    tk.Label(
        header,
        text="⌨  TypeFlow",
        font=("Segoe UI", 16, "bold"),
        bg=theme["bg"],
        fg=theme["primary"]
    ).pack(side="left")

 

    tk.Label(
        main,
        text="Test Complete!",
        font=("Segoe UI", 30, "bold"),
        bg=theme["bg"],
        fg=theme["text"]
    ).pack(pady=(5, 3))

    tk.Label(
        main,
        text="Here's how you performed.",
        font=("Segoe UI", 11),
        bg=theme["bg"],
        fg=theme["secondary"]
    ).pack(pady=(0, 20))

  

    result_card = tk.Frame(
        main,
        bg=theme["card"],
        highlightthickness=1,
        highlightbackground=theme["border"]
    )

    result_card.pack(
        fill="x",
        padx=160,
        pady=(5, 12)
    )

    results = [
        ("⚡", wpm, "WPM"),
        ("🎯", f"{accuracy}%", "Accuracy"),
        ("✕", mistakes, "Mistakes"),
        ("⏱", f"{time_used}s", "Time")
    ]

    for icon, value, title in results:

        box = tk.Frame(
            result_card,
            bg=theme["card"]
        )

        box.pack(
            side="left",
            expand=True,
            padx=20,
            pady=25
        )

        tk.Label(
            box,
            text=icon,
            font=("Segoe UI", 16),
            bg=theme["card"],
            fg=theme["primary"]
        ).pack()

        tk.Label(
            box,
            text=str(value),
            font=("Segoe UI", 22, "bold"),
            bg=theme["card"],
            fg=theme["text"]
        ).pack(pady=(4, 0))

        tk.Label(
            box,
            text=title,
            font=("Segoe UI", 9),
            bg=theme["card"],
            fg=theme["secondary"]
        ).pack()



    try_again_button = tk.Button(
        main,
        text="Try Again  ↻",
        font=("Segoe UI", 11, "bold"),
        bg=theme["primary"],
        fg="white",
        activebackground=theme["primary_hover"],
        activeforeground="white",
        relief="flat",
        bd=0,
        padx=30,
        pady=11,
        cursor="hand2",
        command=show_test_page
    )

    try_again_button.pack(
        pady=(0, 15)
    )



    mistake_card = tk.Frame(
        main,
        bg=theme["card"],
        highlightthickness=1,
        highlightbackground=theme["border"]
    )

    mistake_card.pack(
        fill="x",
        padx=160,
        pady=(0, 15)
    )

    tk.Label(
        mistake_card,
        text="Mistake Details",
        font=("Segoe UI", 13, "bold"),
        bg=theme["card"],
        fg=theme["text"]
    ).pack(
        anchor="w",
        padx=25,
        pady=(15, 5)
    )

    if mistakes == 0:

        tk.Label(
            mistake_card,
            text="✓ Perfect! No mistakes found.",
            font=("Segoe UI", 11),
            bg=theme["card"],
            fg=theme["primary"]
        ).pack(
            anchor="w",
            padx=25,
            pady=(5, 20)
        )

    else:

        
        heading_frame = tk.Frame(
            mistake_card,
            bg=theme["soft_purple"]
        )

        heading_frame.pack(
            fill="x",
            padx=25,
            pady=(5, 5)
        )

        tk.Label(
            heading_frame,
            text="Expected",
            font=("Segoe UI", 10, "bold"),
            bg=theme["soft_purple"],
            fg=theme["text"],
            width=25,
            anchor="w"
        ).pack(
            side="left",
            padx=15,
            pady=7
        )

        tk.Label(
            heading_frame,
            text="You Typed",
            font=("Segoe UI", 10, "bold"),
            bg=theme["soft_purple"],
            fg=theme["text"],
            width=25,
            anchor="w"
        ).pack(
            side="left",
            padx=15,
            pady=7
        )

        for expected, typed in mistake_details[:5]:

            row = tk.Frame(
                mistake_card,
                bg=theme["card"]
            )

            row.pack(
                fill="x",
                padx=25
            )

            tk.Label(
                row,
                text=expected,
                font=("Segoe UI", 10),
                bg=theme["card"],
                fg=theme["text"],
                width=25,
                anchor="w"
            ).pack(
                side="left",
                padx=15,
                pady=4
            )

            tk.Label(
                row,
                text=typed,
                font=("Segoe UI", 10),
                bg=theme["card"],
                fg=theme["primary"],
                width=25,
                anchor="w"
            ).pack(
                side="left",
                padx=15,
                pady=4
            )

        

        if mistakes > 5:

            remaining_frame = tk.Frame(
                mistake_card,
                bg=theme["card"]
            )

            def show_more_mistakes():

    
                for expected, typed in mistake_details[5:]:

                    row = tk.Frame(
                        remaining_frame,
                        bg=theme["card"]
                    )

                    row.pack(fill="x")

                    tk.Label(
                        row,
                        text=expected,
                    font=("Segoe UI", 10),
                    bg=theme["card"],
                    fg=theme["text"],
                    width=25,
                    anchor="w"
                ).pack(
                    side="left",
                    padx=15,
                    pady=4
                )

                tk.Label(
                    row,
                    text=typed,
                    font=("Segoe UI", 10),
                    bg=theme["card"],
                    fg=theme["primary"],
                    width=25,
                    anchor="w"
                ).pack(
                    side="left",
                    padx=15,
                    pady=4
                )

            remaining_frame.pack(
                fill="x",
                padx=25
            )

            show_more_button.destroy()


        show_more_button = tk.Button(
            mistake_card,
            text=f"+ Show {mistakes - 5} more mistakes",
            font=("Segoe UI", 9, "bold"),
            bg=theme["card"],
            fg=theme["primary"],
            activebackground=theme["card"],
            activeforeground=theme["primary_hover"],
            relief="flat",
            bd=0,
            cursor="hand2",
            command=show_more_mistakes
        )

        show_more_button.pack(
            anchor="w",
            padx=35,
            pady=(5, 10)
        )
    

root.mainloop()