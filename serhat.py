import tkinter as tk
import random
import math

# === PENCERE ===
root = tk.Tk()
root.title("🎉 DOĞUM GÜNÜ ŞOVU 🎉")
root.geometry("920x540")
root.configure(bg="black")

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

WIDTH, HEIGHT = 920, 540

# === EMOJİLER ===
hearts = ["❤️", "💖", "💘", "💝", "💕"]
animals = ["🐶", "🐱", "🐰", "🐼", "🐾", "🐮"]
confetti_colors = ["red", "yellow", "cyan", "magenta", "orange", "lime"]

floating_particles = []
running_animals = []
confetti = []

# === 🎂 PASTA INTRO ===
cake = canvas.create_text(
    WIDTH // 2,
    HEIGHT // 2 - 30,
    text="🎂",
    font=("Arial", 120),
    fill="white"
)

cake_text = canvas.create_text(
    WIDTH // 2,
    HEIGHT // 2 + 80,
    text="İYİ Kİ DOĞDUN 🎉",
    font=("Courier", 28, "bold"),
    fill="white"
)

cake_scale = 1.0
cake_dir = 1

def animate_cake():
    global cake_scale, cake_dir
    cake_scale += 0.01 * cake_dir
    if cake_scale > 1.1 or cake_scale < 0.95:
        cake_dir *= -1

    canvas.itemconfig(cake, font=("Arial", int(120 * cake_scale)))
    root.after(40, animate_cake)

# === ANA GÖSTERİ ===
def start_show():
    canvas.delete(cake)
    canvas.delete(cake_text)
    create_main_text()
    animate_floating()
    animate_running_animals()
    animate_confetti()
    animate_text()

# === KALPLER (YAVAŞ YUKARI) ===
def create_floating():
    x = random.randint(0, WIDTH)
    y = HEIGHT + 30
    emoji = random.choice(hearts)
    size = random.randint(18, 26)
    speed = random.uniform(0.6, 1.2)
    item = canvas.create_text(x, y, text=emoji, font=("Arial", size))
    floating_particles.append((item, speed))

def animate_floating():
    for item, speed in floating_particles:
        canvas.move(item, 0, -speed)
        if canvas.coords(item)[1] < -20:
            canvas.coords(item, random.randint(0, WIDTH), HEIGHT + 30)
    if random.random() < 0.15:
        create_floating()
    root.after(40, animate_floating)

# === HAYVANLAR SAĞDAN SOLA ===
def create_running_animal():
    y = random.randint(60, HEIGHT - 60)
    animal = random.choice(animals)
    size = random.randint(22, 30)
    speed = random.uniform(2.5, 4.5)
    item = canvas.create_text(WIDTH + 40, y, text=animal, font=("Arial", size))
    running_animals.append((item, speed))

def animate_running_animals():
    for item, speed in running_animals:
        canvas.move(item, -speed, 0)
        if canvas.coords(item)[0] < -40:
            canvas.coords(item, WIDTH + 40, random.randint(60, HEIGHT - 60))
    if random.random() < 0.05:
        create_running_animal()
    root.after(30, animate_running_animals)

# === KONFETİ ===
def confetti_burst():
    cx = random.randint(200, WIDTH - 200)
    cy = random.randint(150, HEIGHT - 150)
    for _ in range(25):
        dx = random.uniform(-4, 4)
        dy = random.uniform(-4, 4)
        color = random.choice(confetti_colors)
        piece = canvas.create_oval(cx, cy, cx+4, cy+4, fill=color, outline="")
        confetti.append([piece, dx, dy])

def animate_confetti():
    for c in confetti:
        canvas.move(c[0], c[1], c[2])
        c[2] += 0.15
    if random.random() < 0.03:
        confetti_burst()
    root.after(40, animate_confetti)

# === MESAJ ===
def get_treatment():
    base = (
        "Tedavi Planı 💊:\n"
        "• Sınırsız mutluluk 🎈\n"
        "• Bol başarı ve huzur ✨\n"
        "• Hayvan sevgisi (ömür boyu) 🐾\n"
        "• Dostlarla kahkaha terapisi 😂\n"
    )
    if random.random() < 0.2:
        base += "• Kriz anlarında gizli pasta 🎂\n"
    return base

def create_main_text():
    global text_item
    message = (
        "🎉 DOĞUM GÜNÜ TESPİT EDİLDİ 🎉\n\n"
        "Lakap: POZ MEZIN 😎\n"
        "Veterinerlik Modu: AKTİF 🩺🐾\n\n"
        "• Hayvanlar güvende 🐶🐱🐮\n"
        "• Ortam kahkahada 😂\n"
        "• Kalpler stabil ❤️\n\n"
        "Teşhis:\n"
        "Aşırı iyi insan sendromu\n\n"
        f"{get_treatment()}\n"
        "İyi ki doğdun be kardeşim 💙"
    )

    text_item = canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2,
        text=message,
        font=("Courier", 16, "bold"),
        justify="center",
        fill="white"
    )

# === YAZI RENK + YANIP SÖNME ===
t = 0
visible = True

def animate_text():
    global t, visible
    t += 0.02
    r = int(127 + 127 * math.sin(t))
    g = int(127 + 127 * math.sin(t + 2))
    b = int(127 + 127 * math.sin(t + 4))
    color = f"#{r:02x}{g:02x}{b:02x}"
    visible = not visible
    canvas.itemconfig(text_item, fill=color if visible else "#222222")
    root.after(700, animate_text)

# === BAŞLAT ===
animate_cake()
root.after(3000, start_show)  # 3 saniye pasta, sonra şov
root.mainloop()
