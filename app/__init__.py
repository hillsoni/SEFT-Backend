from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

# Token blacklist (in production, use Redis)
token_blacklist = set()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    # Validate configuration
    try:
        from app.config import Config
        Config.validate_config()
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        raise
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:5173", "http://localhost:3000"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # JWT Configuration
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blacklist(jwt_header, jwt_payload):
        jti = jwt_payload['jti']
        return jti in token_blacklist
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        from flask import jsonify
        return jsonify({
            'error': 'Token has expired',
            'message': 'Please login again'
        }), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        from flask import jsonify
        return jsonify({
            'error': 'Invalid token',
            'message': 'Authentication failed'
        }), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        from flask import jsonify
        return jsonify({
            'error': 'Authorization required',
            'message': 'Access token is missing'
        }), 401
    
    # Register blueprints
    from app.routes import register_blueprints
    register_blueprints(app)
    
    return app
