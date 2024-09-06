from rest_framework import viewsets
from rest_framework.response import Response
from .models import PersonalityTest
from .serializers import PersonalityTestSerializer
import requests
import openai

# Initialize OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'
PERSONALITY_API_URL = 'https://16personalities.com/api/your-endpoint'  # Replace with actual API endpoint

class PersonalityTestViewSet(viewsets.ModelViewSet):
    queryset = PersonalityTest.objects.all()
    serializer_class = PersonalityTestSerializer

    def create(self, request, *args, **kwargs):
        # Extract data
        name = request.data.get('name')
        email = request.data.get('email')
        personality_type = request.data.get('personality_type')

        # Get personality details
        personality_data = self.get_personality_details(personality_type)

        # Get color recommendation from ChatGPT
        recommended_color = self.get_color_recommendation(personality_data)

        # Save personality test result
        test_result = PersonalityTest.objects.create(
            name=name,
            email=email,
            personality_type=personality_type,
            recommended_color=recommended_color
        )
        serializer = self.get_serializer(test_result)
        return Response(serializer.data)

    def get_personality_details(self, personality_type):
        # Make an API request to get personality details (mocked here)
        response = requests.get(f'{PERSONALITY_API_URL}?type={personality_type}')
        return response.json()

    def get_color_recommendation(self, personality_data):
        # Example prompt to ChatGPT
        prompt = f"Based on the personality details {personality_data}, recommend a paint color."

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        
        return response.choices[0].text.strip()

