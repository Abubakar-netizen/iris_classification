import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import joblib
import numpy as np
from datetime import datetime

# Load model
model = joblib.load("iris_model.pkl")

# Iris info with extended details
iris_info = {
    "Iris-setosa": "🌿 Iris-setosa:\n- Short and wide petals\n- Typically grows in Europe\n- Often bluish-purple in color",
    "Iris-versicolor": "🌺 Iris-versicolor:\n- Medium-sized petals\n- Petals range from blue to violet\n- Found in North America",
    "Iris-virginica": "🌸 Iris-virginica:\n- Long, narrow petals\n- Deep purple hues\n- Native to eastern U.S."
}

# Prediction function
def predict_species():
    try:
        values = [
            float(entry_sepal_length.get()),
            float(entry_sepal_width.get()),
            float(entry_petal_length.get()),
            float(entry_petal_width.get())
        ]

        if not (4.0 <= values[0] <= 8.5 and 1.5 <= values[1] <= 5.0 and
                1.0 <= values[2] <= 7.5 and 0.1 <= values[3] <= 2.6):
            raise ValueError("Values out of acceptable range")

        result = model.predict([values])[0]
        label_result.config(text=f"✅ Predicted Species: {result}", fg="green")
        messagebox.showinfo("Prediction", f"The model predicts: {result}")
    except Exception as e:
        messagebox.showerror("Error", f"Please enter valid values.\n\n{e}")

# Download results
def download_result():
    try:
        result = label_result.cget("text")
        values = {
            "Sepal Length": entry_sepal_length.get(),
            "Sepal Width": entry_sepal_width.get(),
            "Petal Length": entry_petal_length.get(),
            "Petal Width": entry_petal_width.get()
        }
        with open("iris_result.txt", "w") as f:
            f.write("🌼 Iris Prediction Result\n")
            f.write("-" * 35 + "\n")
            for k, v in values.items():
                f.write(f"{k}: {v} cm\n")
            f.write(f"\n{result}\nGenerated: {datetime.now()}\n")
        messagebox.showinfo("Saved", "Result saved to iris_result.txt")
    except:
        messagebox.showerror("Error", "Failed to save result.")

# Model detail popup
def show_model_details():
    win = tk.Toplevel(root)
    win.title("Model Details")
    win.geometry("400x320")
    tk.Label(win, text="📘 Model: RandomForestClassifier", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Label(win, text="🎯 Accuracy: 100% (on test set)", font=("Arial", 11)).pack()
    tk.Label(win, text="📊 Features Used:", font=("Arial", 11, "underline")).pack()
    tk.Label(win, text="- Sepal Length\n- Sepal Width\n- Petal Length\n- Petal Width", font=("Arial", 10)).pack(pady=5)
    tk.Label(win, text="🧠 Trained on 150 samples using Scikit-learn.\nSplit 80/20 for training/testing.\nModel saved as iris_model.pkl", wraplength=350, font=("Arial", 9)).pack()
    tk.Label(win, text="🔬 By Abubakar Awan", font=("Arial", 10, "italic")).pack(pady=10)

# Save feedback
def save_feedback():
    fb = feedback_box.get("1.0", tk.END).strip()
    if fb:
        with open("feedback.txt", "a") as f:
            f.write(f"{datetime.now()}\n{fb}\n{'-'*40}\n")
        feedback_box.delete("1.0", tk.END)
        messagebox.showinfo("Thanks", "Feedback submitted!")
    else:
        messagebox.showwarning("Empty", "Feedback is empty!")

# Reset inputs
def clear_inputs():
    entry_sepal_length.delete(0, tk.END)
    entry_sepal_width.delete(0, tk.END)
    entry_petal_length.delete(0, tk.END)
    entry_petal_width.delete(0, tk.END)
    label_result.config(text="", fg="blue")

# --- GUI Setup ---
root = tk.Tk()
root.title("🌸 Iris Flower Classifier")
root.geometry("530x770")
root.configure(bg="#fdf6f0")

flower_icon = ImageTk.PhotoImage(Image.open("flower.png"))
root.iconphoto(False, flower_icon)

# --- Title ---
tk.Label(root, text="🌼 Iris Flower Classifier", font=("Arial", 20, "bold"), bg="#fdf6f0", fg="#3b3b3b").pack(pady=10)

# --- Input Frame ---
frame = tk.LabelFrame(root, text="Enter Flower Dimensions (in cm)", bg="#ffffff", fg="#4a4a4a", font=("Arial", 11, "bold"))
frame.pack(pady=10, padx=20, fill="both")

def create_labeled_entry(parent, label_text, default):
    tk.Label(parent, text=label_text, font=("Arial", 10), bg="#ffffff").pack(pady=(5, 0))
    entry = tk.Entry(parent, font=("Arial", 11), justify="center", fg="black")
    entry.insert(0, default)
    entry.pack()
    tk.Label(parent, text=f"e.g., {default} (valid)", font=("Arial", 8), fg="gray", bg="#ffffff").pack(pady=(0, 4))
    return entry

entry_sepal_length = create_labeled_entry(frame, "Sepal Length (cm)", "5.1")
entry_sepal_width  = create_labeled_entry(frame, "Sepal Width (cm)", "3.5")
entry_petal_length = create_labeled_entry(frame, "Petal Length (cm)", "1.4")
entry_petal_width  = create_labeled_entry(frame, "Petal Width (cm)", "0.2")

# --- Predict + Reset Buttons ---
btn_frame = tk.Frame(root, bg="#fdf6f0")
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="🌟 Predict", command=predict_species, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), width=15).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="🔄 Reset", command=clear_inputs, bg="#FF5252", fg="white", font=("Arial", 11, "bold"), width=10).grid(row=0, column=1)

