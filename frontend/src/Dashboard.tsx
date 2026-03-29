import React from 'react';

const Dashboard: React.FC = () => {
    const metrics = {
        totalRequests: 0,
        cost: 0,
        latency: 0,
        qualityScore: 0,
        errors: 0,
        alerts: 0,
        monitoredModels: []
    };
    
    return (
        <div>
            <h1>LLM Observability Dashboard</h1>
            <div>
                <h2>Metrics</h2>
                <p>Total Requests: {metrics.totalRequests}</p>
                <p>Cost: ${metrics.cost.toFixed(2)}</p>
                <p>Latency: {metrics.latency} ms</p>
                <p>Quality Score: {metrics.qualityScore}</p>
                <p>Errors: {metrics.errors}</p>
                <p>Alerts: {metrics.alerts}</p>
                <h3>Monitored Models</h3>
                <ul>
                    {metrics.monitoredModels.map((model, index) => (
                        <li key={index}>{model}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default Dashboard;