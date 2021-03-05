from app import app, render_template

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Loads up app home
    """
    return render_template('views/home/home.html')