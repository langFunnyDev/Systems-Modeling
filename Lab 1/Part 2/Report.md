# Отчет по лабораторной работе №1 ч.2 (Киселев Владислав Александрович) Фт-300008

# Вариант №6

## Используемые обозначения:
	[A, B] – Диапазон значений генерируемых случайных чисел
    a - Потери на единицу хранения
    b - Потери на единицу дефицита 
    n - количество генерируемых чисел
    m - количество опорных точек для графика

## Полученные результаты:

###	[1;1]; a = 1; b = 1; n = 100000; m = 20.
![](https://raw.githubusercontent.com/langFunnyDev/Systems-Modeling/master/Lab%201/Part%202/1%3B1.png)
###	[1;3]; a = 1; b = 3; n = 100000; m = 20.
![](https://raw.githubusercontent.com/langFunnyDev/Systems-Modeling/master/Lab%201/Part%202/1%3B3.png)
###	[2;1]; a = 2; b = 1; n = 100000; m = 20.
![](https://raw.githubusercontent.com/langFunnyDev/Systems-Modeling/master/Lab%201/Part%202/2%3B1.png)

## Исходный код программы:

```python
    import sys
    import pyqtgraph as pg
    import numpy as np
    
    from PyQt5 import QtWidgets
    from pyqtgraph import PlotWidget
    
    
    class MainWindow(QtWidgets.QMainWindow):
        def __init__(self, *args, **kwargs):
            super(MainWindow, self).__init__(*args, **kwargs)
    
            self.setWindowTitle("Lab #1.2-#1.3 Киселев Владислав Александрович Фт-300008")
    
            # layouts
            self.layout = QtWidgets.QGridLayout()
    
            # graph widget
            pg.setConfigOption('background', 'w')
            pg.setConfigOption('foreground', 'k')
            self.graphWidget = PlotWidget()
            self.graphWidget.showGrid(x=True, y=True)
            styles = {'color': 'k', 'font-size': '20px'}
            self.graphWidget.setLabel('left', 'Q(x)', **styles)
            self.graphWidget.setLabel('bottom', 'x', **styles)
            self.graphWidget.setTitle("Метод фон Неймана", color="k", size="20pt")
            self.graphWidget.addLegend(offset=(120, 70))
            # self.graphWidget.setBackground("w")
    
            # pens
            self.pen_theoretic = pg.mkPen(color=(18, 53, 200), width=3)
            self.brush_optimal = pg.mkBrush(color=(215, 38, 56), width=2)
            self.brush_monte_carlo = pg.mkBrush(color=(154, 184, 122), width=2)
            self.pen_deviation = pg.mkPen(color=(80, 81, 79), width=3)
    
            # labels
            self.label_alpha = QtWidgets.QLabel("\u03B1:")
            self.label_beta = QtWidgets.QLabel("\u03B2:")
            self.label_n = QtWidgets.QLabel("n:")
            self.label_m = QtWidgets.QLabel("m:")
    
            # line edits
            self.line_edit_alpha = QtWidgets.QLineEdit("1")
            self.line_edit_beta = QtWidgets.QLineEdit("1")
            self.line_edit_n = QtWidgets.QLineEdit("100000")
            self.line_edit_m = QtWidgets.QLineEdit("20")
    
            self.line_edit_alpha.setFixedWidth(150)
            self.line_edit_beta.setFixedWidth(150)
            self.line_edit_n.setFixedWidth(150)
            self.line_edit_m.setFixedWidth(150)
    
            # buttons
            self.button = QtWidgets.QPushButton("Построить")
            self.button.clicked.connect(self.draw_graph)
    
            # add widgets to layouts
            self.layout.addWidget(self.label_alpha, 2, 0)
            self.layout.addWidget(self.label_beta, 3, 0)
            self.layout.addWidget(self.label_n, 0, 0)
            self.layout.addWidget(self.label_m, 1, 0)
    
            self.layout.addWidget(self.line_edit_alpha, 2, 1)
            self.layout.addWidget(self.line_edit_beta, 3, 1)
            self.layout.addWidget(self.line_edit_n, 0, 1)
            self.layout.addWidget(self.line_edit_m, 1, 1)
    
            self.layout.addWidget(self.button, 4, 0, 1, 2)
    
            self.layout.addWidget(self.graphWidget, 0, 3, 8, 1)
    
            self.widget = QtWidgets.QWidget()
            self.widget.setLayout(self.layout)
            self.setCentralWidget(self.widget)
    
        def draw_graph(self):
            # Логика тут
            n = int(self.line_edit_n.text())
            m = int(self.line_edit_m.text())
            alpha = int(self.line_edit_alpha.text())
            beta = int(self.line_edit_beta.text())
            a = 0
            b = 30
            c = 12
    
            # theoretic
            bins = np.linspace(a, b, m)
            fake_bins = np.linspace(a, b, 100)
            # q = [self.calculate_theoretic(a, b, x, alpha, beta, c) for x in bins]
            random_numbers = self.generate_random_numbers(a=a, b=b, n=500_000, c=c)
            q = self.fake_monte_carlo(bins, random_numbers, alpha, beta)
    
            # optimal
            q_for_min = self.fake_monte_carlo(fake_bins, random_numbers, alpha, beta)
            q_min = min(q_for_min)
            x_min = fake_bins[q_for_min.index(q_min)]
    
            # monte carlo
            q_monte_carlo = []
    
            for x_value in bins:
                y_values = self.generate_random_numbers(a, b, n, c)
    
                q_values = [alpha * (x_value - y_value) if x_value > y_value else beta * (y_value - x_value) for y_value in
                            y_values]
    
                q_monte_carlo.append(sum(q_values) / len(q_values))
    
            # standard deviation
            q_deviation = []
    
            for i in range(len(bins)):
                y_values = self.generate_random_numbers(a, b, n, c)
                q_pre_values = []
                for y_value in y_values:
                    if bins[i] > y_value:
                        q_pre_values.append((q[i] - alpha * (bins[i] - y_value))**2)
                    else:
                        q_pre_values.append((q[i] - beta * (y_value - bins[i])) ** 2)
    
                q_deviation.append(np.sqrt(sum(q_pre_values) / (len(q_pre_values) - 1)))
    
    
    
    
            # for x_value in bins:
            #     y_values = self.generate_random_numbers(a, b, n, c)
            #     q_pre_values = [
            #         (self.calculate_theoretic(a, b, x_value, alpha, beta, c) - alpha * (x_value - y_value)) ** 2
            #         if x_value > y_value else (self.calculate_theoretic(a, b, x_value, alpha, beta, c) -
            #                                    beta * (y_value - x_value)) ** 2 for y_value in y_values]
            #
            #     q_deviation.append(np.sqrt(sum(q_pre_values) / (len(q_pre_values) - 1)))
    
            # drawing
            self.graphWidget.plot(bins, q, pen=self.pen_theoretic, clear=True,
                                  name="Теоретический расчет ожидаемого Q(x)")
            # self.graphWidget.plot(bins, q_monte_carlo, pen=None, symbol="o", symbolBrush=self.brush_monte_carlo, name="Метод Монте-Карло")
            self.graphWidget.plot([x_min], [q_min], pen=None, symbol="o", symbolBrush=self.brush_optimal,
                                  name=f"Оптимальное значение")
            # self.graphWidget.plot(bins, q_deviation, pen=self.pen_deviation, name="Стандартное отклонение")
    
        @staticmethod
        def calculate_theoretic(a, b, x, alpha, beta, c) -> float:
            return (alpha * (x - a) ** 2 + 2 * alpha * (x - c) ** 2 + beta * (x - c) ** 2 + 2 * beta * (x - b) ** 2) / \
                   (2 * b - a - c)  # (1) (2)
    
        @staticmethod
        def generate_random_numbers(a, b, n, c) -> np.array:
            h = 2 / (2 * b - c - a)
            random_numbers_x = np.random.random(n) * (b - a) + a
            random_numbers_y = np.random.random(n) * h
            indexes = []
            for i in reversed(range(len(random_numbers_x))):
                if random_numbers_y[i] > h / 2 and random_numbers_x[i] < c:
                    indexes.append(i)
    
            random_numbers = np.delete(random_numbers_x, indexes)
            return random_numbers
    
        @staticmethod
        def fake_monte_carlo(bins, random_numbers, alpha, beta):
            q_monte_carlo = []
    
            for x_value in bins:
                # y_values = self.generate_random_numbers(a, b, n, c)
    
                q_values = [alpha * (x_value - y_value) if x_value > y_value else beta * (y_value - x_value) for y_value in
                            random_numbers]
    
                q_monte_carlo.append(sum(q_values) / len(q_values))
    
            return q_monte_carlo
    
    
    
    def main():
        app = QtWidgets.QApplication(sys.argv)
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec_())
    
    
    if __name__ == '__main__':
        main()

```