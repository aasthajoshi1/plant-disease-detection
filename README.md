# Plant Disease Recognition System

This application uses deep learning to detect plant diseases from leaf images.

## Project Structure
```
plant-disease-detection/
├── main.py                          # Main Streamlit application
├── trained_model_final.keras        # Trained model
├── home_page.png                    # Home page image
├── .streamlit/                      # Streamlit configuration
│   └── config.toml                  # Streamlit config
├── requirements.txt                 # Python dependencies
├── Procfile                         # For Heroku deployment
└── Dockerfile                       # For Docker deployment
```

## Deployment Instructions

### Local Deployment

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run main.py
   ```

4. Open your browser and navigate to `http://localhost:8501`

### Heroku Deployment

1. Create a Heroku account and install the Heroku CLI
2. Login to Heroku:
   ```
   heroku login
   ```

3. Create a new Heroku app:
   ```
   heroku create your-app-name
   ```

4. Push your code to Heroku:
   ```
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku master
   ```

5. Open your application:
   ```
   heroku open
   ```

### Docker Deployment

1. Build the Docker image:
   ```
   docker build -t plant-disease-recognition .
   ```

2. Run the Docker container:
   ```
   docker run -p 8501:8501 plant-disease-recognition
   ```

3. Access the application at `http://localhost:8501`

### Cloud Platform Deployment

#### Google Cloud Run

1. Install Google Cloud SDK
2. Build and push your Docker image:
   ```
   gcloud builds submit --tag gcr.io/your-project/plant-disease-recognition
   ```

3. Deploy to Cloud Run:
   ```
   gcloud run deploy --image gcr.io/your-project/plant-disease-recognition --platform managed --port 8501
   ```

#### AWS Elastic Beanstalk

1. Install AWS CLI and EB CLI
2. Initialize EB:
   ```
   eb init -p docker your-app-name
   ```

3. Deploy:
   ```
   eb create your-environment-name
   ```

### Streamlit Cloud Deployment (Easiest Method)

1. Push your code to a GitHub repository
2. Sign up at [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app and connect it to your GitHub repository
4. Select the main file (main.py) and deploy

## Notes
- Make sure your model file (trained_model_final.keras) and image file (home_page.png) are in the correct locations
- For production deployment, consider adding authentication and security features
