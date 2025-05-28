# API Reference

## Overview
The backend API is built with FastAPI and provides endpoints for AI interactions and conversation management.

## Base URL
- Development: `http://localhost:8000`
- Production: Configured via environment variables

## Authentication
Currently, the API uses a simple user ID for identification, passed via the `X-User-ID` header.

## Endpoints

### Chat

#### POST /chat
Send a message to the AI assistant.

**Request:**
```json
{
    "message": "string",
    "user_id": "string"
}
```

**Response:**
```json
{
    "response": "string",
    "conversation_id": "string"
}
```

### Conversations

#### GET /conversations
Get all conversations for a user.

**Query Parameters:**
- `user_id` (required): The user's ID

**Response:**
```json
[
    {
        "id": "string",
        "user_id": "string",
        "created_at": "datetime",
        "messages": [
            {
                "id": "string",
                "content": "string",
                "role": "string",
                "created_at": "datetime"
            }
        ]
    }
]
```

#### GET /conversations/{conversation_id}
Get a specific conversation.

**Path Parameters:**
- `conversation_id` (required): The conversation's ID

**Response:**
```json
{
    "id": "string",
    "user_id": "string",
    "created_at": "datetime",
    "messages": [
        {
            "id": "string",
            "content": "string",
            "role": "string",
            "created_at": "datetime"
        }
    ]
}
```

#### DELETE /conversations/{conversation_id}
Delete a conversation.

**Path Parameters:**
- `conversation_id` (required): The conversation's ID

**Response:**
```json
{
    "message": "Conversation deleted successfully"
}
```

## Error Responses

### 400 Bad Request
```json
{
    "detail": "Error message"
}
```

### 404 Not Found
```json
{
    "detail": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
    "detail": "Internal server error"
}
```

## Rate Limiting
The API implements rate limiting to prevent abuse. Current limits:
- 100 requests per minute per user
- 1000 requests per hour per user

## WebSocket Support
The API also supports WebSocket connections for real-time communication:

### WebSocket Endpoint
`ws://localhost:8000/ws`

**Connection Parameters:**
- `user_id`: Required query parameter

**Message Format:**
```json
{
    "type": "message",
    "content": "string"
}
```

**Response Format:**
```json
{
    "type": "response",
    "content": "string"
}
``` 