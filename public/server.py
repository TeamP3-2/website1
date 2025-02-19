import pickle
import pandas as pd
import numpy as np
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

# import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# # Load dataset
# # df = pd.read_csv("Coursera.csv")  # Make sure the file exists
# df = pd.read_csv("coursera_processed_data.csv")  


# # Load similarity matrix from .pkl file
# with open("similarity_matrix.pkl", "rb") as f:
#     similarity_matrix = pickle.load(f)  # Load similarity matrix from pickle file

# print(similarity_matrix)

# # Function to normalize ratings
# def normalize_rating(rating):
#     """Normalize rating to a 0-1 scale."""
#     try:
#         return float(rating) / 5.0  # Assuming max rating is 5
#     except ValueError:
#         return 0  # Default if rating is missing or invalid

# # Recommendation function
# def get_recommendations(course_name, data, similarity_matrix, top_n=4, rating_weight=0.05):
#     """Get top N course recommendations based on similarity to the given course name."""
#     course_row = data[data['Course Name'] == course_name]

#     if course_row.empty:
#         return [{"error": f"Course '{course_name}' not found"}]  # Handle missing course

#     course_idx = course_row.index[0]
#     similarity_scores = list(enumerate(similarity_matrix[course_idx]))

#     recommendations = []
#     for idx, similarity_score in sorted(similarity_scores, key=lambda x: x[1], reverse=True)[:top_n]:
#         course_data = data.iloc[idx]
#         normalized_rating = normalize_rating(course_data.get('Course Rating', '0'))

#         recommendations.append({
#             "course_name": course_data['Course Name'],
#             "skills": course_data.get('Skills', 'Unknown'),
#             "similarity": similarity_score,
#             "final_score": similarity_score * (1 - rating_weight) + normalized_rating * rating_weight
#         })

#     return sorted(recommendations, key=lambda x: x['final_score'], reverse=True)

# # FastAPI Routes
# @app.get("/", response_class=HTMLResponse)
# async def get_form(request: Request):
#     """Serve the HTML form."""
#     return templates.TemplateResponse("index.html", {"request": request})

# # @app.post("/recommendations", response_class=HTMLResponse)
# # async def get_course_recommendations(request: Request, course_name: str = Form(...)):
# #     """Handle form submission and return recommended courses."""
# #     recommended_courses = get_recommendations(course_name, df, similarity_matrix)

# #     return templates.TemplateResponse("index.html", {
# #         "request": request,
# #         "course_name": course_name,
# #         "recommendations": recommended_courses
# #     })



# # @app.post("/recommendations")
# @app.post("/recommendations", response_class=HTMLResponse)
# async def get_course_recommendations(course_name: str = Form(...)):
#     recommended_courses = get_recommendations(course_name, df, similarity_matrix)
#     return JSONResponse(content={"recommendations": recommended_courses})




# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)














##################################################33
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pickle
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load dataset
df = pd.read_csv("coursera_processed_data.csv")

# Load similarity matrix
with open("similarity_matrix.pkl", "rb") as f:
    similarity_matrix = pickle.load(f)

# def get_recommendations(course_id, data, similarity_matrix, top_n=4, rating_weight=0.05):
#     try:
#         course_id = int(course_id)  # Ensure it's an integer
#     except ValueError:
#         return [{"error": "Invalid course ID"}]  # Handle invalid input

#     if course_id not in data["ID"].values:
#         return [{"error": f"Course ID '{course_id}' not found"}]  # Handle missing course

#     course_idx = data.index[data["ID"] == course_id][0]  # Find index
#     similarity_scores = list(enumerate(similarity_matrix[course_idx]))

#     recommendations = []
#     for idx, similarity_score in sorted(similarity_scores, key=lambda x: x[1], reverse=True)[:top_n]:
#         course_data = data.iloc[idx]

#         recommendations.append({
#             "course_id": int(course_data['ID']),
#             "course_name": course_data['Course Name'],
#             "skills": course_data.get('Skills', 'Unknown'),
#             "similarity": similarity_score
#         })

#     return sorted(recommendations, key=lambda x: x['similarity'], reverse=True)


# # # FastAPI Routes
# @app.get("/", response_class=HTMLResponse)
# async def get_form(request: Request):
#     """Serve the HTML form."""
#     return templates.TemplateResponse("index.html", {"request": request})



# @app.get("/recommendations/{course_id}")
# async def get_course_recommendations(course_id: int):
#     recommended_courses = get_recommendations(course_id, df, similarity_matrix)
#     return JSONResponse(content={"recommendations": recommended_courses})

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)





######################################33 


