# hookman

> github webhooks manager

you just need run as a command in Linux

## first

    pip install hookman

## second
cd your github project and run 

    hookman --run -d
    
it will run in background

also you can set your `projectdir` like

    hookman --run -d --projectdir /my/github/project


####setting

pidfile=~/hookman.pid
logfile=~/hookman.log

######Develped by TDD
> you can test it just use `py.test .`

use Apache LICENSE  