#  Explainable & Bias-Aware Product Recommendation System

##  Project Overview
This project is an intelligent e-commerce product recommendation system that suggests relevant products based on similarity, user context, and fairness principles. Unlike traditional systems, it not only recommends products but also explains the reason behind each recommendation while ensuring balanced visibility for both popular and less-known products.

---

##  Objectives
- Improve user experience through personalized recommendations  
- Provide transparency using explainable AI  
- Reduce popularity bias in product recommendations  
- Enhance product discovery in e-commerce platforms  

---

##  Key Features
-  Content-Based Recommendation using TF-IDF and Cosine Similarity  
-  Explainable AI (shows why a product is recommended)  
-  Bias-Aware System (balances popular & less-rated products)  
-  Price-Based Filtering (budget-aware recommendations)  
-  Simple Web Interface using Flask  

---

##  Novelty
This project introduces a hybrid approach combining:

1. **Explainable Recommendation**  
   Displays reasons such as:
   - Same category  
   - Within budget  
   - Highly rated  

2. **Bias-Aware Recommendation**  
   Ensures fair exposure by:
   - Including both popular and less-explored products  
   - Avoiding over-dependence on highly rated items  

This improves transparency, fairness, and user trust in recommendation systems.

---

##  Tech Stack
- Python  
- Pandas  
- Scikit-learn  
- Flask  
- HTML  

---

##  Project Structure

ecommerce-recommendation-system/
│
├── data/
│ └── flipkart_products.csv
│
├── src/
│ └── model.py
│
├── app/
│ ├── app.py
│ └── templates/
│ └── index.html
│
├── requirements.txt
└── README.md


---

## Dataset
- Flipkart Product Dataset (Kaggle)  
- Includes:
  - Product Name  
  - Category  
  - Description  
  - Price  
  - Rating  

---

##  How to Run the Project

### 1️. Clone the Repository

git clone https://github.com/ChandanaKamesh123/project-1.git

cd project-1


### 2️. Install Dependencies

pip install -r requirements.txt


### 3️. Run the Application

python app/app.py


### 4️. Open in Browser

http://127.0.0.1:5000/


---

##  Sample Output

Input:

Product: Redmi Note 10
Budget: 15000


Output:

Product: Realme Narzo
Price: ₹14000
Rating: 4.2
Reason: same category, within your budget, highly rated


---

##  Future Enhancements
- Add user login & personalization  
- Integrate real-time user behavior tracking  
- Use deep learning for better recommendations  
- Deploy on cloud platforms  

---

##  Conclusion
This project demonstrates how machine learning can be applied to build intelligent and fair recommendation systems. By combining explainability and bias-awareness, it improves both user trust and product visibility in e-commerce platforms.

---

##  Author
CHANDANA KAMESH
