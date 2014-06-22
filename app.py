from bottle import route, run, template, static_file, error
import os
music_dir = '/path/to/your/music/directory'

@route('/')
@route('/<name>')
def player(name='index'):
    lst = [m.strip('.mp3') for m in os.listdir(music_dir)]
    return template('music', name=name, lst=lst)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=music_dir)

@error(404)
def error404(error):
    return 'Sorry,nothing here.'

run(host='localhost', port=5000)
