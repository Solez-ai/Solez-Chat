# Solez Chat

A Flask-based chatbot application using the OpenRouter API with Moonshot AI's Kimi model. This application provides an interactive chat interface where users can communicate with the AI model.

## Features

- Clean and simple web interface
- Powered by Moonshot AI's Kimi model through OpenRouter API
- Environment-based configuration
- Production-ready setup for Render deployment

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/Solez-ai/SolezChat-HTML-CSS-Python-.git
cd SolezChat-HTML-CSS-Python-
```

2. Create and activate the virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

3. Install the required packages:
```powershell
pip install -r requirements.txt
```

4. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your OpenRouter API key:
     ```
     OPENROUTER_API_KEY=your_api_key_here
     ```

5. Run the application locally:
```powershell
python app.py
```

6. Open your browser and visit:
```
http://localhost:5000
```

## Deployment to Render

### Prerequisites
- A Render account
- Your OpenRouter API key

### Configuration Steps

1. Create a new Web Service in Render
2. Connect your GitHub repository
3. Configure the following settings:
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

4. Add the following environment variable:
   - `OPENROUTER_API_KEY`: Your OpenRouter API key

### Additional Settings
- Python version is specified in `.python-version` (3.12.11)
- The application automatically configures itself for the Render environment

## Technologies Used

- Flask: Web framework
- Python 3.12
- OpenRouter API
- Gunicorn: Production server
- HTML/CSS: Frontend

## Project Structure

```
.
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── .env               # Local environment variables (not in git)
├── .python-version    # Python version specification
├── static/            # Static files (CSS, JS)
└── templates/         # HTML templates
    ├── index.html
    └── response.html
```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
