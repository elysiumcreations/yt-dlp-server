import os
import subprocess
import uuid
from fastapi import FastAPI, Query
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/download")
def download(url: str = Query(...)):
    out_name = f"{uuid.uuid4()}.m4a"

    cmd = [
        "yt-dlp",
        url,
        "-x",
        "--audio-format", "m4a",
        "-o", out_name
    ]

    subprocess.run(cmd, check=True)

    return FileResponse(out_name, media_type="audio/m4a", filename=out_name)
