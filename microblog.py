from mainapp import app, db
from mainapp.models import User, Post



# регистрирует функцию как функцию контекста оболочки
@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post': Post}
