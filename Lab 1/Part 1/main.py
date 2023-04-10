import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def draw_hist():
    # get values from entries
    low = 0
    middle = 10
    high = 30
    size = int(n_entry.get()) * 2
    bins = int(m_entry.get())

    # generate random numbers
    h = 2 / (2 * high - middle - low)
    random_numbers_x = np.random.random(size) * (high - low) + low
    random_numbers_y = np.random.random(size) * h

    indexes = []
    for i in reversed(range(len(random_numbers_x))):
        if random_numbers_y[i] > h / 2 and random_numbers_x[i] < middle:
            indexes.append(i)

    random_numbers = np.delete(random_numbers_x, indexes)

    # random_numbers_x = np.random.random(size) * (high - low) + low
    # random_numbers_y = np.random.random(size) / 24
    # indexes = []
    # for i in reversed(range(len(random_numbers_x))):
    #     if random_numbers_y[i] > (1/48) and random_numbers_x[i] < 12:
    #         indexes.append(i)
    #
    # random_numbers = np.delete(random_numbers_x, indexes)

    # add axis and draw histogram
    figure = plt.figure(figsize=(7, 7))
    ax = figure.add_subplot()
    ax.set_ylabel("\u03C6(x)")
    ax.set_xlabel("х")
    ax.set_title("Метод фон Неймана")

    ax.hist(random_numbers, bins=bins, alpha=0.75, ec="black", density=True)
    ax.grid(alpha=0.4)

    canvas = FigureCanvasTkAgg(figure, master=histogram_frame)
    canvas.get_tk_widget().pack(anchor="s", fill="both", expand=True)

    toolbar = NavigationToolbar2Tk(canvas)

    # draw line
    height_of_line_1 = h / 2
    height_of_line_2 = h
    plt.plot([low, middle, middle, high], [height_of_line_1, height_of_line_1, height_of_line_2, height_of_line_2],
             color="red")
    figure.legend(["Распределение при С = 10"])


# window
window = tk.Tk()
window.title("Lab #1.1 Киселев Владислав Александрович Фт-300008")

# mainframe
mainframe = tk.Frame(window)
mainframe.grid(row=1, column=1, sticky="n")

# histogram_frame
histogram_frame = tk.Frame(window, width=200)
histogram_frame.grid(row=1, column=2, sticky="n")

# labels
# tk.Label(mainframe, text="A:").grid(column=1, row=2, sticky="nw")
# tk.Label(mainframe, text="B:").grid(column=1, row=3, sticky="nw")
tk.Label(mainframe, text="n:").grid(column=1, row=2, sticky="nw")
tk.Label(mainframe, text="m:").grid(column=1, row=3, sticky="nw")

# button
button = tk.Button(mainframe, text="Построить гистограмму", command=draw_hist)
button.grid(column=2, row=7)

# entries
# a_entry = tk.Entry(mainframe)
# a_entry.insert(0, "0")
# a_entry.grid(column=2, row=2, sticky="nw")
# b_entry = tk.Entry(mainframe)
# b_entry.insert(0, "1")
# b_entry.grid(column=2, row=3, sticky="nw")
n_entry = tk.Entry(mainframe)
n_entry.insert(0, "10000")
n_entry.grid(column=2, row=2, sticky="nw")
m_entry = tk.Entry(mainframe)
m_entry.insert(0, "10")
m_entry.grid(column=2, row=3, sticky="nw")

window.mainloop()

