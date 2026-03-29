class MonitoringService:
    def __init__(self):
        # Initialize necessary attributes
        self.metrics = {}

    def record_metric(self, metric_name, value):
        """Records a metric value for a given metric name."""
        if metric_name not in self.metrics:
            self.metrics[metric_name] = []
        self.metrics[metric_name].append(value)

    def get_metric(self, metric_name):
        """Returns the recorded metrics for a given metric name."""
        return self.metrics.get(metric_name, [])

    def report(self):
        """Logs current metrics for observability."""
        for metric, values in self.metrics.items():
            print(f'{metric}: {values}')