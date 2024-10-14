def log_in_file(log_message):
    with open('log.txt', 'a') as f:
        f.write(log_message + '\n')
