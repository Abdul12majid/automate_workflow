class ReportHandler:

    def run(self, config, context):

        context["report"] = {
            "generated": True
        }

        return context