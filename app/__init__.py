# Load environment variables FIRST before anything else
from dotenv import load_dotenv
import os

# This must be the FIRST thing - load .env file
load_dotenv()

# Now import Flask and extensions
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

# Token blacklist storage
token_blacklist = set()

def create_app():
    app = Flask(__name__)
    
    # Debug: Print environment variables (remove in production)
    print("\n" + "="*70)
    print("🔍 CHECKING ENVIRONMENT VARIABLES")
    print("="*70)
    db_url = os.getenv('DATABASE_URL')
    print(f"DATABASE_URL: {db_url if db_url else '❌ NOT SET'}")
    print(f"JWT_SECRET_KEY: {'✅ SET' if os.getenv('JWT_SECRET_KEY') else '❌ NOT SET'}")
    print(f"SECRET_KEY: {'✅ SET' if os.getenv('SECRET_KEY') else '❌ NOT SET'}")
    print("="*70 + "\n")
    
    # Load config
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Configure CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:5173", "http://localhost:3000", "http://localhost:5174"],
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
        return jsonify({
            'error': 'Token has expired',
            'message': 'Please login again'
        }), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({
            'error': 'Invalid token',
            'message': 'Authentication failed'
        }), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({
            'error': 'Authorization required',
            'message': 'Access token is missing'
        }), 401
    
    # Register blueprints
    print("📝 Registering routes...")
    
    try:
        from app.routes.auth import bp as auth_bp
        app.register_blueprint(auth_bp)
        print("✓ Registered auth routes")
    except Exception as e:
        print(f"✗ Error loading auth routes: {e}")
    
    try:
        from app.routes.user import bp_user as user_bp
        app.register_blueprint(user_bp)
        print("✓ Registered user routes")
    except Exception as e:
        print(f"✗ Error loading user routes: {e}")
    
    try:
        from app.routes.yoga import bp as yoga_bp
        app.register_blueprint(yoga_bp)
        print("✓ Registered yoga routes")
    except Exception as e:
        print(f"✗ Error loading yoga routes: {e}")
    
    try:
        from app.routes.workout import bp as workout_bp
        app.register_blueprint(workout_bp)
        print("✓ Registered workout routes")
    except Exception as e:
        print(f"✗ Error loading workout routes: {e}")
    
    try:
        from app.routes.diet import bp as diet_bp
        app.register_blueprint(diet_bp)
        print("✓ Registered diet routes")
    except Exception as e:
        print(f"✗ Error loading diet routes: {e}")
    
    try:
        from app.routes.exercise import bp_exercise as exercise_bp
        app.register_blueprint(exercise_bp)
        print("✓ Registered exercise routes")
    except Exception as e:
        print(f"✗ Error loading exercise routes: {e}")
    
    try:
        from app.routes.chatbot import bp as chatbot_bp
        app.register_blueprint(chatbot_bp)
        print("✓ Registered chatbot routes")
    except Exception as e:
        print(f"✗ Error loading chatbot routes: {e}")
    
    print("✓ All routes registered\n")
    
    return app