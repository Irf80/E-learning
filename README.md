﻿# I-Learning

**I-Learning** is a comprehensive Learning Management System (LMS) designed to offer users a structured and engaging way to learn various Computer Science (CS) topics. This web-based platform allows users to register, purchase batches, and access a range of educational materials including lectures, notes, assignments, and more. Built using Django, Bootstrap, and other web technologies, I-Learning provides a robust and user-friendly interface for both students and instructors.

## Features

- **User Registration and Batch Purchase:** Users can register on the platform and buy access to CS-based learning batches.
- **Lectures:** Access video lectures for in-depth learning on various topics.
- **Notes:** Downloadable notes for each lecture to assist in study and revision.
- **Assignments:** Engage with assignments to test your knowledge and reinforce learning.
- **My Batches:** View and manage the batches you are enrolled in.
- **Class Timings:** Stay updated with the schedule of upcoming classes.
- **Software Resources:** Download and use the necessary software tools required for the courses.
- **Access to Other Batches:** Explore and join additional batches to expand your learning.
- **Doubts AI (Powered by OpenAI API):** An AI-based feature that helps users clarify doubts. Currently, this feature works only locally due to the demo version of the API, and requires a paid API key for deployment.
- **Dummy Payment Gateway:** A simulated payment gateway is integrated to handle batch purchases.

## Technologies Used

- **Backend:** Django
- **Frontend:** Bootstrap, HTML, JavaScript, CSS
- **AI Integration:** OpenAI API (for Doubts AI)
- **Database:** SQLite (or your choice of database)
- **Others:** Git, GitHub for version control

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**


2. **Run the Server:**
    
    python manage.py runserver 

3. **Access it :**
    
    last Access it at localhost://8000

4. **For Doubts ai:**
   Developed By Irfan Ali

    For using Doubts Ai , You can create your open ai api account from openai official website and put you api in alpha.py in apiKey variable and uncomment Doubts ai link from URls , and Views 
