class TemplateErrorNotification:
    """
    Constructs the onboarding message and stores the state of which tasks were completed.
    Source: https://github.com/slackapi/python-slackclient/blob/master/tutorial/02-building-a-message.md 
    """

    DIVIDER_BLOCK = {"type": "divider"}

    def __init__(self, channel):
        self.channel = channel
        self.username = "alphasentinelbot"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""

    def get_notification_payload(self,monitored_app_name,func,e,function_args=[],
                                function_kwargs=[]):
        """Builds the message in Block UI"""
        self.app_name = monitored_app_name
        self.e = e
        self.function_args = function_args
        self.function_kwargs = function_kwargs

        blocks = [
                *self._get_initial_block(func),
                self.DIVIDER_BLOCK,
                *self._get_error_block()
        ]
        if len(self.function_args) > 0:
            blocks += [
                self.DIVIDER_BLOCK,
                *self._get_args_block()
            ]
        if len(self.function_kwargs) > 0:
            blocks += [
                self.DIVIDER_BLOCK,
                *self._get_kwargs_block()
            ]
        blocks += [self.DIVIDER_BLOCK]

        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": blocks
        }

    def _get_initial_block(self,func):
        text = (
            ":rotating_light: *Oh, no! Something went wrong!* :rotating_light:\n\n"
            f"There was an error with your app *{str(self.app_name)}*:\n\n"
            f"The function `{func.__name__}` threw an error."
        )
        return self._get_text_block(text)

    def _get_error_block(self):
        text = (
            ":warning:The following error was raised\n\n"
            f"```{self.e}```"
        )
        return self._get_text_block(text)
    
    def _get_args_block(self):
        text = (
            ":question:The following arguments were provided\n\n"
            f"{self.function_args}"
        )
        return self._get_text_block(text)
    
    def _get_kwargs_block(self):
        if len(self.function_args) > 0:
            text = "Also, the following keyword arguments were provided\n"
        else:
            text = "The following keyword arguments were provided\n"
        for key,value in self.function_kwargs.items():
            text += f"\n`{key}` = `{value}`"
        return self._get_text_block(text)

    @staticmethod
    def _get_text_block(text):
        return [
            {"type": "section", "text": {"type": "mrkdwn", "text": text}}
        ]