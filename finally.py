import tkinter as tk

class LoanCalculator:
    def __init__(self):
        window = tk.Toplevel()
        window.title("Loan Calculator")

        tk.Label(window, text="Annual Interest Rate").grid(row=1, column=1, sticky=tk.W)
        tk.Label(window, text="Number of Years").grid(row=2, column=1, sticky=tk.W)
        tk.Label(window, text="Loan Amount").grid(row=3, column=1, sticky=tk.W)
        tk.Label(window, text="Monthly Payment").grid(row=4, column=1, sticky=tk.W)
        tk.Label(window, text="Total Payment").grid(row=5, column=1, sticky=tk.W)

        self.annualInterestRateVar = tk.StringVar() 
        tk.Entry(window, textvariable=self.annualInterestRateVar, justify=tk.RIGHT).grid(row=1, column=2)
        self.numberOfYearsVar = tk.StringVar()
        tk.Entry(window, textvariable=self.numberOfYearsVar, justify=tk.RIGHT).grid(row=2, column=2)
        self.loanAmountVar = tk.StringVar()
        tk.Entry(window, textvariable=self.loanAmountVar, justify=tk.RIGHT).grid(row=3, column=2)
        self.monthlyPaymentVar = tk.StringVar()
        tk.Label(window, textvariable=self.monthlyPaymentVar).grid(row=4, column=2, sticky=tk.E)
        self.totalPaymentVar = tk.StringVar()
        tk.Label(window, textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=tk.E)

        btComputePayment = tk.Button(window, text="Compute Payment", command=self.computePayment)
        btComputePayment.grid(row=6, column=2, sticky=tk.E)

    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberOfYearsVar.get())
        )

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears): 
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment

def suggest_car(salary, do_you_drive_in_the_city, passengers_in_the_car, load, prefer_high_car):
    result = ""

    if salary <= 18000:
        if load == "YES" and do_you_drive_in_the_city == "YES":
            result = "Honda City Hatchback Hybrid 850,000 "
        elif load == "NO" and do_you_drive_in_the_city == "YES":
            result = "Honda City Sedan Hybrid 780,000 "
        elif load == "YES" and do_you_drive_in_the_city == "NO":
            result = "Honda City Hatchback 800,000 "
        elif load == "NO" and do_you_drive_in_the_city == "NO":
            result = "Honda City Sedan 720,000 "
    elif 18000 < salary <= 30000:
        if load == "YES" or prefer_high_car == "YES":
            if passengers_in_the_car <= 4:
                if do_you_drive_in_the_city == "YES":
                    result = "Honda HR-V Hybrid 1,200,000 "
                elif prefer_high_car == "NO":
                    result = "Honda Civic Hatchback 1,200,000 "
                elif prefer_high_car == "YES":
                    result = "Honda WR-V 890,000 "
            else:
                result = "Honda BR-V 900,000 "
        elif load == "NO":
            if do_you_drive_in_the_city == "NO":
                result = "Honda Civic Sedan 900,000 "
    elif salary > 30000:
        if load == "YES" or prefer_high_car == "YES":
            if prefer_high_car == "YES":
                if do_you_drive_in_the_city == "YES":
                    result = "Honda CR-V Hybrid 1,800,000"
                else:
                    result = "Honda CR-V Fuel 1,500,000"
            else:
                if do_you_drive_in_the_city == "YES":
                    result = "Honda Accord Hybrid 1,900,000"
                else:
                    result = "Honda Accord Fuel 1,400,000"
        else:
            if do_you_drive_in_the_city == "YES":
                result = "Honda Accord Hybrid 1,900,000"
            else:
                result = "Honda Accord Fuel 1,400,000 "

    return result

# Initialize Tkinter
root = tk.Tk()
root.title("Honda App")
root.geometry("400x300")
root.configure(bg='white')

# Global variables for personal assistance
salary_entry = None
city_drive_var = None
passenger_entry = None
car_load_var = None
high_car_var = None
result_label = None

def open_personal_assistance_gui():
    global salary_entry, city_drive_var, passenger_entry, car_load_var, high_car_var, result_label

    personal_assistance_window = tk.Toplevel()
    personal_assistance_window.title("Honda Car Suggestion")

    tk.Label(personal_assistance_window, text="Enter your salary:").pack()
    salary_entry = tk.Entry(personal_assistance_window)
    salary_entry.pack()

    city_drive_var = tk.StringVar()
    city_drive_var.set("NO")
    tk.Label(personal_assistance_window, text="Do you drive in the city? (YES/NO):").pack()
    city_drive_entry = tk.Entry(personal_assistance_window, textvariable=city_drive_var)
    city_drive_entry.pack()

    tk.Label(personal_assistance_window, text="Number of passengers in the car:").pack()
    passenger_entry = tk.Entry(personal_assistance_window)
    passenger_entry.pack()

    car_load_var = tk.StringVar()
    car_load_var.set("NO")
    tk.Label(personal_assistance_window, text="Do you typically have a heavy load in your car? (YES/NO):").pack()
    car_load_entry = tk.Entry(personal_assistance_window, textvariable=car_load_var)
    car_load_entry.pack()

    high_car_var = tk.StringVar()
    high_car_var.set("NO")
    tk.Label(personal_assistance_window, text="Do you prefer a higher car? (YES/NO):").pack()
    high_car_entry = tk.Entry(personal_assistance_window, textvariable=high_car_var)
    high_car_entry.pack()

    suggest_button = tk.Button(personal_assistance_window, text="Suggest Car", command=suggest_car_from_entries)
    suggest_button.pack()

    # Result display label
    result_label = tk.Label(personal_assistance_window, text="")
    result_label.pack()

def suggest_car_from_entries():
    salary = int(salary_entry.get())
    do_you_drive_in_the_city = city_drive_var.get()
    passengers_in_the_car = int(passenger_entry.get())
    load = car_load_var.get()
    prefer_high_car = high_car_var.get()

    result = suggest_car(salary, do_you_drive_in_the_city, passengers_in_the_car, load, prefer_high_car)
    result_label.config(text=result)

# Welcome label
welcome_label = tk.Label(root, text="Welcome to Honda", fg="red", bg="white", font=("Arial", 16, "bold"))
welcome_label.pack(pady=20)

# Buttons
loan_button = tk.Button(root, text="Loan Calculator", command=LoanCalculator)
loan_button.pack(pady=10)

assistance_button = tk.Button(root, text="Personal Assistance", command=open_personal_assistance_gui)
assistance_button.pack(pady=10)

# Start the main loop
root.mainloop()
