# iris_classification
it is trained model to classify iris .it is trained on dataset of 150 rows by 80 percent training dataset and 20 percent testing data.
# 🌸 Iris Flower Classifier GUI

A beautiful and interactive machine learning desktop application built with **Python (Tkinter)** to classify **Iris flower species** based on petal and sepal dimensions. Trained using **Random Forest Classifier**, the app allows users to predict species, view model insights, explore Iris types, download predictions, and provide feedback.



---

## 🚀 Features

- 🔍 **Predict Iris Species** using trained ML model
- 🎯 **100% Accuracy** on test dataset
- 📊 Accepts user input for:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- 📥 Save Prediction Results as `.txt`
- 📘 View detailed **Model Information**
- 🌺 Explore **Iris Species Info** via dropdown
- 💬 **Feedback** section to record user thoughts
- 🧼 Reset input fields
- 🎨 Enhanced UI with image icon, tooltips, colors

---

## 🧠 Model Details

- **Algorithm**: RandomForestClassifier (from Scikit-learn)
- **Dataset**: Built-in Iris Dataset (150 samples)
- **Train/Test Split**: 80/20
- **Accuracy**: 100% on test set
- **Features Used**:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width

---

## 🖥️ GUI Preview
![image](https://github.com/user-attachments/assets/8c1de829-d446-4777-86d7-6434e01ad5a1)
![image](https://github.com/user-attachments/assets/2aa816df-c776-448b-92c6-7163696abaaf)
![image](https://github.com/user-attachments/assets/b410d5cd-fafd-4715-99a8-4ea9801b7c7c)




---

## 📁 Project Structure

iris-classification/
│
├── iris_gui.py # Main GUI script
├── iris_model.pkl # Trained ML model
├── flower.png # Icon for window
├── iris_result.txt # Output file (generated)
├── feedback.txt # User feedback (generated)
├── README.md # Project documentation
└── requirements.txt # Required libraries



## ✅ Requirements

Install dependencies:

```bash
pip install -r requirements.txt
Contents of requirements.txt:
scikit-learn
numpy
pillow
▶️** How to Run**
Clone the repository:
git clone https://github.com/your-username/iris-classifier-gui.git
cd iris-classifier-gui

Run the GUI:
python iris_gui.py
💡 Sample Inputs
Sepal Length	Sepal Width	Petal Length	Petal Width	Predicted Species
5.1	3.5	1.4	0.2	Iris-setosa
6.0	2.2	4.0	1.0	Iris-versicolor
6.5	3.0	5.5	2.0	Iris-virginica

📢 Feedback
Have suggestions or want to contribute? Use the built-in feedback form or open an issue on GitHub!
🙌 Credits
Developed  by Abubakar Awan
University: FAST National University

