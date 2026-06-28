from openai import OpenAI

from django.conf import settings


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

class AIExtractHandler:

    def run(self, config, context):

        text = context.get("text", "")

        fields = config.get("fields", [])

        prompt = f"""
        Extract the following fields:

        {fields}

        Text:

        {text}

        Return JSON only.
        """

        response = client.chat.completions.create(
            model="gpt-5",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        context["ai_data"] = response.choices[0].message.content

        return context