from flask import Flask, request, render_template_string
import random
from apscheduler.schedulers.background import BackgroundScheduler
import datetime

app = Flask(__name__)

# Different categories of responses
responses = {
    "notification": [
        "Notification: Check out our new products!",
        "Notification: Don't miss our special offers!",
        "Notification: New arrivals are now available!",
        "Notification: Limited-time discounts just for you!"
    ],
    "product_inquiry": [
        "We offer a wide range of products! Please specify the category you're interested in.",
        "Our latest products are top quality and reasonably priced. Let us know what you're looking for!",
        "Are you looking for something specific? We have new items in electronics, clothing, and more!"
    ],
    "shipping_info": [
        "Standard shipping usually takes 3-5 business days.",
        "You can track your order in your account under 'Order History'.",
        "Need faster shipping? We offer express options at checkout."
    ],
    "returns_refunds": [
        "You can return items within 30 days of purchase for a full refund.",
        "Refunds are processed within 5-7 business days after we receive the returned item.",
        "Please check our Returns Policy page for more details on how to process a return."
    ],
    "account_help": [
        "You can reset your password from the 'Forgot Password' link on the login page.",
        "For account security, please contact our support team to change sensitive information.",
        "Need help logging in? Make sure your credentials are correct or reset your password."
    ],
    "general_assistance": [
        "How can I assist you further?",
        "Let me know if you need help with anything.",
        "I'm here to help with any questions you have.",
        "Feel free to ask about our products or services."
    ]
}

# Keywords to match different response categories
keywords = {
    "notification": ["new", "offer", "discount", "deal", "latest", "product", "arrival", "special"],
    "product_inquiry": ["product", "item", "buy", "purchase", "category", "latest"],
    "shipping_info": ["shipping", "delivery", "track", "time", "order status"],
    "returns_refunds": ["return", "refund", "exchange", "policy"],
    "account_help": ["account", "login", "password", "reset", "security"],
}

# Predefined questions related to notifications
notification_related_questions = [
    "What triggers users to open notifications more often?",
    "What percentage of users interact with notifications?",
    "How can we personalize notifications for better engagement?",
    "How often should we send notifications to maximize user retention?",
    "What are the open rates for push notifications sent in the last month?",
    "What percentage of notifications result in conversions?",
    "How does the frequency of notifications affect user retention?",
    "What trends can we observe in user engagement with notifications?",
    "How can we use notifications to increase sales?",
    "What is the impact of promotional notifications on user purchases?",
    "How do users respond to notifications about cart abandonment?",
    "What is the best time to send sales-related notifications?",
    "How can notifications encourage users to revisit the app?",
    "How do limited-time offers in notifications influence user behavior?",
    "What is the effectiveness of segmented notifications in driving purchases?",
    "How can notifications be used to upsell products?",
    "What content works best for re-engagement notifications?",
    "How do users react to notifications about price drops?",
    "What is the role of notifications in user loyalty programs?",
    "How can real-time notifications enhance user experience?",
]

# Placeholder responses for predefined questions
predefined_answers = {
    "What are the most common reasons users abandon their carts?": "Users often abandon carts due to high shipping costs, unexpected fees, or a complicated checkout process.",
    "How can we identify users most likely to make a purchase?": "By analyzing browsing patterns, time spent on pages, and cart additions, we can identify high-purchase-intent users.",
    "What triggers users to open notifications more often?": "Personalized and time-sensitive notifications are more likely to be opened.",
    "What percentage of users interact with notifications?": "Approximately 20% of users interact with notifications, varying by industry.",
    "How can we personalize notifications for better engagement?": "Use user behavior data, like preferences and purchase history, to personalize notifications.",
    "How often should we send notifications to maximize user retention?": "Sending 2-3 notifications per week ensures retention without overwhelming users.",
    "What are the open rates for push notifications sent in the last month?": "Open rates average 15-25%, depending on the content and audience.",
    "What percentage of notifications result in conversions?": "About 5-10% of notifications lead to purchases, based on relevance and timing.",
    "How does the frequency of notifications affect user retention?": "Higher frequency risks fatigue; 2-3 weekly notifications balance retention and engagement.",
    "What trends can we observe in user engagement with notifications?": "Engagement trends show higher interaction with personalized and limited-time offers.",
    "How can we use notifications to increase sales?": "Sales can be increased by sending targeted notifications about discounts, new arrivals, and limited-time offers.",
    "What is the impact of promotional notifications on user purchases?": "Promotional notifications significantly boost sales, with up to a 10% conversion rate for well-timed offers.",
    "How do users respond to notifications about cart abandonment?": "Cart abandonment notifications have a 15-20% open rate and often result in users completing their purchases.",
    "What is the best time to send sales-related notifications?": "Evenings between 6-8 PM and lunch hours (12-2 PM) show the highest engagement rates for sales notifications.",
    "How can notifications encourage users to revisit the app?": "Notifications about exclusive content, trending products, or loyalty rewards can effectively bring users back to the app.",
    "How do limited-time offers in notifications influence user behavior?": "Limited-time offers create urgency, driving up to a 30% increase in click-through rates.",
    "What is the effectiveness of segmented notifications in driving purchases?": "Segmented notifications tailored to user preferences can double conversion rates compared to generic notifications.",
    "How can notifications be used to upsell products?": "Send notifications suggesting complementary products based on recent purchases or browsing behavior.",
    "What content works best for re-engagement notifications?": "Content such as personalized discounts, price drops, and new arrivals works best for re-engagement.",
    "How do users react to notifications about price drops?": "Notifications about price drops have a 20-30% open rate and are highly effective for price-sensitive users.",
    "What is the role of notifications in user loyalty programs?": "Notifications keep users informed about loyalty points, upcoming rewards, and exclusive member benefits.",
    "How can real-time notifications enhance user experience?": "Real-time notifications provide immediate updates about order status, flash sales, and time-sensitive offers, improving user satisfaction.",
}

