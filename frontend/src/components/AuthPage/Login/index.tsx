import React, { useContext } from 'react';
import { useAuth } from '../../../contexts/AuthContext'


const Login = () => {
  const { loginUser } = useAuth();

  return (
    <>
    <h1>Login</h1>
    <form method="POST" action="" onSubmit={loginUser}>
      <div className="form-row">
        <label className="required">Email address:</label>
        <input type="email" name="email" required id="id_email" />
      </div>

      <div className="form-row">
        <label  className="required">Password:</label>
        <input type="password" name="password" required id="id_password" />
      </div>

      <div className="submit-row">
        <input type="submit" value="Log in" />
      </div>
    </form>
    </>
  )
}
export default Login;