from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
import pickle
import pandas as pd

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins (or specify specific origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow only localhost:3000 (your frontend)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Load dataset and similarity matrix
df = pd.read_csv("coursera_processed_data.csv")
with open("similarity_matrix.pkl", "rb") as f:
    similarity_matrix = pickle.load(f)

templates = Jinja2Templates(directory="templates")  # Directory where your HTML templates are located

# Function to get recommendations based on course ID
def get_recommendations(course_id, data, similarity_matrix, top_n=4, rating_weight=0.05):
    try:
        course_id = int(course_id)  # Ensure it's an integer
    except ValueError:
        return [{"error": "Invalid course ID"}]  # Handle invalid input

    if course_id not in data["ID"].values:
        return [{"error": f"Course ID '{course_id}' not found"}]  # Handle missing course

    course_idx = data.index[data["ID"] == course_id][0]  # Find index
    similarity_scores = list(enumerate(similarity_matrix[course_idx]))

    recommendations = []
    for idx, similarity_score in sorted(similarity_scores, key=lambda x: x[1], reverse=True)[:top_n]:
        course_data = data.iloc[idx]

        recommendations.append({
            # "course_id": int(course_data['ID']),
            # "course_name": course_data['Course Name'],
            # "skills": course_data.get('Skills', 'Unknown'),
            # "similarity": similarity_score


            "course_name": course_data['Course Name'],
            "course_id": int(course_data['ID']), 
            "university": course_data['University'],
            "difficulty_level": course_data['Difficulty Level'],
            "course_rating": course_data['Course Rating'],
            "course_url": course_data['Course URL'] ,
            "similarity": similarity_score
                    })

    return sorted(recommendations, key=lambda x: x['similarity'], reverse=True)


# def get_recommendations_from_list_of_courses(courses_id, data, top_n=5):
#     recommended = {}
#     for course_id in courses_id:
#         courses = get_recommendations(course_id=course_id,similarity_matrix= similarity_matrix, data= df)
#         for course in courses:
#             if(course['course_id'] in recommended):
#                 recommended[course['course_id']] += course['similarity']
#             else:
#                 recommended[course['course_id']] = course['similarity']
#     recommended = sorted(recommended.items(), key=lambda item: item[1], reverse=True)
#     return [id[0] for id in recommended[0: top_n]]


def get_recommendations_from_list_of_courses(courses_id, data, similarity_matrix, top_n=5):
    recommended = {}

    for course_id in courses_id:
        courses = get_recommendations(course_id=course_id, similarity_matrix=similarity_matrix, data=data)

        for course in courses:
            course_id = course['course_id']
            similarity_score = course['similarity']

            if course_id in recommended:
                recommended[course_id]['similarity'] += similarity_score
            else:
                course_data = data[data['ID'] == course_id].iloc[0]

                recommended[course_id] = {
                    "course_id": int(course_data['ID']),
                    "course_name": course_data['Course Name'],
                    "university": course_data['University'],
                    "difficulty_level": course_data['Difficulty Level'],
                    "course_rating": course_data['Course Rating'],
                    "course_url": course_data['Course URL'],
                    "similarity": similarity_score
                }

    return sorted(recommended.values(), key=lambda x: x['similarity'], reverse=True)[:top_n]



# FastAPI Routes
@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    """Serve the HTML form."""
    return templates.TemplateResponse("index.html", {"request": request})

# Get course recommendations based on course ID from path parameter
@app.get("/recommendations")
async def get_course_recommendations(course_id: int):
    print("hellp")
    print("*////*******************")
    print(get_recommendations_from_list_of_courses([17], data= df, similarity_matrix=similarity_matrix))
    print("*////*******************")

    recommended_courses = get_recommendations(course_id, df, similarity_matrix)
    # console.log(recommended_courses)
    return JSONResponse(content={"recommendations": recommended_courses})
    # return JSONResponse(content={recommended_courses})



# @app.get("/myrec")
# async def get_all_recommendations(courses_id: list):
    
#     # recommended_courses = get_recommendations(course_id, df, similarity_matrix)
#     recommended_courses = get_recommendations_from_list_of_courses(courses_id, df, similarity_matrix, top_n=5)
#     # console.log(recommended_courses)
#     return JSONResponse(content={"recommendations": recommended_courses})
#     # return JSONResponse(content={recommended_courses})


from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

 
@app.post("/myrec")
async def get_all_recommendations(request: Request):
    body = await request.json()
    courses_id = body.get("course_ids", [])
    
    # Assuming you have the get_recommendations_from_list_of_courses function defined
    recommended_courses = get_recommendations_from_list_of_courses(
        courses_id, df, similarity_matrix, top_n=5
    )
    
    if not recommended_courses:
        return JSONResponse(content={"recommendations": []})
    
    return JSONResponse(content={"recommendations": recommended_courses})
 
 



if __name__ == "__main__":
    
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
    
