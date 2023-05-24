import { createContext, useContext } from "react";
import axios from "axios";
const AuthContext = createContext();
export default AuthContext;


export const AuthContextProvider = ({ children }) => {
  const loginUser = (e) => {
    e.preventDefault();
    console.log(e.target.email.value)
    console.log(e.target.password.value)
    axios({
      url: 'http://localhost:8000/accounts/token/login',
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      data: {
        "email": e.target.email.value,
        "password": e.target.password.value,
      }
    }).then(res => {
      console.log(res.data)
    }).catch(err => {
      console.log(err)
    })

  }
  const authPara = {
    loginUser: loginUser,
  }
  return (
    <AuthContext.Provider value={authPara}>
      { children }
    </AuthContext.Provider>
  )
}

const useAuth = () => useContext(AuthContext);

export { useAuth }
