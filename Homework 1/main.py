import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def draw_hist():
    # get values from entries
    low = int(a_entry.get())
    high = int(b_entry.get())
    size = int(n_entry.get())
    bins = int(m_entry.get())

    # generate random numbers
    random_numbers = np.random.random(size) * (high - low) + low

    # add axis and draw histogram
    figure = plt.figure(figsize=(7, 7))
    ax = figure.add_subplot()
    ax.set_ylabel("Значение функции распределения \u03C6(x)")
    ax.set_xlabel("Сгенерированные значения х")
    ax.set_title("Гистограмма функции распределения")

    ax.hist(random_numbers, bins=bins, alpha=0.75, ec="black", density=True)
    ax.grid(alpha=0.4)

    canvas = FigureCanvasTkAgg(figure, master=histogram_frame)
    canvas.get_tk_widget().pack(anchor="s", fill="both", expand=True)

    toolbar = NavigationToolbar2Tk(canvas)

    # draw line
    height_of_line = 1 / (high - low)
    plt.plot([low, high], [height_of_line, height_of_line], color="red")
    figure.legend(["Равномерное распределение"])


# window
window = tk.Tk()
window.title("Homework #1 Киселев Владислав Александрович Фт-300008")

# mainframe
mainframe = tk.Frame(window)
mainframe.grid(row=1, column=1, sticky="n")

# histogram_frame
histogram_frame = tk.Frame(window, width=100)
histogram_frame.grid(row=1, column=2, sticky="n")

# labels
tk.Label(mainframe, text="A:").grid(column=1, row=2, sticky="nw")
tk.Label(mainframe, text="B:").grid(column=1, row=3, sticky="nw")
tk.Label(mainframe, text="n:").grid(column=1, row=4, sticky="nw")
tk.Label(mainframe, text="m:").grid(column=1, row=5, sticky="nw")

# button
button = tk.Button(mainframe, text="Построить гистограмму", command=draw_hist)
button.grid(column=2, row=7)

# entries
a_entry = tk.Entry(mainframe)
a_entry.insert(0, "0")
a_entry.grid(column=2, row=2, sticky="nw")
b_entry = tk.Entry(mainframe)
b_entry.insert(0, "1")
b_entry.grid(column=2, row=3, sticky="nw")
n_entry = tk.Entry(mainframe)
n_entry.insert(0, "10000")
n_entry.grid(column=2, row=4, sticky="nw")
m_entry = tk.Entry(mainframe)
m_entry.insert(0, "10")
m_entry.grid(column=2, row=5, sticky="nw")

window.mainloop()