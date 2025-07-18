def read_logs(file_path="logs/app.log", lines=50):
    try:
        with open(file_path, 'r') as file:
            return ''.join(file.readlines()[-lines:])
    except Exception as e:
        return f"Error reading log: {str(e)}"
