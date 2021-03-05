from app import app, render_template

@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    Loads up app page
    """
    return render_template('views/index.html')