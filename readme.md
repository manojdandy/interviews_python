#conda create -p venv python==3.12
# uvicorn ui.main_async:app --reload
#swagger http://localhost:8000/docs
pip install fastapi uvicorn
uvicorn main:app --reload
#uvicorn main:app --reload --host 0.0.0.0 --port 5050

http://127.0.0.1:8000/items/42?q=test

#for embedding pull ollama pull llama3
#do not pull llama4 as it is too big  ~ 65GB
#ollama run aravhawk/llama4
