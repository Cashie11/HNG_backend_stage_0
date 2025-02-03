# **HNG12 Public API**  

## **Overview**  
The **HNG12 Public API** is a simple RESTful API that returns essential information, including:  
- The registered email address.  
- The current date and time in **ISO 8601 format (UTC)**.  
- The **GitHub repository URL** of this project.  

This API is built using **FastAPI** and follows best practices for performance, security, and deployment.  

---

## **API Endpoint**  

### **Base URL:**  
```
https://your-api-url.com/
```

### **Request Method:**  
```http
GET /
```

### **Response Format (200 OK)**  
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

| Field            | Type   | Description                                        |
|-----------------|--------|----------------------------------------------------|
| `email`         | string | The registered email address.                      |
| `current_datetime` | string | The current date and time in ISO 8601 format (UTC). |
| `github_url`    | string | The GitHub repository URL of this project.        |

---

## **Getting Started**  

### **Prerequisites**  
Ensure you have the following installed on your system:  
- **Python 3.8+**  
- **Git**  

### **Installation & Running Locally**  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Cashie11/HNG_backend_stage_0.git
   cd your-repo
   ```

2. **Create a virtual environment**  
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**  
   - **Windows:**  
     ```bash
     env\Scripts\activate
     ```
   - **Mac/Linux:**  
     ```bash
     source env/bin/activate
     ```

4. **Install dependencies**  
   ```bash
   pip install fastapi uvicorn
   ```

5. **Run the API locally**  
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the API in your browser or via cURL/Postman**  
   - Open: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
   - API Docs (Swagger UI): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

---

## **Deployment**  
To deploy this API, you can use **Render, Railway, or Vercel**.  

### **Deployment on Render (Recommended)**  
1. Create a **free account** at [Render](https://render.com/).  
2. Click **New Web Service** and connect your GitHub repo.  
3. Set the **Build Command**:  
   ```bash
   pip install -r requirements.txt
   ```
4. Set the **Start Command**:  
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 10000
   ```
5. Click **Deploy** and get your **API URL**.  

---

## **CORS Handling**  
This API includes **Cross-Origin Resource Sharing (CORS)** support to allow external clients to access the API.  
By default, all origins are allowed (`*`). Update `main.py` to restrict access if needed.  

---

## **Version Control & Contribution**  
### **GitHub Repository:**  
🔗 [https://github.com/Cashie11/HNG_backend_stage_0.git))  

### **Contributing**  
We welcome contributions! To contribute:  
1. Fork the repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit:  
   ```bash
   git commit -m "Added new feature"
   ```
4. Push changes:  
   ```bash
   git push origin feature-branch
   ```
5. Open a **Pull Request** on GitHub.  

---

## **License**  
This project is licensed under the **MIT License**. See the `LICENSE` file for details.  

---

## **Contact**  
For any questions or support, feel free to reach out via email:  
📧 frankizuchukwu094@gmail.com
