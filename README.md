# Assistant

Text-based assistant  

# Install
echo OPENAI_API_KEY="insert your key" >> .env

python3 -m venv venv  
source venv/bin/activate  

pip install openai  
pip install python-dotenv  
pip install pyttsx3  

python assistant.py
