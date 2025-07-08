# Twitter Sentiment Classifier

A simple machine learning web app that classifies tweets as **Positive** or **Negative** using natural language processing and logistic regression. Built with Python, Scikit-learn, and deployed using Streamlit.

## 📌 Features
- Clean and minimal Streamlit interface
- Enter any tweet to get instant sentiment prediction
- Pre-trained ML model using TF-IDF vectorization and logistic regression
- Preprocessing includes stopword removal and stemming
- Easily deployable to Streamlit Cloud

## 📁 Project Structure
```
TwitterSentimentApp/
│
├── app.py                  # Streamlit web app
├── predictor.py            # Preprocessing and prediction logic
├── models/
│   ├── model.pkl           # Trained sentiment classification model
│   └── vectorizer.pkl      # Saved TF-IDF vectorizer
├── requirements.txt        # Python dependencies
└── README.md               # Project overview
```

## 🚀 How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/your-username/twitter-sentiment-app.git
cd twitter-sentiment-app
```

2. **Create a virtual environment** (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app**
```bash
python -m streamlit run app.py
```

## 🌐 Deploy on Streamlit Cloud

1. Push this project to a public GitHub repository
2. Visit [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub account and select the repo
4. Set the app entry point as `app.py`
5. Click **Deploy**

## 🧠 Model Info

- Model: Logistic Regression
- Vectorizer: TF-IDF
- Task: Binary sentiment classification (Positive or Negative)
- Dataset:[Twitter sentiment dataset](https://www.kaggle.com/datasets/kazanova/sentiment140)

## 📚 Based On

This project is inspired by the [Twitter Sentiment Analysis using ML](https://www.youtube.com/watch?v=4YGkfAd2iXM&t=4866s) tutorial by **GeeksforGeeks**.

> I followed the tutorial for initial logic, and added structure, UI, model saving, and deployment readiness.

## 📄 License

This project is licensed under the MIT License.

> Note: Parts of this code were adapted from public tutorial material by GeeksforGeeks, used under fair-use for educational purposes.

## 🙋‍♂️ Author

Made with ❤️ by [Daron John](https://github.com/DaronJohn)
