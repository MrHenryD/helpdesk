import time
import logging

from fastapi import Request, JSONResponse


async def log_request(
    request: Request,
    call_next,
    logger: logging.Logger
) -> Request:
    start_time = time.perf_counter()
    log = {
        "source": request.client.host,
        "user_agent": (
            request.headers["user-agent"] if "user-agent" in request.headers else ""
        ),
        "referer": request.headers["referer"] if "referer" in request.headers else "",       
        "method": request.method,
        "url": request.url,
    }
    try:
        response = await call_next(request)
    except Exception as e:
        log.update(
            {
                "status_code": 500,
                "process_time": round((time.perf_counter() - start_time) * 1000, 3),
                "message": str(e),
            }
        )
        logger.error(log)
        return JSONResponse(
            status_code=500,
            content={
                "message": "Internal Server Error",
                "error": str(e)
            },
        )
    log.update(
        {
            "status_code": response.status_code,
            "process_time": round((time.perf_counter() - start_time) * 1000, 3),
        }
    )
    logger.info(log)
    return response
