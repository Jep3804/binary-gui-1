#BINARY DECIMAL TWO WAY CONVERTER SOURCE CODE
#WRITTEN BY JOSH PHILIP

import tkinter as tk

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Binary<->Decimal")
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)


        self.frames = {}

        for F in (Start, Binary, Decimal, Ones, Twos):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame(Start)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        if hasattr(frame, "show"):
            frame.show()

class Start(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select one from below")
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Binary->Decimal", command=lambda: controller.show_frame(Binary))
        button2 = tk.Button(self, text="Decimal->Binary", command=lambda: controller.show_frame(Decimal))
        button3 = tk.Button(self, text="Ones' Complement", command=lambda: controller.show_frame(Ones))
        button4 = tk.Button(self, text="Two's Complement", command=lambda: controller.show_frame(Twos))
        button1.pack(fill=tk.BOTH, expand=True)
        button2.pack(fill=tk.BOTH, expand=True)
        button3.pack(fill=tk.BOTH, expand=True)
        button4.pack(fill=tk.BOTH, expand=True)

class Binary(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Enter a binary string")
        label.pack(pady=10, padx=10)

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=40)
        
        button = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(Start))
        button.pack(pady=40)
        self.entry.bind('<Return>', self.binaryToDecimal)
        vcmd = (self.register(self.validate_input), '%P')
        self.entry.config(validate='key', validatecommand=vcmd)

    def validate_input(self, new_value):
        char_count = len(new_value)
        new_width = char_count + 2  
        self.entry.config(width=new_width)
        return True

    def binaryToDecimal(self, event=None):
        self.result_label.config(text="")
        binary = self.entry.get()
        if binary == "":
            self.result_label.config(text="Invalid Binary String");
            raise ValueError("ERROR")
        nums = [int(x) for x in binary]
        nums.reverse()
        decimal = 0
        for num in nums:
            if num != 0 and num != 1:
                self.result_label.config(text="Invalid Binary String");
                self.entry.delete(0, tk.END)
                raise ValueError("ERROR")
        for idx in range(len(nums)):
            decimal = decimal + (nums[idx] * (2 ** idx))
        self.result_label.config(text=f"Decimal: {decimal}")
        self.entry.delete(0, tk.END)

    def show(self):
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)

class Decimal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Enter a positive integer")
        label.pack(pady=10, padx=10)

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=40)
        
        button = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(Start))
        button.pack(pady=40)
        self.entry.bind('<Return>', self.decimalToBinary)
        vcmd = (self.register(self.validate_input), '%P')
        self.entry.config(validate='key', validatecommand=vcmd)

    def validate_input(self, new_value):
        char_count = len(new_value)
        new_width = char_count + 2  
        self.entry.config(width=new_width)
        return True
    
    def decimalToBinary(self, event=None):
        decimal = int(self.entry.get())
        acc = []
        if decimal == 0:
            self.result_label.config(text="Binary String: 0")
            self.entry.delete(0, tk.END)
            return 
        while(decimal != 0):
                acc.append(decimal % 2)
                decimal = decimal // 2
        acc.reverse()
        binary = ""
        for x in acc:
            binary = binary + str(x)
        self.result_label.config(text = "Binary String: " + binary)
        self.entry.delete(0, tk.END)

    def show(self):
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)

    
class Ones(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Enter a binary string")
        label.pack(pady=10, padx=10)

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=40)
        
        button = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(Start))
        button.pack(pady=40)
        self.entry.bind('<Return>', self.ones_complement)
        vcmd = (self.register(self.validate_input), '%P')
        self.entry.config(validate='key', validatecommand=vcmd)

    def validate_input(self, new_value):
        char_count = len(new_value)
        new_width = char_count + 2 
        self.entry.config(width=new_width)
        return True

    def ones_complement(self, event=None):
        binary = self.entry.get()
        if binary == "":
            self.result_label.config(text="Invalid Binary String");
            raise ValueError("ERROR")
        nums = [int(x) for x in binary]
        nums.reverse()
        decimal = 0
        for num in nums:
            if num != 0 and num != 1:
                self.result_label.config(text="Invalid Binary String");
                self.entry.delete(0, tk.END)
                raise ValueError("INVALID INPUT DETECTED")
        for idx in range(len(nums)):
            if idx == len(nums) -1 and nums[idx] == 1:
                decimal = decimal + (nums[idx] * ((-2 ** idx) + 1))
            else:
                decimal = decimal + (nums[idx] * (2 ** idx))
        self.result_label.config(text=f"Decimal: {decimal}")
        self.entry.delete(0, tk.END)

    def show(self):
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)

        

class Twos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter a binary string")
        label.pack(pady=10, padx=10)

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=40)
        
        button = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(Start))
        button.pack(pady=40)
        self.entry.bind('<Return>', self.twos_complement)
        vcmd = (self.register(self.validate_input), '%P')
        self.entry.config(validate='key', validatecommand=vcmd)

    def validate_input(self, new_value):
        char_count = len(new_value)
        new_width = char_count + 2 
        self.entry.config(width=new_width)
        return True
    
    def twos_complement(self, event=None):
        binary = self.entry.get()
        if binary == "":
            self.result_label.config(text="Invalid Binary String");
            raise ValueError("INVALID INPUT DETECTED")
        nums = [int(x) for x in binary]
        nums.reverse()
        decimal = 0
        for num in nums:
            if num != 0 and num != 1:
                self.result_label.config(text="Invalid Binary String");
                self.entry.delete(0, tk.END)
                raise ValueError("INVALID INPUT DETECTED")
        for idx in range(len(nums)):
            if idx == len(nums) -1 and nums[idx] == 1:
                decimal = decimal + (nums[idx] * (-2 ** idx))
            else:
                decimal = decimal + (nums[idx] * (2 ** idx))
        self.result_label.config(text=f"Decimal: {decimal}")
        self.entry.delete(0, tk.END)

    def show(self):
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)

        
app = App()
app.geometry("400x300")
app.mainloop()


