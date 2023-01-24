import { useRef, useState, useEffect, useContext } from "react";
import AuthContext from "../../context/AuthProvider";
import axios from "axios";


const Login = () => {

    const authContext = useContext(AuthContext)
    const userRef = useRef()

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [errorMsg, setErrorMsg] = useState('')
    const [success, setSucess] = useState('') /* reroute to profile page */

    useEffect(() => {
        userRef.current.focus()
    }, [])

    useEffect(() => {
        setErrorMsg('')
    }, [email, password])

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const response = await axios.post('/accounts/login/',
                JSON.stringify({ email, password }),
                {
                    headers: { 'Content-Type': 'application/json' },
                    withCredentials: true
                })
            if (response.data.accessToken) {
                localStorage.setItem("user", authContext.setAuth({
                    accessToken: JSON.stringify(response.data),
                    authenticated: true
                }));
            }
            console.log(JSON.stringify(response?.data))

            setEmail('')
            setPassword('')
            setSucess(true)

        } catch (error) {
            if (!error?.response) {
                setErrorMsg('No Server Response')
            }
        }
    }

    return (
        <section>
            <h1>Sign In</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="email"> Email:</label>
                <input
                    type='text'
                    id='email'
                    ref={userRef}
                    onChange={(e) => setEmail(e.target.value)}
                    value={email}
                    required>
                </input>

                <label htmlFor="password"> Password:</label>
                <input
                    type='password'
                    id='password'
                    onChange={(e) => setPassword(e.target.value)}
                    value={password}
                    required>
                </input>
                <button> Sign In</button>

            </form>
        </section>
    )

}

export default Login