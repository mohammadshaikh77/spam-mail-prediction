📧 Spam Mail Prediction
A Machine Learning project that predicts whether an email is Spam or Ham (Not Spam) using Logistic Regression and TF-IDF vectorization. The project is deployed with Streamlit Cloud for easy access.
🔗 Live Demo: Spam Mail Prediction App
🚀 Features
Classifies email messages as Spam or Ham
Built with Logistic Regression for classification
Uses TF-IDF Vectorizer to transform text into numerical features
Includes keyword-based filtering to detect tricky spam mails
Deployed as an easy-to-use Streamlit Web App
🛠️ Tech Stack
Python
Pandas, NumPy
Scikit-learn (ML Model, TF-IDF, Evaluation)
Joblib (Model Serialization)
Streamlit (Deployment & Web App)
📊 Model Performance
Training Accuracy: ~98%
Testing Accuracy: ~97%
📂 Project Structure
app.py → Streamlit app script
spam-ham.pkl → Trained Logistic Regression model
tfidf.pkl → TF-IDF vectorizer
requirements.txt → Project dependencies
mail_data.csv → Dataset (if included)
README.md → Project documentation
🌐 Deployment
The app is hosted on Streamlit Cloud.
Pushing updates to GitHub automatically refreshes the deployment.
🔗 Live App: https://spam-mail-prediction-db5gleesejdwcfygmyhwp7.streamlit.app
📚 Learning Outcomes
Text preprocessing & vectorization with TF-IDF
Training and evaluating ML classification models
Saving & reusing models with Joblib
Building an end-to-end ML pipeline
Deploying ML projects using Streamlit Cloud
Debugging real-world deployment challenges
✨ Future Improvements
Experiment with advanced models (Random Forest, SVM, Deep Learning)
Add visualizations for word importance & feature weights
Enhance UI/UX for a smoother user experience
Expand to multilingual spam detection
🙌 Acknowledgements
Dataset: SMS Spam Collection Dataset (UCI/Kaggle)
Libraries: Scikit-learn, Pandas, NumPy, Streamlit
