import sys, os
sys.path.append(os.path.abspath('../'))

from webserver import app

if __name__ == '__main__':
    app.run(debug=True)