# ALX Travel App 0x01

This project extends the functionality of `alx_travel_app_0x00` by adding robust API endpoints for managing travel listings and bookings, along with integrated Swagger documentation for the API.

## 📌 Project Goals

- Develop complete CRUD APIs for Listings and Bookings.
- Maintain clean, RESTful URL patterns.
- Auto-generate API docs using Swagger via `drf-yasg`.

## 🚀 Key Features

### ✅ REST API Endpoints
- `ListingViewSet`: Supports all standard CRUD operations for listings.
- `BookingViewSet`: Supports all standard CRUD operations for bookings.
- All routes are organized under `/api/` using Django REST Framework's router.

### 🔁 CRUD Functionality
- Add new listings or bookings  
- Retrieve one or multiple entries  
- Modify existing records  
- Remove listings or bookings  

### 📄 Interactive API Docs
- Available at `/swagger/`
- Built using `drf-yasg` for real-time, user-friendly API testing

## 🛠️ Getting Started

1. Clone or duplicate the base project:
   ```bash
   cp -r alx_travel_app_0x00 alx_travel_app_0x01
