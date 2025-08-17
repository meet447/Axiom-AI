# Axiom-AI

A modern AI-powered chat application built with FastAPI backend and Next.js frontend, featuring multiple AI models and advanced search capabilities.

## 🚀 Features

- **Multiple AI Models**: Choose from different model tiers (Fast, Powerful, Hyper)
- **Pro Search**: Enhanced search capabilities with expert-level responses
- **Real-time Streaming**: Server-sent events for real-time chat responses
- **Modern UI**: Built with Next.js, Tailwind CSS, and Radix UI components
- **Type-safe**: Full TypeScript support with OpenAPI code generation

## 🛠 Tech Stack

### Backend
- **FastAPI** - Fast, modern Python web framework
- **Google Gemini AI** - Multiple AI model variants
- **Pydantic** - Data validation and serialization
- **Uvicorn** - ASGI server
- **Beautiful Soup** - Web scraping capabilities

### Frontend
- **Next.js 14** - React framework with App Router
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Radix UI** - Accessible UI components
- **Framer Motion** - Animation library
- **React Query** - Data fetching and caching
- **Zustand** - State management

## 📁 Project Structure

```
axiom/
├── backend/                 # FastAPI backend
│   ├── chat/               # Chat functionality
│   ├── models/             # Data models
│   ├── services/           # Business logic
│   ├── system/             # System utilities
│   ├── main.py             # FastAPI application entry point
│   ├── config.py           # Configuration settings
│   └── requirements.txt    # Python dependencies
├── frontend/               # Next.js frontend
│   ├── src/                # Source code
│   ├── public/             # Static assets
│   ├── generated/          # Auto-generated API client
│   └── package.json        # Node.js dependencies
└── README.md               # This file
```

## 🚦 Getting Started

### Prerequisites

- Python 3.8+
- Node.js 18+
- pnpm (recommended) or npm

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd axiom/backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables (create a `.env` file):
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd axiom/frontend
   ```

2. Install dependencies:
   ```bash
   pnpm install
   # or
   npm install
   ```

3. Generate API client (make sure backend is running):
   ```bash
   pnpm generate
   # or
   npm run generate
   ```

4. Start the development server:
   ```bash
   pnpm dev
   # or
   npm run dev
   ```

The frontend will be available at `http://localhost:3000`

## 📖 API Reference

### Chat Endpoint

**POST** `/chat`

Send a chat message and receive a streaming response.

```json
{
  "thread_id": 1,
  "query": "Your question here",
  "history": [],
  "model": "fast|powerful|hyper",
  "pro_search": false
}
```

**Models Available:**
- `fast` - Gemini 2.5 Flash (Quick responses)
- `powerful` - Gemini 2.5 Pro (Enhanced reasoning)
- `hyper` - Gemini 2.5 Flash Lite (Ultra-fast responses)

## 🔧 Development

### Backend Development

- The backend uses FastAPI with automatic OpenAPI documentation
- Visit `http://localhost:8000/docs` for interactive API documentation
- Code is organized into modules for chat, models, and services

### Frontend Development

- Built with Next.js App Router for optimal performance
- Uses TypeScript for type safety
- Styled with Tailwind CSS and Radix UI components
- State managed with Zustand
- API client auto-generated from OpenAPI schema

### Code Generation

The frontend automatically generates TypeScript API clients from the backend's OpenAPI schema:

```bash
cd frontend
pnpm generate
```

## 🌟 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 🤝 Support

If you have any questions or need help, please open an issue on GitHub.