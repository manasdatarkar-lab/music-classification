import tkinter as tk

# Function to show songs
def show_songs(mood):
    songs = {
        "happy": ["🎉 Kala Chashma", "😊 Gallan Goodiyan", "🎊 Jai Jai Shivshankar"],
        "sad": ["💔 Channa Mereya", "😢 Tum Hi Ho", "🥀 Agar Tum Saath Ho"],
        "energetic": ["🔥 Zinda", "💪 Sultan Title Track", "⚡ Malhari"],
        "calm": ["🌿 Iktara", "😌 Shayad", "🌙 Raabta"]
    }

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Songs for {mood.upper()} mood:\n\n")

    for song in songs[mood]:
        result_text.insert(tk.END, song + "\n")

# Create window
root = tk.Tk()
root.title("Music Mood Classifier 🎵")
root.geometry("500x400")
root.configure(bg="#1e1e2f")

# Heading
title = tk.Label(
    root,
    text="Music Mood Classifier 🎧",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=15)

# Instruction
label = tk.Label(
    root,
    text="Select Your Mood:",
    font=("Arial", 14),
    bg="#1e1e2f",
    fg="white"
)
label.pack(pady=10)

# Buttons Frame
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

# Mood Buttons
tk.Button(frame, text="😊 Happy", width=12, command=lambda: show_songs("happy")).grid(row=0, column=0, padx=10, pady=10)
tk.Button(frame, text="😢 Sad", width=12, command=lambda: show_songs("sad")).grid(row=0, column=1, padx=10, pady=10)
tk.Button(frame, text="🔥 Energetic", width=12, command=lambda: show_songs("energetic")).grid(row=1, column=0, padx=10, pady=10)
tk.Button(frame, text="😌 Calm", width=12, command=lambda: show_songs("calm")).grid(row=1, column=1, padx=10, pady=10)

# Result Box
result_text = tk.Text(root, height=10, width=50, font=("Arial", 12))
result_text.pack(pady=20)

# Run app
root.mainloop()