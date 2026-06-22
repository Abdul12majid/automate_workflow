class EmailHandler:

    def run(self, config, context):

        recipient = config.get("recipient")

        context["email_sent"] = {
            "recipient": recipient,
            "status": "sent"
        }

        return context