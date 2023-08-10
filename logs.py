import logging



def setup_logger(name, filename, formatter_format):
    logger = logging.getLogger(name)
    f_handler = logging.FileHandler(filename)
    f_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(formatter_format)
    f_handler.setFormatter(formatter)
    logger.addHandler(f_handler)
    return logger





def commit_log(name, Message='Test'):
    filename = f'./logs/{name.lower()}_commit.log'
    formatter_format = '%(message)s'
    logger = setup_logger(f'{name}_commit', filename, formatter_format)
    logger.warning(Message)



