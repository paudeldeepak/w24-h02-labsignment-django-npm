import os
import sys

def get_script_dir():
    """
    Returns the directory where the script is located.
    """
    return os.path.dirname(os.path.realpath(__file__))

def run_command(command):
    """
    Executes a given shell command and logs the command.
    Exits the script if the command fails.

    :param command: The shell command to be executed.
    """
    print(f"Running command: {command}")
    if os.system(command) != 0:
        sys.exit(f"Command failed: {command}")

def get_python_bin_path():
    """
    Returns the absolute path to the Python binary inside the virtual environment.
    """
    return os.path.join(get_script_dir(), 'venv', 'bin', 'python3')

def get_pip_bin_path():
    """
    Returns the absolute path to the pip binary inside the virtual environment.
    """
    return os.path.join(get_script_dir(), 'venv', 'bin', 'pip')

def setup_virtualenv():
    """
    Creates a virtual environment if it does not already exist.
    """
    if not os.path.exists(os.path.join(get_script_dir(), 'venv')):
        print("Creating virtual environment...")
        run_command("virtualenv venv --python=python3")
    else:
        print("Virtual environment already exists")

def install_requirements():
    """
    Installs Python dependencies listed in requirements.txt.
    """
    if not os.path.exists(os.path.join(get_script_dir(), 'requirements.txt')):
        sys.exit("requirements.txt not found")
    pip_path = get_pip_bin_path()
    print(f"Installing Python requirements from {pip_path}")
    run_command(f'"{pip_path}" install -r requirements.txt')

def install_npm_packages():
    """
    Installs Node.js dependencies listed in package.json using npm.
    """
    if not os.path.exists(os.path.join(get_script_dir(), 'package.json')):
        sys.exit("package.json not found")
    print("Installing npm packages...")
    run_command("npm install")

def run_esbuild():
    """
    Runs esbuild to bundle JavaScript files.
    """
    os.chdir(os.path.join(get_script_dir(), 'lab2'))
    if not os.path.exists('main.js'):
        sys.exit("main.js not found")
    print("Running esbuild...")
    run_command("npx esbuild main.js --bundle --minify --sourcemap --outfile=./emojis/static/main.min.js")

def start_django_server():
    """
    Starts the Django development server.
    """
    print("Starting Django server...")
    python_path = get_python_bin_path()
    os.chdir(os.path.join(get_script_dir(), 'lab2'))
    run_command(f'"{python_path}" manage.py runserver 0.0.0.0:8000')

def main():
    setup_virtualenv()
    install_requirements()
    install_npm_packages()
    run_esbuild()
    start_django_server()

if __name__ == '__main__':
    main()
