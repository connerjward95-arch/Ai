import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Navigation.css';

interface NavItem {
  path: string;
  label: string;
  icon: string;
}

const Navigation: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const location = useLocation();

  const navItems: NavItem[] = [
    { path: '/', label: 'Chat', icon: '💬' },
    { path: '/dashboard', label: 'Dashboard', icon: '📊' },
    { path: '/settings', label: 'Settings', icon: '⚙️' },
  ];

  const isActive = (path: string) => location.pathname === path;

  return (
    <>
      <nav className="navigation">
        <div className="nav-header">
          <div className="nav-logo">
            <div className="logo-icon">⚙️</div>
            <span className="logo-text">AI Learning</span>
          </div>
          <button className="nav-toggle" onClick={() => setIsOpen(!isOpen)}>
            {isOpen ? '✕' : '☰'}
          </button>
        </div>

        <div className={`nav-items ${isOpen ? 'open' : ''}`}>
          {navItems.map((item) => (
            <Link
              key={item.path}
              to={item.path}
              className={`nav-item ${isActive(item.path) ? 'active' : ''}`}
              onClick={() => setIsOpen(false)}
            >
              <span className="nav-icon">{item.icon}</span>
              <span className="nav-label">{item.label}</span>
            </Link>
          ))}
        </div>

        <div className="nav-footer">
          <div className="user-badge">
            <div className="user-avatar">👤</div>
            <div className="user-info">
              <p className="user-name">User</p>
              <p className="user-status">Online</p>
            </div>
          </div>
        </div>
      </nav>
    </>
  );
};

export default Navigation;
