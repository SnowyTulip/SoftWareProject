import React, { useState } from 'react';

const Login = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onLogin(username, password);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>Username:</label>
      <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} required/>
      <label>Password:</label>
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required/>
      <input type="submit" value="Login" />
    </form>
    // 12301238 
  );
};

export default Login;