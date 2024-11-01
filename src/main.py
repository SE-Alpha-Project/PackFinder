# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List, Dict

# app = FastAPI()

# # Sample data
# items = [
#     {'size': 1, 'color': 2, 'price': 5},
#     {'size': 2, 'color': 1, 'price': 3},
#     # Add more items as needed
# ]

# class Weights(BaseModel):
#     size: int
#     color: int
#     price: int

# @app.post("/filter", response_model=List[Dict])
# def filter_items(weights: Weights):
#     def calculate_score(item, weights):
#         score = 0
#         score += item.get('size', 0) * weights.size
#         score += item.get('color', 0) * weights.color
#         score += item.get('price', 0) * weights.price
#         return score

#     scored_items = [(item, calculate_score(item, weights)) for item in items]
#     sorted_items = sorted(scored_items, key=lambda x: x[1], reverse=True)
#     return [item for item, score in sorted_items]

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
