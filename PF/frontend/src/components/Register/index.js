import React from "react";
import { useRef, useState, useEffect, useContext } from "react"
import { Grid, Paper, Avatar, Typography, TextField, Button } from '@mui/material'
import axios from "axios"
import AuthContext from "../../context/AuthProvider";


const EMAIL_REGEX = /^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$/
const PASSWORD_REGEX = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$/
const PHONE_REGEX = /^\d{3}-\d{3}-\d{4}$/

const Register = () => {
    const { setAuth } = useContext(AuthContext)

    const [avatar, setAvatar] = useState()

    const errorRef = useRef()
    const [errorMsg, setErrorMsg] = useState('')
    const [success, setSucess] = useState(false)

    const emailRef = useRef()
    const [email, setEmail] = useState('')
    const [validEmail, setValidEmail] = useState(false)
    const [emailFocus, setEmailFocus] = useState(false)

    const [password, setPassword] = useState('')
    const [validPassword, setValidPassword] = useState(false)
    const [passwordFocus, setPasswordFocus] = useState(false)

    const [password2, setPassword2] = useState('')
    const [validPassword2, setValidPassword2] = useState(false)
    const [password2Focus, setPassword2Focus] = useState(false)

    const fnRef = useRef()
    const [firstName, setFirstName] = useState('')
    const [firstNameFocus, setFirstNameFocus] = useState(false)

    const lnRef = useRef()
    const [lastName, setLastName] = useState('')
    const [lastNameFocus, setLastNameFocus] = useState(false)

    const phoneNumRef = useRef()
    const [phoneNum, setPhoneNum] = useState('')
    const [validPhoneNum, setValidPhoneNum] = useState(false)
    const [phoneNumFocus, setPhoneNumFocus] = useState(false)

    /*     useEffect(() => {
            emailRef.current ? emailRef.current.focus() : console.log("unfocus")
        }, []) */

    useEffect(() => {
        setValidEmail(EMAIL_REGEX.test(email))
    }, [email])

    useEffect(() => {
        setValidPassword(PASSWORD_REGEX.test(password));
        setValidPassword2(password === password2);
    }, [password, password2])

    useEffect(() => {
        setValidPhoneNum(PHONE_REGEX.test(phoneNum));
    }, [phoneNum])

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const response = await axios.post('/accounts/register/',
                JSON.stringify({
                    email: email,
                    password: password,
                    password2: password2,
                    first_name: firstName,
                    last_name: lastName,
                    phone_num: phoneNum,
                    avatar: null,
                    lon: null,
                    lat: null
                }),
                {
                    headers: { 'Content-Type': 'application/json' },
                    withCredentials: true
                })
            console.log(response.data)
            console.log(response)
        }
        catch (err) {
            if (!err?.response) {
                setErrorMsg("no server response")
            }
            errorRef.current.focus()

        }
    }

    return (
        <>
            <section>
                <form onSubmit={handleSubmit}>
                    <TextField fullWidth
                        id='firstName'
                        label='first name'
                        placeholder="Enter your name"
                        autoFocus
                        required
                        onChange={(e) => setFirstName(e.target.value)}
                        value={firstName}
                        inputRef={fnRef} />
                    <TextField fullWidth
                        id='lastName'
                        label='last name'
                        placeholder="Enter your last name"
                        autoFocus
                        required
                        onChange={(e) => setLastName(e.target.value)}
                        value={lastName}
                        inputRef={lnRef} />

                    <TextField fullWidth
                        id='email'
                        label='email'
                        placeholder="Enter your email"
                        required
                        /* error={validEmail ? "false" : "true"} */
                        autoFocus
                        onChange={(e) => setEmail(e.target.value)}
                        value={email}
                        inputRef={emailRef} />
                    <TextField fullWidth
                        id='phoneNum'
                        label='phone number'
                        placeholder="Enter your phone number"
                        autoFocus
                        required
                        onChange={(e) => setPhoneNum(e.target.value)}
                        value={phoneNum}
                        inputRef={phoneNumRef} />
                    <input type="file"
                        id="avatar"
                        onChange={(e) => setAvatar(e.target.files[0])}
                        accept=".png, .jpg, .jpeg" />
                    <TextField fullWidth
                        id='password'
                        label='password'
                        placeholder="Enter your password"
                        autoFocus
                        required
                        onChange={(e) => setPassword(e.target.value)}
                        value={password} />
                    <TextField fullWidth
                        id='password2'
                        label='password'
                        required
                        placeholder="Confirm your password"
                        autoFocus
                        onChange={(e) => setPassword2(e.target.value)}
                        value={password2} />
                    <Button type='submit' variant='contained' color='primary'>
                        Sign up
                    </Button>
                </form>
            </section>
        </>
    )

    /* disabled={!validEmail || !validPassword || !validPassword2 ? true : false} */
}
export default Register