# --- Prediction Result ---
label_result = tk.Label(root, text="", font=("Arial", 13, "bold"), bg="#fdf6f0", fg="blue")
label_result.pack(pady=5)

# --- Divider ---
tk.Label(root, text="―" * 80, fg="#cccccc", bg="#fdf6f0").pack()

# --- Dropdown Info ---
tk.Label(root, text="Learn About Iris Species:", font=("Arial", 11, "bold"), bg="#fdf6f0").pack()
species_var = tk.StringVar()
species_dropdown = ttk.Combobox(root, textvariable=species_var, values=list(iris_info.keys()), font=("Arial", 11))
species_dropdown.set("Choose a species")
species_dropdown.pack(pady=5)

info_label = tk.Label(root, text="", bg="#fdf6f0", font=("Arial", 9), wraplength=450, justify="center", fg="#444")
info_label.pack()

def update_info(event):
    selected = species_var.get()
    info_label.config(text=iris_info.get(selected, ""))

species_dropdown.bind("<<ComboboxSelected>>", update_info)

# --- Action Buttons ---
action_frame = tk.Frame(root, bg="#fdf6f0")
action_frame.pack(pady=10)
tk.Button(action_frame, text="💾 Download Result", command=download_result, bg="#2196F3", fg="white", font=("Arial", 10)).grid(row=0, column=0, padx=10)
tk.Button(action_frame, text="📘 Model Info", command=show_model_details, bg="#9C27B0", fg="white", font=("Arial", 10)).grid(row=0, column=1, padx=10)

# --- Feedback Section ---
tk.Label(root, text="💬 Feedback", font=("Arial", 11, "bold"), bg="#fdf6f0").pack(pady=5)
feedback_box = tk.Text(root, height=4, width=55, font=("Arial", 10))
feedback_box.pack(pady=5)
tk.Button(root, text="Submit Feedback", command=save_feedback, bg="#FF9800", fg="white", font=("Arial", 10, "bold")).pack()

# --- Footer ---
tk.Label(root, text="Made with ❤️ by Abubakar Awan", font=("Arial", 9, "italic"), bg="#fdf6f0", fg="#777").pack(pady=10)

# --- Run GUI ---
root.mainloop()
