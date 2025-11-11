from flask import Flask
from .pages import pages_bp, api_bp

def create_app():
    app = Flask(__name__)
    
    app.json.ensure_ascii = False  
    
    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    return app
