from fastapi import FastAPI
import subprocess

app = FastAPI()


@app.get("/sendquote")
def read_root():
    # run a2sv.py file
    subprocess.run(["python", "./a2sv.py"])
    
    return {"message": "Quote sent successfully"}
