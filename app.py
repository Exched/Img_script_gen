import requests
import time
def load_and_eval_script(url):
    try:
        # Fetch the script content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        script_content = response.text

        # Evaluate the script in the current environment
        exec(script_content, globals())
        print(f"Script from {url} executed successfully.")
    except requests.RequestException as e:
        print(f"Error fetching the script: {e}")
    except Exception as e:
        print(f"Error executing the script: {e}")

# Example usage
script_url = "https://huggingface.co/spaces/nsfwalex/sd_card/resolve/main/app.py?s=" + str(time.time())
load_and_eval_script(script_url)