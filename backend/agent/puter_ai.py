import requests


WORKER_URL = "https://django-ai-bridge.puter.work/api/chat"


def ask_puter(prompt):
    try:
        response = requests.post(
            WORKER_URL,
            json={
                "message": prompt
            },
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        if not data.get("success"):
            return {
                "success": False,
                "error": data.get(
                    "error",
                    "Unknown Puter AI error"
                )
            }

        ai_response = data.get("response", {})
        message = ai_response.get("message", {})
        content = message.get("content", "")

        return {
            "success": True,
            "response": content
        }

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "Puter AI request timed out."
        }

    except requests.exceptions.RequestException as error:
        return {
            "success": False,
            "error": f"Worker request failed: {error}"
        }

    except Exception as error:
        return {
            "success": False,
            "error": f"Unexpected error: {error}"
        }