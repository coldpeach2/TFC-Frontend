import { createContext, useContext } from "react";
import AuthContext from "./AuthProvider";
import axios from "axios";

const AxiosContext = createContext({})

export const AxiosProvider = ({ children }) => {
    const authContext = useContext(AuthContext)

    const authAxios = axios.create({
    baseURL: 'http://localhost:3000/accounts/profile',
    })

    const publicAxios = axios.create({
        baseURL: 'http://localhost:3000/accounts',
      })

      authAxios.interceptors.request.use(
        config => {
          if (!config.headers.Authorization) {
            config.headers.Authorization = `Bearer ${authContext.getAccessToken()}`
          }
          return config;
        },
        error => {
          return Promise.reject(error);
        }
      )
    return (
        <AxiosContext.Provider value={{ authAxios, publicAxios }}>
            {children}
        </AxiosContext.Provider>
    )
}
export default AxiosContext