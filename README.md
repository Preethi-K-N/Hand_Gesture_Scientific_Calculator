# ✋ Hand Gesture Scientific Calculator

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

## 🧠 **How It Works**

1.  **Hand Landmark Detection**: MediaPipe processes the webcam feed to detect a single hand and pinpoint 21 key **landmarks** on it.
2.  **Gesture Recognition**: Specifically, it tracks the positions of the **Thumb Tip (ID 4)** and **Index Finger Tip (ID 8)**.
3.  **"Pinch" Detection**: The Euclidean distance between these two finger tips is continuously calculated. If this distance falls below a predefined `pinch_threshold`, it's registered as a "pinch" gesture, simulating a button click.
4.  **Button Interaction**: When a pinch is detected, the coordinates of the index finger tip determine which calculator button is being "pressed."
5.  **Expression Evaluation**: The `expression` string is updated based on button presses. When the `=` button is "clicked," the `calculate_expression()` function securely evaluates the mathematical string using a controlled `eval()` environment, preventing arbitrary code execution.
6.  **Dynamic UI**: The calculator interface, including buttons, display, and an icon, is drawn directly onto the video frame using OpenCV. Visual feedback (button highlighting) is provided on hover and click.
7.  **Angle Mode Handling**: Trigonometric and inverse trigonometric functions dynamically adjust their behavior based on the `angle_mode` (radians or degrees), which can be toggled via a dedicated button.
8.  **Memory Functions**: `M+`, `M-`, `MR`, and `MC` buttons interact with a `memory` variable, allowing users to store and recall results.

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

*(Insert a screenshot or GIF of the scientific calculator UI in action here, similar to the original README's UI Preview)*

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

