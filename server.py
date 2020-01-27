from flask import Flask
from flask import render_template
from hsl_client import get_next_route

application = Flask(__name__)


@application.route("/")
def next_routes():
    routes = {
        'Mäkkylä - Leppävaara': get_next_route('Mäkkylä::60.22257,24.83063', 'Leppävaara::60.218887,24.812701'),
        'Leppävaara - Mäkkylä': get_next_route('Leppävaara::60.218887,24.812701', 'Mäkkylä::60.22257,24.83063'),
        'Mäkkylä - Keskusta': get_next_route('Mäkkylä::60.22257,24.83063', 'Keskusta::60.17187,24.939226'),
        'Keskusta - Mäkkylä': get_next_route('Keskusta::60.17187,24.939226', 'Mäkkylä::60.22257,24.83063')}

    return render_template('routes.html', routes=routes)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=80)
