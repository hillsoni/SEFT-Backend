import google.generativeai as genai
import os

class GeminiService:
    def __init__(self):
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        for model in genai.list_models():
            if 'generateContent' in model.supported_generation_methods:
                print(model.name)
        self.model = genai.GenerativeModel('models/gemini-2.0-flash')
    
    def generate_diet_plan(self, user_data):
        """Generate personalized diet plan using Gemini"""
        prompt = f"""
        Create a detailed diet plan for:
        Age: {user_data['age']}
        Gender: {user_data['gender']}
        Weight: {user_data['weight']} kg
        Height: {user_data['height']} cm
        Activity Level: {user_data['activity_level']}
        Goal: {user_data['goal']}
        Diet Type: {user_data['diet_type']}
        Health Conditions: {user_data.get('health_conditions', [])}
        
        Provide a complete daily meal plan with breakfast, lunch, snack, and dinner.
        Include calorie counts and nutritional information.
        """
        response = self.model.generate_content(prompt)
        return response.text
    
    def chat_response(self, question, context="diet"):
        """Generate chatbot response - restricted to diet topics"""
        if context != "diet":
            return "I can only answer questions related to diet and nutrition."
        
        prompt = f"""
        As a professional nutritionist, answer this question:
        {question}
        
        Provide accurate, helpful information about diet and nutrition.
        """
        response = self.model.generate_content(prompt)
        return response.text