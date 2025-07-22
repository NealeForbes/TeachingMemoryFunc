import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Team Memory Function triggered.")

    try:
        req_body = req.get_json()
        message = req_body.get("message")
    except ValueError:
        logging.error("Invalid JSON body received.")
        return func.HttpResponse("Invalid JSON body.", status_code=400)

    if not message:
        logging.warning("No 'message' field found in the request body.")
        return func.HttpResponse("Please provide a 'message' in the request body.", status_code=400)

    logging.info(f"Received message: {message}")
    return func.HttpResponse(f"Message received: {message}", status_code=200)
