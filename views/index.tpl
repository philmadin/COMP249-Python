% rebase('base.tpl')


% for image in images:
    <div class='flowtow'>
        <p><span class='date'>{{image['timestamp']}}</span> <span class='user'>{{image['user']}}</span></p>
        <img src='/static/images/{{image['filename']}}'>
        <p class='likes'>  {{image['likes']}} Likes</p>
        <form role='form' method='post' action='/like'>
          <input type='hidden' name='filename' value="{{image['filename']}}">
          <input class='btn btn-primary' type='submit' value='Like'>
        </form>
    </div>
% end