# Predefined questions
predefined_questions = list(predefined_answers.keys())

# Store chat history
chat_history = []
user_feedback = []

# Scheduler for sending notifications
scheduler = BackgroundScheduler()

def send_notification():
    print("Simulated Notification: Sending a push notification...")

# Schedule the notification function
scheduler.add_job(send_notification, 'interval', minutes=10)
scheduler.start()

def determine_response(user_message):
    # Check if the message matches a predefined question
    if user_message in predefined_answers:
        # If the question relates to notifications, simulate a notification push
        if user_message in notification_related_questions:
            send_notification()  # Simulate the notification push
        return predefined_answers[user_message]
    
    # Check for category-based responses by keyword matching
    for category, keywords_list in keywords.items():
        if any(keyword in user_message.lower() for keyword in keywords_list):
            return random.choice(responses[category])
    
    # Default to general assistance if no keywords are matched
    return random.choice(responses["general_assistance"])

# HTML template with integrated wallpaper and updated Bootstrap styles
html_template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="manifest" href="/static/manifest.json">
    <script>
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/static/service-worker.js')
          .then(() => console.log('Service Worker Registered'))
          .catch((error) => console.log('Service Worker Registration Failed:', error));
      }
    </script>
    <style>
      body {
        background: url('/static/ecommerce.png') no-repeat center center fixed;
        background-size: cover;
        color: white;
      }
      .card {
        background-color: rgba(0, 0, 0, 0.7);
        color: white;
        border-radius: 15px;
        padding: 20px;
      }
      .btn-primary {
        background-color: #ff7f50;
        border-color: #ff7f50;
      }
      .btn-primary:hover {
        background-color: #ff4500;
        border-color: #ff4500;
      }
      .btn-secondary {
        background-color: #ffdf80;
        border-color: #ffdf80;
      }
      .btn-secondary:hover {
        background-color: #ffd700;
        border-color: #ffd700;
      }
      .form-control {
        border-radius: 10px;
      }
    </style>
    <title>Notification Chatbot</title>
  </head>
  <body>
    <div class="container my-5">
      <div class="card mx-auto">
        <div class="card-header text-center">
          <h2>Notification Chatbot</h2>
        </div>
        <div class="card-body">
          <form method="POST" action="/" class="mb-4">
            <div class="form-group">
              <label for="message">Enter your message:</label>
              <input type="text" id="message" name="message" class="form-control" placeholder="Type your message here..." required>
            </div>
            <button type="submit" class="btn btn-primary btn-block">Send</button>
          </form>
          <h3>Or select a predefined question:</h3>
          <form method="POST" action="/">
            <div class="form-group">
              <label for="predefined-question">Choose a question:</label>
              <select id="predefined-question" name="message" class="form-control">
                {% for question in predefined_questions %}
                  <option value="{{ question }}">{{ question }}</option>
                {% endfor %}
              </select>
            </div>
            <button type="submit" class="btn btn-secondary btn-block">Ask</button>
          </form>
          <h3>Chat History:</h3>
          <div id="chat-history" class="mt-3">
            {% for interaction in chat_history %}
              <div class="alert alert-light">
                <p><strong>User:</strong> {{ interaction['user_message'] }}</p>
                <p><strong>Bot:</strong> {{ interaction['bot_response'] }}</p>
              </div>
            {% endfor %}
          </div>
          <h3>Feedback:</h3>
          <form id="feedback-form">
            <div class="form-group">
              <label for="feedback">Rate the notification system:</label>
              <select class="form-control" id="feedback" name="feedback">
                <option value="relevant">Relevant</option>
                <option value="irrelevant">Irrelevant</option>
              </select>
            </div>
            <button type="button" class="btn btn-success btn-block" onclick="submitFeedback()">Submit Feedback</button>
          </form>
          <div id="feedback-message" class="mt-3"></div>
        </div>
      </div>
    </div>
    <script>
      function submitFeedback() {
        const feedback = document.getElementById('feedback').value;
        fetch('/feedback', {
          method: 'POST',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          body: `feedback=${encodeURIComponent(feedback)}`
        }).then(response => response.json())
          .then(data => {
            document.getElementById('feedback-message').innerHTML = '<div class="alert alert-success">Feedback submitted successfully!</div>';
          })
          .catch(error => {
            document.getElementById('feedback-message').innerHTML = '<div class="alert alert-danger">Failed to submit feedback.</div>';
          });
      }
    </script>
  </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_message = request.form['message']
        bot_response = determine_response(user_message)
        chat_history.append({'user_message': user_message, 'bot_response': bot_response})

    return render_template_string(html_template, chat_history=chat_history, predefined_questions=predefined_questions)

@app.route('/feedback', methods=['POST'])
def feedback():
    feedback = request.form.get('feedback')
    user_feedback.append(feedback)
    return {"status": "Feedback recorded successfully"}, 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
