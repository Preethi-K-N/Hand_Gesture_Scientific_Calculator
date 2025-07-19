import cv2
import mediapipe as mp
import math
import numpy as np

# Global variables for calculator state
expression = ''
memory = 0.0  # Stores the value in calculator memory
angle_mode = 'radians' # 'radians' or 'degrees'

# --- Helper Functions for Expression Evaluation ---
# These functions wrap math module functions to handle angle mode conversion
# and are exposed to the eval() environment for safer and controlled execution.

def _sin(x):
    """Calculates sine, converting degrees to radians if angle_mode is 'degrees'."""
    return math.sin(math.radians(x)) if angle_mode == 'degrees' else math.sin(x)

def _cos(x):
    """Calculates cosine, converting degrees to radians if angle_mode is 'degrees'."""
    return math.cos(math.radians(x)) if angle_mode == 'degrees' else math.cos(x)

def _tan(x):
    """Calculates tangent, converting degrees to radians if angle_mode is 'degrees'."""
    return math.tan(math.radians(x)) if angle_mode == 'degrees' else math.tan(x)

def _asin(x):
    """Calculates arcsin, converting result to degrees if angle_mode is 'degrees'."""
    try:
        result = math.asin(x)
        return math.degrees(result) if angle_mode == 'degrees' else result
    except ValueError:
        return float('nan') # Return NaN for domain errors (e.g., asin(2))

def _acos(x):
    """Calculates arccos, converting result to degrees if angle_mode is 'degrees'."""
    try:
        result = math.acos(x)
        return math.degrees(result) if angle_mode == 'degrees' else result
    except ValueError:
        return float('nan') # Return NaN for domain errors

def _atan(x):
    """Calculates arctan, converting result to degrees if angle_mode is 'degrees'."""
    result = math.atan(x)
    return math.degrees(result) if angle_mode == 'degrees' else result

def _sinh(x):
    """Calculates hyperbolic sine."""
    return math.sinh(x)

def _cosh(x):
    """Calculates hyperbolic cosine."""
    return math.cosh(x)

def _tanh(x):
    """Calculates hyperbolic tangent."""
    return math.tanh(x)

def _sqrt(x):
    """Calculates square root."""
    return math.sqrt(x)

def _log(x):
    """Calculates natural logarithm (ln)."""
    return math.log(x)

def _log10(x):
    """Calculates base-10 logarithm (log10)."""
    return math.log10(x)

def _factorial_wrapper(x):
    """Calculates factorial, ensuring input is a non-negative integer."""
    if not isinstance(x, (int, float)) or x < 0 or not x.is_integer():
        raise ValueError("Factorial input must be a non-negative integer")
    return math.factorial(int(x))

def calculate_expression(expr):
    """
    Calculates the result of the given mathematical expression.
    Uses a controlled environment for eval() to include custom functions.
    """
    global memory, angle_mode # Not directly modified here, but used by helper functions
    try:
        # Define a safe dictionary for eval's scope
        # This prevents arbitrary code execution and provides our custom functions
        safe_dict = {
            'math': math, # Allow access to math module directly for constants like math.pi
            'sqrt': _sqrt,
            'log': _log,
            'log10': _log10,
            'pi': math.pi, # Direct constant
            'e': math.e,   # Direct constant
            'cosh': _cosh,
            'tanh': _tanh,
            'sinh': _sinh,
            'sin': _sin,
            'cos': _cos,
            'tan': _tan,
            'asin': _asin,
            'acos': _acos,
            'atan': _atan,
            'fact': _factorial_wrapper,
            # Add other functions/constants as needed
        }

        # Replace custom operators/constants with eval-compatible ones
        expr = expr.replace('x^y', '**')
        expr = expr.replace('x^2', '**2')
        expr = expr.replace('x^3', '**3')
        expr = expr.replace('2pi', '(2 * math.pi)') # Ensure 2pi is evaluated as 2 * pi
        expr = expr.replace('%', '/100') # Percentage as division by 100

        # Evaluate the expression using the safe dictionary
        result = eval(expr, {"__builtins__": None}, safe_dict)
        return str(result)
    except Exception as e:
        # Catch specific math errors for better feedback
        if isinstance(e, ValueError) and ("domain error" in str(e) or "math domain error" in str(e)):
            return "Domain Error"
        if isinstance(e, ZeroDivisionError):
            return "Div by Zero"
        return "Error" # Generic error for other issues

