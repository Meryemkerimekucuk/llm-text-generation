import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("google_apikey")
client = genai.Client(api_key=api_key)

def text_generate(topic, temperature=0.7, max_output_tokens=1024, top_p=0.9):
    try:
        prompt = f"{topic} konusunu araştır."
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="""
                Sen bir sağlık uzmanısın.
                Her zaman türkçe cevap ver.
                Cevap verirken kaynak belirt.
                Profosyonel bir şekilde cevap ver.
                Sade bir dil kullan.""" ,
                temperature=temperature,
                max_output_tokens=max_output_tokens,
                top_p=top_p,
                response_mime_type="application/json",
                response_schema={
                    "type": "OBJECT",
                    "properties": {
                        "konu": {"type": "STRING"},
                        "seviye": {"type": "STRING"},
                        "aciklama": {"type": "STRING"},
                    },
                    "required": ["konu", "seviye", "aciklama"],
                },
            )
        )

        return response.text

    except Exception as e:
        print(f"Error generating text: {e}")
        return None