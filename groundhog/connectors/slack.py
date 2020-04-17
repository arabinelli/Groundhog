from slack import WebClient
import ssl as ssl_lib
import certifi

from templates.slack import TemplateErrorNotification


class SlackConnector():
    def __init__(self, slack_bot_token,channel):
        """
        Initializes the connection with slack

        ARGUMENTS:
        slack_bot_token (str) - The Bot token obtained from Slack
        channel (str) - The string of the channel to post the messages to
        """
        self.slack_web_client = WebClient(token=slack_bot_token)
        self.message_template = TemplateErrorNotification(channel)
        

    def notify(self,monitored_app_name,func,error,func_args,func_kwargs):
        """Sends notification to slack channel"""
        payload = self.message_template\
                        .get_notification_payload(monitored_app_name = monitored_app_name,
                                                  func=func,
                                                  e = error,
                                                  function_args=func_args,
                                                  function_kwargs=func_kwargs)

        self.slack_web_client.chat_postMessage(**payload)