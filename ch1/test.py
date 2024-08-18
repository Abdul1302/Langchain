from decouple import config
SECRET_KEY=config('GROQ_API_KEY')
print(SECRET_KEY)