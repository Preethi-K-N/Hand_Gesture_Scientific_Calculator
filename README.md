# ✋ Hand Gesture Scientific Calculator

<img width="2816" height="1536" alt="Gemini_Generated_Image_m5lmafm5lmafm5lm" src="https://github.com/user-attachments/assets/fbc2801c-5a57-431f-9729-0cfecc0d7ad5" />


A real-time, touch-free scientific calculator operated through hand gestures detected via webcam. This project leverages **OpenCV** for video processing and **MediaPipe Hands** for robust hand and finger tracking, offering a futuristic and hygienic way to perform complex calculations.

🖐️ **Pinch to click!** No physical contact required.

---

## 💡 **Overview**

This project transforms your webcam into an interactive input device for a scientific calculator. By simply performing a "pinch" gesture (bringing your thumb and index finger together), you can select buttons and input calculations. It supports a wide array of scientific functions, memory operations, and even angle mode toggling (radians/degrees).

---

## 🚗 _**Key Applications**_
Ideal for:
-   **Enhanced Education**: Interactive STEM learning.
-   **Sterile Operations**: Touch-free calculations in sensitive environments.
-   **Advanced UI Demos**: Showcasing cutting-edge gesture control.
-   **Accessibility**: Hands-free access to complex math.
-   **Public Engagement**: Innovative interactive displays.

---

## 🚀 **Features**

| Feature                         | Description                                                                     | Status |
| :------------------------------ | :------------------------------------------------------------------------------ | :----- |
| **Webcam Input**                | Utilizes real-time video stream for gesture detection.                          | ✅     |
| **Pinch-to-Click Gesture**      | Recognizes thumb-to-index finger pinch for button activation.                   | ✅     |
| **Basic Arithmetic**            | Supports addition, subtraction, multiplication, and division.                   | ✅     |
| **Scientific Functions**        | Includes square root, logarithms (natural and base-10), powers (x^y, x^2, x^3). | ✅     |
| **Trigonometric Functions**     | Sine, Cosine, Tangent, and their inverse (arcsin, arccos, arctan).              | ✅     |
| **Hyperbolic Functions**        | Sinh, Cosh, Tanh.                                                               | ✅     |
| **Factorial**                   | `fact()` function for calculating factorials.                                   | ✅     |
| **Constants**                   | `pi` (π) and `e`.                                                               | ✅     |
| **Memory Operations**           | `M+`, `M-`, `MR` (Memory Recall), `MC` (Memory Clear).                          | ✅     |
| **Angle Mode Toggle**           | Switch between **Radians** and **Degrees** for trigonometric calculations.      | ✅     |
| **Clear Functions**             | `C` (Clear All), `CE` (Clear Entry / Backspace).                                | ✅     |
| **Error Handling**              | Displays "Error," "Domain Error," or "Div by Zero" for invalid operations.      | ✅     |
| **Intuitive UI**                | Organized button layout with visual feedback for clicks.                        | ✅     |

---

## 🛠️ **Technologies Used**

* **Python 3.9+**: The core programming language.
* **OpenCV (`opencv-python`)**: For real-time video capture, frame manipulation, and drawing the calculator UI.
* **MediaPipe Hands (`mediapipe`)**: A powerful framework for accurate hand landmark detection and tracking.
* **NumPy (`numpy`)**: Utilized for numerical operations, particularly in calculating distances between hand landmarks.
* **Python `math` Module**: Provides mathematical functions and constants for evaluating expressions.

---

Markdown

# ✋ Hand Gesture Scientific Calculator

A real-time, touch-free scientific calculator operated through hand gestures detected via webcam. This project leverages **OpenCV** for video processing and **MediaPipe Hands** for robust hand and finger tracking, offering a futuristic and hygienic way to perform complex calculations.

🖐️ **Pinch to click!** No physical contact required.

---

## 🚗 _**Key Applications**_
Ideal for:
-   **Enhanced Education**: Interactive STEM learning.
-   **Sterile Operations**: Touch-free calculations in sensitive environments.
-   **Advanced UI Demos**: Showcasing cutting-edge gesture control.
-   **Accessibility**: Hands-free access to complex math.
-   **Public Engagement**: Innovative interactive displays.

---

## 🚀 **Features**

