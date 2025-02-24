import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import scrolledtext

# Укажите полный путь к tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Открываем изображение
image_path = "image.png"
image = Image.open(image_path)

# Извлекаем текст
extracted_text = pytesseract.image_to_string(image)

# Создаем окно с помощью tkinter
root = tk.Tk()
root.title("Извлеченный текст")

# Создаем текстовое поле с прокруткой
text_area = scrolledtext.ScrolledText(root, width=160, height=80)
text_area.pack()

# Вставляем извлеченный текст в текстовое поле
text_area.insert(tk.END, extracted_text)

# Разрешаем выделение и копирование текста, но не редактирование
text_area.config(state=tk.NORMAL)  # Позволяет выделять текст
# text_area.config(state=tk.DISABLED)  # Это делает текст доступным только для копирования

# Отображаем окно
root.mainloop()