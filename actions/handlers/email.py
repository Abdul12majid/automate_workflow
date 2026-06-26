from actions.utils.variables import insert


class EmailHandler:

    def run(self, config, context):

        recipient = insert(
            config.get("recipient"),
            context
        )

        subject = insert(
            config.get("subject", ""),
            context
        )

        context["email_sent"] = {
            "recipient": recipient,
            "subject": subject,
            "status": "sent",
        }

        return context