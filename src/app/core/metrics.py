from typing import Callable

from fastapi import FastAPI
from prometheus_client import Counter
from prometheus_fastapi_instrumentator import Instrumentator, metrics


def http_4xx_errors() -> Callable[[metrics.Info], None]:
    METRIC = Counter(
        "http_4xx_errors_total",  # Name of the metric
        "Number of 400 errors.",  # Description of the metric
        labelnames=("section",),  # Labels used for dimensionality
    )

    def instrumentation(info: metrics.Info) -> None:
        status_code = info.response.status_code
        if status_code >= 400 and status_code < 500:
            METRIC.labels(
                section="a",
            ).inc()

    return instrumentation


def get_instrumentator(app: FastAPI) -> FastAPI:
    """Setup Instrumentator

    Metrics Types:
        Counter: increasing counter that can only go up.
            Ex. Number of requests received
        Gauge: a value that can go up and down.
            Ex. Number of requests currently being processed, memory usage
        Histogram: samples observations and counts them in configurable buckets.
            Ex. Request duration, response size
        Summary: similar to histogram, but calculates quantiles on the fly.
            Ex. 95th percentile of request duration over the last 5 minutes

    Default metrics are:
    - http_requests_total
    - http_request_size_bytes
    - http_response_size_bytes
    - http_request_duration_seconds
    - http_request_duration_highr_seconds

    """
    instrumentator = Instrumentator()
    # If no metrics are added, the default metrics will be used
    # instrumentator.add(
    #     http_4xx_errors()
    # )
    instrumentator.instrument(
        app,
        metric_namespace="helpdesk_dev",  # must not contain any special characters besides _
        metric_subsystem="api",
    ).expose(app)

    return app
