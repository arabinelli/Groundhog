# Groundhog - WIP
 A simple decorator to get notified if there's an issue with your deployed code

## TL;DR
When running pre-alpha stage code, there isn't the time to properly build stable and error-proof code. When deployed (e.g. for concept validation tests in early product discovery), a code failing silently could mean losing valuable data. 

Groundhog provides a framework that can be easily added to existing code and push notifications to channels

## Install
Hold on, will be there soon :) 

## Usage

Follow this three steps process:
1) Initialize suricato giving the name of the app that it's monitoring
2) Register a connector (Slack is included as a demo, but whatever class meeting requirements could work!)
3) Decorate a function with Suricato

``` python
import math

#TODO Change this into groundhog.connectors.slack 
from connectors.slack import SlackConnector
from groundhog import Groundhog

# tell Alan the groundhog what is it that it's watching
# Why alan? https://www.youtube.com/watch?v=xaPepCVepCg
alan = Groundhog(app_name="Groundhog test")

# register a connector - Slack for example
CHANNEL = "#sif-testing-slack-bot" # the cannel name where you want to receive the notifications
alan.register_connector(SlackConnector,SLACK_BOT_TOKEN,CHANNEL)

# assign the sentinel to watch this function
@alan.watch
def failable_func(n):
    """Just a function that could easily fail with the wrong input"""
    math.sqrt(n)

# all good!
failable_func(4)

# doesn't look too good...
failable_func(-4)
```


