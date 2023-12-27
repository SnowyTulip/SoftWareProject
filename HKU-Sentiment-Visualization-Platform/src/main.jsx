import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)

// import React, { useState } from 'react';
// import ReactDOM from 'react-dom/client';
// import {
//   BrowserRouter as Router,
//   Switch,
//   Route,
//   Redirect,
// } from "react-router-dom";
// import App from './App.jsx';
// import Login from './components/Login/login.jsx';  // the Login component you created
// import './index.css'

// const Main = () => {
//   const [isLoggedIn, setIsLoggedIn] = useState(false);
  
//   const handleLogin = (username, password) => {
//     // handle your login logic here
//     // if login is successful, call setIsLoggedIn(true)

//     // for demonstration purposes, we'll assume the login is always successful
//     setIsLoggedIn(true);  
//   };
  
//   return (
//     <Router>
//       <Switch>
//         <Route path="/login">
//           {isLoggedIn ? <Redirect to="/" /> : <Login onLogin={handleLogin} />}
//         </Route>
//         <Route path="/">
//           {isLoggedIn ? <App /> : <Redirect to="/login" />}
//         </Route>
//       </Switch>
//     </Router>
//   );
// };

// ReactDOM.createRoot(document.getElementById('root')).render(
//   <React.StrictMode>
//     <Main /> 
//   </React.StrictMode>,
// )
