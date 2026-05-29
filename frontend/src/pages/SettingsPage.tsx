import React, { useState } from 'react';
import './SettingsPage.css';

interface Settings {
  modelType: string;
  learningRate: number;
  maxMemory: number;
  responseTimeout: number;
  autoSave: boolean;
  notifications: boolean;
  darkMode: boolean;
}

const SettingsPage: React.FC = () => {
  const [settings, setSettings] = useState<Settings>({
    modelType: 'advanced',
    learningRate: 0.8,
    maxMemory: 1000,
    responseTimeout: 5000,
    autoSave: true,
    notifications: true,
    darkMode: false,
  });

  const [isSaved, setIsSaved] = useState(false);

  const handleChange = (key: keyof Settings, value: any) => {
    setSettings((prev) => ({ ...prev, [key]: value }));
    setIsSaved(false);
  };

  const handleSave = () => {
    setIsSaved(true);
    setTimeout(() => setIsSaved(false), 3000);
  };

  const handleReset = () => {
    setSettings({
      modelType: 'advanced',
      learningRate: 0.8,
      maxMemory: 1000,
      responseTimeout: 5000,
      autoSave: true,
      notifications: true,
      darkMode: false,
    });
  };

  return (
    <div className="settings-page">
      <div className="settings-header">
        <h1>Settings</h1>
        <p className="settings-subtitle">Configure AI behavior and preferences</p>
      </div>

      <div className="settings-container">
        <div className="settings-card">
          <h2>AI Configuration</h2>
          
          <div className="setting-group">
            <label htmlFor="model-type">AI Model Type</label>
            <select
              id="model-type"
              value={settings.modelType}
              onChange={(e) => handleChange('modelType', e.target.value)}
              className="setting-select"
            >
              <option value="basic">Basic</option>
              <option value="standard">Standard</option>
              <option value="advanced">Advanced</option>
              <option value="expert">Expert</option>
            </select>
            <p className="setting-hint">Higher complexity = more accurate but slower</p>
          </div>

          <div className="setting-group">
            <label htmlFor="learning-rate">Learning Rate</label>
            <div className="range-container">
              <input
                id="learning-rate"
                type="range"
                min="0"
                max="1"
                step="0.1"
                value={settings.learningRate}
                onChange={(e) => handleChange('learningRate', parseFloat(e.target.value))}
                className="setting-range"
              />
              <span className="range-value">{settings.learningRate.toFixed(1)}</span>
            </div>
            <p className="setting-hint">How quickly the AI learns from interactions</p>
          </div>
        </div>

        <div className="settings-card">
          <h2>Preferences</h2>

          <div className="toggle-group">
            <div className="toggle-header">
              <label>Auto-Save Conversations</label>
              <input
                type="checkbox"
                checked={settings.autoSave}
                onChange={(e) => handleChange('autoSave', e.target.checked)}
                className="toggle-checkbox"
              />
            </div>
            <p className="setting-hint">Automatically save all conversations</p>
          </div>

          <div className="toggle-group">
            <div className="toggle-header">
              <label>Enable Notifications</label>
              <input
                type="checkbox"
                checked={settings.notifications}
                onChange={(e) => handleChange('notifications', e.target.checked)}
                className="toggle-checkbox"
              />
            </div>
            <p className="setting-hint">Receive notifications for AI responses</p>
          </div>
        </div>

        <div className="settings-card info-card">
          <h2>About AI Learning Machine</h2>
          <div className="about-content">
            <p><strong>Version:</strong> 1.0.0</p>
            <p><strong>Model:</strong> Advanced Neural Network</p>
            <p><strong>Backend:</strong> Python FastAPI</p>
            <p><strong>Frontend:</strong> React TypeScript</p>
            <div className="status-indicator">
              <span className="status-dot"></span>
              System running optimally
            </div>
          </div>
        </div>

        <div className="settings-actions">
          <button className="btn-reset" onClick={handleReset}>
            🔄 Reset to Defaults
          </button>
          <button className={`btn-save ${isSaved ? 'saved' : ''}`} onClick={handleSave}>
            💾 {isSaved ? 'Saved!' : 'Save Changes'}
          </button>
        </div>
      </div>
    </div>
  );
};

export default SettingsPage;
