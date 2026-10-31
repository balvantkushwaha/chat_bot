
# home/views.py

import json
import os

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from groq import Groq


def home(request):
    return render(request, "index.html")


@require_POST
def chat(request):
    try:
        data = json.loads(request.body)
        user_message = data.get("message", "").strip()

        if not user_message:
            return JsonResponse(
                {"error": "Please enter a message."},
                status=400
            )

        # Current browser session se conversation history lein
        history = request.session.get("chat_history", [])

        # Groq API ko current message aur previous context bhejein
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful AI assistant. "
                    "Use previous messages in this conversation "
                    "to answer follow-up questions."
                ),
            },
            *history,
            {"role": "user", "content": user_message},
        ]

        client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
        )

        answer = response.choices[0].message.content or ""

        # User aur assistant dono messages session mein save karein
        history.extend([
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": answer},
        ])

        # Sirf recent 20 messages rakhein
        request.session["chat_history"] = history[-20:]
        request.session.modified = True

        return JsonResponse({"reply": answer})

    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"error": "Invalid request."}, status=400)

    except Exception:
        # API key ya internal server details user ko expose na karein
        return JsonResponse(
            {"error": "Chat service error. Please try again."},
            status=500,
        )


@require_POST
def new_chat(request):
    # Current session ki conversation history delete karein
    request.session.pop("chat_history", None)
    request.session.modified = True

    return JsonResponse({"success": True, "message": "New chat started."})
