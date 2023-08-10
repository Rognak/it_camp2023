import uvicorn
from fastapi import FastAPI

import ipr.routes as rts

app = FastAPI()

app.include_router(rts.main_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
