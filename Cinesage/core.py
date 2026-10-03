
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Create model
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=1
)

# Create prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert movie information extraction assistant.

Analyze the movie summary provided below and extract all meaningful and useful information about the movie.

Movie Summary:
{paragraph}

Organize the extracted information using clear headings and bullet points.

Include the following sections whenever the information is available:

### Basic Information
- Movie Title
- Release Year / Release Date
- Genre
- Language
- Country
- Runtime
- Movie Type

### Cast
- Main Actors and the characters they play
- Supporting Actors and the characters they play

### Crew
- Director
- Writers / Screenwriters
- Producers
- Cinematographer
- Editor
- Music Composer
- Production Companies

### Story
- Main plot
- Main protagonist
- Main antagonist
- Major characters
- Central conflict
- Important events
- Setting and time period

### Themes & Style
- Main themes
- Mood
- Tone
- Important topics explored
- Story style

### Additional Information
- Awards
- Nominations
- Budget
- Box office
- Based on / Adapted from
- Important keywords
- Content warnings
- Similar movies or influences mentioned

### Overall Description
Give a concise but informative description of what the movie is about and what makes its story distinctive.

Important rules:

1. Extract only information supported by the provided text.
2. Do not invent or guess missing information.
3. If something is not mentioned, simply omit that section or write "Not mentioned."
4. Preserve actor, director, character, and movie names exactly as given.
5. Extract all important people mentioned, not just the main actors.
6. Clearly distinguish between actors and the characters they portray.
7. Identify the central conflict and major themes from the summary.
8. Keep the information organized and easy to read.
9. Do not return JSON, XML, tables, or code.
10. Do not add unnecessary commentary about the extraction process.
"""
    ),
    (
        "human",
        """
Extract information from this paragraph:

{paragraph}
"""
    )
])

# Take input from user
para = input("Give your paragraph: ")

# Fill the prompt
final_prompt = prompt.invoke({
    "paragraph": para
})

# Send prompt to model
response = model.invoke(final_prompt)

# Print response
print(response.content)

