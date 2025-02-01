import traceback
import logging

# Make sure logging is configured
logging.basicConfig(level=logging.ERROR)

element = "sample_element"  # Define `element` with an appropriate value

try:
    # Your code logic here
    pass
except Exception as e:
    error_message = (
        f"Error processing element: {element}\n"
        f"Exception Type: {type(e).__name__}\n"
        f"Exception Message: {e}\n"
        f"Traceback: {traceback.format_exc()}"
    )
    logging.error(error_message)
    print(error_message)
