from mainapp import app, db, User, Post



# регистрирует функцию как функцию контекста оболочки
@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post': Post}
