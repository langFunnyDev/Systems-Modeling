# Отчет по домашней работе №3 (Киселев Владислав Александрович) Фт-300008

## Задание:
	Необходимо сгенерировать ряд случайных чисел и построить график вычислений методом Монте-Карло

## Используемые обозначения:
	[A, B] – Диапазон значений генерируемых случайных чисел
    a - Потери на единицу хранения
    b - Потери на единицу дефицита 
    n - количество генерируемых чисел
    m - количество опорных точек для графика

## Полученные результаты:

###	[0; 1]; a = 1; b = 1; n = 100000; m = 20.
![](https://raw.githubusercontent.com/langFunnyDev/Systems-Modeling/master/Homework%203/0%3B1%3B1%3B1%3B100000%3B20.png)
###	[0; 10]; a = 1; b = 2; n = 1000; m = 20.
![](https://raw.githubusercontent.com/langFunnyDev/Systems-Modeling/master/Homework%203/0%3B10%3B1%3B2%3B1000%3B20.png)
###	[0; 10]; a = 1; b = 2; n = 100000; m = 20.
![](https://raw.githubusercontent.com/langFunnyDev/Systems-Modeling/master/Homework%203/0%3B10%3B1%3B2%3B100000%3B20.png)
###	[20; 100]; a = 3; b = 1; n = 100000; m = 30.
![](https://raw.githubusercontent.com/langFunnyDev/Systems-Modeling/master/Homework%203/20%3B100%3B3%3B1%3B100000%3B30.png)
###	[25; 100]; a = 3; b = 1; n = 1000; m = 30.
![](https://raw.githubusercontent.com/langFunnyDev/Systems-Modeling/master/Homework%203/25%3B100%3B3%3B1%3B1000%3B30.png)
###	[25; 100]; a = 5; b = 1; n = 100000; m = 25.
![](https://raw.githubusercontent.com/langFunnyDev/Systems-Modeling/master/Homework%203/25%3B100%3B5%3B1%3B100000%3B25.png)
###	[25; 100]; a = 5; b = 4; n = 100000; m = 25.
![](https://raw.githubusercontent.com/langFunnyDev/Systems-Modeling/master/Homework%203/25%3B100%3B5%3B4%3B100000%3B25.png)

## Вывод:
    Внимательно рассмотрев графики полученные в ходе работы программы, можно сделать о том, что график полученный методом Монте-Карло близок к ожидаемому теоретическому значению.
    Отклонения наблюдаются при уменьшении количества генерируемых значений, следовательно мы можем сделать вывод о том, что программа работает корректно.

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
    
            self.setWindowTitle("Homework #3 Киселев Владислав Александрович Фт-300008")
    
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
            self.graphWidget.setTitle("Метод Монте-Карло", color="k", size="20pt")
            self.graphWidget.addLegend(offset=(120, 70))
            # self.graphWidget.setBackground("w")
    
            # pens
            self.pen_theoretic = pg.mkPen(color=(18, 53, 200), width=3)
            self.brush_optimal = pg.mkBrush(color=(215, 38, 56), width=2)
            self.brush_monte_carlo = pg.mkBrush(color=(154, 184, 122), width=2)
            self.pen_deviation = pg.mkPen(color=(80, 81, 79), width=3)
    
            # labels
            self.label_A = QtWidgets.QLabel("A:")
            self.label_B = QtWidgets.QLabel("B:")
            self.label_alpha = QtWidgets.QLabel("\u03B1:")
            self.label_beta = QtWidgets.QLabel("\u03B2:")
            self.label_n = QtWidgets.QLabel("n:")
            self.label_m = QtWidgets.QLabel("m:")
    
            # line edits
            self.line_edit_A = QtWidgets.QLineEdit("0")
            self.line_edit_B = QtWidgets.QLineEdit("1")
            self.line_edit_alpha = QtWidgets.QLineEdit("1")
            self.line_edit_beta = QtWidgets.QLineEdit("1")
            self.line_edit_n = QtWidgets.QLineEdit("100000")
            self.line_edit_m = QtWidgets.QLineEdit("20")
    
            self.line_edit_A.setFixedWidth(150)
            self.line_edit_B.setFixedWidth(150)
            self.line_edit_alpha.setFixedWidth(150)
            self.line_edit_beta.setFixedWidth(150)
            self.line_edit_n.setFixedWidth(150)
            self.line_edit_m.setFixedWidth(150)
    
            # buttons
            self.button = QtWidgets.QPushButton("Построить")
            self.button.clicked.connect(self.draw_graph)
    
            # add widgets to layouts
            self.layout.addWidget(self.label_A, 0, 0)
            self.layout.addWidget(self.label_B, 1, 0)
            self.layout.addWidget(self.label_alpha, 2, 0)
            self.layout.addWidget(self.label_beta, 3, 0)
            self.layout.addWidget(self.label_n, 4, 0)
            self.layout.addWidget(self.label_m, 5, 0)
    
            self.layout.addWidget(self.line_edit_A, 0, 1)
            self.layout.addWidget(self.line_edit_B, 1, 1)
            self.layout.addWidget(self.line_edit_alpha, 2, 1)
            self.layout.addWidget(self.line_edit_beta, 3, 1)
            self.layout.addWidget(self.line_edit_n, 4, 1)
            self.layout.addWidget(self.line_edit_m, 5, 1)
    
            self.layout.addWidget(self.button, 6, 0, 1, 2)
    
            self.layout.addWidget(self.graphWidget, 0, 3, 8, 1)
    
            self.widget = QtWidgets.QWidget()
            self.widget.setLayout(self.layout)
            self.setCentralWidget(self.widget)
    
        def draw_graph(self):
            a = float(self.line_edit_A.text())
            b = float(self.line_edit_B.text())
            alpha = float(self.line_edit_alpha.text())
            beta = float(self.line_edit_beta.text())
            n = int(self.line_edit_n.text())
            m = int(self.line_edit_m.text())
    
            # theoretic
            bins = np.linspace(a, b, m)
            q = [self.calculate_theoretic(a, b, x, alpha, beta) for x in bins]
    
            # optimal
            x_min = (alpha * a + beta * b) / (alpha + beta)
            q_min = (alpha * (x_min - a) ** 2 + beta * (x_min - b) ** 2) / (2 * (b - a))
    
            # monte carlo
            q_monte_carlo = []
    
            for x_value in bins:
                y_values = np.random.random(n) * (b - a) + a
    
                q_values = [alpha * (x_value - y_value) if x_value > y_value else beta * (y_value - x_value) for y_value in
                            y_values]
    
                q_monte_carlo.append(sum(q_values) / n)
    
            # standard deviation
            q_deviation = []
    
            for x_value in bins:
                y_values = np.random.random(n) * (b - a) + a
                q_pre_values = [(self.calculate_theoretic(a, b, x_value, alpha, beta) - alpha * (x_value - y_value)) ** 2
                                if x_value > y_value else (self.calculate_theoretic(a, b, x_value, alpha, beta) -
                                                           beta * (y_value - x_value)) ** 2 for y_value in y_values]
    
                q_deviation.append(np.sqrt(sum(q_pre_values) / (n - 1)))
    
            # drawing
            self.graphWidget.plot(bins, q, pen=self.pen_theoretic, clear=True,
                                  name="Теоретический расчет ожидаемого Q(x)")
            self.graphWidget.plot(bins, q_monte_carlo, pen=None, symbol="o", symbolBrush=self.brush_monte_carlo,
                                  name="Метод Монте-Карло")
            self.graphWidget.plot([x_min], [q_min], pen=None, symbol="o", symbolBrush=self.brush_optimal,
                                  name=f"Оптимальное значение({x_min:.3f}, {q_min:.3f})")
            self.graphWidget.plot(bins, q_deviation, pen=self.pen_deviation, name="Стандартное отклонение")
    
        @staticmethod
        def calculate_theoretic(a, b, x, alpha, beta):
            return (alpha * (x - a) ** 2 + beta * (x - b) ** 2) / (2 * (b - a))
    
    
    def main():
        app = QtWidgets.QApplication(sys.argv)
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec_())
    
    
    if __name__ == '__main__':
        main()
```