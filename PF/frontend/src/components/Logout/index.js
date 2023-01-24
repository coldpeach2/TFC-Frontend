import React from 'react'
import { useState, useRef, useEffect, useContext } from "react";
import AuthContext from "../../context/AuthProvider";
import axios from "axios";

function Logout() {
    const authContext = useContext(AuthContext)
    const isMounted = useRef(true)

    const logout = async () => {
        const request = await axios.get('/accounts/profile/logout/')
        localStorage.removeItem("user")
        return request
    }
    useEffect(() => {
        logout().then(() => {
            if (isMounted.current) {
                authContext.setAuth(({
                    accessToken: null,
                    authenticated: null
                }))
            }
            return () => {
                isMounted.current = false
            }
        })
    }, [])

    return (
        <div>
            <h1>You are logged out!</h1>
        </div>
    )
}

export default Logout