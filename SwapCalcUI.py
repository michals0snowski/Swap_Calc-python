import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Gather inputs
        tokenA = entry_tokenA.get()
        tokenB = entry_tokenB.get()
        tokenA_price = float(entry_tokenA_price.get())
        tokenB_price = float(entry_tokenB_price.get())
        tokenA_toSwap = float(entry_tokenA_toSwap.get())
        swapFee = float(entry_swapFee.get())
        slippage = float(entry_slippage.get())

        # Calculations
        priceRatio = tokenA_price / tokenB_price
        toRecieve = tokenA_toSwap * priceRatio
        minimumToRecieve = (tokenA_toSwap - swapFee) * ((100 - slippage) / 100) * priceRatio

        # Display results in a new window
        result_window = tk.Toplevel(root)
        result_window.title("Results")
        result_window.geometry("400x300")

        result_text = (
            f"Price ratio ({tokenA} to {tokenB}): {priceRatio:.5f}\n\n"
            f"Amount of {tokenB} to receive: {toRecieve:.5f}\n"
            f"Minimum amount of {tokenB} to receive: {minimumToRecieve:.5f}\n\n"
            "Press 'q' to exit the program"
        )

        result_label = tk.Label(result_window, text=result_text, justify=tk.LEFT)
        result_label.pack(padx=10, pady=10)

        result_window.bind('<q>', lambda event: root.quit())

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Main window setup
root = tk.Tk()
root.title("Crypto Swap Calculator")
root.geometry("500x350")

# Create a frame to hold all input widgets
frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

# Labels and entries for input
tk.Label(frame, text="What's the name of the currency to swap:").grid(row=0, column=0, sticky='e')
entry_tokenA = tk.Entry(frame)
entry_tokenA.grid(row=0, column=1, pady=5)

tk.Label(frame, text="And what's the name of the currency you want to swap to:").grid(row=1, column=0, sticky='e')
entry_tokenB = tk.Entry(frame)
entry_tokenB.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Current price of Token A (in $):").grid(row=2, column=0, sticky='e')
entry_tokenA_price = tk.Entry(frame)
entry_tokenA_price.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Current price of Token B (in $):").grid(row=3, column=0, sticky='e')
entry_tokenB_price = tk.Entry(frame)
entry_tokenB_price.grid(row=3, column=1, pady=5)

tk.Label(frame, text="Amount of Token A you want to swap:").grid(row=4, column=0, sticky='e')
entry_tokenA_toSwap = tk.Entry(frame)
entry_tokenA_toSwap.grid(row=4, column=1, pady=5)

tk.Label(frame, text="What's the swap fee?:").grid(row=5, column=0, sticky='e')
entry_swapFee = tk.Entry(frame)
entry_swapFee.grid(row=5, column=1, pady=5)

tk.Label(frame, text="What's the slippage %?:").grid(row=6, column=0, sticky='e')
entry_slippage = tk.Entry(frame)
entry_slippage.grid(row=6, column=1, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=20)

root.mainloop()