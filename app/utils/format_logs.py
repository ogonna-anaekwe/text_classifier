import logging
import uuid

def format_logs():
    """
    Extends the base configuration of the logging module to include the transaction_id.
    This ensures a unique id is captured for every transaction with the server.

    Parameters:
        None
    
    Returns:
        logger: new logging object with the transaction_id.
    """
    transaction_id = {'transaction_id': uuid.uuid1()}
    logger = logging.getLogger(__name__)
    syslog = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(transaction_id)s : %(message)s')
    syslog.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(syslog)

    logger = logging.LoggerAdapter(logger, transaction_id)
    return logger
