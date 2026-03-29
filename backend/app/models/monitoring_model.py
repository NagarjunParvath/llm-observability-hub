from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class PromptMetrics(BaseModel):
    prompt_id: str
    model_name: str
    prompt_text: str
    response_text: str
    latency_ms: float
    cost_usd: float
    tokens_used: int
    timestamp: datetime
    quality_score: Optional[float] = None
    error_message: Optional[str] = None

class MonitoringAlert(BaseModel):
    alert_id: str
    alert_type: str  # "latency_high", "cost_spike", "quality_degradation", "error_rate"
    severity: str  # "low", "medium", "high", "critical"
    message: str
    threshold_value: float
    actual_value: float
    timestamp: datetime
    resolved: bool = False

class ModelPerformance(BaseModel):
    model_name: str
    total_requests: int
    average_latency_ms: float
    average_cost_usd: float
    error_rate: float
    average_quality_score: float
    last_updated: datetime

class DashboardMetrics(BaseModel):
    total_requests: int
    total_cost: float
    average_latency: float
    average_quality_score: float
    error_count: int
    active_alerts: int
    models_monitored: List[str]
    timestamp: datetime
