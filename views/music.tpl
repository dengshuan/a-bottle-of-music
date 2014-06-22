<!doctype html>
<html>
  <head>
    <title>{{name}} - A Bottle of Music</title>
  </head>
  <body>
    <h1><a href="/">Music List</a></h1>
    %if name != 'index':
        <audio src="/static/{{name}}.mp3" controls autoplay></audio>
    %end
    %for music in lst:
        <li><a href="/{{music}}">{{music}}</a></li>
    %end
  </body>
</html>
