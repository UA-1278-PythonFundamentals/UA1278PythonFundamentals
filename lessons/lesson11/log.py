import logging

import datetime

datetime.datetime.now()


log_dir = "./lessons/lesson11/log/"
logging.basicConfig(
    level=logging.INFO,
    filename=f"{log_dir}user_log{datetime.datetime.now().strftime('%d.%m.%Y__%H_%M_%S')}.log",
    filemode="a",
    format="%(asctime)s  %(name)s - %(levelname)s  >> %(funcName)s - %(message)s"
    )




if __name__ == "__main__":
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')