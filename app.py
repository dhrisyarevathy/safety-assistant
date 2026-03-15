import gradio as gr
import random
import time

# --- App 1: Safety Check ---
def safety_check(name):
    return "Hello " + name + " ✅ Area looks safe"

# --- App 2: Area Safety / SOS ---
def check_safety(lat, lon):
    safety = random.randint(1,10)
    crowd = random.choice(["Low","Medium","High"])
    police = random.choice([
        "Central Police Station",
        "Town Police Station",
        "Highway Patrol"
    ])
    hospital = random.choice([
        "District Hospital",
        "City Care Hospital",
        "General Hospital"
    ])
    status = "⚠ Area may be Unsafe" if safety <= 3 else "✅ Area Looks Safe"
    return f"""
📍 Location : {lat}, {lon}

🛡 Safety Score : {safety}/10
👥 Crowd Level : {crowd}

🚓 Nearest Police : {police}
🏥 Nearest Hospital : {hospital}

Status : {status}
"""

def send_sos(lat, lon):
    return f"""
🚨 EMERGENCY ALERT SENT 🚨

Live Location Shared:
Latitude : {lat}
Longitude : {lon}

Message sent to Emergency Contact
"""

# --- App 3: Live Tracking ---
tracking = False  # global tracking state

def get_live_location():
    lat = round(random.uniform(10.7, 10.9), 5)
    lon = round(random.uniform(76.5, 76.8), 5)
    return lat, lon

def start_tracking():
    global tracking
    tracking = True
    result = ""
    for i in range(10):  # simulate 10 updates
        if tracking == False:
            break
        lat, lon = get_live_location()
        safety = random.randint(1,10)
        crowd = random.choice(["Low","Medium","High"])
        alert = "🚨 UNSAFE AREA – ALERT SENT" if safety <= 3 else "✅ SAFE"
        result += f"""
Update {i+1}

Location : {lat}, {lon}
Safety Score : {safety}/10
Crowd : {crowd}
Status : {alert}

"""
        time.sleep(2)
    return result

def stop_tracking():
    global tracking
    tracking = False
    return "⛔ Tracking Stopped"

def sos_now():
    return """
🚨 EMERGENCY ALERT ACTIVATED
📍 Live location shared to emergency contact
☎ Calling nearest help service
"""

# --- Unified Gradio Interface ---
with gr.Blocks() as assistant:

    gr.Markdown("# 🌆 All-in-One Women & Child Safety Assistant")

    # --- Tab 1: Area Safety / SOS (now first) ---
    with gr.Tab("Area Safety / SOS"):
        lat_input = gr.Textbox(label="Latitude")
        lon_input = gr.Textbox(label="Longitude")
        output2 = gr.Textbox(lines=15, label="System Output")  # Bigger box
        gr.Button("Check Area Safety").click(check_safety, inputs=[lat_input, lon_input], outputs=output2)
        gr.Button("SOS Emergency").click(send_sos, inputs=[lat_input, lon_input], outputs=output2)

    # --- Tab 2: Safety Check (now second) ---
    with gr.Tab("Safety Check"):
        name_input = gr.Textbox(label="Enter Name")
        output1 = gr.Textbox(label="Result")
        gr.Button("Check Safety").click(safety_check, inputs=name_input, outputs=output1)

    # --- Tab 3: Live Tracking ---
    with gr.Tab("Live Tracking"):
        output3 = gr.Textbox(lines=20, label="System Status")
        gr.Button("▶ Start Live Tracking").click(start_tracking, outputs=output3)
        gr.Button("⛔ Stop Tracking").click(stop_tracking, outputs=output3)
        gr.Button("🚨 SOS Emergency").click(sos_now, outputs=output3)

assistant.launch()
