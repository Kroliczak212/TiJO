from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# figure_colors = {"square": "#808080", "circle": "#808080", "triangle": "#808080"} # code smell

# Klasy reprezentujące figury
class Figure:
    def __init__(self, color="#808080"):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        self._color = new_color


class Square(Figure):
    pass


class Circle(Figure):
    pass


class Triangle(Figure):
    pass


# Serwis zarządzający figurami
class FigureService:
    def __init__(self):
        self.figures = {
            "square": Square(),
            "circle": Circle(),
            "triangle": Triangle()
        }

    def get_colors(self):
        return {name: figure.get_color() for name, figure in self.figures.items()}

    def change_color(self, figure_type, new_color):
        if figure_type in self.figures:
            self.figures[figure_type].set_color(new_color)
            return True
        return False

    def change_color_all(self, new_color):
        for figure in self.figures.values():
            figure.set_color(new_color)


figure_service = FigureService()


# -------------------------------
# Funkcje obsługi żądań HTTP (Flask)
@app.route('/')
def index():
    # Pobieramy stan kolorów z serwisu i przekazujemy do szablonu
    colors = figure_service.get_colors()
    return render_template('index.html', figure_colors=colors)


@app.route('/change-color', methods=['POST'])
def change_color():
    data = request.get_json()
    figure_type = data.get('figure_type')
    new_color = data.get('new_color')

    if figure_type and new_color:
        if figure_service.change_color(figure_type, new_color):
            return jsonify({"status": "success", "figure_colors": figure_service.get_colors()})
    return jsonify({"status": "error", "message": "Błędny typ figury lub kolor"}), 400


@app.route('/change-color-all', methods=['POST'])
def change_color_all():
    data = request.get_json()
    new_color = data.get('new_color')
    if new_color:
        figure_service.change_color_all(new_color)
        return jsonify({"status": "success", "figure_colors": figure_service.get_colors()})
    return jsonify({"status": "error", "message": "Brak nowego koloru"}), 400


if __name__ == '__main__':
    app.run(debug=True)
