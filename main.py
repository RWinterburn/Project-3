import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Use the port assigned by Heroku, default to 5000 for local development
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)