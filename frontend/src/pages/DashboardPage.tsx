import React, { useState } from 'react';
import './DashboardPage.css';

const DashboardPage: React.FC = () => {
  const [stats] = useState({
    totalMessages: 234,
    learningAccuracy: 87.5,
    responseTime: 145,
    sessionDuration: 1240,
  });

  const chartData = [
    { time: '00:00', accuracy: 65 },
    { time: '04:00', accuracy: 72 },
    { time: '08:00', accuracy: 78 },
    { time: '12:00', accuracy: 82 },
    { time: '16:00', accuracy: 85 },
    { time: '20:00', accuracy: 87 },
  ];

  return (
    <div className="dashboard-page">
      <div className="dashboard-header">
        <h1>Analytics Dashboard</h1>
        <p className="dashboard-subtitle">Learning Progress & Performance Metrics</p>
      </div>

      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-label">Total Messages</div>
          <div className="stat-value">{stats.totalMessages}</div>
          <div className="stat-change">+12 today</div>
        </div>
        <div className="stat-card">
          <div className="stat-label">Learning Accuracy</div>
          <div className="stat-value">{stats.learningAccuracy}%</div>
          <div className="stat-change">+2.5% this week</div>
        </div>
        <div className="stat-card">
          <div className="stat-label">Avg Response Time</div>
          <div className="stat-value">{stats.responseTime}ms</div>
          <div className="stat-change">-20ms improvement</div>
        </div>
        <div className="stat-card">
          <div className="stat-label">Session Duration</div>
          <div className="stat-value">{(stats.sessionDuration / 60).toFixed(1)}m</div>
          <div className="stat-change">+15% engagement</div>
        </div>
      </div>

      <div className="charts-grid">
        <div className="chart-card">
          <h2>Learning Accuracy Over Time</h2>
          <div className="chart-placeholder">
            <div style={{ textAlign: 'center', padding: '40px', color: '#a0aec0' }}>
              📊 Chart visualization would appear here
            </div>
          </div>
        </div>
      </div>

      <div className="insights-card">
        <h2>Key Insights</h2>
        <ul className="insights-list">
          <li>✓ Learning accuracy has improved 22.5% over the past week</li>
          <li>✓ Response time optimization is ahead of schedule</li>
          <li>✓ User engagement has increased significantly</li>
          <li>✓ Pattern recognition accuracy: 91.2%</li>
          <li>✓ Recommended next focus: Advanced context understanding</li>
        </ul>
      </div>
    </div>
  );
};

export default DashboardPage;
