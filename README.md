<<<<<<< HEAD
# YouTube Trending Data Pipeline

An End-to-End data pipeline that extracts, transforms, and visualizes daily trending YouTube videos.

## Features
- Extract trending data using YouTube Data API
- Transform & clean with Python (Pandas)
- Store structured data in SQLite
- Serve API with FastAPI backend
- Visualize results on React.js dashboard

## Tech Stack
- Python, FastAPI, SQLite
- React.js, Node.js
- Pandas, Logging
- YouTube Data API v3

## Folder Structure
=======
# Data-Pipeline-ETL-Project
End-to-End data engineering solution with API integration, Data transformation, SQL storage, API serving and Dashboard visualization and also demonstrated real-world ETL and analytics pipeline with scope for automation and scaling and Improved understanding of API-based data ingestion, backend integration, and full-stack visualization.


///////////////////c7b99b9ef6ff24349b72a002091258ba395aaced (api key)





Data Pipeline ETL Project
Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) data pipeline built by Darshan P at MBRDI as part of a Data Engineering initiative.
The system automates the extraction of trending YouTube video data, transforms and cleans it, loads it into a relational database, and visualizes the results through a modern frontend dashboard.

Objective

To design and deploy a fully functional data pipeline that automates data collection, transformation, storage, and visualization — replicating real-world analytics workflows in an enterprise environment.

Key Components
Layer	Technology	Purpose
Extraction	YouTube Data API	Fetch trending videos automatically
Transformation	Python (pandas)	Clean, normalize, and structure data
Storage	SQLite	Lightweight relational database for processed data
Backend	FastAPI	Expose RESTful APIs for frontend data consumption
Frontend	React.js	Interactive dashboard displaying trending video insights
Version Control	Git & GitHub	Code collaboration and version management
Automation	Python Scheduler / CRON	Automate pipeline runs (optional extension)

ETL Workflow

Extract
Pulls daily trending YouTube video data via the YouTube Data API.
Configurable by region or category.

Transform
Cleans and formats data using Python (removes nulls, extracts key metadata).
Ensures schema consistency and type validation.

Load
Loads transformed data into trending_videos.db (SQLite database).
Supports history tracking and incremental updates.

Visualize
React.js frontend fetches processed data via FastAPI backend.
Displays titles, channels, views, and engagement metrics dynamically.

Tools & Technologies
Category	Tools Used
Languages	Python, JavaScript (ES6)
Backend	FastAPI
Frontend	React.js, Axios
Database	SQLite
Data Processing	pandas
Version Control	Git, GitHub
IDE	VS Code
Environment	Node.js, Python 3.11
OS	Windows 10


How It Works
Backend (FastAPI)
Runs a REST API server at http://localhost:8000
Endpoint /api/videos returns trending video data from SQLite.
Can be extended to handle multiple regions or time-based trends.

Frontend (React.js)
Runs a dashboard on http://localhost:3000
Uses Axios to fetch and display data dynamically.
Provides a clear, tabular visualization of trending metrics.

Key Features Implemented
Step	Task	Description	You Get
1	Add Logging	Print when extract, transform & load starts/ends	Cleaner debugging and visibility
2	Run History	Track daily runs instead of overwriting	New DB schema + better traceability
3	Error Handling	Manage API rate limits, invalid responses	No crashes, better feedback
4	Export to CSV	Create a CSV backup per run	Optional for data sharing
5	Manual Run Support	Run pipeline anytime from terminal	Flexibility and control

Results

Successfully automated the ETL workflow.
Integrated backend API with a live React dashboard.
Displayed real-time YouTube trending analytics.
Prepared for scheduling and production deployment.



Future Enhancements
Multi-region data fetch (US, IN, GB)
Automated daily runs using Task Scheduler or CRON
Integration with AWS S3 or Azure Data Lake for scalable storage
Deployment on Docker for containerization


Author

Darshan P
Data Engineering Enthusiast | MBRDI
shettydarshu.29@gmail.com
GitHub: letscrackthis
