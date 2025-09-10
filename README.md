## Backend API (Django REST Framework + JWT + PostgreSQL)

A simple Django REST Framework project with **Signup, Login, and Hello World (protected endpoint)** using JWT authentication.  
For Production Database used: **PostgreSQL**  
For Developer Database used: **SQLite3**

---

### Features
- User registration (signup) with extra fields
- User login with JWT authentication
- Protected endpoint (`/hello/`) accessible only with valid token
- PostgreSQL as database
- Custom User model (email-based authentication)

### End Point

| Endpoint       | Method | Auth Required | Description                                             | Request Body (JSON)                                                                                                                                                                 | Response (JSON)                                                                                                                                                                                 |
| -------------- | ------ | ------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/api/signup/` | POST   |  No          | নতুন user create করবে                                   | `{ "first_name": "Tushar", "last_name": "Ahmed", "phone_number": "01712345678", "email": "tushar@example.com", "password": "StrongPass123!", "retype_password": "StrongPass123!" }` | `{ "id": 1, "first_name": "Tushar", "last_name": "Ahmed", "phone_number": "01712345678", "email": "tushar@example.com" }`                                                                       |
| `/api/login/`  | POST   |  No          | JWT token generate করবে                                | `{ "email": "tushar@example.com", "password": "StrongPass123!" }`                                                                                                                   | `{ "refresh": "<refresh_token>", "access": "<access_token>", "user": { "id": 1, "first_name": "Tushar", "last_name": "Ahmed", "email": "tushar@example.com", "phone_number": "01712345678" } }` |
| `/api/hello/`  | GET    |  Yes (JWT)   | Protected route → শুধু logged-in user access করতে পারবে  | **Headers:** `Authorization: Bearer <access_token>`                                                                                                                                 | `{ "message": "Hello World, Tushar" }`                                                                                                                                                          |
