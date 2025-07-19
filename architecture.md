## 🧠 Hand Gesture Calculator System Architecture

### 🎯 _**Overview**_

- A real-time, computer vision-based calculator that interprets hand gestures using a webcam.
- It detects a pinch gesture (thumb + index finger) to simulate button presses and performs either basic or scientific calculations.
- All interaction is done touch-free using OpenCV and MediaPipe.

---

## 🏗️ _**Architecture Diagram**_

```plaintext
                +------------------+
                |     Webcam       |
                +--------+---------+
                         |
                         v
           +-------------------------------+
           |   MediaPipe Hands (21 Points) |
           +-------------------------------+
                          |
                          v
        +---------------------------------------+
        | Pinch Detection (Thumb & Index Finger)|
        +---------------------------------------+
                          |
                          v
               +-------------------------+
               | Button Press Detection  |
               +-------------------------+
                          |
                          v
          +----------------------------------+
          |     Scientific Calculator Logic  |
          | (Trig, Log, Power, Memory, Modes)|
          +----------------------------------+
                         |
                         v
           +-------------------------+
           |  Expression Evaluation  |
           +-------------------------+
                         |
                         v
           +-------------------------+
           | Visual Output on Frame  |
           +-------------------------+

```
---

## ⚡️ _**Key Components**_

| Component              | Purpose                                                                                 |
| :--------------------- | :-------------------------------------------------------------------------------------- |
| Webcam Feed            | Captures real-time video input for gesture tracking                                     |
| MediaPipe Hands        | Detects 21 hand landmarks to track thumb and index finger                               |
| Pinch Detection        | Calculates distance between thumb and index tip to simulate button press                |
| Button Detection       | Checks for intersections between finger and calculator buttons                          |
| Scientific Calculator  | Performs advanced functions (sin, cos, tan, log, sqrt, power, memory, angle modes, etc.)|
| Expression Evaluator   | Parses and calculates expressions using math module                                     |
| Visual Feedback        | Displays current expression and results on screen                                       |

---

## ✅ _**Benefits**_

* ✋ Fully touchless — gesture-based input using just a webcam
* 🖥️ Clean, interactive calculator interface rendered in real-time
* 🧠 Scientific mode with safe evaluation of complex math expressions
* 🔄 Easily extendable for more gestures or voice commands
* ♿ Ideal for accessibility, smart environments, or public use kiosks
