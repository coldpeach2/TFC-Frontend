import { createContext, useState } from "react";

const AuthContext = createContext({})

export const AuthProvider = ({ children }) => {
    const [auth, setAuth] = useState({
        accessToken: null,
        authenticated:null
    })

const getAccessToken = () => {
    return auth.accessToken;
}
    return (
        <AuthContext.Provider value={{ auth, setAuth, getAccessToken }}>
            {children}
        </AuthContext.Provider>
    )
}
export default AuthContext