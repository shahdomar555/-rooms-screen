import tkinter as tk #عشان نرسم الوجهه
from tkinter import messagebox#عشان يطلع الرسايل
import random#عشان يختار عمود عشوائي ويلعب فيه
ROWS = 6  # عدد الصفوف
COLS = 7  # عدد الأعمدة
CELL_SIZE = 80  # حجم كل خلية
PLAYER_COLORS = ["#FF6B6B", "#FFD93D"]  # ألوان اللاعبين (أحمر فاتح وأصفر فاتح)
HUMAN = 0  # رقم اللاعب البشري
AI = 1     # رقم الذكاء الاصطناعي
#عشان نعرف نميزهم ونبدل بينهم

game_board = [[None for _ in range(COLS)] for _ in range(ROWS)] #مصفوفه فاضيه كلها ف الاول
current_player = HUMAN#الي هيبدا يلعب البشري
game_over = False#اللعبه لسه مخلصتش
# إنشاء نافذة اللعبة
root = tk.Tk()
root.title("Connect 4 - Human vs AI")

# إنشاء اللوحة (Canvas) ورسمها
canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="#4D96FF")  # خلفية زرقاء هادية
canvas.pack()

# رسم الدوائر (الخانات) على اللوحة
circles = []
for row in range(ROWS):
    row_list = []
    for col in range(COLS):#بنحط كل دايره ف مصفوفه
        x0 = col * CELL_SIZE + 10#بدايه الدايره من الشمال
        y0 = row * CELL_SIZE + 10
        x1 = x0 + CELL_SIZE - 20
        y1 = y0 + CELL_SIZE - 20
        oval = canvas.create_oval(x0, y0, x1, y1, fill="white", outline="#E0E0E0")  # بنحط كل دايره ف مصفوفه عشان نقدر نغير لونها 
        row_list.append(oval)#بنضيف الدايره للمصفوفه المؤقته
    circles.append(row_list)#بنضيف الصف كله للاساسيه
    # دالة التحقق من الفوز
def check_winner(player):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # 4 اتجاهات (عمودي، أفقي، مائل)
    for row in range(ROWS):
        for col in range(COLS):
            if game_board[row][col] == player:#لو الخانه للاعب بنفحص ونشوف
                for dr, dc in directions:
                    count = 1
                    for step in range(1, 4):
                        r, c = row + dr * step, col + dc * step#بنمشي خطوه خطوه بالاتجاه الي بنفحصه
                        if 0 <= r < ROWS and 0 <= c < COLS and game_board[r][c] == player:
                            count += 1#لقينا نفس اللاعب بنزود العدد
                        else:
                            break#لو مش نفس اللاعب او طلعنا برا اللوحه نوقف
                    if count == 4:
                        return True#لقينا 4 ع التوالي
    return False

# دالة التحقق هل اللوحة ممتلئة بالكامل
def is_board_full():
    return all(game_board[0][col] is not None for col in range(COLS))#بنشوف اول صف لو كله مليان يبقي اللوحه مليانه

# دالة لإسقاط القطعة في العمود المختار
def drop_piece(col):
    global current_player, game_over
    if game_over:
        return False#لو اللعب خلص ميعملش حاجه
        
    # نحط القرص في أول خانة فاضية من تحت
    for row in range(ROWS - 1, -1, -1):
        if game_board[row][col] is None:
            game_board[row][col] = current_player
            canvas.itemconfig(circles[row][col], fill=PLAYER_COLORS[current_player])#بنغير لون الدايره

            if check_winner(current_player):
                game_over = True
                messagebox.showinfo("Game Over", f"Player {current_player + 1} wins!")
                return True#لو كسب هيظهرله المسج

            if is_board_full():
                game_over = True
                messagebox.showinfo("Game Over", "It's a draw!")
                return True#لو مليانه هيظهر تعادل

            current_player = 1 - current_player  # تبديل اللاعب
            return True
    return False#لو مفيش مكان يحط فيه

# دالة حركة الذكاء الاصطناعي
def ai_move():
    global current_player
    if game_over:
        return

    available_cols = [col for col in range(COLS) if game_board[0][col] is None]#بنجيب كل الاعمده الي لسه مش مليانه
    if available_cols:
        col = random.choice(available_cols)#نختار عمود عشوائي
        if drop_piece(col):#نلعب
            if not game_over:
                current_player = HUMAN#نخلي الدور يرجع للبشري

# دالة استجابة للنقر على اللوحة (للبشري)
def player_click(event):
    if current_player == HUMAN and not game_over:
        col = event.x // CELL_SIZE#بنشوف العمود الي ضغط عليه
        if col >= COLS:
            return#لو ضغط برا منعملش حاجه
        if drop_piece(col):
            if not game_over:
                root.after(500, ai_move)  # بعد نص ثانية يلعب الذكاء الاصطناعي

# دالة إعادة تعيين اللعبة (Reset)
def reset_game():
    global game_board, current_player, game_over
    game_board = [[None for _ in range(COLS)] for _ in range(ROWS)]#نخلي المصفوفه فاضيه
    current_player = HUMAN#نرجع البشري يلعب
    game_over = False#نخلي اللعبه مش منتهيه

    # إعادة رسم الخانات للون الأبيض
    for row in range(ROWS):
        for col in range(COLS):
            canvas.itemconfig(circles[row][col], fill="white")

# إنشاء زر إعادة التشغيل
reset_button = tk.Button(root, text="Restart Game", command=reset_game, font=("Arial", 14),
                         bg="#6D597A", fg="white", activebackground="#9E768F")
reset_button.pack(pady=10)

# ربط النقر على اللوحة بدالة اللاعب
canvas.bind("<Button-1>", player_click)

# تشغيل البرنامج
root.mainloop()