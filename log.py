from datetime import datetime

logFile = 'logger.txt'

def log(msg):
    """
    Saves the msg in a log file {log_file} and prints it in the console.
    :param msg: the message to be append in the log file
    """
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
    formatted = f'{timestamp} - {msg}'
    with open(logFile, 'a') as f:
        f.write(formatted + '\n')

def show_log():
    try:
        with open(logFile, 'r') as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f'Cannot open {logFile}. error={e}')