def insert_value(val):
    """
    Appends a value (button label) to the current expression.
    """
    global expression
    # Prevent appending to an 'Error' or 'nan' state directly
    if expression == "Error" or expression == "Domain Error" or expression == "Div by Zero" or expression == "nan":
        expression = val
    else:
        expression += val

def clear_expression():
    """
    Clears the entire expression.
    """
    global expression
    expression = ''

# Hand detection setup using MediaPipe
mp_hands = mp.solutions.hands
# Initialize MediaPipe Hands with improved confidence thresholds
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Finger tip IDs for gesture detection (MediaPipe landmark indices)
tip_ids = [4, 8, 12, 16, 20] # Thumb, Index, Middle, Ring, Pinky

# Button Layout - Redesigned to match the desired black-themed scientific calculator layout
# Added memory functions (M+, M-, MR, MC) and angle mode toggle (DEG/RAD)
# Replaced '!' with 'fact(' and 'deg', 'rad' with 'asin(', 'acos(', 'atan('
buttons = [
    ['C', 'CE', 'sqrt(', '+', 'pi', 'cos(', 'tan(', 'sin('],
    ['1', '2', '3', '-', '2pi', 'cosh(', 'tanh(', 'sinh('],
    ['4', '5', '6', '*', 'ln(', 'asin(', 'acos(', 'atan('],
    ['7', '8', '9', '/', 'log10(', '(', ')', 'fact('],
    ['0', '.', '%', '=', 'CLR', 'x^y', 'x^2', 'x^3'],
    ['M+', 'M-', 'MR', 'MC', 'DEG/RAD', '', '', ''] # New row for memory and angle mode
]

# Button size and spacing - Adjusted for the new layout with more buttons
button_w = 100  # Width of each button
button_h = 60   # Height of each button
padding_x = 10  # Horizontal spacing between buttons
padding_y = 10  # Vertical spacing between button rows
display_h = 120 # Height of the expression display area

def draw_buttons(frame):
    """
    Draws all calculator buttons on the frame.
    """
    start_y = display_h + 30 # Buttons start below the display and icon area
    for i, row in enumerate(buttons):
        for j, label in enumerate(row):
            # Calculate button position
            x = j * (button_w + padding_x) + 10
            y = i * (button_h + padding_y) + start_y
            
            # Draw button background (dark grey)
            cv2.rectangle(frame, (x, y), (x + button_w, y + button_h), (30, 30, 30), -1)
            # Draw button border (light grey)
            cv2.rectangle(frame, (x, y), (x + button_w, y + button_h), (100, 100, 100), 2)

            # Text color (white)
            text_color = (255, 255, 255)
            font_scale = 0.8 # Smaller font scale for more buttons
            font_thickness = 2

            # Adjust text position for centering
            text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)[0]
            text_x = x + (button_w - text_size[0]) // 2
            text_y = y + (button_h + text_size[1]) // 2

            cv2.putText(frame, label, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, font_thickness)

def detect_button_click(x, y):
    """
    Detects which button, if any, was clicked based on the given coordinates.
    """
    start_y = display_h + 30 # Same starting Y as in draw_buttons
    for i, row in enumerate(buttons):
        for j, label in enumerate(row):
            bx = j * (button_w + padding_x) + 10
            by = i * (button_h + padding_y) + start_y
            # Check if coordinates fall within a button's bounds
            if bx < x < bx + button_w and by < y < by + button_h:
                return label
    return None

