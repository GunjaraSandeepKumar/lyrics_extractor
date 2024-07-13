import tkinter as tk
from tkinter import messagebox
import lyricsgenius

# Function to fetch lyrics based on user input
def fetch_lyrics():
    # Get user input
    song_title = entry_song.get()
    artist_name = entry_artist.get()

    # Initialize LyricsGenius API
    genius = lyricsgenius.Genius("your_api_key_here")  # Replace with your API key

    try:
        # Search for lyrics
        song = genius.search_song(song_title, artist_name)
        if song is not None:
            # Display lyrics
            lyrics_text.delete('1.0', tk.END)  # Clear previous lyrics
            lyrics_text.insert(tk.END, song.lyrics)
        else:
            messagebox.showinfo("Error", "Lyrics not found for this song.")
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching lyrics: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Lyrics Extractor")

# Create GUI components
label_song = tk.Label(root, text="Song Title:")
label_song.pack()

entry_song = tk.Entry(root, width=40)
entry_song.pack()

label_artist = tk.Label(root, text="Artist:")
label_artist.pack()

entry_artist = tk.Entry(root, width=40)
entry_artist.pack()

btn_fetch = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics)
btn_fetch.pack()

lyrics_text = tk.Text(root, wrap=tk.WORD, width=60, height=20)
lyrics_text.pack()

# Function to get currently playing system song (example, not functional for all systems)
def get_current_song():
    # Replace with actual implementation to get currently playing song dynamically
    # For example, on Windows with a specific music player API

    # For demonstration, manually setting song details
    entry_song.insert(0, "Shape of You")
    entry_artist.insert(0, "Ed Sheeran")

# Call function to demonstrate (replace with actual implementation)
get_current_song()

# Start the GUI event loop
root.mainloop()