| Feature                         | Description                                                                 | Status |
| :------------------------------ | :-------------------------------------------------------------------------- | :----- |
| **Webcam Input** | Utilizes real-time video stream for gesture detection.                      | ✅     |
| **Pinch-to-Click Gesture** | Recognizes thumb-to-index finger pinch for button activation.               | ✅     |
| **Basic Arithmetic** | Supports addition, subtraction, multiplication, and division.               | ✅     |
| **Scientific Functions** | Includes square root, logarithms (natural and base-10), powers (x^y, x^2, x^3). | ✅     |
| **Trigonometric Functions** | Sine, Cosine, Tangent, and their inverse (arcsin, arccos, arctan).        | ✅     |
| **Hyperbolic Functions** | Sinh, Cosh, Tanh.                                                           | ✅     |
| **Factorial** | `fact()` function for calculating factorials.                               | ✅     |
| **Constants** | `pi` (π) and `e`.                                                           | ✅     |
| **Memory Operations** | `M+`, `M-`, `MR` (Memory Recall), `MC` (Memory Clear).                   | ✅     |
| **Angle Mode Toggle** | Switch between **Radians** and **Degrees** for trigonometric calculations. | ✅     |
| **Clear Functions** | `C` (Clear All), `CE` (Clear Entry / Backspace).                          | ✅     |
| **Error Handling** | Displays "Error," "Domain Error," or "Div by Zero" for invalid operations. | ✅     |
| **Intuitive UI** | Organized button layout with visual feedback for clicks.                    | ✅     |

---

## 🛠️ **Technologies Used**

* **Python 3.9+**: The core programming language.
* **OpenCV (`opencv-python`)**: For real-time video capture, frame manipulation, and drawing the calculator UI.
* **MediaPipe Hands (`mediapipe`)**: A powerful framework for accurate hand landmark detection and tracking.
* **NumPy (`numpy`)**: Utilized for numerical operations, particularly in calculating distances between hand landmarks.
* **Python `math` Module**: Provides mathematical functions and constants for evaluating expressions.

---

## 🧠 **How It Works**

1.  **Hand Tracking**: MediaPipe detects 21 hand landmarks from webcam input.
2.  **Gesture-to-Click**: A "pinch" gesture (thumb-index tip proximity) is recognized as a button click.
3.  **UI Interaction**: The index finger's position during a pinch determines the selected calculator button.
4.  **Expression Processing**: Button presses update the display; pressing `=` triggers secure evaluation of the mathematical expression.
5.  **Dynamic Display**: OpenCV renders the calculator UI with real-time visual feedback (button highlighting).
6.  **Functionality**: Supports scientific calculations, angle mode toggling (radians/degrees), and memory operations, adapting behavior dynamically based on user input.

---

## ⚙️ **Setup and Execution**

### **Code Requirements**

* Python 3.9 or later
* A working virtual environment (`venv`) is highly recommended to manage dependencies.

### **Installation**

1.  **Clone the repository (if you haven't already from the main project):**
    ```bash
    git clone [https://github.com/Preethi-K-N/Hand_Gesture_Calculator-using_Normal_and_Scientific.git](https://github.com/Preethi-K-N/Hand_Gesture_Calculator-using_Normal_and_Scientific.git)
    cd Hand_Gesture_Calculator-using_Normal_and_Scientific
    ```
2.  **Navigate to the scientific calculator directory:**
    ```bash
    cd scientific_calculator
    ```
3.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    ```
4.  **Activate the virtual environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
5.  **Install the required libraries:**
    ```bash
    pip install opencv-python mediapipe numpy
    ```

### **Running the Calculator**

1.  **Ensure your virtual environment is activated.**
2.  **Execute the script:**
    ```bash
    python scientific_hand_gesture_calculator.py
    ```

---

## 📸 **UI Preview**

![Untitled video - Made with Clipchamp](https://github.com/user-attachments/assets/f0bc2cc1-1ebb-41e0-accc-387a89d09a94)

---

## ⚠️ **Important Notes**

* **`pinch_threshold`**: You might need to adjust the `pinch_threshold` variable in the `scientific_hand_gesture_calculator.py` script based on your webcam's distance, lighting conditions, and hand size to ensure optimal "pinch" detection.
* **Performance**: The performance can vary depending on your webcam quality and CPU capabilities.
* **Quit**: Press the `Esc` key to exit the calculator application at any time.

---

## 🗂️ **Project Structure (relevant to this file)**

```
Hand_Gesture_Scientific_Calculator
│
├── scientific_calculator/
│   └── scientific_hand_gesture_calculator.py # Scientific calculator with trigonometry, log, etc.
│
├── architecture.md                     # High-level architecture and system overview
├── requirements.txt                    # All required Python libraries for the project
└── README.md                           # Project documentation (this file)
```
---

## 📚 **References**

* [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands) – Hand landmark detection
* [OpenCV Documentation](https://docs.opencv.org/) – Real-time image processing and UI drawing
* [Python `math` Module](https://docs.python.org/3/library/math.html) – Used for evaluating scientific expressions

---

