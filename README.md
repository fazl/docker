dockertutorial
==============
learning how to use docker.. encapsulating development dependencies into a portable package sounds great

https://docs.docker.com/get-started/

for one thing you can treat the docker file like a recipe for installing all the bits needed in your development environment
and you can fire it off on any machine with a build command
theoretically you can kiss goodbye to your "one special developement machine" risk

NOTE TO SELF: Remember to start each new tutorial/project inside this repo on a separate branch!


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


On windows to really stop the running container:
- first CTRL+C in the Docker Toolbox to get the prompt back
- the container is still running (test it by browsing the url.. yep)
- use the commands:
    docker container ls --> list it
    docker container stop <name or id> --> stop it
Otherwise next time you try start that container, error..

To start the container in detached mode (ie in the background) use the -d switch:

    docker run -d -p 4000:80 friendlyhello

Tagging
=======

You can version control your images (although, maybe Dockerfile versioning is less wasteful of space?) thus:
    docker tag friendlyhello fazl/get-started:part2
    (docker tag image username/repository:tag)
Register your username at hub.docker.com if you need one.

!!NB!! Login to docker locally before you try to push your tagged images to your repo.
    docker login
    docker push fazl/get-started:part2
    Then you can see your image at the docker website:
    
