class ExtractHandler:

    def run(self, config, context):

        fields = config.get("fields", [])

        extracted = {}

        for field in fields:
            extracted[field] = context.get(field)

        context["extracted_data"] = extracted

        return context