## Advanced ETL Pipeline
🚀 A robust ETL (Extract, Transform, Load) pipeline in Python that cleans, transforms, and loads data into a PostgreSQL database.

## 📌 Features
- ✅ Extract messy data from CSV files.
- ✅ Transform by fixing incorrect values, handling duplicates, and cleaning data.
- ✅ Load clean data into a PostgreSQL database.
- ✅ Data Quality Report generated for tracking fixes.
- ✅ Handles Missing Data, Fixes Incorrect Dates, Validates Emails, and Removes Duplicates.

## 📂 Folder Structure
- bash
- Copy
- Edit
- /ETL-Project

  │── advanced_etl_pipeline.py  # Main ETL script
  
  │── raw_messy_data.csv        # Sample raw data
  
  │── data_quality_report.csv   # Auto-generated quality report
  
  │── requirements.txt          # Dependencies
  
  │── README.md                 # Project documentation
  

## 🛠 Installation

1️⃣ Clone the Repository
- git clone https://github.com/yourusername/ETL-Project.git
- cd ETL-Project

2️⃣ Create & Activate Virtual Environment (Optional)
- python3 -m venv venv
- source venv/bin/activate  # On Mac/Linux
- venv\Scripts\activate     # On Windows
  
3️⃣ Install Dependencies
- pip install -r requirements.txt
  
## 📝 Configuration
- Update Database Credentials
- Modify the database URI inside advanced_etl_pipeline.py:
- db_uri = "postgresql://postgres:yourpassword@localhost:5433/yourdatabase"

## 🚀 Running the ETL Pipeline
python advanced_etl_pipeline.py

🔍 Example Output
Raw Data:
... (original messy data)
<img width="545" alt="image" src="https://github.com/user-attachments/assets/916285f9-2cf5-440e-92bc-6786d5a42ff2" />


Transformed Data:
... (cleaned data)
<img width="854" alt="image" src="https://github.com/user-attachments/assets/b4a7adbd-5a11-4a38-ac98-07113bd3befd" />

Cleaned data loaded successfully.
Data quality report saved as data_quality_report.csv
<img width="781" alt="image" src="https://github.com/user-attachments/assets/b0a94d24-a7c0-4c2f-8beb-48abde1c2a60" />


## 📊 Data Cleaning Rules
<img width="781" alt="image" src="https://github.com/user-attachments/assets/d1b7f3d2-8d5f-4289-af47-87e083b40ab1" />


## 🔗 Dependencies
- pandas
- sqlalchemy
- psycopg2
- datetime
- Install them using: pip install pandas sqlalchemy psycopg2

## 🎯 Future Enhancements
- 📌 Add support for different databases (MySQL, SQLite).
- 📌 Implement a streaming ETL pipeline using Apache Kafka.
- 📌 Deploy as a Dockerized microservice.

## 🤝 Contributing
Want to contribute? Fork the repository, create a branch, and submit a pull request! 🚀

## 📜 License
This project is licensed under the MIT License.

## 📫 Connect with Me
- [LinkedIn](https://www.linkedin.com/in/sanjeev-kumar-singh-sks-b7b612ba/)
- [Twitter](https://x.com/iamsks267)
- [Email](mailto:sanjeevksingh267@gmail.com)
