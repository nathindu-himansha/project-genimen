import React from 'react';
import './nav.css';
import about from '../../assests/AboutLight.png';
import search from '../../assests/Search.png';
import home from '../../assests/HomeWhite.png';
import hamIcon from '../../assests/HamburgerLight.png';
import cross from '../../assests/CroseLight.png';
import logo from '../../assests/Geniman.png';
import downArrow from '../../assests/DropDownArrow.png';
import rightArraw from '../../assests/DropDownRightArrow.png';

const NavBar = (props) => {
  const routes = [
    {
      title: 'Home',
      icon: home,
      subMenu: [],
      active: false,
    },
    {
      title: 'Analytics',
      icon: search,
      subMenu: [
        { title: 'Feature Sentiments', active: false },
        { title: 'Product Feature Sentiments', active: false },
        { title: 'TRENDZ', active: false },
      ],
      active: false,
    },
    {
      title: 'About',
      icon: about,
      subMenu: [],
      active: false,
    },
  ];
  return (
    <div>
      <nav className="navbar">
        <div className="nav-logo">
          <img src={logo} />
          <span className="logo-name">genimen</span>
        </div>
        <div className="hamburger">
          <div className="hamburger-icon">
            <img src={hamIcon} className="menu-icon" />
            <img src={cross} className="close-icon" />
          </div>
          <span className="link-text hamburger-lbl">Menu</span>
        </div>
        <ul className="navbar-nav">
          {routes.map((route, i) => (
            <li key={'route' + i} className="nav-item parent-link">
              <a href="#" className={`nav-link ${route.active ? 'nav-link-active' : ''}`}>
                <div className="nav-icon">
                  <img src={route.icon} />
                </div>
                <span className="link-text">{route.title}</span>
              </a>
              {route.subMenu.length ? (
                <div className="nav-link-icon">
                  <img src={downArrow} className="dropdown-arrow" />
                </div>
              ) : (
                ''
              )}
              <ul className={route.subMenu.length ? 'navbar-sub-nav' : '-display-none'}>
                {route.subMenu.map((menu, i) => (
                  <a key={'submenu' + i} href="#" className="sub-nav-link">
                    <li
                      key={'submenu' + i}
                      className={`nav-sub-item ${menu.active ? 'sub-nav-link-active' : ''}`}
                    >
                      <span className="sub-link-text">{menu.title}</span>
                      <div className="sub-nav-link-icon">
                        <img src={rightArraw} className="dropright-arrow" />
                      </div>
                    </li>
                  </a>
                ))}
              </ul>
            </li>
          ))}
        </ul>
      </nav>
    </div>
  );
};

export default NavBar;
