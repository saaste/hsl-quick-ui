from flask import Flask
from flask import render_template
from hsl_client import get_next_route

app = Flask(__name__)

@app.route("/")
def next_routes():
    routes = {
        'Mäkkylä - Leppävaara': get_next_route('Koti::60.22257,24.83063', 'Leppavaaran asema::60.218887,24.812701'),
        'Leppävaara - Mäkkylä': get_next_route('Leppavaaran asema::60.218887,24.812701', 'Koti::60.22257,24.83063')}

    return render_template('routes.html', routes=routes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
