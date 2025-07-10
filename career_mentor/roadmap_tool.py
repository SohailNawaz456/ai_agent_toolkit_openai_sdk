from agents import function_tool
@function_tool
def get_career_roadmap(field: str) -> str:
    maps = {
        "software engineer": "Learn Python, DSA, Web Dev, GitHub, Projects.",
        "software developer": "Learn Python, DSA, Web Dev, GitHub, Projects.",
        "software development": "Learn Python, DSA, Web Dev, GitHub, Projects.",
        "developer": "Learn Python, DSA, Web Dev, GitHub, Projects.",
        "data science": "Master Python, Pandas, ML, and real-world datasets.",
        "data scientist": "Master Python, Pandas, ML, and real-world datasets.",
        "graphic designer": "Learn Figma, Photoshop, UI/UX, Portfolio.",
        "graphic design": "Learn Figma, Photoshop, UI/UX, Portfolio.",
        "ai": "Study Python, Deep Learning, Transformers, and AI tools.",
        "artificial intelligence": "Study Python, Deep Learning, Transformers, and AI tools."
    }
    return maps.get(field.strip().lower(), "No roadmap found for that field.")