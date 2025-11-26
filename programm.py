import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model
import os

class RoadSignClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Классификатор дорожных знаков")
        self.root.geometry("1000x700") 
        self.root.configure(bg='#f0f0f0')
        
   
        self.model = None
        self.selected_model = tk.StringVar(value="") 
        self.model_paths = {
            "VGG16": "models/VGG16_road_sign.h5",  
            "ResNet18": "models/resnet50_model.h5"  
        }
        self.image_path = tk.StringVar()
        self.class_names = ['Круговое движение', 'Движение прямо или направо', 'Односторонее движение', 'Объезд','Движение налево или направо']
        
        self.setup_ui()
        
    def setup_ui(self):
        title_label = tk.Label(self.root, text="Классификатор дорожных знаков", 
                              font=('Arial', 16, 'bold'), bg='#f0f0f0')
        title_label.pack(pady=10)
        
        model_frame = tk.LabelFrame(self.root, text="1. Выбор модели", 
                                   font=('Arial', 24, 'bold'), bg='#f0f0f0')
        model_frame.pack(fill='x', padx=20, pady=10)
   
        tk.Radiobutton(model_frame, text="VGG16", variable=self.selected_model, 
                      value="VGG16", bg='#f0f0f0', font=('Arial', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='w')
        tk.Radiobutton(model_frame, text="ResNet18", variable=self.selected_model, 
                      value="ResNet18", bg='#f0f0f0', font=('Arial', 20)).grid(row=0, column=1, padx=10, pady=5, sticky='w')
        
     
        tk.Button(model_frame, text="Загрузить модель", command=self.load_model, 
                 bg='#2196F3', fg='white', font=('Arial',20)).grid(row=0, column=2, padx=10, pady=5)
        
        self.model_status = tk.Label(model_frame, text="Модель не загружена", 
                                    fg='red', bg='#f0f0f0', font=('Arial', 20))
        self.model_status.grid(row=1, column=0, columnspan=3, pady=5)
        
        image_frame = tk.LabelFrame(self.root, text="2. Загрузка изображения", 
                                   font=('Arial', 24, 'bold'), bg='#f0f0f0')
        image_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(image_frame, text="Файл изображения:",font=('Arial', 20), bg='#f0f0f0').grid(row=0, column=0, padx=5, pady=5, sticky='w')
        tk.Entry(image_frame, textvariable=self.image_path, width=50).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(image_frame, text="Обзор",font=('Arial', 24), command=self.browse_image, 
                 bg='#4CAF50', fg='white').grid(row=0, column=2, padx=5, pady=5)
        tk.Button(image_frame, text="Классифицировать",font=('Arial', 24), command=self.classify_image, 
                 bg='#FF9800', fg='white').grid(row=0, column=3, padx=5, pady=5)
        
        result_frame = tk.LabelFrame(self.root, text="3. Результаты", 
                                    font=('Arial', 24, 'bold'), bg='#f0f0f0')
        result_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
      
        image_container = tk.Frame(result_frame, bg='white', relief='solid', bd=1)
        image_container.pack(side='left', padx=10, pady=10, fill='both', expand=True)
        
        self.image_label = tk.Label(image_container, text="Изображение не загружено", 
                                   bg='white', font=('Arial', 24))
        self.image_label.pack(expand=True, fill='both')
        

        results_subframe = tk.Frame(result_frame, bg='#f0f0f0')
        results_subframe.pack(side='right', padx=10, pady=10, fill='both', expand=True)
        
        tk.Label(results_subframe, text="Результаты классификации:", 
                font=('Arial', 25, 'bold'), bg='#f0f0f0').pack(anchor='w', pady=5)
        
 
        main_results_frame = tk.Frame(results_subframe, bg='#f0f0f0')
        main_results_frame.pack(anchor='w', pady=10, fill='x')
        
    
        class_frame = tk.Frame(main_results_frame, bg='#f0f0f0')
        class_frame.pack(anchor='w', pady=10, fill='x')

     
        class_header_frame = tk.Frame(class_frame, bg='#f0f0f0')
        class_header_frame.pack(anchor='w', fill='x')
        
        tk.Label(class_header_frame, text="Предсказанный класс:", 
                font=('Arial', 25, 'bold'), bg='#f0f0f0').pack(anchor='w')

        self.predicted_class = tk.Label(class_header_frame, text="-", 
                               font=('Arial', 35, 'bold'), bg='#f0f0f0', fg='#2196F3',
                               wraplength=450, justify='left')
        self.predicted_class.pack(anchor='w', pady=(5, 0), fill='x', expand=True)
        
    
        confidence_frame = tk.Frame(main_results_frame, bg='#f0f0f0')
        confidence_frame.pack(anchor='w', pady=10, fill='x')
        
        
        confidence_header_frame = tk.Frame(confidence_frame, bg='#f0f0f0')
        confidence_header_frame.pack(anchor='w', fill='x')
        
        tk.Label(confidence_header_frame, text="Уверенность:", 
                font=('Arial', 35, 'bold'), bg='#f0f0f0').pack(anchor='w')
        
        self.confidence_label = tk.Label(confidence_header_frame, text="-", 
                                        font=('Arial', 35, 'bold'), bg='#f0f0f0', fg='#FF5722')
        self.confidence_label.pack(anchor='w', pady=(5, 0))
        
   
        separator = ttk.Separator(results_subframe, orient='horizontal')
        separator.pack(fill='x', pady=10)
        

        probabilities_frame = tk.LabelFrame(results_subframe, text="Вероятности по всем классам", 
                                          font=('Arial', 20, 'bold'), bg='#f0f0f0')  
        probabilities_frame.pack(anchor='w', pady=5, fill='both', expand=True)
        
       
        progress_container = tk.Frame(probabilities_frame, bg='#f0f0f0')
        progress_container.pack(fill='both', expand=True, padx=10, pady=10)
        
     
        self.canvas = tk.Canvas(progress_container, bg='#f0f0f0', height=180)  
        scrollbar = ttk.Scrollbar(progress_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg='#f0f0f0')
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        
        self.probabilities_content = tk.Frame(self.scrollable_frame, bg='#f0f0f0')
        self.probabilities_content.pack(fill='both', expand=True)
    
    def browse_image(self):
        filename = filedialog.askopenfilename(
            title="Выберите файл изображения",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp"), ("All files", "*.*")]
        )
        if filename:
            self.image_path.set(filename)
            self.display_image(filename)
    
    def load_model(self):
        if not self.selected_model.get():
            messagebox.showerror("Ошибка", "Сначала выберите модель!")
            return
        
        model_path = self.model_paths.get(self.selected_model.get())
        if not model_path:
            messagebox.showerror("Ошибка", "Путь к выбранной модели не найден!")
            return
        
        try:
      
            if not os.path.exists(model_path):
                messagebox.showerror("Ошибка", f"Файл модели не найден по пути:\n{model_path}")
                return
                
            self.model = load_model(model_path)
            self.model_status.config(text=f"Модель {self.selected_model.get()} успешно загружена!", fg='green')
            messagebox.showinfo("Успех", f"Модель {self.selected_model.get()} успешно загружена!")
            
        except Exception as e:
            self.model_status.config(text="Ошибка загрузки модели", fg='red')
            messagebox.showerror("Ошибка", f"Не удалось загрузить модель {self.selected_model.get()}:\n{str(e)}")
    
    def display_image(self, image_path):
        try:
            image = Image.open(image_path)
            
            image.thumbnail((400, 400), Image.Resampling.LANCZOS)
            
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo, text="")
            self.image_label.image = photo
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить изображение:\n{str(e)}")
    
    def preprocess_image(self, image_path):
        try:
            image = Image.open(image_path)
            image = image.resize((224, 224))

            image_array = np.array(image)
            image_array = image_array / 255.0 
            
            image_array = np.expand_dims(image_array, axis=0)
            
            return image_array
            
        except Exception as e:
            raise Exception(f"Ошибка предобработки изображения: {str(e)}")
    
    def update_probabilities_display(self, predictions):
        for widget in self.probabilities_content.winfo_children():
            widget.destroy()
    
        sorted_indices = np.argsort(predictions[0])[::-1]
    
        
        predicted_class_idx = np.argmax(predictions[0])
    
  
        for i, class_idx in enumerate(sorted_indices):
      
            if class_idx == predicted_class_idx:
                continue
            
            confidence = predictions[0][class_idx]
            confidence_percent = confidence * 100
        
            row_frame = tk.Frame(self.probabilities_content, bg='#f0f0f0')
            row_frame.pack(fill='x', pady=3)
        
            class_name = self.class_names[class_idx] if class_idx < len(self.class_names) else f"Класс {class_idx}"
            class_label = tk.Label(row_frame, text=class_name, font=('Arial', 16, 'bold'),
                              bg='#f0f0f0', anchor='w', justify='left',
                              wraplength=350)  
            class_label.pack(side='left', padx=5, fill='x', expand=True)
        
            progress = ttk.Progressbar(row_frame, orient='horizontal', length=180,
                                 mode='determinate', maximum=100)
            progress['value'] = confidence_percent
            progress.pack(side='left', padx=10)
        
            percent_label = tk.Label(row_frame, text=f"{confidence_percent:.2f}%", 
                               font=('Arial', 16, 'bold'), bg='#f0f0f0', width=10, anchor='w')
            percent_label.pack(side='left', padx=5)
    
    def classify_image(self):
        if self.model is None:
            messagebox.showerror("Ошибка", "Сначала загрузите модель!")
            return
        
        if not self.image_path.get():
            messagebox.showerror("Ошибка", "Сначала выберите изображение!")
            return
        
        try:
            processed_image = self.preprocess_image(self.image_path.get())
            
            predictions = self.model.predict(processed_image)
            predicted_class = np.argmax(predictions[0])
            confidence = predictions[0][predicted_class]
            
            confidence_percent = confidence * 100
            
            class_name = self.class_names[predicted_class] if predicted_class < len(self.class_names) else f"Класс {predicted_class}"
            
            self.predicted_class.config(text=class_name)
            self.confidence_label.config(text=f"{confidence_percent:.2f}%")
            
            self.update_probabilities_display(predictions)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка классификации:\n{str(e)}")

def main():
    root = tk.Tk()
    app = RoadSignClassifierApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()