# Start camera capture
cap = cv2.VideoCapture(0)
# Create a named window and resize it to fit the new UI
cv2.namedWindow("Scientific Calculator", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Scientific Calculator", 900, 700) # Window size adjusted for more buttons

prev_label = None # Stores the previously clicked button label to prevent rapid multiple clicks
cooldown = 0 # Cooldown counter to prevent rapid clicks
cooldown_frames = 20 # Number of frames to wait before another click is registered (adjust as needed)

# Threshold for detecting a "pinch" gesture (distance between thumb tip and index finger tip)
pinch_threshold = 50 # This value might need to be tuned based on your webcam and hand size.

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1) # Flip frame horizontally for a mirror effect
    frame = cv2.resize(frame, (900, 700)) # Ensure consistent frame size

    # Convert frame to RGB for MediaPipe processing
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    # Draw the overall black background for the calculator UI
    cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 0), -1)

    # Draw calculator icon (simple white rectangle with internal elements)
    icon_x, icon_y = 20, 20
    icon_size = 80
    cv2.rectangle(frame, (icon_x, icon_y), (icon_x + icon_size, icon_y + icon_size), (255, 255, 255), 2) # Outer border
    cv2.rectangle(frame, (icon_x + 10, icon_y + 10), (icon_x + icon_size - 10, icon_y + 30), (255, 255, 255), -1) # Display part
    # Draw small buttons inside the icon for visual effect
    for k in range(3):
        for l in range(3):
            cv2.rectangle(frame, (icon_x + 10 + l * 20, icon_y + 40 + k * 15), (icon_x + 20 + l * 20, icon_y + 45 + k * 15), (255, 255, 255), -1)

    # Draw the expression display area (black background with light grey border)
    display_border_thickness = 2
    display_start_x = icon_x + icon_size + 20
    display_end_x = frame.shape[1] - 20
    display_start_y = 20
    display_end_y = display_h - 20
    
    cv2.rectangle(frame, (display_start_x, display_start_y), (display_end_x, display_end_y), (0, 0, 0), -1) # Inner black
    cv2.rectangle(frame, (display_start_x, display_start_y), (display_end_x, display_end_y), (100, 100, 100), display_border_thickness) # Light grey border

    # Display the expression text (green text)
    text_display_x = display_start_x + 10
    text_display_y = int(display_start_y + (display_end_y - display_start_y) / 2) + 10 # Vertically center text
    
    # Dynamically adjust font scale for the expression display to prevent overflow
    font_scale_display = 1.0
    text_width, text_height = cv2.getTextSize(expression, cv2.FONT_HERSHEY_SIMPLEX, font_scale_display, 2)[0]
    
    max_text_width = (display_end_x - display_start_x) - 20 # Available width with padding
    if text_width > max_text_width:
        font_scale_display = max_text_width / text_width * font_scale_display * 0.9 # Reduce proportionally
        # Recalculate text size with new font scale
        text_width, text_height = cv2.getTextSize(expression, cv2.FONT_HERSHEY_SIMPLEX, font_scale_display, 2)[0]

    cv2.putText(frame, expression, (text_display_x, text_display_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale_display, (0, 255, 0), 2)

    # Display Angle Mode (RAD/DEG)
    angle_mode_text = angle_mode.upper() # "RADIANS" or "DEGREES"
    cv2.putText(frame, angle_mode_text, (frame.shape[1] - 100, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2) # Yellow text

    # Display Memory value (optional, for debugging or user info)
    # cv2.putText(frame, f"M: {memory:.2f}", (frame.shape[1] - 100, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 165, 0), 1)

    # Draw all calculator buttons
    draw_buttons(frame)

    # Process hand landmarks if detected
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            # Draw hand landmarks and connections
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            
            lm_list = []
            h, w, c = frame.shape
            # Extract landmark coordinates
            for id, lm in enumerate(handLms.landmark):
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            # Get coordinates for thumb tip (landmark 4) and index finger tip (landmark 8)
            thumb_tip_x, thumb_tip_y = lm_list[tip_ids[0]]
            index_tip_x, index_tip_y = lm_list[tip_ids[1]]

            # Calculate Euclidean distance between thumb tip and index finger tip
            distance = math.hypot(index_tip_x - thumb_tip_x, index_tip_y - thumb_tip_y)

            # The "click" point will still be the index finger tip's position
            # This is the point that will determine which button is under the "pinch"
            ix, iy = index_tip_x, index_tip_y
            
            # Draw a circle on the index finger tip to visualize the interaction point
            cv2.circle(frame, (ix, iy), 10, (0, 255, 255), -1) # Yellow circle

            # Draw a line between thumb and index finger tips to visualize pinch distance
            cv2.line(frame, (thumb_tip_x, thumb_tip_y), (index_tip_x, index_tip_y), (255, 0, 0), 3) # Blue line

            # Check for button click if a "pinch" gesture is detected (distance below threshold)
            if distance < pinch_threshold: 
                label = detect_button_click(ix, iy) # Determine which button is under the index finger
                if label: # If a button is being pointed at by the index finger during a pinch
                    # Highlight the button being hovered over
                    start_y = display_h + 30
                    for i, row in enumerate(buttons):
                        for j, btn_label in enumerate(row):
                            if btn_label == label:
                                bx = j * (button_w + padding_x) + 10
                                by = i * (button_h + padding_y) + start_y
                                # Draw a slightly lighter grey background for hover effect
                                cv2.rectangle(frame, (bx, by), (bx + button_w, by + button_h), (50, 50, 50), -1)
                                # Draw a white border for hover effect
                                cv2.rectangle(frame, (bx, by), (bx + button_w, by + button_h), (255, 255, 255), 2)
                                
                                # Redraw text on the highlighted button
                                text_color = (255, 255, 255)
                                font_scale = 0.8
                                font_thickness = 2
                                text_size = cv2.getTextSize(btn_label, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)[0]
                                text_x = bx + (button_w - text_size[0]) // 2
                                text_y = by + (button_h + text_size[1]) // 2
                                cv2.putText(frame, btn_label, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, font_thickness)
                                break # Exit inner loops once the button is found and highlighted

                    # Process button click if it's a new label and cooldown is over
                    if label != prev_label and cooldown == 0:
                        if label == '=':
                            expression = calculate_expression(expression)
                        elif label == 'CLR' or label == 'C': # 'CLR' and 'C' both clear the expression
                            clear_expression()
                        elif label == 'CE': # Clear Entry: removes the last character or clears "Error"
                            if expression and expression not in ["Error", "Domain Error", "Div by Zero", "nan"]:
                                expression = expression[:-1]
                            else: # If it's an error/NaN, clear it completely
                                clear_expression()
                        elif label == 'M+':
                            try:
                                memory += float(expression)
                                expression = "" # Clear display after M+
                            except ValueError:
                                expression = "Error"
                        elif label == 'M-':
                            try:
                                memory -= float(expression)
                                expression = "" # Clear display after M-
                            except ValueError:
                                expression = "Error"
                        elif label == 'MR':
                            expression = str(memory)
                        elif label == 'MC':
                            memory = 0.0
                            expression = "" # Clear display after MC
                        elif label == 'DEG/RAD':
                            angle_mode = 'degrees' if angle_mode == 'radians' else 'radians'
                            expression = "" # Clear expression on mode change
                        else:
                            insert_value(label)
                        prev_label = label # Store current label as previous
                        cooldown = cooldown_frames # Reset cooldown
            else:
                prev_label = None # Reset prev_label if pinch is not detected

    # Decrease cooldown timer
    if cooldown > 0:
        cooldown -= 1

    # Display the frame
    cv2.imshow("Scientific Calculator", frame)

    # Exit loop if 'Esc' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release camera and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()