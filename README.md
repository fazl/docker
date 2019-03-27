dockertutorial
==============
learning how to use docker.. encapsulating development dependencies into a portable package sounds great

https://docs.docker.com/get-started/

Misc Notes 
==========
   
git: On adding these file to git I again see this warning:

    warning: LF will be replaced by CRLF in dockertutorial/runfriendlyhello.bat.
    The file will have its original line endings in your working directory.

Nowadays even windows based editors can cope with \n line endings, so I disabled the line-ending conversions like this:
    git config --unset core.autocrlf
Doh! this didn't help, so I had to add it back :
    git config --add core.autocrlf false
And check it's worked via: 
    $ git config --get core.autocrlf
    false

