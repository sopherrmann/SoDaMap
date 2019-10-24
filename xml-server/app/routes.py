from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/import', methods=['POST'])
def import_xml():
    pass


@app.route('/annotation', methods=['POST'])
def annotation():
    # needs to include mapped session, annotation, user (?)
    pass


@app.route('/logs', methods=['GET', 'POST'])
def get_all_logs():
    # get all logs
    # for POST add new log comment
    pass


@app.route('/logs/<id>')
def get_log(id: int):
    pass

